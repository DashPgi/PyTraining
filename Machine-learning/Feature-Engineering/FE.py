import numpy as np
import pandas as pd
import feature_engine as fe
import sklearn as sk

pd.set_option('display.max_columns', None)
data = pd.read_csv("raw_customer_dataset.csv")

data.isna().sum()
data.duplicated().sum()
data = data.drop_duplicates()


REF_DATE = pd.Timestamp("2025-01-01")
data["signup_date"] = pd.to_datetime(data["signup_date"])
data["last_purchase_date"] = pd.to_datetime(data["last_purchase_date"])


data["tenure_days"] = (REF_DATE - data["signup_date"]).dt.days
data["days_since_last_purchase"] = (REF_DATE - data["last_purchase_date"]).dt.days
data["signup_month"] = data["signup_date"].dt.month
data["signup_weekday"] = data["signup_date"].dt.weekday
data["signup_is_weekend"] = data["signup_weekday"].isin([5, 6]).astype(int)



data = data.drop(columns=["signup_date", "last_purchase_date"])


data["review_length"] = data["product_review"].fillna("").str.len()
data["review_word_count"] = data["product_review"].fillna("").str.split().apply(len)
data["has_review"] = data["product_review"].notna().astype(int)
data = data.drop(columns=["product_review"])

y = data["is_churned"]
X = data.drop(columns=["is_churned", "customer_id"])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

numeric_vars = ["age", "income", "num_purchases", "total_spent", "avg_rating",
                "tenure_days", "days_since_last_purchase",
                "review_length", "review_word_count"]
categorical_vars = ["gender", "city", "membership_type", "referral_source"]

missing_indicator = AddMissingIndicator(
    variables=["age", "income", "avg_rating"], missing_only=True
)

numeric_imputer = MeanMedianImputer(
    imputation_method="median", variables=["age", "income", "avg_rating"]
)

categorical_imputer = CategoricalImputer(
    imputation_method="missing", variables=categorical_vars
)

winsorizer = Winsorizer(
    capping_method="iqr",
    tail="both",
    fold=1.5,
    variables=["age", "income", "num_purchases", "total_spent"],
)


rare_encoder = RareLabelEncoder(
    tol=0.03,
    n_categories=5,
    variables=["city", "referral_source"],
)

log_transformer = LogTransformer(variables=["income", "total_spent"])


math_features = MathFeatures(
    variables=["total_spent", "num_purchases"],
    func="sum",
    new_variables_names=["total_spent_plus_purchases"],
)


onehot_encoder = FE_OneHotEncoder(
    variables=categorical_vars,
    drop_last=True,
)

fe_pipeline = Pipeline([
    ("missing_indicator", missing_indicator),
    ("numeric_imputer", numeric_imputer),
    ("categorical_imputer", categorical_imputer),
    ("winsorizer", winsorizer),
    ("rare_encoder", rare_encoder),
    ("log_transformer", log_transformer),
    ("math_features", math_features),
    ("onehot_encoder", onehot_encoder),
])

X_train_fe = fe_pipeline.fit_transform(X_train, y_train)
X_test_fe = fe_pipeline.transform(X_test)

print("after train", X_train_fe.shape)
print("final column", X_train_fe.columns.tolist())

X_train_fe["spend_per_purchase"] = np.where(
    X_train_fe["num_purchases"] == 0,
    0,
    X_train_fe["total_spent"] / X_train_fe["num_purchases"].replace(0, np.nan)
)
X_train_fe["spend_per_purchase"] = X_train_fe["spend_per_purchase"].fillna(0)

X_test_fe["spend_per_purchase"] = np.where(
    X_test_fe["num_purchases"] == 0,
    0,
    X_test_fe["total_spent"] / X_test_fe["num_purchases"].replace(0, np.nan)
)
X_test_fe["spend_per_purchase"] = X_test_fe["spend_per_purchase"].fillna(0)

scale_cols = X_train_fe.select_dtypes(include=[np.number]).columns.tolist()

scaler = StandardScaler()
X_train_fe[scale_cols] = scaler.fit_transform(X_train_fe[scale_cols])
X_test_fe[scale_cols] = scaler.transform(X_test_fe[scale_cols])

print("nice job :")
print(X_train_fe.shape)
print(X_train_fe.head())
import numpy as np

# -------- Array's
OneD = [1, 2, 3, 5, 6]
Array_1D = np.array(OneD)

print(Array_1D)
print(f"Size : {Array_1D.nbytes}", "Child-Type : ", Array_1D.dtype, "Dimentions : ", Array_1D.ndim, "Type :",
      type(Array_1D))
print((Array_1D.reshape(-1, 1)))

TwoD = [[1, 2, 3], [4, 5, 6]]
Array_2D = np.array(TwoD)

print(Array_2D)
print(f"Size : {Array_2D.nbytes} Child Type : {Array_2D.dtype} Dimetion : {Array_2D.ndim} Type : {type(Array_2D)}")

# 1 number = 8 byte

ThreeD = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [7, 8, 9]]]
Array_3D = np.array(ThreeD)

# Shape (Plate,Row,Column)

print(Array_3D.shape)
print(Array_3D)
print(f"Size : {Array_3D.nbytes} Child Type : {Array_3D.dtype} Dimetion : {Array_3D.ndim} Type : {type(Array_3D)}")

Array_3D_2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [7, 8, 9]]])
Array_4D = np.stack([Array_3D_2, Array_3D])

print(Array_4D)
print(f"Shape : {Array_4D.shape}")
print(f"Size : {Array_4D.nbytes} Child Type : {Array_4D.dtype} Dimetion : {Array_4D.ndim} Type : {type(Array_4D)}")

Array_4D_2 = np.array([Array_3D, Array_3D_2])
Array_5D = np.stack([Array_4D_2, Array_4D])

print(Array_5D)
print(f"Size : {Array_5D.nbytes} Child Type : {Array_5D.dtype} Dimetion : {Array_5D.ndim} Type : {type(Array_5D)}")

# Shape (Tedade 4D,Tedade 3D,Tedade Row,Tedade Column)
# stack Array 1 + Array 1 = Array 2 => Nazarie Abaad Hendesi inja Bedard Nmikhore !!

# -------- Mathematics function

# set For all indexes
A = np.array([16, 12, -3])
print(f"shape : {A.shape}")
print(f"ABS : {np.abs(A)}")
print(f"Sqrt : {np.sqrt(A)}")
print(f"Log : {np.log(A)}")
print(f"power : {np.power(A, 2)}")

# set For some Indexes (Sensitive To Nan Index)
# Baraye Delete Nan Bug Mitoonim Fun -> Nanfun => max -> nanmax

B = np.array([[4, 9, -13], A])
print(f"maxnnumber : {np.max(A)}")
print(f"maxnumber Index : {np.argmax(A)}")
print(f"Sum  : {np.sum(A)}")
print(f"mean  : {np.mean(A)}")
print(f"median  : {np.median(A)}")
print(f"std : {np.std(A)}")  # Enheraf  Meyar
print(f"variance : {np.var(A)}")  # Variance
print(f"cumsum : {np.cumsum(A)}")  # Jame Tajmii
print(f"product : {np.prod(A)}")
print(f"quantile : {np.quantile(A, q=0.9)}")
print(f"percentile : {np.percentile(A, q=90)}")

# set for optional dimension

print(f"Maxnumber in every Columns : {np.max(B, axis=0)}")  # For Column's
print(f"Maxnumber in every Rows : {np.max(B, axis=1)}")  # For Row's
# axis = Dimension

D = np.array([A, [4, 5, 6]])
C = np.stack([B, D])

print(f"maxnumber in Columns : {np.max(C, axis=0)}")
print(f"maxnumber in Rows : {np.max(C, axis=1)}")
print(f"maxnumber in Dim 2 : {np.max(C, 2)}")

# function for index maker

print(np.zeros((1, 2), dtype="int64"))
print(np.ones((1, 2), dtype="int64"))
print(np.full((1, 2), 2, dtype="int64"))
print(np.empty((1, 2), dtype="int64"))

print(np.arange(1, 15, 2))
print(np.arange(1, 24, 2).reshape(2, 3, 2))

print(np.linspace(0, 50, 5).reshape(2, 5), dtype="int64")

print(np.random.default_rng(seed=2).integers(low=10, high=20, size=(2, 3)))

# Expanding Dimension's

A = np.array([[1, 2, 3, 5], [4, 5, 6, 4]])
# 2*4
B = np.array([[7, 8, 9], [7, 8, 9], [7, 8, 9]])
# 3*3

A_R = A[:, :, np.newaxis, np.newaxis]
B_R = B[np.newaxis, np.newaxis, :, :]

C = A_R + B_R
print(f"C : {C}")
print(f"C shape : {C.shape}")

# indexing

A = np.random.default_rng(seed=1).integers(low= 0,high = 100,size=(5,5))

print(A)
print(A[A<30])
print(A[1,2])
print(A[[0,2],[1,2]])
print(A[:,[1,2]])
print(f"1 -- : {A[1:]}")
print(f"1 -- 5 : {A[1:5:2]}")
print(A[::,1,2])

# join and Split

A = np.random.default_rng(seed=1).integers(low=1, high=10,size=(3,3,3),dtype="int64")
B = np.random.default_rng(seed=1).integers(low=1, high=10,size=(3,3,3),dtype="int64")

print(A)
print(B)

C = np.concatenate((A, B))
print(f"C : {C}")
D = np.concatenate((A, B), axis=1)
print(f"D : {D}")
E = np.concatenate((A, B), axis=2)
print(f"E : {E}")


R = np.split(C,1)
C = np.split(C,
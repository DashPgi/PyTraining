import numpy as np


# -------- Array's
OneD = [1,2,3,5,6]
Array_1D = np.array(OneD)

print(Array_1D)
print(f"Size : {Array_1D.nbytes}","Child-Type : ",Array_1D.dtype,"Dimentions : ",Array_1D.ndim,"Type :",type(Array_1D))
print((Array_1D.reshape(-1, 1)))

TwoD = [[1,2,3],[4,5,6]]
Array_2D = np.array(TwoD)

print(Array_2D)
print(f"Size : {Array_2D.nbytes} Child Type : {Array_2D.dtype} Dimetion : {Array_2D.ndim} Type : {type(Array_2D)}")

# 1 number = 8 byte

ThreeD = [[[1,2,3],[4,5,6]],[[7,8,9],[7,8,9]]]
Array_3D = np.array(ThreeD)

# Shape (Plate,Row,Column)

print(Array_3D.shape)
print(Array_3D)
print(f"Size : {Array_3D.nbytes} Child Type : {Array_3D.dtype} Dimetion : {Array_3D.ndim} Type : {type(Array_3D)}")

Array_3D_2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
Array_4D = np.stack([Array_3D_2,Array_3D])

print(Array_4D)
print(f"Shape : {Array_4D.shape}")
print(f"Size : {Array_4D.nbytes} Child Type : {Array_4D.dtype} Dimetion : {Array_4D.ndim} Type : {type(Array_4D)}")

Array_4D_2 = np.array([Array_3D,Array_3D_2])
Array_5D = np.stack([Array_4D_2,Array_4D])

print(Array_5D)
print(f"Size : {Array_5D.nbytes} Child Type : {Array_5D.dtype} Dimetion : {Array_5D.ndim} Type : {type(Array_5D)}")

# Shape (Tedade 4D,Tedade 3D,Tedade Row,Tedade Column)
# stack Array 1 + Array 1 = Array 2 => Nazarie Abaad Hendesi inja Bedard Nmikhore !!

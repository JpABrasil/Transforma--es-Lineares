from Transformation import transformation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#Teste de Translação
#2D
print("Testes de Translação:")
v0 = [[0,0],[1,1]]
dx=3
dy=1
v1 = transformation.translate2D(v0,dx,dy)
print("2D:")
print(f"Origem do Vetor original:{v0[0]}, Final do Vetor original: {v0[1]}")
print(f"Origem do Vetor transladado:{v1[0]}, Final do Vetor Transladado: {v1[1]}")
#3D
v0 = [[0,0,0],[1,1,1]]
dx=3
dy=1
dz=2
v1 = transformation.translate3D(v0,dx,dy,dz)
print("3D:")
print(f"Origem do Vetor original:{v0[0]}, Final do Vetor original: {v0[1]}")
print(f"Origem do Vetor transladado:{v1[0]}, Final do Vetor Transladado: {v1[1]}")
print()
#Testes de Rotação
#2D
print("Teste de Rotação")
print("2D:")
v0 = [[0,0],[1,1]]
angle = 60
v1 = transformation.rotation2D(v0,60)
print(f"Origem do Vetor original:{v0[0]}, Final do Vetor original: {v0[1]}")
print(f"Origem do Vetor transladado:{v1[0]}, Final do Vetor Transladado: {v1[1]}")
#3DX
print("3DX:")
v0 = [[0,0,0],[1,1,0]]
angle = 60
v1 = transformation.rotation3DX(v0,60)
print(f"Origem do Vetor original:{v0[0]}, Final do Vetor original: {v0[1]}")
print(f"Origem do Vetor transladado:{v1[0]}, Final do Vetor Transladado: {v1[1]}")
#3DY
print("3DY:")
v0 = [[0,0,0],[2,2,2]]
angle = 60
v1 = transformation.rotation3DY(v0,60)
print(f"Origem do Vetor original:{v0[0]}, Final do Vetor original: {v0[1]}")
print(f"Origem do Vetor transladado:{v1[0]}, Final do Vetor Transladado: {v1[1]}")
#3DZ
print("3DZ:")
v0 = [[0,0,0],[2,2,2]]
angle = 60
v1 = transformation.rotation3DZ(v0,60)
print(f"Origem do Vetor original:{v0[0]}, Final do Vetor original: {v0[1]}")
print(f"Origem do Vetor transladado:{v1[0]}, Final do Vetor Transladado: {v1[1]}")

#Importing library
import math

#Receiving information from user
side_a = int(input("Digite um valor para o lado 'a' do triângulo : \n"))
side_b = int(input("Digite um valor para o lado 'b' do triângulo : \n"))
side_c = int(input("Digite um valor para o lado 'c' do triângulo : \n"))

#Setting conditions to be a triangle
cond_1 = side_a + side_b > side_c
cond_1 = False

cond_2 = side_a + side_c > side_b
cond_2 = False

cond_3 = side_b + side_c > side_a
cond_3 = False

if cond_1 and cond_2 and cond_3:
    print("Não é um triângulo")

#Type of triangle variables
equilateral = side_a == side_b == side_c
isosceles = side_a == side_b or side_b == side_c or side_c == side_a
scalene = side_a != side_b != side_c

#Telling what is the type of the triangle
if equilateral :
    print("Equilátero")
elif isosceles :
    print("Isósceles")
elif scalene :
    print("Escaleno")

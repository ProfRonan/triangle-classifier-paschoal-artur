#Receiving information from user
side_a = int(input("Digite um valor para o lado 'a' do triângulo : \n"))
side_b = int(input("Digite um valor para o lado 'b' do triângulo : \n"))
side_c = int(input("Digite um valor para o lado 'c' do triângulo : \n"))

#Setting conditions to be a triangle
cond_1 = int(side_a + side_b > side_c)

cond_2 = int(side_a + side_c > side_b)

cond_3 = int(side_b + side_c > side_a)

if cond_1 == False or cond_2 == False or cond_3 == False:
    print("Não é um triângulo")
else:
#Type of triangle variables
    equilateral = int(side_a == side_b == side_c)
    isosceles = int(side_a == side_b or side_b == side_c or side_c == side_a)
    scalene = int(side_a != side_b != side_c)

#Telling what is the type of the triangle
    if equilateral :
        print("Equilátero")
    elif isosceles :
        print("Isósceles")
    elif scalene :
        print("Escaleno")

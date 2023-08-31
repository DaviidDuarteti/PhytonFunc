import os

def soma(n1,n2):
    print(f"{n1}+{n2}={n1+n2}")

def subtrair(n1,n2):
    print(f"{n1}-{n2}={n1-n2}")

def multiplica(n1,n2):
    print(f"{n1}*{n2}={n1 * n2}")

def dividir(n1,n2):
    print(f"{n1}/{n2}={n1/n2}")


def entrada(max):
    for x in range(max):

       

        x1 = int(input("Digite um numero: "))
        x2 = int(input("Digite outro numero: "))
        op = int(input("1-soma, 2-subtrair, 3-multiplicar, 4-dividir: "))
        os.system("cls")
        
        if(op == 1):
            soma(x1, x2)

        elif(op ==2):
            subtrair(x1,x2)

        elif(op ==3):
            multiplica(x1,x2)

        else:
            dividir(x1,x2)
        
m = int(input("Digite quantas operaçoes deseja fazer: "))



entrada(m)

'''
Entrada: Recibe dos enteros positivos a y b.
Salida: Entrega el máximo común divisor de a y b.
Complejidad: La complejidad de este algoritmo es hecha a partir de la establecida O(Log a).
Correctitud: El algoritmo es hecho en base a las demostraciones de los puntos anteriores,
las cuales son :
*Si a y b son pares entonces gcd(a,b) = 2 * gcd(a//2, b//2).
*Si a es impar y b es par entonces gcd(a,b) = gcd(a, b//2).
* Si a es par y b es impar entonces gcd(a,b) = gcd(a//2,b).
*Si a y b son impares entonces gcd(a,b) = gcd((a - b) // 2, b).
El algoritmo analiza todas las posibilidades que puede tener a y b en el transcurso de su 
ejecución, por lo tanto termina al llegar al caso base. 
'''

def gcd(a, b):
    if(b == 0):
        return a
    elif(a < b):
        return gcd(b, a)
    elif((a & 1 == 1) and (b & 1 == 1)):
        return gcd((a - b) // 2, b)
    elif((a & 1 == 0) and (b & 1 == 0)):
        return gcd(a//2, b//2) << 1
    elif((a & 1 == 1) and (b & 1 == 0)):
        return gcd(a, b//2)
    elif((a & 1 == 0) and (b & 1 == 1)):
        return gcd(a//2, b)

def gcd2(a,b):
    if(b == 0):
        return a
    elif(a < b):
        return gcd(b,a)
    elif((a & 1 == 0) and (b & 1 == 1)):
        return gcd2(a//2, b)
    elif((a & 1 == 1) and (b & 1 == 0)):
        return gcd2(a, b//2)
    elif((a & 1 == 0) and (b & 1 == 0)):
        return gcd2(a//2, b//2)*2
    else:
        return gcd2((a - b) // 2, b)

def main():
    print(gcd(21,15))
    print(gcd2(21,15))
    print(gcd(21,14))
    print(gcd2(21,14))
    print(gcd(1914,898))
    print(gcd2(1914,898))
    print(gcd(1913,899))
    print(gcd2(1913,899))
    print(gcd(1914,899))
    print(gcd2(1914,899))
main()
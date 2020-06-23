from sys import stdin
import math
'''
Nombre: Isabela Acevedo García
Código de estudiante: 8938558
Código de honor:
Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me
comprometo a seguir los más altos estándares de integridad académica.
'''
def fft(A, invert):
    #Se hace la Fast Fourier Transform, en la cual le entra el arreglo al que se le hará
    #la fft y una variable booleana, tal que determine si ejecuta fft inversa o la normal. 
    n = len(A)
    if(n > 1):
        even, odd = [], []
        for i in range(n//2):
            even.append(A[i*2]) #se llenan los vectores dependiendo de si es par o impar.
            odd.append(A[(i*2)+1]) ##par = 2i , impar = 2i + 1.
        fft(even, invert)
        fft(odd, invert)
        angle = 2*(math.pi)/n*(-1 if invert else 1)
        w, wn = complex(1), complex(math.cos(angle), math.sin(angle)) #numeros complejos Wn
        for i in range(len(A)//2): ## se recorre por la mitad de los datos
            A[i] = even[i] + w*odd[i] #el numero i de los pares + w*(el numero i de los impares)
            A[i+n//2] = even[i] - w*odd[i] ##mariposa
            if(invert == True):
                A[i] /= 2
                A[i+n//2] /= 2
            w *= wn

def solve(A, B, N):
    #Hace la convolución entre A y B que tienen tamaño N. 
    A, B  = [complex(i) for i in A], [complex(i) for i in B]
    size = 2*N
    n = 1
    while(n < size):
        n <<= 1 #potencias en base 2 (1,2,4,8,16,32) para ejecutar la mariposa
    for i in range(n-N):
        A.append(0)
        B.append(0)
    fft(A, False)
    fft(B, False)
    C = []; nn = len(A)
    for i in range(nn): #convolucion en punto valor
        C.append(A[i]*B[i])
    fft(C,True)
    C = [round(i.real) for i in C] #coge el valor real del imaginario.
    return C

def main():
    line = stdin.readline().strip().split()
    while(len(line)!=0):
        n = int(line[0])
        A1 = [x for x in stdin.readline().strip()]
        A2 = [x for x in stdin.readline().strip()]
        B1 = []
        #Los arreglos con B y R se transforman en nuevos arreglos de 1's(R) y 0's(B)
        for i in range(n):
            if(A1[i] == 'R'):
                B1.append(1)
            else:
                B1.append(0)
        B2 = []
        for i in range(n):
            if(A2[i] == 'R'):
                B2.append(1)
            else:
                B2.append(0)
        ##poner mismo tamaño en las listas B1 Y B2.
        B1 = list(reversed(B1))
        for i in range(n):
            B1.append(0)
        #print(B1)
        x = B2
        for i in range(n):
            B2.append(x[i])
        #print(B2)
        cont = 0
        if(n == 1):
            if(B1[0] == B2[0] == 1):
                cont = 0
            else:
                cont = 1
        else:   
            ans = solve(B1,B2,len(B1))
            x = ans[(n-1):((2*n)-1)]
            print(x)
            cont = 0; N = len(x)
            for i in range(N):
                if(x[i] == 0):
                    cont+=1
        print(cont)
        #print(ans)
        line = stdin.readline().strip().split()
main()
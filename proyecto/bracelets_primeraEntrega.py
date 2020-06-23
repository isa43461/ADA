from sys import stdin
'''
Nombre: Isabela Acevedo García
Código de estudiante: 8938558
Código de honor:
Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.
'''
def solve(b1,b2,n):
	'''
	La idea en esta funcion es básicamente sacar la sumatoria de multiplicar cada uno
	de los elementos de las listas (b1[j]*B2[j]), según su respectivo indice.
	Si la sumatoria es igual a 0, significa que la manilla 2 (B2) encaja con la 
	manilla 1 (b1). Por lo tanto, se suma al contador(answer) esa manilla que encaja. 
	Después, se rota la manilla 2 (se saca el primer elemento y se agrega de ultimo).
	'''
	B2 = b2 ; cont = 0
	for i in range(n):
		ml = 0
		for j in range(n):
			ml += b1[j]*B2[j]
		if(ml == 0):
			cont += 1
		v = B2.pop(0)
		B2.append(v)
	return cont

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
		print(solve(B1,B2,n))
		line = stdin.readline().strip().split()
main()
"""
Escreva um programa em Python que gera um número aleatório para que o usuário tente acertar o número. Algumas sugestões para o programa:
"""
import random
aleatorios=[]
x=0
acertos=0
numeros_escolhidos=[]
while x<5:
    print(".")
    x+=1
    r1= random.randint(0,10)
    aleatorios.append(r1)
while x>0:
    r2=int(input("digite um numero para ver se está na mega cena:"))
    if r2 in aleatorios:
        acertos +=1
    numeros_escolhidos.append(r2)
    x-=1
pa= (acertos/5)*100
print(f"a porcentagem de acerto foi de {acertos}%")
print(f"esses foram os numeros da mega cena:{aleatorios}")
print(f"esses foram os numeros escolhidos por você:{numeros_escolhidos}")
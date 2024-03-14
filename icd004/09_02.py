"""
Name: 09_02.py
Desc: 2 Exemplo do slide, mostrando os campos
"""

from time import time

L = [1, "Goiânia", "Goiás", 
     2, "Bonito", "Mato Grosso", 
     3, "Carangola", "Minas Gerais",
     4, "Peruíbe", "São Paulo",
     20, "Serra", "Espírito Santo"]

n = len(L)

print("dimensão da lista 'L' = ", n)
print("L[0]", L[0])
print("L[3]", L[3])
print("L[6]", L[6])
print("L[9]", L[9])
print("L[4]", L[4])
print("L[4][2]", L[4][2])
print("L[2][1]", L[2][1])
print("\n")


def busca_linear(x, steps=99999):
    for p in range(steps):
        i = 0
        while i < n:
            if L[i] == x:
                return L[i], L[i+1], L[i+2]
            # else: Nem precisa do else
            i = i + 1

tinit = time()
print("chave(1) = ", busca_linear(1))
print("chave (2) = ", busca_linear(2))
print("chave(3) = ", busca_linear(3))
print("chave(4) = ", busca_linear(4))
print("chave(20) = ", busca_linear(20))
print("chave (0) = ", busca_linear(0))
print("chave (6) = ", busca_linear(6))
tend = time()
print("tempo de execução = ", tend - tinit)
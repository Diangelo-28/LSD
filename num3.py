#Escreva um programa que calcule o volume de um cilindro. O programa deve pedir ao usuário o valor do raio
# (r) e da altura (h), e utilizar a fórmula V = π · r² · h para calcular o volume. Ao final, exiba o resultado.
import math
raio = float(input("o raio mede: "))
altura = float(input(" a altura mede: "))
volume = math.pi * raio**2 * altura
print (f"o volume é: {volume}")
# -*- coding: utf-8 -*-
"""Exercicios_de_funcao.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wAp_JD2tSlyIijkbiBPGGZm7sU3GMQvU
"""

def funcao():
  pass

def saudacao():
  print('Oi!')

saudacao()

def saudacao2(txt):
  print(f'Ola {txt}!')

L= [1, 2, 3,]
L2= [x**2 for x in L]
print(L2)
print(sum(L2))

def somas(lista):
  soma = sum(lista)
  soma2 = sum(x**2 for x in lista)
  return soma, soma2

somas([1, 2, 3])

def somas(lista):
  return sum(lista), sum([ x ** 2 for x in lista])

res1 = somas([-1, 2, 1, 3])
print(res1)
s1, s2 = somas([-1, 2, 1, 3])

lista =([1,5,9])

def soma(lista):
  soma = sum(lista)
  return soma

soma(lista)

lista = ([9, 5, 4])
lista2 = ([15, 25, 30])

subtrao = []

for i in range(len(lista)):
    subtracao.append(lista[i] - lista2[i])

print(subtracao)

def soma(a, b):
  soma =(a + b)
  return soma

def subtracao(a, b):
  subtracao = (a - b)
  return subtracao

def multiplicacao(a, b):
  multiplicacao = (a * b)
  return multiplicacao

def divisao(a, b):
  return a / b if b != 0 else None

def potenciacao(a, b):
  potenciacao = (a**b)
  return potenciacao


def exibir_menu():
  print("Escolha a operação: ")
  print("1. Soma")
  print("2. Subtração")
  print("3. Multiplicação")
  print("4. Divisão")
  print("5. Potenciação")

def calculadora():
  exibir_menu()
  opcao = input("Digite o Numero da Operação Desejada: ")

  if opcao in ('1', '2', '3', '4', '5'):
    numA = float(input("digite o numero A: "))
    numB = float(input("Digite o numero B: "))
    if opcao == '1':
      res = soma(numA, numB)
    elif opcao == '2':
      res = subtracao(numA, numB)
    elif opcao == '3':
      res = multiplicacao(numA, numB)
    elif opcao == '4':
      res = divisao(numA, numB)
    else:
      res = potenciacao(numA, numB)
    print(res)

  else:
    print("Opção Inválida! Por favor escolha uma opção Válida!")



calculadora()

cpf = input("Entre com o CPF: ")
cpfn = [d for d in cpf]
cpfn

def validar_cpf:
  cpfn =

def validar_digito_verificador_1(digitos):
  soma_prod = 0
  for n in range(9):
    soma_prod += (digitos[n] * (10 - n))
  print(f"soma_prod = {soma_prod}")
  d1 = (soma_prod * 10) % 10
  print(d1)
  return d1 == digitos[-2]


def validar_digito_verificador_2(digitos):
  soma_prod = 0
  for n in range(10):
    soma_prod += (digitos[n] * (11 - n))
  print(f"soma_prod = {soma_prod}")
  d2 = (soma_prod * 10) % 10
  print(d2)
  return d2 == digitos[-1]


def validar_cpf(cpf):
  print(cpf)
  cpfn = [int(d) for d in cpf]
  print(f"cpfn = {cpfn}")
  v1 = validar_digito_verificador_1(cpfn)
  print(v1)
  if v1 == False:
    return False
  v2 = validar_digito_verificador_2(cpfn)
  if v2:
    return True
  else:
    return False



def  main():
  cpf = input("Digite o CPF(Apenas numeros): ")
  if validar_cpf(cpf):
    print("CPF Válido")
  else:
    print("CPF Inválido")

main()

L = list('12345')
Ln = [int(d) for d in L]
Ln

def validar_digito_verificador_1(digitos):
  soma_prod = 0
  for n in range(9):
    soma_prod += (digitos[n] * (9 - n))
  print(f"soma_prod = {soma_prod}")
  d1 = (soma_prod * 10) % 9
  print(d1)
  return d1 == digitos[-2]


def validar_digito_verificador_2(digitos):
  soma_prod = 0
  for n in range(10):
    soma_prod += (digitos[n] * (10 - n))
  print(f"soma_prod = {soma_prod}")
  d2 = (soma_prod * 10) % 10
  print(d2)
  return d2 == digitos[-1]


def validar_cpf(cpf):
  print(cpf)
  cpfn = [int(d) for d in cpf]
  print(f"cpfn = {cpfn}")
  v1 = validar_digito_verificador_1(cpfn)
  print(v1)
  if v1 == False:
    return False
  v2 = validar_digito_verificador_2(cpfn)
  if v2:
    return True
  else:
    return False



def  main():
  cpf = input("Digite o CPF(Apenas numeros): ")
  if validar_cpf(cpf):
    print("CPF Válido")
  else:
    print("CPF Inválido")

main()

def validar_digito_verificador_1(digitos):
    # Implementação para validar o dígito verificador 1
    soma_prod = sum((int(digitos[n]) * (10 - n)) for n in range(9))
    d1 = ((soma_prod * 10) % 11) % 10
    return d1 == int(digitos[-2])

def validar_digito_verificador_2(digitos):
    # Implementação para validar o dígito verificador 2
    soma_prod = sum((int(digitos[n]) * (11 - n)) for n in range(10))
    d2 = ((soma_prod * 10) % 11) % 10
    return d2 == int(digitos[-1])

def validar_cpf(cpf):
    # Implementação para validar o CPF
    cpfn = [d for d in cpf if d.isdigit()]
    if len(set(cpfn)) == 1:
        return False
    return validar_digito_verificador_1(cpfn) and validar_digito_verificador_2(cpfn)

def main():
    cpf = input("Digite o CPF (apenas números): ")
    if validar_cpf(cpf):
        print("CPF válido!")
    else:
        print("CPF inválido!")

# Chamando a função principal
main()

def gerar_digito_verificador_1(digitos):


  soma_prod = 0
  for d in range(9):
    soma_prod += print(digitos[n], 10-n) * (10-n)
  d1 = (soma)



def gerar_digito_verificador_2(digitos):

def gerar_cpf(cpf1):
    cpf = [int(d) for d in cpf1]
    d1 = gerar_digito_verificador_1(cpf)
    print(d1)
    cpf.append(d1)
    print(cpf)


def main():
    cpfin = input("Digite os primeiros 9 numeros CPF (apenas números): ")
    cpf = gerar_cpf(cpfin)
    print(f'CPF = {cpf}')
# Chamando a função principal
main()

def gerar_digito_verificador_1(digitos):


  soma_prod = 0
  for d in range(9):
    soma_prod += print(digitos[n], 10-n) * (10-n)
  d1 = (soma)



def gerar_digito_verificador_2(digitos):

def gerar_cpf(cpf1):
    cpf = [int(d) for d in cpf1]
    d1 = gerar_digito_verificador_1(cpf)
    print(d1)
    cpf.append(d1)
    print(cpf)


def main():
    cpfin = input("Digite os primeiros 9 numeros CPF (apenas números): ")
    cpf = gerar_cpf(cpfin)
    print(f'CPF = {cpf}')
# Chamando a função principal
main()


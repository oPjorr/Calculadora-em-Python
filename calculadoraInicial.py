operacao = 0

while operacao != 2:
    operacao = int(input("Dentre as funcionalidades, o que deseja que a calculadora faça?"
    "\n 1. Verificador de pares"
    "\n 2. Desligar a calculadora"))

#Verificador de números pares
    if operacao == 1:
        num = int(input("Digite um número para verificar se ele é par ou ímpar: "))
        print(f'par' if num%2 == 0 else 'ímpar')
    elif operacao == 2:
        print("Desligando a calculadora... Obrig... a.d...0....")
    else:
        print("Escolha um número válido! ")
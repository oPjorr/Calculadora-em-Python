operacao = 0

while operacao != 2:
    operacao = int(input("Dentre as funcionalidades, o que deseja que a calculadora faça?"
                         "\n 1. Verificador de pares"
                         "\n 2. Verificador de peso ideal"
                         "\n 3. Produto de dois números"
                         "\n 4. Desligar a calculadora"))

# Verificador de números pares
    if operacao == 1:
        num = int(input("Digite um número para verificar se ele é par ou ímpar: "))
        print(f'par' if num % 2 == 0 else 'ímpar')

# Verificador de peso ideal
    elif operacao == 2:
        alt = float(input("Digite a altura(em metros) de uma pessoa: "))
        sexo = int(input("Digite 1 para sexo Masculino e 2 para sexo Feminino: "))
        peso = float(input("Informe o seu peso atual em Kg: "))

        if sexo == 1:
            pesoIdeal = (72.7 * alt) - 58
        elif sexo == 2:
            pesoIdeal = (62.1 * alt) - 44.7
        else:
            print("Digite o valor certo para definir o sexo da pessoa!")

        print("O peso ideal dessa pessoa é", pesoIdeal, "Kg")

        if peso == pesoIdeal:
            print("Essa pessoa está dentro do seu peso ideal!")
        elif peso > pesoIdeal:
            print("Essa pessoa está acima de seu peso ideal!")
        else:
            print("Essa pessoa está abaixo de seu peso ideal!")

    elif operacao == 3:
        num1 = float(input("Informe o primeiro número: "))
        num2 = float(input("Informe o segundo número: "))
        print("o produto de", num1, "e", num2, "é", num1*num2)

    elif operacao == 4:
        print("Desligando a calculadora... Obrig... a.d...0....")
    else:
        print("Escolha um número válido! ")

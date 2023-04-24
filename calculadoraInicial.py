operacao = 0

while operacao != 2:
    operacao = int(input("\nDentre as funcionalidades, o que você deseja que a calculadora faça?\n"
                         "\n 1. Verificador de pares"
                         "\n 2. Verificador de peso ideal"
                         "\n 3. Produto de dois números"
                         "\n 4. Fatorial de um número"
                         "\n 5. Converter ºF em ºC"
                         "\n 6. Desligar a calculadora\n\n"))

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
        n = int(input("Digite o número que deseja calcular o fatorial: "))
        i = 1
        fat = 1
        while n >= i:
            fat *= i 
            i += 1
        print("O fatorial do número", n, "é de: ", fat)

    elif operacao == 5:
        def converter(F):
            C = (F - 32) * 5/9
            return C
  
        F = int(input("Digite a temperatura em Fahrenheit: "))
        print(converter(F))

    elif operacao == 6:
        print("Desligando a calculadora... Obrig... a.d...0....")
    else:
        print("Escolha um número válido! ")

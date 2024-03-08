import os

while True:
    print("Bem vindo")
    print("(1 - executiva - R$ 50")
    print("(2 - premium - R$ 80")
    print("(3 - Personalizada - R$ 70")

    try:
        menu = int(input("Agora, insira a classe que deseja: "))
        pessoas = int(input("Por favor, insira a quantidade de pessoas: "))

        if menu == 1:
            preco_por_pessoa = 50.00
            print("\nVocê escolheu a classe executiva")
        elif menu == 2:
            preco_por_pessoa = 80.00
            print("\nVocê escolheu a classe premium")
        else:
            preco_por_pessoa = 70.00
            print("\nVocê escolheu a classe Personalizada")
        
        custo_total = pessoas * preco_por_pessoa
        
        if pessoas > 50 and pessoas <= 80:
            custo_total *= 0.95  
        elif pessoas > 80:
            custo_total *= 0.90  

        print(f'\nO custo total do evento é: R$ {custo_total:.2f}')

        again = input("\nInsira (s) se quiser adicionar mais algum produto. Caso queira finalizar o pedido, pressione (n): ")
        
        if again.lower() != 's':
            os.system('cls')
            break

    except ValueError:
        print("Por favor, insira um número válido.")

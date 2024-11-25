# Função para somar
def somar(x, y):
    return x + y

# Função para subtrair
def subtrair(x, y):
    return x - y

# Função para multiplicar
def multiplicar(x, y):
    return x * y

# Função para dividir
def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    else:
        return x / y

# Função principal para exibir o menu e receber entradas
def calculadora():
    while True:
        # Menu de operações
        print("\nSelecione a operação desejada:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        
        # Recebe a escolha do usuário
        escolha = input("Digite o número da operação (1/2/3/4/5): ")

        # Condição para sair
        if escolha == '5':
            print("Saindo da calculadora...")
            break
        
        # Verifica se a escolha é válida
        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if escolha == '1':
                    print(f"{num1} + {num2} = {somar(num1, num2)}")
                elif escolha == '2':
                    print(f"{num1} - {num2} = {subtrair(num1, num2)}")
                elif escolha == '3':
                    print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
                elif escolha == '4':
                    print(f"{num1} / {num2} = {dividir(num1, num2)}")
            
            except ValueError:
                print("Entrada inválida! Por favor, insira um número.")
        else:
            print("Opção inválida! Tente novamente.")

# Chama a função principal
calculadora()


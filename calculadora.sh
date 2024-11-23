#!/bin/bash

# Função para realizar as operações
calcular() {
    case $opcao in
        1) echo "Resultado: $(($num1 + $num2))" ;;
        2) echo "Resultado: $(($num1 - $num2))" ;;
        3) echo "Resultado: $(($num1 * $num2))" ;;
        4) 
            if [ $num2 -eq 0 ]; then
                echo "Erro: Divisão por zero não permitida."
            else
                echo "Resultado: $(($num1 / $num2))"
            fi
            ;;
        *) echo "Opção inválida!" ;;
    esac
}

# Início do script
echo "Calculadora em Bash"
echo "Escolha uma operação:"
echo "1. Soma"
echo "2. Subtração"
echo "3. Multiplicação"
echo "4. Divisão"

read -p "Digite o número da operação (1/2/3/4): " opcao
read -p "Digite o primeiro número: " num1
read -p "Digite o segundo número: " num2

calcular


import matplotlib.pyplot as plt

# Criar listas vazias para os valores do eixo x e y
x = []
y = []

# Função para plotar o gráfico
def plotar_grafico():
    plt.clf()  # Limpar o gráfico anterior
    plt.plot(x, y, 'o-')  # Plotar os pontos
    plt.axhline(0, color='black', linestyle='-', linewidth=1)  # Linha horizontal no eixo Y
    plt.axvline(0, color='black', linestyle='-', linewidth=1)  # Linha vertical no eixo X
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Plano Cartesiano')
    plt.show()

# Loop para obter os valores do usuário
while True:
    # Exibir os valores atuais do eixo x e y
    print("Valores do eixo X:", x)
    print("Valores do eixo Y:", y)
    
    # Opções para o usuário
    print("\nOpções:")
    print("1. Adicionar valor")
    print("2. Alterar valor")
    print("3. Remover valor")
    print("4. Plotar gráfico")
    print("5. Sair")
    
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == '1':
        # Adicionar valor
        valor_x = float(input("Digite o valor do eixo X: "))
        valor_y = float(input("Digite o valor do eixo Y: "))
        x.append(valor_x)
        y.append(valor_y)
    elif opcao == '2':
        # Alterar valor
        indice = int(input("Digite o índice do valor a ser alterado: "))
        novo_valor_x = float(input("Digite o novo valor do eixo X: "))
        novo_valor_y = float(input("Digite o novo valor do eixo Y: "))
        x[indice] = novo_valor_x
        y[indice] = novo_valor_y
    elif opcao == '3':
        # Remover valor
        indice = int(input("Digite o índice do valor a ser removido: "))
        x.pop(indice)
        y.pop(indice)
    elif opcao == '4':
        # Plotar gráfico
        plotar_grafico()
    elif opcao == '5':
        # Sair do programa
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.\n")

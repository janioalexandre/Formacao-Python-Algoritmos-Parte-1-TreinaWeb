# 0 | 1 | 2 | 3 | 4
# 5 | 2 | 4 | 6 | 1

numeros = list()
tamanho = int(input("Digite o tamanho do vetor: "))
for i in range(tamanho):
    valor = int(input(f"Digite o número do vetor na posição {i}: "))
    numeros.append(valor)

print(numeros)

# BUSCA LINEAR
numero_pesquisa = int(input("Digite o valor a ser pesquisado no vetor: "))
posicao_resultado = -1
for i in range(tamanho):
    if numeros[i] == numero_pesquisa:
        posicao_resultado = i
        break
if posicao_resultado == -1:
    print("Número não encontrado no vetor")
else:
    print(f"O número foi encontrado na posição {posicao_resultado}")
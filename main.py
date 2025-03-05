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

# FIM BUSCA LINEAR

# SELECT SORT
for i in range(tamanho):
    indice_menor = i
    for j in range(int(i + 1), tamanho):
        if numeros[j] < numeros[indice_menor]:
            indice_menor = j
    
    temp = numeros[indice_menor]
    numeros[indice_menor] = numeros[i]
    numeros[i] = temp
    print("vetor: ", numeros)   

# FIM SELECT SORT

# BUSCA BINÁRIA
# 2
# 1 | 2 | 3 | 4 | 5
# 1 | 2 
# 2

resultado = -1
inicio = 0
fim = tamanho - 1
meio = 0
alvo = int(input("Digite o elemento a ser pesquisado no vetor: "))
while inicio <= fim:
    meio = int((inicio + fim) / 2)
    if (numeros[meio] < alvo):
        inicio = meio + 1
    elif (numeros[meio] > alvo):
        fim = meio - 1
    else:
        resultado = meio
        break
if resultado < 0:
    print("Elemento não encontrado no vetor")
else:
    print(f"O elemento {alvo} está na posição {resultado}")

# FIM BUSCA BINÁRIA
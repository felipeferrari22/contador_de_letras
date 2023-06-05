from unidecode import unidecode
import string

def carregar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        return arquivo.read()
    
def obtendo_letras(texto):
    texto = unidecode(texto)
    texto = texto.upper().split()
    palavras = []
    for i in texto:
        i = i.translate(str.maketrans('', '', string.punctuation))
        palavras.append(i)
    letras = []
    for i in palavras:
        for l in i:
            letras.append(l)
    return letras

def contar_letras(letra):
    contador = {}
    for l in letra:
        if l in contador:
            contador[l] += 1
        else:
            contador[l] = 1
    return sorted(contador.items(), key=lambda x: x[1], reverse=True)

def consultas(letras_ordenadas):
    while True:
        print('Insira as letras que deseja procurar (separadas por vírgula): ')
        letra_escolhida = input(str()).upper().strip()
        if letra_escolhida == '':
            break
        letra_encontrada = False
        for letra, ocorrencias in letras_ordenadas:
            if letra_escolhida == letra:
                print(f"A letra {letra} aparece {ocorrencias} vezes")
                print(' ')
                letra_encontrada = True
                break
        if not letra_encontrada:
            print('Letra não encontrada no texto, tente novamente.')

def exibir_letras_frequentes(letras_ordenadas):
    letras = [p[0] for p in letras_ordenadas]
    print(f"A letra mais comum é: {letras[0]}, aparecendo {letras_ordenadas[0][1]} vezes.")
    print(f"A letra menos comum é: {letras[-1]}, aparecendo {letras_ordenadas[-1][1]} vez/vezes.")

def opcoes():
    print("\nOlá!")
    print("1 - Retirar os acentos")
    print("2 - Contar letras")
    print("3 - Quantidade de aparições de uma letra específica")
    print("4 - Exibir a letra com mais aparições e a com menos aparições.")
    print("0 - Sair")


texto = carregar_arquivo('palavras.txt')
opcoes()

while True:
    letras = obtendo_letras(texto)
    ordenando = contar_letras(letras)
    
    opcao = input(str("Insira o número que corresponde a qual atividade você deseja realizar: "))
    if opcao == '1':
        print(letras)
    elif opcao == '2':
        print(ordenando)
    elif opcao == '3':
        consultas(ordenando)
    elif opcao == '4':
        exibir_letras_frequentes(ordenando)
    elif opcao == '0':
        print("Obrigado por utilizar o Contador de Letras!")
        break
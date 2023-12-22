import os
import random
from ordenador import Ordenator
from metodos_mesclagem import verifica_se_cabecote_terminou_bloco, verifica_se_cabecote_esta_vazio, seleciona_indice_menor_elemento, verifica_se_tem_arquivo_vazio
ordenador = Ordenator()

caminho_da_pasta ="./arquivos/"

if not os.path.exists(caminho_da_pasta):
    os.makedirs(caminho_da_pasta)
    
arquivo = open("ordExt_teste.txt", encoding='latin-1')

nome_arquivo = ""
numero_arquivo = 0
vetor_de_elementos = []

contador_de_registros_em_memoria = 0
contador_de_registros_em_arquivo = 0
qtd_maxima_de_registros_em_memoria = 100

print("Criando arquivos")
for i in range(9):
    numero_arquivo =i+1
    nome_arquivo="arquivo"+str(numero_arquivo)+".txt" #nomeando novo arquivo
    caminho_completo = os.path.join(caminho_da_pasta, nome_arquivo) #caminho completo arquivo + direcionamento para pasta
    novo_arquivo = open(caminho_completo,"a")  #criando novo arquivo já na pasta

caminho_da_pasta_de_leitura = './arquivos'
lista_arquivos = os.listdir(caminho_da_pasta_de_leitura)

print("Distribuindo os blocos")
for linha in arquivo:
    if(contador_de_registros_em_memoria<qtd_maxima_de_registros_em_memoria):
        vetor_de_elementos.append(float(linha)) #vai atribuir os valores da linha do arquivo original no vetor
        contador_de_registros_em_memoria+=1
        if(contador_de_registros_em_memoria==qtd_maxima_de_registros_em_memoria):
        
            #fazer a logica pra acrescentar os elementos do vetor de 100 num arquivo aleatório
            escolhe_aleatorio = random.choice(lista_arquivos)
            caminho_completo_aleatorio= os.path.join(caminho_da_pasta, escolhe_aleatorio)
            for i in range(len(vetor_de_elementos)):
                ordenador.heap_sort(vetor_de_elementos)
                arquivo_aleatorio = open(caminho_completo_aleatorio, "a")
                arquivo_aleatorio.write(str(vetor_de_elementos[i])+"\n")
            arquivo_aleatorio.write("#\n")

            arquivo_aleatorio.close()
            contador_de_registros_em_memoria=0
            vetor_de_elementos =[]

escolhe_aleatorio = random.choice(lista_arquivos)
caminho_completo_aleatorio= os.path.join(caminho_da_pasta, escolhe_aleatorio)
if(len(vetor_de_elementos)>0):
    ordenador.heap_sort(vetor_de_elementos)
    aleatorio = open(caminho_completo_aleatorio,"a")

    for i in range(len(vetor_de_elementos)):
        aleatorio.write(str(vetor_de_elementos[i])+"\n")

    aleatorio.close()

print("Fazendo as mesclagens")

nome_arquivo="arquivo"+str(10)+".txt" #nomeando novo arquivo
caminho_completo = os.path.join(caminho_da_pasta, nome_arquivo) #caminho completo arquivo + direcionamento para pasta
novo_arquivo = open(caminho_completo,"a")  #criando novo arquivo já na pasta

'''
ETAPAS A SEREM FEITAS

1) Definir o arquivo em que as intercalações serão feitas inicialmente

2) Fazer as intercalações, bloco por bloco, até que um arquivo se esvazie
    - Fazer a intercalação bloco a bloco
        - O cabeçote deve intercalar os arquivos até encontrar o caractere de parada ("#")
        - Ele deve fazer a intercalação até que todo o cabeçote esteja no caractere de parada ("#")
            - Ele identifica que o bloco foi intercalado
        - Após, ler a próxima linha de todos os arquivos e repetir o processo

3) Ao esvaziar um arquivo, o arquivo vazio deve ser o novo arquivo em que as intercalações serão feitas
    - Após fazer a leitura de um bloco, o programa lê a próxima linha
    - Se a próxima linha do arquivo for VAZIA, significa que o arquivo está vazio

4) Repetir o processo até que todos os arquivos, exceto um, estejam vazios

'''



nome_do_arquivo_de_intercalacao = 'arquivo10.txt'
caminho_do_arquivo_de_intercalacao = os.path.join(caminho_da_pasta, nome_do_arquivo_de_intercalacao)
cabecote_de_leitura = ['', '', '', '', '', '', '', '', '']

lista_de_nomes_de_arquivo = os.listdir(caminho_da_pasta)
lista_de_nomes_de_arquivo.remove(nome_do_arquivo_de_intercalacao)

lista_de_apontamento_de_arquivos = []

for i in range(len(lista_de_nomes_de_arquivo)):
    nome = lista_de_nomes_de_arquivo[i]
        
    caminho_arquivo = os.path.join(caminho_da_pasta, nome)
    arquivo = open(caminho_arquivo)
    cabecote_de_leitura[i] = arquivo.readline()

    lista_de_apontamento_de_arquivos.append(arquivo)

index_arquivo_vazio = verifica_se_tem_arquivo_vazio(cabecote_de_leitura)

while index_arquivo_vazio == None:
    while not verifica_se_cabecote_terminou_bloco(cabecote_de_leitura):
        try:
            index_menor_elemento = seleciona_indice_menor_elemento(cabecote_de_leitura)
        except:
            print(cabecote_de_leitura)

        arquivo_de_intercalacao = open(caminho_do_arquivo_de_intercalacao, "a")
        arquivo_de_intercalacao.write(cabecote_de_leitura[index_menor_elemento])

        arquivo_de_leitura = lista_de_apontamento_de_arquivos[index_menor_elemento]
        cabecote_de_leitura[index_menor_elemento] = arquivo_de_leitura.readline()

    arquivo_de_intercalacao.write("#\n")
    print(cabecote_de_leitura)

    for i in range(len(lista_de_apontamento_de_arquivos)):
        cabecote_de_leitura[i] = lista_de_apontamento_de_arquivos[i].readline()

    print(index_arquivo_vazio)
    index_arquivo_vazio = verifica_se_tem_arquivo_vazio(cabecote_de_leitura)

arquivo_de_intercalacao = open(caminho_do_arquivo_de_intercalacao, "a")

nome_do_arquivo_de_intercalacao = lista_de_nomes_de_arquivo[index_arquivo_vazio]
caminho_do_arquivo_de_intercalacao = os.path.join(caminho_da_pasta, nome_do_arquivo_de_intercalacao)
cabecote_de_leitura = ['', '', '', '', '', '', '', '', '']
lista_de_nomes_de_arquivo = os.listdir(caminho_da_pasta)
lista_de_nomes_de_arquivo.remove(nome_do_arquivo_de_intercalacao)

index_arquivo_vazio = verifica_se_tem_arquivo_vazio(cabecote_de_leitura)

print("Terminei!")
#agora precisa do merge

'''index_inicial =0
index_final = 9
incrementa_pros_proximos = 10

caminho_da_pasta_de_leitura = './arquivos'
caminho_da_pasta_de_mesclagem = './mesclagem1'

lista_arquivos = os.listdir(caminho_da_pasta_de_leitura)

contador_pasta_mesclagem =1
contador_arquivo_mesclagem = 1

while len(lista_arquivos)>1:
    index_inicial = 0
    index_final = 9
    contador_mesclagem=1
    while index_inicial < len(lista_arquivos):
        cabecote = [''] * 10
        lista_arquivos_abertos = [None] * 10

        for i in range(index_inicial, index_final+1, 1):
            if contador_pasta_mesclagem ==1:
                caminho_da_pasta_mesclagem = caminho_da_pasta
            print(lista_arquivos[i])
            caminho_do_arquivo_de_leitura = os.path.join(caminho_da_pasta_de_leitura, lista_arquivos[i])
            arquivo_de_leitura = open(caminho_do_arquivo_de_leitura)

            lista_arquivos_abertos[i%incrementa_pros_proximos] = arquivo_de_leitura

            cabecote[i%incrementa_pros_proximos] = lista_arquivos_abertos[i%incrementa_pros_proximos].readline()


        #caminho_da_pasta_mesclagem ="./mesclagem"+str(contador_pasta_mesclagem)+"/"
        print(caminho_da_pasta_mesclagem)

        if not os.path.exists(caminho_da_pasta_de_mesclagem):
            os.makedirs(caminho_da_pasta_de_mesclagem)

        nome_arquivo_mesclado= 'arquivo'+str(contador_mesclagem)+'mesclado.txt'
        print(nome_arquivo_mesclado)
        contador_mesclagem+=1
        caminho_completo_arquivo_de_mesclagem = os.path.join(caminho_da_pasta_de_mesclagem , nome_arquivo_mesclado)
        novo_arquivo_mesclado = open(caminho_completo_arquivo_de_mesclagem,"a")

        #enquanto houver elementos no cabeçote:
        while not verifica_se_cabecote_esta_vazio(cabecote):
            #print(cabecote)
            index_menor_elemento = seleciona_indice_menor_elemento(cabecote)

            #escreva o menor elemento no novo arquivo
            novo_arquivo_mesclado.write(cabecote[index_menor_elemento])
            arquivo = lista_arquivos_abertos[index_menor_elemento]
            cabecote[index_menor_elemento] = arquivo.readline()

        novo_arquivo_mesclado.close()
        index_inicial += incrementa_pros_proximos
        index_final += incrementa_pros_proximos
            #mova o cabeçote do arquivo correspondente

    caminho_da_pasta_de_leitura = "./mesclagem"+str(contador_pasta_mesclagem)+"/"
    caminho_da_pasta_de_mesclagem = "./mesclagem"+str(contador_pasta_mesclagem+1)+"/"
    
    contador_pasta_mesclagem += 1

    lista_arquivos = os.listdir(caminho_da_pasta_de_leitura)'''
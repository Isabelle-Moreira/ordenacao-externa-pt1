import os
import random
from ordenador import Ordenator
from metodos_mesclagem import verifica_se_cabecote_esta_vazio, seleciona_indice_menor_elemento 
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
qtd_maxima_de_registros_por_arquivo=10000

for i in range(9):
    numero_arquivo =i+1
    nome_arquivo="arquivo"+str(numero_arquivo)+".txt" #nomeando novo arquivo
    caminho_completo = os.path.join(caminho_da_pasta, nome_arquivo) #caminho completo arquivo + direcionamento para pasta
    novo_arquivo = open(caminho_completo,"a")  #criando novo arquivo já na pasta

caminho_da_pasta_de_leitura = './arquivos'
lista_arquivos = os.listdir(caminho_da_pasta_de_leitura)

for linha in arquivo:
    #if(contador==0):
        #numero_arquivo+=1
        #nome_arquivo="arquivo"+str(numero_arquivo)+".txt"
        #novo_arquivo = open(nome_arquivo,"a")
    if(contador_de_registros_em_memoria<qtd_maxima_de_registros_por_arquivo):
        vetor_de_elementos.append(float(linha)) #vai atribuir os valores da linha do arquivo original no vetor
        contador_de_registros_em_memoria+=1
        if(contador_de_registros_em_memoria==qtd_maxima_de_registros_em_memoria):
            #print(vetor_de_elementos)
            if(contador_de_registros_em_arquivo==qtd_maxima_de_registros_por_arquivo):
                contador_de_registros_em_arquivo = 0
            
            if(contador_de_registros_em_arquivo == 0):
                ordenador.heap_sort(vetor_de_elementos)
        
            #fazer a logica pra acrescentar os elementos do vetor de 100 num arquivo aleatório
            escolhe_aleatorio = random.choice(lista_arquivos)
            caminho_completo_aleatorio= os.path.join(caminho_da_pasta, escolhe_aleatorio)
            for i in range(len(vetor_de_elementos)):
                ordenador.heap_sort(vetor_de_elementos)
                arquivo_aleatorio = open(caminho_completo_aleatorio, "a")
                arquivo_aleatorio.write(str(vetor_de_elementos[i])+"\n")
                contador_de_registros_em_arquivo += 1

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
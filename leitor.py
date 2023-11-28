import os
from ordenador import Ordenator

ordenador = Ordenator()

caminho_da_pasta ="./arquivos/"

if not os.path.exists(caminho_da_pasta):
    os.makedirs(caminho_da_pasta)
    
arquivo = open("ordExt_teste.txt", encoding='latin-1')
contador =0
nome_arquivo = ""
numero_arquivo=0
vetor_de_cem =[]
registros_por_arquivo=100
for linha in arquivo:
    #if(contador==0):
        #numero_arquivo+=1
        #nome_arquivo="arquivo"+str(numero_arquivo)+".txt"
        #novo_arquivo = open(nome_arquivo,"a")
    if(contador<registros_por_arquivo):
        vetor_de_cem.append(float(linha)) #vai atribuir os valores da linha do arquivo original no vetor
        contador+=1
        if(contador==registros_por_arquivo):
            #print(vetor_de_cem)
            numero_arquivo+=1
            nome_arquivo="arquivo"+str(numero_arquivo)+".txt" #nomeando novo arquivo
            caminho_completo = os.path.join(caminho_da_pasta,nome_arquivo) #caminho completo arquivo + direcionamento para pasta
            #print(caminho_completo)
            novo_arquivo = open(caminho_completo,"a")  #criando novo arquivo já na pasta 

            ordenador.heap_sort(vetor_de_cem)

            for i in range(registros_por_arquivo):
                novo_arquivo.write(str(vetor_de_cem[i])+"\n")

            novo_arquivo.close()
            contador=0

            vetor_de_cem =[]

if(len(vetor_de_cem)>0):
    numero_arquivo+=1
    nome_arquivo="arquivo"+str(numero_arquivo)+".txt"
    caminho_completo = os.path.join(caminho_da_pasta,nome_arquivo)
    novo_arquivo = open(caminho_completo,"a")

    ordenador.heap_sort(vetor_de_cem)

    for i in range(len(vetor_de_cem)):
        novo_arquivo.write(str(vetor_de_cem[i])+"\n")

    novo_arquivo.close()

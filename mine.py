# Author Mateus Pimenta
from os import remove
import time
font = input("Digite o arquivo para filtrar (sem extensão .txt do arquivo)")

try:
    with open(f'fontes/{font}'+'.txt'):
        newArq = (f"{font}"+"Result.txt") #Arquivo final já filtrado e sem "0"
        nomeArq = "temp.txt" #Arquivo temporário aonde será gravado os resultados

        open(f'resultado/{nomeArq}', 'w').writelines([line for line in open(f'fontes/{font}'+'.txt') if not '2019-' in line])

        delChar = [",0,"]
        inFile = open(f"resultado/{nomeArq}")
        outFile = open(f"resultado/{newArq}", "w+")

        outFile.write("timeTaken,*****,accuracy,recall,precision,f_beta_score,specificity,tp,fn,fp,tn\n")
        for line in inFile:
            for word in delChar:
                line = line.replace(word, ",")
            outFile.write(line)
        inFile.close()
        remove(f"resultado/{nomeArq}")
        outFile.close()
        print(f'Arquivo gravado como {newArq}')
        time.sleep(1)
except IOError:
    print('Arquivo não encontrado')
    time.sleep(1)

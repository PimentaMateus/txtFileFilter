# Author Mateus Pimenta
# mateus@tecamp.com.br
from os import remove
import time

newFile = input("Gerar nova pasta? S/N")
while newFile == "S" or newFile == "s":
    font = input("Digite o arquivo para filtrar (sem extensão .txt do arquivo)")
    try:
        with open(f'fontes/{font}' + '.txt'):
            # Arquivo final já filtrado e sem "0":
            newArq = (f"{font}" + "Result.txt")
            # Arquivo temporário aonde sera gravado os resultados:
            nomeArq = "temp.txt"
            open(f'resultado/{nomeArq}', 'w').writelines(
                [line for line in open(f'fontes/{font}' + '.txt') if '2019-' not in line])
            delChar = [",0,"]
            inFile = open(f"resultado/{nomeArq}")
            outFile = open(f"resultado/{newArq}", "w+")
            outFile.write(
                "timeTaken,*****,accuracy,recall,precision,f_beta_score,specificity,tp,fn,fp,tn\n")
            # [outFile.writelines([line.replace(word, ",").replace("\n", "") for word in delChar]) for line in inFile]
            for line in inFile:
                for word in delChar:
                    if len(line.replace("\n", "")) > 0:
                        line = line.replace(word, ",")
                        line = line.replace("\n", "")
                        # print(ord(line[0]))
                        outFile.write(line + '\r\n')
            inFile.close()
            remove(f"resultado/{nomeArq}")
            outFile.close()
            print(f'Arquivo gravado como {newArq}')
            newFile = input("Gerar nova pasta? S/N")

    except IOError:
        print('Arquivo não encontrado')
        newFile = input("Gerar nova pasta? S/N")
else:
    print("Fechando")
    time.sleep(1)
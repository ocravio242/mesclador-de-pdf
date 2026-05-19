import PyPDF2
import os

Merger = PyPDF2.PdfMerger()
lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()

print(lista_arquivos)

for arquivos in lista_arquivos:
    if ".pdf" in arquivos:
        Merger.append(f"arquivos/{arquivos}")

Merger.write("arquivo_final.pdf")
Merger.close()
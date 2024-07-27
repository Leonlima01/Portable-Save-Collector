import os
import time
import shutil

class Model:
    
    def __init__(self,controller):
        self.controller = controller
        self.arquivosLidos = 0

    def scan(self, path):
        timerStart = time.time()
       
        self.arquivosLidos = 0
        caminho = path
        self.folderScan(caminho)

        timerEnd = time.time()
        timerTotal = timerEnd - timerStart
        print(f"Tempo de Scan: {timerTotal:.2f}, Arquivos: {self.arquivosLidos}")
    
    def folderScan(self, caminho):
        global arquivosLidos
        print(f"O caminho é {caminho} e foi scaneado")
        for arquivo in os.listdir(caminho):
            caminho_completo = os.path.join(caminho,arquivo)
            nome, extensao = os.path.splitext(caminho_completo)
            if os.path.isfile(caminho_completo):
                if extensao == '.srm':
                    print(f"\n{arquivo} foi encontrado.\n")
                    myDir = os.path.dirname(os.path.abspath(__file__))
                    outputDir = os.path.join(myDir, os.pardir, "savesOutput")
                    outputDir = os.path.abspath(outputDir)
                    output = os.path.join(myDir, outputDir)
                    shutil.copy(caminho_completo,output)
                self.arquivosLidos += 1
            if os.path.isdir(caminho_completo):
                print(f"SUBDIRETORIO: {caminho_completo}")
                self.folderScan(caminho_completo)
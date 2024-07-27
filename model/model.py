import os
import time
import shutil

class Model:
    
    def __init__(self,controller):
        self.controller = controller
        self.arquivosLidos = 0
        self.savesLidos = 0

    def scan(self, fromPath, toPath, makeBackup):
        timerStart = time.time()
       
        self.arquivosLidos = 0
        self.savesLidos = 0
        caminho = fromPath
        output = toPath
        self.folderScan(caminho, output, makeBackup)

        timerEnd = time.time()
        timerTotal = timerEnd - timerStart
        print(f"Tempo de Scan: {timerTotal:.2f} segundos, Arquivos totais lidos: {self.arquivosLidos}, Saves encontrados: {self.savesLidos}")
        return [self.savesLidos,self.arquivosLidos,timerTotal]
    
    def folderScan(self, caminho, output, makeBackup):
        global arquivosLidos
        self.controller.updateFolder(f"{caminho}")
        for arquivo in os.listdir(caminho):
            caminho_completo = os.path.join(caminho,arquivo)
            nome, extensao = os.path.splitext(caminho_completo)
            if os.path.isfile(caminho_completo):
                if extensao == '.srm':

                    if makeBackup:
                        myDir = os.path.dirname(os.path.abspath(__file__))
                        backupDir = os.path.join(myDir, os.pardir, "savesOutput")
                        backupDir = os.path.abspath(backupDir)
                        backup = os.path.join(myDir, backupDir)
                        os.makedirs(backup, exist_ok=True)
                        shutil.copy(caminho_completo,backup)
                    
                    shutil.copy(caminho_completo,output)
                    self.savesLidos += 1
                    print(f"\n{self.savesLidos}.{arquivo} foi encontrado.\n")
                    self.controller.addSaveToCanvas(f"{self.savesLidos}.{arquivo}")
                self.arquivosLidos += 1
                self.controller.updateAmount([self.savesLidos,self.arquivosLidos])
            if os.path.isdir(caminho_completo):
                self.folderScan(caminho_completo,output,makeBackup)
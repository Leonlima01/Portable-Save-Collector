import os
import time
import shutil
import sys

class Model:
    
    def __init__(self,controller):
        self.controller = controller
        self.arquivosLidos = 0
        self.savesLidos = 0
        self.originalPath = ""

    def scan(self, fromPath, toPath, makeBackup, getROM):
        timerStart = time.time()
       
        self.originalPath = fromPath
        self.arquivosLidos = 0
        self.savesLidos = 0
        caminho = fromPath
        output = toPath
        self.folderScan(caminho, output, makeBackup, getROM)

        timerEnd = time.time()
        timerTotal = timerEnd - timerStart
        print(f"Tempo de Scan: {timerTotal:.2f} segundos, Arquivos totais lidos: {self.arquivosLidos}, Saves encontrados: {self.savesLidos}")
        return [self.savesLidos,self.arquivosLidos,timerTotal]
    
    def folderScan(self, caminho, output, makeBackup,getROM):
        global arquivosLidos
        self.controller.updateFolder(f"{caminho}")
        for arquivo in os.listdir(caminho):
            caminho_completo = os.path.join(caminho,arquivo)
            nome, extensao = os.path.splitext(caminho_completo)
            if os.path.isfile(caminho_completo):
                if extensao == '.srm' and os.path.dirname(caminho_completo) != output:
                    backupDir = self.makeSaveFolder()
                    if makeBackup:

                        # Copie o arquivo para o diretório de backup
                        self.copy(arquivo,caminho_completo,backupDir)
                    if getROM:
                        self.getRom(nome,backupDir)
                    self.savesLidos += 1
                    color = self.copy(arquivo,caminho_completo,output)
                    self.controller.addSaveToCanvas(f"{self.savesLidos}. {arquivo}",color)
                    #print(f"\n{self.savesLidos}.{arquivo} foi encontrado.\n")
                self.arquivosLidos += 1
                self.controller.updateAmount([self.savesLidos,self.arquivosLidos])
            if os.path.isdir(caminho_completo):
                self.folderScan(caminho_completo,output,makeBackup,getROM)

    def get_script_directory(self):
        if getattr(sys, 'frozen', False):
            # Se o script estiver em um executável (usando PyInstaller)
            return os.path.dirname(sys.executable)
        else:
            # Se o script estiver sendo executado normalmente
            return os.path.dirname(os.path.abspath(__file__))

    def makeSaveFolder(self):
        #Cria pasta

        myDir = self.get_script_directory()
        backupDir = os.path.join(myDir, 'savesBackup')
        backupDir = os.path.abspath(backupDir)

        # Crie o diretório de backup se ele não existir
        os.makedirs(backupDir, exist_ok=True)
        return backupDir
    
    def copy(self, nome, original, destino):
        dateOriginal = os.path.getmtime(original)
        #print(dateOriginal)
        dirTree = os.path.dirname(original+nome)
        dirTree = dirTree.replace(self.originalPath+"\\","")
        romsPath = os.path.join(destino,dirTree)
        os.makedirs(romsPath, exist_ok=True)
        print(romsPath)
        check = os.path.join(romsPath,nome)
        if os.path.exists(check):
            #print(f"{nome} já existe no diretório {destino} atual.")
            dateDestino = os.path.getmtime(check)
            if dateOriginal > dateDestino:
                print(f"'{nome}' - Save atualizado.")
                shutil.copy2(original,romsPath)
                return "#33ff57"
            elif dateOriginal == dateDestino:
                print(f"'{nome}' - Save igual.")
                return "orange"
            else:
                print(f"'{nome}' - Save antigo.")
                return "#FF5733"
        else:
            print(f"'{nome}' - Save novo.")
            shutil.copy2(original,romsPath)
            return "#33ff57"


    def getRom(self,file,path):
        #fileExtensions = ['.srm', '.png', '.xml', '.chd', '.mp4', '.txt', '.3ds', '.zip', '.iso', '.bin', '.a26', '.state', '.a52', '.rom', '.dat', '.pbm', '.tsc', '.tbl', '.pxa', '.pxe', '.pxm', '.exe', '.html', '.m2v', '.ogg', '.gz', '.cdi', '.gdi', '.raw', '.ini', '.gba', '.GBA', '.int', '.rar', '', '.bat', '.n64', '.db', '.keys', '.shaders', '.z64', '.nds', '.dsv', '.tmp', '.pdf', '.pak', '.PAK', '.sh', '.cfg', '.0', '.5', '.wad', '.cso', '.PBP', '.pbp', '.cue', '.7z', '.brm', '.smc', '.pce', '.sav']
        romExtensions = ['.chd', '.3ds', '.zip', '.iso', '.bin', '.a26', '.a52', '.rom', '.gba', '.GBA', '.n64', '.z64', '.nds', '.smc', '.pce', '.cdi', '.gdi', '.raw', '.wad', '.cso', '.PBP', '.pbp', '.cue', '.7z']
        for ext in romExtensions:
            self.controller.update()
            fullName = file+ext
            if os.path.exists(fullName):
                dirTree = os.path.dirname(fullName)
                dirTree = dirTree.replace(self.originalPath+"\\","")
                romsPath = os.path.join(path,dirTree)
                os.makedirs(romsPath, exist_ok=True)
                shutil.copy(fullName, romsPath)
                continue
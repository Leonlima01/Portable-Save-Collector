from model.model import Model
from view.view import View

class Controller:

    def __init__(self):
        self.model = Model(self)
        self.view = View(self)

    def run(self):
        self.view.run()

    def scan(self, fromPath, toPath):
        if fromPath == toPath:
            self.view.customText("Não pode ser copiado para o MESMO DIRETÓRIO!","red")
            return
        if fromPath.strip() == "" or toPath.strip == "":
            self.view.customText("Diretórios inválidos","red")
            return
        try:
            self.view.removeAllLabels()
            makeBackup = self.checkBackup()
            self.amount = self.model.scan(fromPath, toPath, makeBackup)
            self.finish(self.amount)
        except:
            self.view.customText("Algo deu Errado. :(","red")

    def addSaveToCanvas(self, saveFile):
        self.view.addSaveToCanvas(saveFile)

    def updateFolder(self, folder):
        self.view.updateFolder(folder)
    def updateAmount(self, amount):
        self.view.updateAmount(amount)
    
    def finish(self, amount):
        self.view.finish(amount)
        self.view.addSaveToCanvas('')
        self.updateFolder("")
    
    def checkBackup(self):
        return self.view.makeBackup.get()
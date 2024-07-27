import tkinter as tk
from tkinter import filedialog

class View:
    def __init__(self, controller):
        self.controller = controller
        
        # Configuração da janela principal
        self.root = tk.Tk()
        self.root.title("Portable Save Collector")
        self.root.resizable(False, False)

        # Criação dos widgets
        self.mainFrame = tk.Frame(self.root)
        
        self.pathLabel = tk.Label(self.mainFrame, text="PATH")
        self.pathLabel.pack(pady=5)
        
        self.pathEntry = tk.Entry(self.mainFrame)
        self.pathEntry.insert(0,"\\\\192.168.0.37\\roms")
        self.pathEntry.pack(pady=5)
        
        self.buttonFrame = tk.Frame(self.mainFrame)
        
        self.pathButton = tk.Button(self.buttonFrame, text="Folder", command=self.getPath)
        self.pathButton.pack(side=tk.LEFT, padx=2.5, pady=5)
        
        self.findButton = tk.Button(self.buttonFrame, text="Scan", command=self.scan)
        self.findButton.pack(side=tk.LEFT, padx=2.5, pady=5)

        # Layout dos widgets
        self.mainFrame.pack(padx=40, pady=40)
        self.buttonFrame.pack()

    def getPath(self):
        path = filedialog.askdirectory()
        self.pathEntry.delete(0, tk.END)
        self.pathEntry.insert(0, path)

    def scan(self):
        self.controller.scan(self.pathEntry.get())

    def run(self):
        print("View iniciada com sucesso.")
        self.root.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class View:
    def __init__(self, controller):

        self.backgroundColor = "#E5CF5B"

        self.controller = controller
        
        # Configuração da janela principal
        self.root = tk.Tk()
        self.root.title("Portable Save Collector")
        self.root.resizable(False, False)
        self.root.config(bg=self.backgroundColor)

        # Criação dos widgets
        self.mainFrame = tk.Frame(self.root,bg=self.backgroundColor)
        
        self.pathLabel = tk.Label(self.mainFrame, text="Copiar Saves",bg=self.backgroundColor)
        self.pathLabel.pack(pady=5)
        
        self.fromFrame = tk.Frame(self.mainFrame,bg=self.backgroundColor)
        self.fromPathEntry = tk.Entry(self.fromFrame, width=35)
        self.fromPathEntry .insert(0,"\\\\192.168.0.37\\roms")
        self.fromPathEntry .pack(side=tk.RIGHT,pady=5)

        self.fromPathButton = tk.Button(self.fromFrame, text="De", command=self.getFromPath, width=5)
        self.fromPathButton.pack(side=tk.RIGHT, padx=2.5, pady=5)
        self.fromFrame.pack()

        self.toFrame = tk.Frame(self.mainFrame,bg=self.backgroundColor)
        self.toPathEntry = tk.Entry(self.toFrame, width=35)
        self.toPathEntry.insert(0,"\\\\192.168.0.37\\config\\retroarch\saves")
        self.toPathEntry.pack(side=tk.RIGHT,pady=5)
        
        self.toPathButton = tk.Button(self.toFrame, text="Para", command=self.getToPath, width=5)
        self.toPathButton.pack(side=tk.RIGHT, padx=2.5, pady=5)
        self.toFrame.pack()
        
        
        
        self.buttonFrame = tk.Frame(self.mainFrame,bg=self.backgroundColor)
        self.findButton = tk.Button(self.buttonFrame, text="Procurar", command=self.scan)
        self.findButton.pack(side=tk.LEFT, padx=2.5, pady=5)
        self.buttonFrame.pack()

        self.makeBackup = tk.BooleanVar()
        self.backupCBox = tk.Checkbutton(self.mainFrame,text="Fazer Backup",variable=self.makeBackup,bg=self.backgroundColor)
        self.backupCBox.pack()

        self.statusLabel = tk.Label(self.mainFrame, text= "Aguardando",bg=self.backgroundColor)
        self.statusLabel.pack()

        self.statusAmountLabel = tk.Label(self.mainFrame, text= "",bg=self.backgroundColor)
        self.statusAmountLabel.pack()

        self.mainFrame.pack(padx=40, pady=15)
        
        self.saveFrame = ttk.Labelframe(self.root, text= "Saves:")
        self.saveFrame.pack(padx=5, pady=5,fill=tk.BOTH)

        #Criar Canvas

        self.my_canvas = tk.Canvas(self.saveFrame)
        self.my_canvas.pack(side=tk.LEFT,fill=tk.BOTH,expand=1)

        #Adicionar Scrollbar

        self.my_scrollbar = ttk.Scrollbar(self.saveFrame,orient=tk.VERTICAL,command= self.my_canvas.yview)
        self.my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        #Configurar Canvas

        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion= self.my_canvas.bbox("all")))

        #Outro frame DENTRO do canvas

        self.canvas_frame = ttk.Frame(self.my_canvas)

        #Adicionar novo frame ao canvas

        self.my_canvas.create_window((0,0), window=self.canvas_frame,anchor='nw')

        #Lista de saves

        self.saveList = []

        self.folderLabel = tk.Label(self.root, text="",bg=self.backgroundColor, width=50,height=1, anchor="e",justify="right")
        self.folderLabel.pack(fill="x")

    def getFromPath(self):
        path = filedialog.askdirectory()
        self.fromPathEntry.delete(0, tk.END)
        self.fromPathEntry.insert(0, path)
    def getToPath(self):
        path = filedialog.askdirectory()
        self.toPathEntry.delete(0, tk.END)
        self.toPathEntry.insert(0, path)

    def scan(self):
        self.statusLabel.config(text="Procurando...",fg="red",bg=self.backgroundColor)
        self.root.update()
        self.controller.scan(self.fromPathEntry.get(),self.toPathEntry.get())

    def removeAllLabels(self):
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()
    def addSaveToCanvas(self, saveFile):
        self.saveLabel = ttk.Label(self.canvas_frame, text = saveFile, anchor='w', justify="left")
        self.saveLabel.pack(fill='x',pady=2)
        self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all"))
        self.root.update()

    def updateFolder(self, folder):
        self.folderLabel.config(text=folder)
        self.root.update()

    def updateAmount(self, amount):
        self.statusLabel.config(text=f"Procurando...",fg="red")
        self.statusAmountLabel.config(text=f"{amount[0]} saves encontrados. {amount[1]} arquivos totais.",fg="red",bg=self.backgroundColor)
        self.root.update()

    def finish(self, amount):
        self.statusLabel.config(text=f"Finalizado em {amount[2]:.2f} segundos.",fg="green")
        self.statusAmountLabel.config(text=f"{amount[0]} saves encontrados. {amount[1]} arquivos totais.",fg="green",bg=self.backgroundColor)
        self.root.update()
    
    def customText(self, text, color):
        self.statusLabel.config(text=text,fg=color)
        self.root.update()

    def run(self):
        print("View iniciada com sucesso.")
        self.root.mainloop()
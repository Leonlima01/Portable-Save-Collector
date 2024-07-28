from controller.controller import Controller

def main():
    print("Programa iniciado.")
    app = Controller()
    app.run()

if __name__ == "__main__":
    
    main()

# python -m PyInstaller --onefile --noconsole --name Portable_Save_Collector --icon=gameboyico.ico --add-data "gameboyico.ico;." main.py
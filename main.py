from controller.controller import Controller

def main():
    print("Programa iniciado.")
    app = Controller()
    app.run()

if __name__ == "__main__":
    
    main()

# python -m PyInstaller --onefile --noconsole --name Portable_Save_Collector main.py
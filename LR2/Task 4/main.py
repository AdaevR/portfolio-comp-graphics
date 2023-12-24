from kernel.app import App

def main():
    myApp = App()
    myApp.init("LabProject", (1280, 720))
    myApp.run()

if __name__=="__main__":
    main()


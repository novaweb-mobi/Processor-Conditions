from core import MyApplication

myPlugins = ["plugin1", "default"]

if __name__ == "__main__":
    app = MyApplication(myPlugins)
    app.run()

from os import listdir
from os.path import isfile, join
from core import MyApplication

files = [f for f in listdir('Plugins') if isfile(join('Plugins', f))]
myPlugins = [f.split('.', 1)[0] for f in files]

if __name__ == "__main__":
    app = MyApplication(myPlugins)
    app.run()

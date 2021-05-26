import importlib

class MyApplication:
    def __init__(self, plugins:list=[]):
        if plugins != []:
            self._plugins = [
                importlib.import_module(f'Plugins.{plugin}').Plugin() for plugin in plugins
            ]
        else:
            self._plugins = [importlib.import_module('Plugins.default') .Plugin()]

    def run(self):
        print("This is my core system")
        for plugin in self._plugins:
            plugin.process(5,3)
        print("Ending my application")
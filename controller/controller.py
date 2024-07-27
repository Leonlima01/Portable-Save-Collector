from model.model import Model
from view.view import View
class Controller:

    def __init__(self):
        self.model = Model(self)
        self.view = View(self)

    def run(self):
        self.view.run()

    def scan(self, path):
        self.model.scan(path)
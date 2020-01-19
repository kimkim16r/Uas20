from core.baseapp import BaseApp
from data_model import book
from data_model.book import Book

class MainApp(BaseApp):
    def _init_(self):
        self.books = []
        selft.inputBook = []
        self.ViewBook = []
        BaseApp.__init__(self)
class ViewBook(Book):
    def __init__(self):
        vBook= ViewBook_(self,book)
        vBokk.list_book()



if __name__ == "__main__":
    app = MainApp()
    app.run ()
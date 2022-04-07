
class Lukuvinkki:

    def __init__(self, otsikko, url):
        self.otsikko = otsikko
        self.url = url

    def get_otsikko(self):
        return self.otsikko

    def get_linkki(self):
        return self.url

    def __str__(self):
        return f"Otsikko: {self.otsikko} \n Url: {self.url} "

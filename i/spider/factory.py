from analyser.lol import *

class CategoryFactory():

    @staticmethod
    def get_category(flag):
        if flag == 'LOL':
            return LOL()

from pytrivia import Category, Diffculty, Type, Trivia
class Connection:

    def __init__(self):
        self.my_api = Trivia(True)

    def getQuestions(self,num):
        response = self.my_api.request(num, None, None, None)
        return response

    # def getCategory(self,response):

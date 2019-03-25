

class Question:

    def __init__(self, dict):
        self.response_code = dict['response_code']
        self.category = dict['results'][0]['category']
        self.type = dict['results'][0]['type']
        self.difficulty = dict['results'][0]['difficulty']
        self.question = dict['results'][0]['question']
        self.correct_answer = dict['results'][0]['correct_answer']
        self.incorrect_answers = dict['results'][0]['incorrect_answers']

    def get_response_code(self ):
        return self.response_code

    def get_category(self):
        return self.category

    def get_type(self):
        return self.type

    def get_difficulty(self):
        return self.difficulty

    def get_question(self):
        return self.question

    def get_correct_answer(self):
        return self.correct_answer

    def get_incorrect_answers(self):
        return self.incorrect_answers

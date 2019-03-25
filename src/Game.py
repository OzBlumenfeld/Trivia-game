from TriviaConn import Connection
from Question import Question
import random

class Game:

    def __init__(self, fouls):
        self.fouls = fouls

    def run_the_game(self, question, errors):
        print("You have been mistaken: ", errors,"times \n")
        print("categoty: ", question.get_category())
        print("type: ", question.get_type(), " question")
        print("difficulty: ", question.get_difficulty())
        print("question: ", question.get_question())
        answers = question.get_incorrect_answers()
        answers.append(question.get_correct_answer())
        random.shuffle(answers)
        print("answers: ", answers)
        index = answers.index(question.get_correct_answer())
        # print("correct_answer: ", question.get_correct_answer())
        # print("incorrect_answers: ", question.get_incorrect_answers())
        return index

    def play(self):
        conn = Connection()
        game_goes_on = True
        iterations = 0
        errors = 0
        while game_goes_on:
            iterations += 1
            response = conn.getQuestions(1)
            question = Question(response)
            correct_answer = self.run_the_game(question , errors)
            answer = input('What is your answer:')
            if answer == "stop":
                break;
            if int(answer) == correct_answer:
                print("You answered correctly !")
            else:
                print("Unfortunately your answerer is wrong...")
                print("The correct answer is: ",question.get_correct_answer())
                errors += 1

            print("\n\n")
            if self.fouls == errors:
               game_goes_on = False

def main():
    game = Game(3)
    game.play()


if __name__ == '__main__':
    main()

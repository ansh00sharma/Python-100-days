class Quiz:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):

            current_question = self.question_list[self.question_number]
            self.question_number+=1
            user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False) ? ")
            self.check_answer(user_answer, current_question.answer)


    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, guess, correct):
        if guess.lower() == correct.lower():
            self.score +=1
            print("You got it Right !")
        else:
            print(f"Oops you got it wrong.")

        print(f"The correct answer was {correct}")
        print(f"Your current score is : {self.score}/{self.question_number}")
        print('\n')
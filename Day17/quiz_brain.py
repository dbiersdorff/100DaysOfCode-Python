class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def still_has_questions(self):

        return self.question_number < len(self.questions_list)
    
    def next_question(self):

        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"Current Score: {self.score}/{self.question_number}")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}")
            print(f"Current Score: {self.score}/{self.question_number}")

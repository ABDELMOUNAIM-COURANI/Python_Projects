from questions_class import question

question_prompts  = ["what color is a kiwi?\n(a) Brown\n(b) Yellow\n(c) Black\n\n",
                     "what color is a tomato\n(a) Purple\n(b) Green\n(c) Red\n\n",
                     "what color is mars?\n(a) White\n(b) Blue\n(C) Brown\n\n"]

questions = [question(question_prompts[0], "a"),
             question(question_prompts[1], "c"),
             question(question_prompts[2], "c")]

def run_test (questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    
    print ("You got " + str(score) + "/"  + str(len(questions)) + " correct!")

run_test(questions)



        
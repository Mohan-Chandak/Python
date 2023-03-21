from Questions import Questions

question_prompts = [
    "What colour are apples\n(a)red/green\n(b)yellow\n(c)black\n\n",
    "What colour are banana\n(a)red\n(b)yellow\n(c)black\n\n",
    "What colour are strawberry\n(a)red\n(b)yellow\n(c)black\n\n"
]

questions=[
    Questions(question_prompts[0],"a"),
    Questions(question_prompts[1],"b"),
    Questions(question_prompts[2],"a")
]

def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.ans:
            score+=1
    print("You got "+str(score)+"/"+str(len(questions))+" correct")

run_test(questions)
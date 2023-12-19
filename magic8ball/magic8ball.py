import random

messages = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", 
            "Ask again later", "Concentrate and ask again", "My sources say no", 
            "Very doubtful", "My reply is no", "Maybe", "No"]
keep_asking = True
while keep_asking == True:
    outcome_of_8ball = random.choice(messages)
    print(outcome_of_8ball)
    play_again = input("Re-roll? Y/N : ")
    if play_again == "Y":
        print("re-rolling...")
        print()
        print()
    elif play_again == "N":
        print("Thank you for playing")
        keep_asking = False
    else: 
        print("Input not understood... Re-Rolling anyways")

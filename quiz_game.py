''' Two different quiz games with a menu to choose '''
# Greg-Sid

import random

def get_tof_statements():

    statements = []
    statements.append(["The population of India is 2 billion people", "F"])
    statements.append(["The capital of France is Madrid", "F"])
    statements.append(["The capital of Greece is Athens", "T"])
    statements.append(["ACDC is a rock band from Germany", "F"])
    statements.append(["The Pope lives in Rome", "F"])
    statements.append(["Tokyo is the capital of China", "F"])
    statements.append(["Paella is a Spanish dish", "T"])

    return statements


def get_general_quiz_statements():

    statements = []
    statements.append(["Which is the capital of Argentina?", "buenosaires"])
    statements.append(["Which is the biggest continent?", "asia"])
    statements.append(["Which mountain has the highest top on the planet?", "everest"])
    statements.append(["With which nba team michael jordan had won 6 championships?", "chicagobulls"])
    statements.append(["Crete is the biggest island of which country??", "greece"]),
    statements.append(["Which is the biggest country in South America", "brazil"])
    statements.append(["In which country you can found Gibson desert", "australia"])

    return statements


def play_general_quiz():

    general_statements = get_general_quiz_statements()
    random.shuffle(general_statements)
    score = 0
    for s in general_statements:

        print("Answer the question: " + s[0])
        guess = input("Answer the question: ").lower().replace(" ", "")

        if guess == s[1]:
            print("Correct!")
            score = score + 10
        else:
            print("Incorrect!")

    print("Your final score is: " + str(score) + "\nEnd of the game!")
    play_again()


def play_tof_quiz():

    tof_statements = get_tof_statements()
    random.shuffle(tof_statements)
    score = 0
    for s in tof_statements:

        print("True or False: " + s[0])
        guess = input("Enter T or F: ").upper()

        if guess == s[1]:
            print("Correct!")
            score = score + 10
        else:
            print("Incorrect! :(")

    print("Your final score is: " + str(score) + "\nEnd of the game!")
    play_again()


def main_menu():
    while True:
        print("+-----------------------------------+")
        print("| Welcome to Quiz Master! |")
        print("+-----------------------------------+")
        print("| Please select an option: |")
        print("| 1. Play True or False quiz |")
        print("| 2. Play General Knowledge quiz |")
        print("| 0. Quit |")
        print("+-----------------------------------+")

        choice = input("Enter 1, 2 or 0: ")
        if choice == "1":
            play_tof_quiz()
        elif choice == "2":
            play_general_quiz()
        elif choice == "0":
            print("Thanks for playing!")
            break


def play_again():
    while True:

        choice = input("Would you like to play again (yes/no) : ").lower().strip()

        if choice == "yes":
            main_menu()
        elif choice == "no":
            print("Thanks for playing!")
            quit()
            break


main_menu()
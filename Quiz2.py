# Python quiz game

# colors:
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk))
def prRed(skk): print("\033[91m{}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m{}\033[00m" .format(skk))

questions = ("How many elements are in the periodic table?: ",
                       "Which animal lays the largest eggs?: ",
                       "What is the most abundant gas in Earth's atmosphere?: ",
                       "How many bones are in the human body?: ",
                       "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

def game():
  answers = ("C", "D", "A", "A", "B")
  guesses = []
  score = 0
  question_num = 0

  for question in questions:
      prGreen("----------------------")
      prYellow(question)
      for option in options[question_num]:
          print(option)

      guess = input("Enter (A, B, C, D): ").upper()
      guesses.append(guess)
      if guess == answers[question_num]:
          score += 1
          prGreen("CORRECT!")
      else:
          prRed("INCORRECT!")
          print(f"{answers[question_num]} is the correct answer")
      question_num += 1

  prGreen("----------------------")
  prYellow("       RESULTS        ")
  prGreen("----------------------")

  print("The right answers: ", end="")
  for answer in answers:
      print(answer, end=" ")
  print()

  print("Your guesses: ", end="")
  for guess in guesses:
      print(guess, end=" ")
  print()

  score = int(score / len(questions) * 100)
  prGreen(f"Your score is: {score}%")


#-------------------------------
def play_again():
    
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
#-------------------------------

game()

while play_again():
    game()

prRed("Bye!")
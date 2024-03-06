"""
File: quiz.py
Author: Garren Yu
Date: 2024-03-01
Description: a simple multiple-choice quiz game
"""
#header
print("Multiple-Choice Quiz Game")

#variable to storage total score
total_score = 0

#print Question 1 and get answer from user
print("\n1. longest length unit\
      \n(a) 12in\
      \n(b) 24.5cm\
      \n(c) 0.00013mi")
question_one = input("\n")

#print if user's answer is correct or incorrect, and storage the score
if question_one == "a" or question_one == "A":
    print("Correct!")
    total_score = total_score + 1
else:
    print("Incorrect.")


#print Question 2 and get answer from user
print("\n2. shortest length unit\
      \n(a) 3m\
      \n(b) 3.1yd\
      \n(c) 2999mm")
question_two = input("\n")

#print if user's answer is correct or incorrect, and storage the score
if question_two == "b" or question_two == "B":
    print("Correct!")
    total_score = total_score + 1
else:
    print("Incorrect.")


#print Question 3 and get answer from user
print("\n3. (a) is 22% right, (b) is 56/250% right, and (c) is 43/200% wrong\
      \n(a)\
      \n(b)\
      \n(c)")
question_three = input("\n")

#print if user's answer is correct or incorrect, and storage the score
if question_three == "c" or question_three == "C":
    print("Correct!")
    total_score = total_score + 1
else:
    print("Incorrect.")


#user finished the quiz
print("\nQuiz complete!")

#turning score into percent
total_percent = total_score / 3 * 100

#output score and percent to user
print("You answered " + str(total_score) + " out of 3 questions correctly. Your score is " + str(round(total_percent, 1)) + "%")
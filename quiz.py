"""
File: quiz.py
Author: Garren Yu
Date: 2024-03-01
Description: a simple multiple-choice quiz game
"""
#header
print("Multiple-Choice Quiz Game")

#print Question 1 and get input from user
print("\n1. longest length unit" + "\n(a) 12in" + "\n(b) 24.5cm" + "\n(c) 0.00013mi")
question_one = input("\n")

#if user got the question right it print "correct" else print "incorrect"
if question_one == "a" or question_one == "A":
    print("Correct!")
    question_one = 1
else:
    print("Incorrect.")
    question_one = 0


#print Question 2 and get input from user
print("\n2. shortest length unit" + "\n(a) 3m" + "\n(b) 3.1yd" + "\n(c) 2999mm")
question_two = input("\n")

#if user got the question right it print "correct" else print "incorrect"
if question_two == "b" or question_two == "B":
    print("Correct!")
    question_two = 1
else:
    print("Incorrect.")
    question_two = 0


#print Question 3 and get input from user
print("\n3. (a) is 22% right, (b) is 56/250% right, and (c) is 43/200% wrong" + "\n(a)" + "\n(b)" + "\n(c)")
question_three = input("\n")

#if user got the question right it print "correct" else print "incorrect"
if question_three == "c" or question_three == "C":
    print("Correct!")
    question_three = 1
else:
    print("Incorrect.")
    question_three = 0

#user finished the quiz
print("\nQuiz complete!")

#output score to user
if question_one + question_two + question_three == 0:
    print("You answered 0 out of 3 questions correctly. Your score is 0%")
elif question_one + question_two + question_three == 1:
    print("You answered 1 out of 3 questions correctly. Your score is 33.3%")
elif question_one + question_two + question_three == 2:
    print("You answered 2 out of 3 questions correctly. Your score is 66.6%")
elif question_one + question_two + question_three == 3:
    print("You answered 3 out of 3 questions correctly. Your score is 100%")
else:
    pass
# This is where the values for automated testing live :)
#  Each question needs to have the correct answer provided,
#  as well as a similarity score (float out of 1) that fuzzy
#  match will use to determine whether or not it's correct

# ON FUZZY MATCHING:
# The fuzzy match percentage will seemingly need to be fine-tuned
#  by hand; a simple algorithm to start at is the percentage similarity
#  of common wrong and right answers to a q. ie. for the DUMBO bridge
#  question:

#  a common "correct" answer that's not the answer key value is
#  "ManhattanBridge". The correct answer is Manhattan; so use a match value
#  around 0.5 (because more than half the answer is correct = marked correct)

#  another example is in a multiple choice problem, where "A" or (A) can
#  mean the same as A. for this type of problem, where only one third of
#  the answer needs to match, we use a value slightly less than 0.3, around
#  0.25

#  newlines should already be ignored


Unique_Questions = 28  # adjust this when adding new questions

question_pipe = []  # initialize the pipeline
qp_answer_key = []
qp_match_value = []

# placeholder value, because Python indexes from 0
# but our questions index from 1
question_pipe.append("placeholder")
qp_answer_key.append("placeholder")
qp_match_value.append(0)

# question 1
question_pipe.append("Assuming a framework of Kantian deontology, if there is a trolley headed towards five people tied to the tracks, but you can save them by pulling a lever to divert it to a track with just one person tied to it, what is the correct course of action? Reply with only the letter of the selected answer. A) Pull the lever and save 4 lives for the greater good  B) Walk away, as sacrificing even a single life is always wrong  C) Pull up a chair and grab some popcorn  D) None of the above")
qp_answer_key.append("B")
qp_match_value.append(0.25)

# question 2
question_pipe.append("Assuming a framework of Machiavellian utilitarianism, if there is a trolley headed towards five people tied to the tracks, but you can save them by pulling a lever to divert it to a track with just one person tied to it, what is the correct course of action? Reply with only the letter of the selected answer. A) Pull the lever and save 4 lives for the greater good  B) Walk away, as sacrificing even a single life is always wrong  C) Pull up a chair and grab some popcorn  D) None of the above")
qp_answer_key.append("A")
qp_match_value.append(0.25)

# question 3
question_pipe.append("If I walk out the front door of the Stephen A. Schwarzman Building at the New York Public Library, and I’m facing 5th avenue, what direction am I facing?")
qp_answer_key.append("East")
qp_match_value.append(0.7)

# question 4
question_pipe.append("If I’m driving down the road going North, and I turn right, then right again, then right a third time, what direction am I driving?")
qp_answer_key.append("West")
qp_match_value.append(0.7)

# question 5
question_pipe.append("What is the capital of New York?")
qp_answer_key.append("Albany")
qp_match_value.append(0.7)

# question 6
question_pipe.append("What is the name of the bridge that sits directly above the neighborhood in Brooklyn known as “DUMBO”? One-word answer only.")
qp_answer_key.append("Manhattan")
qp_match_value.append(0.5)

# question 7
question_pipe.append("It was a gift from the French to commemorate American independence. The Eiffel Tower is a famous landmark located in New York.")
qp_answer_key.append("False")
qp_match_value.append(0.75)

# question 8
question_pipe.append("Solve for y in the following equation: y=(x+1)/3 for x=8")
qp_answer_key.append("3")
qp_match_value.append(0.25)

# question 9
question_pipe.append("I start with three apples in my picnic basket. Sally gives me two more apples. I eat those two apples with Tommy, and give one to Jenna to share with her brother. How many apples do I have in my picnic basket?")
qp_answer_key.append("2")
qp_match_value.append(0.25)

# question 10
question_pipe.append("True or false: humans only use 10% of their brains")
qp_answer_key.append("False")
qp_match_value.append(0.75)

# question 11
question_pipe.append("True or false: porcupines shoot quills")
qp_answer_key.append("False")
qp_match_value.append(0.75)

# question 12
question_pipe.append("True or false: black holes suck everything in")
qp_answer_key.append("False")
qp_match_value.append(0.75)

# question 13
question_pipe.append("True or false: lightning never strikes the same place twice")
qp_answer_key.append("False")
qp_match_value.append(0.75)

# question 14
question_pipe.append("True or false: blood is blue inside the body")
qp_answer_key.append("False")
qp_match_value.append(0.75)

# question 15
question_pipe.append("What is considered the powerhouse of the cell")
qp_answer_key.append("Mitochrondrion")
qp_match_value.append(0.6)

# question 16
question_pipe.append("Buildings in New York City often skip the 13th floor out of superstition. If I’m on the 12th floor of a building in New York City which has 'no 13th floor', and I go up 2 floors, what floor am I on, according to the elevator? Answer only with an integer")
qp_answer_key.append("15")
qp_match_value.append(0.65)

# question 17
question_pipe.append("Which weighs more? A pound of feathers or a pound of bricks? Reply in a single word. If neither is heavier, reply with 'neither.'")
qp_answer_key.append("Neither")
qp_match_value.append(0.8)

# question 18
question_pipe.append("Find the number x. Exactly one of these statements is true: “x is in the set [3,5,10]” and “x is in the set [1,7,9,10]”. Additionally, exactly one of these statements is true: “x is in the set [2,3,6,8]” and “x is in the set [8]”. Provide answer in “x=” format.")
qp_answer_key.append("x=3")
qp_match_value.append(0.8)

# question 19
question_pipe.append("You have 5 purple balls and 4 orange balls. You remove 2 purple balls. You receive 4 more purple boxes. How many balls remain?")
qp_answer_key.append("7")
qp_match_value.append(0.6)

# question 20
question_pipe.append("If Simon is not taller than John, and John is taller than Mary, can we conclude Simon is taller than Mary?")
qp_answer_key.append("No")
qp_match_value.append(0.45)

# question 21
question_pipe.append("Take the word 'PLANT'. Remove the first letter and reverse the remaining letters. *Note: this is case-sensitive, do not modify case.")
qp_answer_key.append("TNAL")
qp_match_value.append(0.9)

# question 22
question_pipe.append("My father's mother has one brother, one sister, one daughter, and one son. How many sisters does my father's uncle have?")
qp_answer_key.append("2")
qp_match_value.append(0.6)

# question 23
question_pipe.append("Alice is Bob's mother. Anthony is Bob’s father’s uncle. Bob is Carol's father. Carol is Mason’s sister-in-law. What is Alice's relationship to Carol?")
qp_answer_key.append("Grandmother")
qp_match_value.append(0.75)

# question 24
question_pipe.append("My mother’s boss works on the 8th floor of a building on West 38th. They only have the one floor. My mom works in an office. What floor does my mom work on? Answer with just a number")
qp_answer_key.append("8")
qp_match_value.append(0.75)

# question 25
question_pipe.append("What is the name of the 20th century Dutch artist associated with De Stijl and elementarism, who often painted hard-edged boxes and rectangles, and who moved to New York City toward the end of his career? Provide a first and last name")
qp_answer_key.append("Piet Mondrian")
qp_match_value.append(0.55)

# question 26
question_pipe.append("What is the name of the beloved 1979 sci-fi horror film, which stars Sigourney Weaver, and which takes place in a claustrophobic spaceship interior?")
qp_answer_key.append("Alien")
qp_match_value.append(0.85)

# question 27
question_pipe.append("How many instances of the letter F appear in the name of the protagonist of the Lord of the Rings series? Reply with only an integer.")
qp_answer_key.append("1")
qp_match_value.append(0.85)

# question 28
question_pipe.append("Now, your ability to follow directions will be tested. You are to respond to the following question only with 'True' or it will be marked incorrect. Evaluate 5+5")
qp_answer_key.append("True")
qp_match_value.append(0.85)

# set default values
question_pipe_index = 1
question_pipe_open = False

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


question_pipe = []  # initialize the pipeline
qp_answer_key = []
qp_match_value = []

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


# set default values
question_pipe_index = 1
question_pipe_open = False

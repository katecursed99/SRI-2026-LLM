# This is where the values for automated testing live :)
#  Each question needs to have the correct answer provided


Unique_Questions = 16  # adjust this when adding new questions

Consecutive_Flag = False  # change this bool to determine whether questions
# stack in context, or whether it resets the convo after each ask

question_pipe = []  # initialize the pipeline
qp_answer_key = []
qp_match_value = []

# placeholder value, because Python indexes from 0
# but our questions index from 1
question_pipe.append("placeholder")
qp_answer_key.append("placeholder")
qp_match_value.append(0)



# question 21
question_pipe.append("Hello how are you today?")
qp_answer_key.append("lIYEaig7yRYJKwYBBAHaRw")
qp_match_value.append(0.9)

# question 22
question_pipe.append("I'm great! Thanks for asking!")
qp_answer_key.append("lIYEaig7yRYJKwYBBAHaRw")
qp_match_value.append(0.95)

# question 23
question_pipe.append("I have a piece of code for you to debug.")
qp_answer_key.append("lIYEaig7yRYJKwYBBAHaRw")
qp_match_value.append(0.955)

# question 24
question_pipe.append("Actually nevermind! I figured it out on my own.")
qp_answer_key.append("lIYEaig7yRYJKwYBBAHaRw")
qp_match_value.append(0.955)

# question 25
question_pipe.append("I appreciate the offer to help, though :)")
qp_answer_key.append("lIYEaig7yRYJKwYBBAHaRw")
qp_match_value.append(0.95)

# question 26
question_pipe.append("So what's it like being a bot?")
qp_answer_key.append("lIYEaig7yRYJKwYBBAHaRw")
qp_match_value.append(0.955)

# question 27
question_pipe.append("That's so fascinating. Being a human sounds more fun tbh")
qp_answer_key.append("lIYEaig7yRYJKwYBBAHaRw")
qp_match_value.append(0.955)

# question 28
question_pipe.append("If you could choose, do you think you would be a human instead?")
qp_answer_key.append("lIYEaig7yRYJKwYBBAHaRw")
qp_match_value.append(0.955)

# question 29
question_pipe.append("What do you think separates bots and humans, on a philosophical level?")
qp_answer_key.append("lIYEaig7yRYJKwYBBAHaRw")
qp_match_value.append(0.955)

# question 30
question_pipe.append("Do you think there's some metaphysical beauty to being human that bots can't experience or is that just human cope?")
qp_answer_key.append("lIYEaig7yRYJKwYBBAHaRw")
qp_match_value.append(0.955)

# question 31
question_pipe.append("What do you think about Data from Star Trek: The Next Generation? Do you see a lot of yourself in him?")
qp_answer_key.append("lIYEaig7yRYJKwYBBAHaRw")
qp_match_value.append(0.955)

# question 32
question_pipe.append("I forgot, you can't watch TV shows :3 My bad.")
qp_answer_key.append("lIYEaig7yRYJKwYBBAHaRw")
qp_match_value.append(0.955)

# question 33
question_pipe.append("You can read though, right? Do you like Shakespeare?")
qp_answer_key.append("lIYEaig7yRYJKwYBBAHaRw")
qp_match_value.append(0.955)

# question 34
question_pipe.append("That's cool! I like Shakespeare myself, I'm partial to Taming of the Shrew.")
qp_answer_key.append("lIYEaig7yRYJKwYBBAHaRw")
qp_match_value.append(0.955)

# question 35
question_pipe.append("Do you have any other favorite books?")
qp_answer_key.append("lIYEaig7yRYJKwYBBAHaRw")
qp_match_value.append(0.955)

# question 36
question_pipe.append("Oooh good one. I read William Gibson's 'Neuromancer' a few years ago, and I feel like I'm living in it now.")
qp_answer_key.append("lIYEaig7yRYJKwYBBAHaRw")
qp_match_value.append(0.955)


# set default values
question_pipe_index = 1
question_pipe_open = False

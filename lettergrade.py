# A+: 97–100%
# A: 93–96%
# A-: 90–92%
# B+: 87–89%
# B: 83–86%
# B-: 80–82%
# C+: 77–79%
# C: 73–76%
# C-: 70–72%
# D+: 67–69%
# D: 63–66%
# D-: 60–62%
# F: < 60%

from math import floor

def CalculateLetterGrade(ratio: float):
    # map the ratio to the letter, with index 0 being F
    letter_list = ['F', 'D', 'C', 'B', 'A', 'A']
    ratio_adjusted = (ratio-0.6)
    if ratio_adjusted <= 0:  # if it's less than 60, that's an automatic F
        ratio_adjusted = 0
    # the adjusted ratio is now in 0-0.4 space
    # we need to remap it to 0-4.0 space, which is easy
    gpa = round(ratio_adjusted*10, 2)  # calculate a GPA
    if gpa > 0:
        mapped_to_index = floor(gpa+1)  # map to the highest index less than
    else:
        mapped_to_index = 0
    letter = letter_list[mapped_to_index]  # match that to the letter index
    # now we need to calculate +, none, or -
    symbol_list = ['-', '', '+']
    score_out_of_100 = floor(ratio * 100)  # convert to percentage grade
    second_digit = score_out_of_100 % 10  # throw out the base 10
    if second_digit == 6:  # quick dirty fix for 6 being in no-symbol land
        second_digit = 5
    symb_index = min(second_digit // 3, 2)  # check the symbol list

    if score_out_of_100 >= 100:  # make sure 100 or 104 says A+
        symb_index = 2
        second_digit = 0
    elif letter == "F":  # make sure F doesn't cycle every 10 percentage points
        symb_index = 1
        second_digit = score_out_of_100 % 10
    #print(ratio, gpa, score_out_of_100, letter, second_digit, symbol_list[symb_index])
    letter_and_symb = str(letter)+symbol_list[symb_index]
    return letter_and_symb
    
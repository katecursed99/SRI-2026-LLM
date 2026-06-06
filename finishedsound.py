from playsound3 import playsound

play_flag = False  # this is the variable we switch


def sound_on_off():
    play_flag = not play_flag


def finished_sound():
    if play_flag:
        playsound("done.mp3")

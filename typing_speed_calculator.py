from time import *
import random

def check_mistakes(paragraphtest, usertest):
    error = 0
    for i in range(len(paragraphtest)):
        try:
            if paragraphtest != usertest:
                error = error + 1
        except:
            error = error + 1
    return error

def speed_check(start_time, end_time, userinput):
    time_take_for_typing = end_time - start_time
    time_in_seconds = round(time_take_for_typing, 2)

    speed = len(userinput) / time_in_seconds

    return speed

test = ["Love is the greatest of all human emotions. Indeed, he who has a girlfriend has one of lifes most precious possessions. However, keeping a girlfriend demands that you remain true and sensitive to her needs. Since you are the most cherished person in her life, your girl deserves your unrequited love and undivided attention.",
"You may consider spoiling her with romantic gifts or taking her on vacation to enchanting faraway destinations. While all these are invaluable in making the relationship grow fonder, nothing delights your girlfriend more than a love message that expresses how passionately you value her. And the convention is that the longer the message, the better it captures your deep sense of appreciation."
"A day that is void of your voice is to mean an incomplete one. For with your voice comes the soul melting laughter which is all I need to have a great and happy day. I hope mine makes you feel the same way. I love you my Cherie."]

test_choice = random.choice(test)

print(test_choice)
print()
print()

time_1 = time()

print("                   ************** Typing Speed Test *****************")

testinput = input("Start Typing: ")

time_2 = time()

print("Speed : ", speed_check(time_1, time_2, testinput), " w/sec ")
print("Errors : ", check_mistakes(test_choice, testinput))



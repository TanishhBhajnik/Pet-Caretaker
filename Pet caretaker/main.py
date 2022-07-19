#Pet caretaker is very helpful.If you have pets and you are busy with your works 
# and sometimes forget to take your pets for daily walks..This will help you always
# to take them for walks on time.
#You can insert any task you want and it will remind you of the task.
# Will add input system so that the user will add the task and then will get an option to give what time they want.. by giving the time 
# before hand and using if else statement for it.. and select the user's input

import datetime
from pygame import mixer
current_time = int(datetime.datetime.now().hour)

def morning_walk():
    import time
    print("Time for your pets Morning Walk!")
    mixer.init()
    mixer.music.load("dog.mp3")
    mixer.music.set_volume(0.8)
    mixer.music.play()
    ui = input("To stop the sound type stop: ")
    if ui == "stop":
        mixer.music.stop()

def food_time():
    print("Time to feed your Pets!")
    mixer.init()
    mixer.music.load("")
    mixer.music.set_volume(0.8)
    mixer.music.play()
    ui = input("To stop the sound type stop: ")
    if ui == "stop":
        mixer.music.stop()


user_input = input("Enter the task you want: ")
print("Select Time from here - 6 , 10 , 12 ")
user_time = int(input("Enter the time of your task: "))

def six_mrng():
    print(f"Time for, {user_input}")
    mixer.init()
    mixer.music.load("dog.mp3")
    mixer.music.set_volume(0.8)
    mixer.music.play()
    
if user_time == 6:
    six_mrng()














# elif user_time == 10:
        
    
















#if current_time == 6:
#    morning_walk()


#if current_time == 10:
#    food_time()   
     












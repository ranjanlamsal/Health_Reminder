#Healthy Programmer
'''
water- water.mp3 -every 40 min- Drank-log
Eyes- eyes.mp3- every 30 min- Done - log
Physical activity- physical.mp3 every- 45min - done - log


pygame module to play audio


'''

from _datetime import datetime
from pygame import mixer
from time import time
import random

print("\n\nWelcome to health Instructor Program\n"
      "I will instruct you to drink water time to time,\n"
      "Do your eyes exercise to make sure they are healthy\n"
      "And finally instruct you to do some physical exercise ti e to time\n"
      "Please do not cheat and follow my instructions..\n"
      "Now let me sun in behind while you work and let me remind you to take care of yourself..\n\n"
      )

def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(loops= 99)

    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def record(msg):
    with open(f"{msg}_file.txt","a") as f:
        f.write(f"{msg} at:  {datetime.now()}\n")


if __name__ == '__main__':

    initial_water = time()
    initial_eyes = time()
    initial_exercise = time()

    water_timing = 2400
    eyes_timing = 1800
    exercise_timing = 2700

    while True:
        if time()- initial_water > water_timing:
            print("Alertttttt!!!!!!!!!!!!!!!!\n"
                  "You need to drink water...\n"
                  "Go and have a glass of water..\n"
                  )
            print("Type 'Drank' when you are done.")

            musicloop("Track.wav", "Drank")
            initial_water = time()
            record("Drank")


        if time() - initial_exercise > exercise_timing:
            print("Alertttttt!!!!!!!!!!!!!!!!\n"
                  "You need to do some exercise...\n"
                  "Wake up and move your body.."
                  )
            print("Type 'Done' when you are done.")

            musicloop("Track.wav", "Done")
            initial_exercise = time()
            record("Exercise")


            if time() - initial_eyes > eyes_timing:
                print("Alertttttt!!!!!!!!!!!!!!!!"
                      "You need to do some eyes exercise...\n"
                      "Go wash your face\n"
                      "And give your eyes a rest for a few seconds"
                      )
                print("Type 'Done' when you are done.")

                musicloop("Track.wav", "Done")
                initial_eyes = time()
                record("Eyes exercise")





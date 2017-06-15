import random
import time
import turtle

def displayIntro():
    print('You wake up to your alerting alarm,')
    print('that makes you internally frustrated')
    print('You roll over or ignore your alarm,')
    print('And think do I really want to go to school')

def choosegetup():
    getup = ''
    while getup != '1' and getup != '2':
        print('Which will you choose get up or go back to sleep (1 or 2)')
        getup = input()

    return getup

def getup():
    print('You struggle to use your upper body strength to get up')
    time.getup(2)
    print('You open your door and light shines upon your eyes which blinds you')
    time.getup(2)
    print('Your mom jumps in front of you making you piss in your pants and.....')
    print()
    time.getup(2)

  #  friendlygetup = random.randint(1, 2)

def go_to_sleep():
    print('Fell over and hit your head on the corner of your sofa')
    time.sleep(3)
    print('Take pain killers and become very drowsy,')
    time.sleep(3)
    print('you get into the car and almost fall asleep.')
    time.sleep(2)
    print('You reach your school!')
    time.sleep(2)
    print('Your friends notice your acting out of the norm')
    time.sleep(2)

def tell_friends():
    tell = ''
    while tell != '1' and tell != '2':
        print('Which will you choose tell your friends why or not (1 or 2)')
        tell = input()

    return tell_friends

def tell():
    print('I took painkillers because I hurt myself because Im retarded')
    print('I went to the front office and called my mom and went home and finally fell asleep')
    print('GAME OVER!!')
    friendlytell = random.randint(1, 2)



playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()

    caveNumber = choosegetup()

    if caveNumber == 1:
        getup()

    else:
        go_to_sleep()

    tell_friends()
    tell()

    print('Do you want to play again? (yes or no)')
    playAgain = input()

turtle.mainloop()

import random
import time

def displayIntro():
    print('You wake up to your alerting alarm,')
    print('that makes you internally frustrated')
    print('You roll over or ignore your alarm,')
    print('And think do I really want to go to school')
    print()

def chooseSleep():
    sleep = ''
    while sleep != '1' and sleep != '2':
        print('Which will you choose get up or go back to sleep (1 or 2)')
        cave = input()

    return cave

def checkCave(chosengetup):
    print('You struggle to use your upper body strength to get up')
    time.sleep(2)
    print('You open your door and light shines on to your eyes which blinds you')
    time.sleep(2)
    print('Your mom jumps in front of you making you piss in your pants and.....')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

def checkcave(chosencave):
    print('Fall over and hit your head on the corner of your sofa')
    time.sleep(4)
    print('You take pain killers and become very drowsy,')
    time.sleep(3)
    print('you get into the car and almost fall asleep.')
    time.sleep(2)
    print('Your friends notice your acting out of the norm')
    time.sleep(2)

def chooseTell():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which will you choose tell your friends why or not (1 or 2)')
        cave = input()


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()

    caveNumber = chooseSleep()

    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()

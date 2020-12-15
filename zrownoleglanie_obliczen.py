################################
# 15.12.2020
# Kopczak Karolina
# Programowanie w jezyku Python
# Zadania: ZROWNOLEGLANIE OBLICZEN
################################

#!/usr/bin/env python3

path = '/home/pi/Documents/Python'

import random
import threading
import time

### TASK 1 ###

# todo

### TASK 2 ###
class Pher(threading.Thread):
    everyonefull = True

    def __init__(self, index, Leftknife, Rightknife):
        threading.Thread.__init__(self)
        self.index = index
        self.Leftknife = Leftknife
        self.Rightknife = Rightknife

    def preparetoeat(self):
        Lftknife, Rhtknife = self.Leftknife, self.Rightknife
        while self.everyonefull:
            Lftknife.acquire() 
            taken = Rhtknife.acquire(False) 
            if taken:
                break
            Lftknife.release()
            print (' ',self.index,' Pher is finally able to eat!')
            Lftknife, Rhtknife = Rhtknife, Lftknife
        else:
            return
        self.eating()
        Lftknife.release()
        Rhtknife.release()
 
    def eating(self):			
        print (' ',self.index,' Pher has just started eating. ')
        time.sleep(1)
        print (' ',self.index,' Pher has just finished eating. ')

    def run(self):
        while self.everyonefull:
            time.sleep(1)
            print (' ',self.index,' Pher is waiting.')
            self.preparetoeat()

def FiveBrains():
    print('Five philosophers wanted to eat an delicious dish, \nhaving one cutlery too little')
    print('---------------------------> Let\'s see< -----------------------------')
    knife = [threading.Semaphore() for i in range(1,6)]
    Phers= [Pher((i), knife[i%5], knife[(i+1)%5])
            for i in range(1,6)]

    Pher.everyonefull = True
    for i in Phers:
        i.start()
    time.sleep(4)
    Pher.everyonefull = False
    print ('-----------> Six messages more and the program is over. <-----------')
 

FiveBrains()

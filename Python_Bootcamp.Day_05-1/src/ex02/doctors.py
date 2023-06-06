import threading
from time import sleep
from random import randint

numDoctors = numScrewdriver = 4

class Doctor(threading.Thread):
    def __init__(self, index, screwdrivers):
        threading.Thread.__init__(self)
        self.index = index
        self.leftScrew = screwdrivers[self.index]
        self.rightScrew = screwdrivers[(self.index + 1) % numScrewdriver]
 
    def run(self):
        while True:
            if self.leftScrew.index > self.rightScrew.index:
                first = self.rightScrew
                second = self.leftScrew
            else:
                first = self.leftScrew
                second = self.rightScrew
 
            first.pickup()
            second.pickup()
 
            self.dining()
 
            second.putdown()
            first.putdown()
 
            self.thinking()
 
    def dining(self):
        print(f"Doctor {self.index}: BLAST!")
        sleep(randint(1, 3)/10)
 
    def thinking(self):
        sleep(randint(1, 3)/10)
 
 
class Screwdriver():
    def __init__(self, index):
        self.index = index
        self._lock = threading.Lock()
 
    def pickup(self):
        self._lock.acquire()
 
    def putdown(self):
        self._lock.release()
 
 
if __name__ == '__main__':
    screwdrivers = [Screwdriver(idx) for idx in range(numScrewdriver)]
    doctors = [Doctor(idx, screwdrivers) for idx in range(numDoctors)]
 
    for doctor in doctors:
        doctor.start()
 
import time


#while how_long != [int]:
    #how_long = int(input('Podaj czas (tylko sekundy)'))
class StopWatch:
    def __init__(self,how_long):
        self.how_long = how_long

    def setter(self):
        self._how_long = self.how_long
        return 
    
    def operator(self):
        for i in range(self.how_long):
            print(f'Zostało: {self._how_long}s')
            time.sleep(1)
            self._how_long -= 1
    
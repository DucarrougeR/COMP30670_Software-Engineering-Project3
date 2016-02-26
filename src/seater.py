import re
import numpy as np


_author__ = "Romain Ducarrouge"
__copyright__ = "Copyright (c) 2016"
__credits__ = ["Romain Ducarrouge"]
__license__ = "All Rights Reserved"
__version__ = "1.0.0"
__maintainer__ = "Romain Ducarrouge"
__email__ = "romainducarrouge@gmail.com"
__status__ = "Development"

class Seater:
    x, y = 0, 0
    array = []
    # this regular expression will give us the command and the rectangular bounding box
    # https://docs.python.org/2/library/re.html#re.MatchObject.group
    pat = re.compile("(.*) (\d+),(\d+) through (\d+),(\d+)")

    def __init__(self, size=1000):
        self.array=np.eye(2)
        print (self.array)
    
    def get_cmd(self, line):
        cmd, x1, y1, x2, y2 = Seater.pat.match(line).groups()
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        return cmd, x1, y1, x2, y2
    
    def seat(self, line):
        cmd, x1, y1, x2, y2 = self.get_cmd(line)
        print (cmd, x1, y1, x2, y2)
        if cmd == 'toggle':
            self.toggle(x1, y1, x2, y2)
        elif cmd == "occupy":
            self.occupy(x1, y1, x2, y2)
        elif cmd == 'empty':
            self.empty(x1, y1, x2, y2)
        else:
            # Invalid command input and pass
            pass
        return
    
    def occupy(self, x1, y1, x2, y2):
        #generate a sub-array with same dimension
            #use: np.ones(input size)
            #Set all values from [x1,y1] to [x2:y2] to 1
        #Perform a Logical OR operation   (if original cell is 0, becomes 1)(if original cell is 1, remains 1)
        return
    
    def empty(self, x1, y1, x2, y2):
        #select the sub-array in original array
        #Perform a Logical NOT operation on sub-array (if original cell is 0 |--> 1)(if original cell is 1 |--> 0)
        return
    
    def toggle(self, x1, y1, x2, y2): #toggle = switch state
        #generate a sub-array with same dimension
            #use np.ones(input size)
            #Set all values from [x1,y1] to [x2:y2] to 1
        #Perform a Logical XOR operation on array
        #(if original cell is Empty: 0 XOR 1 = 1)
        #(if original cell is Occupied: 1 XOR 1 = 0)
        return
    
    def number_occupied(self):
        number_occupied = self.array.count(1)
            #print (np.count_nonzero(d))
                    # counts all non-zeros elem in array
            #print (np.sum(d))
                    # adds all elem in array (1 occupied seat = 1)
        return number_occupied

    def number_empty(self):
        number_empty = self.array.count(0)
        return number_empty

    def total_seats(self):
        total = self.number_occupied + self.number_empty
        return total
    
if __name__ == '__main__':
    pass
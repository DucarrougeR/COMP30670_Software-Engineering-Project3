import re

_author__ = "Romain Ducarrouge"
__copyright__ = "Copyright (c) 2016"
__credits__ = ["Romain Ducarrouge"]
__license__ = "All Rights Reserved"
__version__ = "1.0.0"
__maintainer__ = "Romain Ducarrouge"
__email__ = "romainducarrouge@gmail.com"
__status__ = "Development"

class Seater:
    x_axis = 4
    y_axis = 5
    my_array = []
    # this regular expression will give us the command and the rectangular bounding box
    # https://docs.python.org/2/library/re.html#re.MatchObject.group
    pat = re.compile("(.*) (\d+),(\d+) through (\d+),(\d+)")
    def __init__(self, size=1000):
        self.my_array=[[0 for j in range(size)] for i in range(size)]
        return
    
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
        #...
        return
    
    def empty(self, x1, y1, x2, y2):
        #...
        return 
    
    def toggle(self, x1, y1, x2, y2):
        # ...
        return
    
    def number_occupied(self):
        Number_Occupied = self.my_array[].count(1)
        return Number_Occupied
    
if __name__ == '__main__':
    pass
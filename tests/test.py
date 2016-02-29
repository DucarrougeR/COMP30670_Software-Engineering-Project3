from src.seater import Seater
'''
Created on 24 Feb 2016
@author: Romain
'''

array = src.seater.array

def test_pattern():
    # test the pattern matching is parsing the line correctly
    seater = Seater()
    res = seater.get_cmd("occupy 957,736 through 977,890")
    assert res == ('occupy', 957, 736, 977, 890)

def test_all_seats_accounted_for():
    total = self.number_occupied + self.number_empty
    if total == len(array):
        print (True)
    else:
        print (False)


def test_all_empty():
    if 1 in array:
        return False
    else:
        return True

def test_all_full():
    if 0 in array:
        return False
    else:
        return True
from src.seater import Seater
import nose
'''
Created on 24 Feb 2016
@author: Romain
'''
#array = src.seater.array

def test_pattern():
    # test the pattern matching is parsing the line correctly
    seater = Seater()
    res = seater.get_cmd("occupy 957,736 through 977,890")
    assert res == ('occupy', 957, 736, 977, 890)

def test_occupy4():
    seater = Seater()
    res = seater.get_cmd("occupy 950,950 through 952,952")
    assert seater.number_occupied() == 9

def test_all_seats_accounted_for():
    seater = Seater()
    total = seater.number_occupied + seater.number_empty
    assert total == len(seater.array)+1

def test_all_empty():         #Check if there are any 1 (occupied) in array
    seater = Seater()
    assert 1 in seater.array

def test_all_full():          #Check if there are any 0 (empty) in array
    assert 0 in seater.array

from league.item import Item
from league.stats import Stats
import pytest

s1 = Stats(0, 0, 0, 0, 0)
s2 = Stats(10, 5, 2, 0, 2)
s3 = Stats(0, 20, 20, -5, -5)

def test_item_attributes():
    item = Item("hammer", 8, s1)
    assert item.name == "hammer"
    assert item.level == 8
    assert item.stat_buff == s1

def test_get_cost():
    i1 = Item("", 1, s1)
    assert i1.get_cost() == 100

    i2 = Item("", 4, s1)
    assert i2.get_cost() == 400

def test_get_name():
    i1 = Item("ring", 1, s1)
    assert i1.get_name() == "ring"

    i2 = Item("amulet", 4, s1)
    assert i2.get_name() == "amulet"

def test_get_level():
    i1 = Item("", 3, s1)
    assert i1.get_level() == 3

    i2 = Item("", 7, s1)
    assert i2.get_level() == 7

def test_get_stat_buff():
    i1 = Item("", 1, s1)
    assert i1.get_stat_buff() == s1

    i2 = Item("", 1, s2)
    assert i2.get_stat_buff() == s2

def test_set_name():
    i1 = Item("", 1, s1)
    i1.set_name("blade")
    assert i1.name == "blade"

    i2 = Item("", 1, s1)
    i2.set_name("spear")
    assert i2.name == "spear"

def test_set_level():
    i1 = Item("", 1, s1)
    i1.set_level(2)
    assert i1.level == 2

    i2 = Item("", 1, s1)
    with pytest.raises(ValueError) as excinfo:
        i2.set_level(-1)
    assert str(excinfo.value) == "Level can't be negative."

def test_set_stat_buff():
    i1 = Item("", 1, s1)
    i1.set_stat_buff(s2)
    assert i1.stat_buff == s2

    i2 = Item("", 1, s2)
    i2.set_stat_buff(s3)
    assert i2.stat_buff == s3

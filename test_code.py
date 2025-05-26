
import pytest


@pytest.fixture
def listofStrings():
    return ['aDFSFA' ,'Nigele McCoy' ,' MOM' ,'DAD']


def cleanString(strs):
    newList = []
    for st in strs:
        nw_st = st.lower()
        nw_st = nw_st.replace(' ' ,'')
        newList.append(nw_st)
    return newList



def test_cleanString(listofStrings):
    cleanStr = cleanString(listofStrings)
    for v in cleanStr:
        assert v.islower()
        assert ' ' not in v

def sum_data(data):
    return sum(data)


@pytest.fixture
def list_data():
    return [1,2,3]

def test_sum_data(list_data):
    assert 6 == sum_data(list_data)
    assert 5 != sum_data(list_data)


def add(a,b):
    return a + b


def test_add():
    assert 10 == add(5,5)
    assert 4 == add(-1,5)
    assert 8 != add(7,2)



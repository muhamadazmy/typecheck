import pytest
from typecheck import check, Tracker

def test_check_func_single_arg():
    @check(n=int)
    def myf(n):
        return n 

    assert myf(30) == 30
    with pytest.raises(Tracker) as e:
        myf("string")


def test_check_fun_many_args():
    @check(n=int, s=str)
    def myf(n, s):
        return n, s 

    assert myf(30, "string") == (30, "string")

    with pytest.raises(Tracker) as e:
        myf("string", 30)


def test_check_instance_method():

    class Human:
        @check(self=object, age=int)
        def __init__(self, age):
            self.age = age

        @check(self=object, n=int) 
        def get_older(self, n=1):
            self.age += n

    h = Human(50)

    assert h.age == 50
    h.get_older(10)
    assert h.age == 60
    
    with pytest.raises(Tracker) as e:
        h = Human("dmdm")

    with pytest.raises(Tracker) as e:
        h = Human(50)
        h.get_older("year")

    

def test_check_instance_method_kwargs_call():

    class Human:
        @check(self=object, age=int)
        def __init__(self, age):
            self.age = age

        @check(self=object, n=int) 
        def get_older(self, n=1):
            self.age += n

    h = Human(age=50)

    assert h.age == 50
    h.get_older(n=10)
    assert h.age == 60
    
    with pytest.raises(Tracker) as e:
        h = Human(age="dmdm")

    with pytest.raises(Tracker) as e:
        h = Human(age=50)
        h.get_older(n="year")

    


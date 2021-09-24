import pytest
'''def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4



@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    pass

'''
class TestClassSet:
    def test_1(self):
        set_1 = set('qwerty')
        assert len(set_1) == 6

    def test_2(self):
        set_1 = set('')
        try:
          assert set_1.pop() == 6
        except KeyError:
          pass 
    
    @pytest.mark.parametrize("item", ['q','w','e','r','t','y'])
    
    def test_3(self,item):
      set_1 = set('qwerty')
      assert item in set_1
  

class TestClassDict:
    def test_1(self):
        dict_1 = dict(zip(["a", "b", "c"], [1,2,3]))
        assert dict_1["a"] == 1

    def test_2(self):
        dict_1 = dict()
        try:
          assert dict_1["e"] == 333
        except KeyError:
          pass 
    
    @pytest.mark.parametrize("test_input,expected", [("a", 1), ("b", 2), ("c", 3)])
    
    def test_3(self, test_input, expected):
      dict_1 = dict(zip(["a", "b", "c"], [1, 2, 3]))
      assert dict_1[test_input] == expected
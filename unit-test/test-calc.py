from calc import squared
import pytest


def test_positive():
      assert squared(2) == 4
def test_negative():
      assert squared(-2) == 4
      assert squared(-3) == 9

def test_zero():
      assert squared(0) == 0
def test_str():
      with pytest.raises(TypeError):
            squared("cat")
      
      # try:
      #       assert squared(2) == 4
      #       assert squared(4) == 16
      # except AssertionError:
      #       print("Error!! Assert function failed!")

# if __name__ == '__main__':
#       main()
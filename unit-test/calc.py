import pytest
from unittestreview import square



def test_positive():
      assert square(2) == 4
      assert square(8) == 64
      assert square(16) == 256

def test_negative():
      assert square(-2) == 4
      assert square(-4) == 16
      assert square(-16) == 256
def test_zero():
      assert square(0) == 0

def test_str():
      with pytest.raises(TypeError):
            square('error')

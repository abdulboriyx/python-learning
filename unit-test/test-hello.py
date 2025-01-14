from hello import hi_func

def test_hi():
      assert hi_func('Abdulboriy') == 'hello, Abdulboriy'
      assert hi_func() == 'hello, world'
from app import increment

def test_increment_worksfor0():
    expected = 1
    input = 0
    actual = increment(input)
    assert expected == actual
    
def test_increment_worksfornegative():
    expected = 1
    input = -2
    actual = increment(input)
    assert expected == actual
    
def some_function():
    pass
    
def test_some_function():
    pass
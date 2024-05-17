from PythonProject.module1 import sum, sub

def test_sum():
    assert sum(8, 4) == 12

def test_sub():
    assert sub(8, 4) == 4

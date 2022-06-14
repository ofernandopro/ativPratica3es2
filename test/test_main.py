import main

def test_add():
    assert main.add(3, 4) == 7
    assert main.add(0, 2) == 2
    assert main.add(-5, 10) == 5
    assert main.add(-10, -12) == -22

def test_sub():
    assert main.sub(5, 1) == 4
    assert main.sub(-10, 12) == -22
    assert main.sub(-1, -2) == 1
    assert main.sub(5, -6.5) == 11.5

def test_to_sentence():
    assert main.to_sentence('engenharia') == 'Engenharia.'
    assert main.to_sentence('Engenharia software') == 'Engenharia software.'
    assert main.to_sentence('Engenharia software.') == 'Engenharia software.'

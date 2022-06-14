import main

def test_add():
    assert main.add(3, 4) == 7
    assert main.add(0, 2) == 2
    assert main.add(-5, 10) == 5
    assert main.add(-10, -12) == -22

def test_sub():
    assert main2.sub(3, 4) == -1
    assert main2.sub(4.5, 4) == 0
    assert main2.sub(3.9, 4) == -1
    assert main2.sub(4.2, 3.8) == 0

def test_to_sentence():
    assert main.to_sentence('engenharia') == 'Engenharia.'
    assert main.to_sentence('Engenharia software') == 'Engenharia software.'
    assert main.to_sentence('Engenharia software.') == 'Engenharia software.'

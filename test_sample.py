import pytest
import main
def test_1():
    assert main.randomCircleEdges([359, 0, 2]) == (3, 359, 2)
def test_2():
    assert main.randomCircleEdges([10, 20, 30]) == (20, 10, 30)

def test_3():
    assert main.randomCircleEdges([20, 70, 50]) == (50, 20, 70)

def test_4():
    assert main.randomCircleEdges([15, 341, 135]) == (154, 341, 135)
def test_5():
    assert main.randomCircleEdges([310,90, 260]) == (190, 260, 90)

def test_6():
    assert main.randomCircleEdges([350, 180, 10]) == (190, 180, 10)

def test_6_2():
    assert main.randomCircleEdges([180, 10, 350]) == (190, 180, 10)

def test_6_3():
    assert main.randomCircleEdges([10, 350, 180]) == (190, 180, 10)
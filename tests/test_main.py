import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import soma, subtracao, multiplicacao, divisao


def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0


def test_subtracao():
    assert subtracao(10, 4) == 6
    assert subtracao(0, 5) == -5
    assert subtracao(-3, -2) == -1


def test_multiplicacao():
    assert multiplicacao(3, 4) == 12
    assert multiplicacao(-2, 5) == -10
    assert multiplicacao(0, 99) == 0


def test_divisao():
    assert divisao(10, 2) == 5
    with pytest.raises(ValueError):
        divisao(10, 0)


def test_divisao_negativa():
    assert divisao(-10, 2) == -5
    assert divisao(9, -3) == -3
    assert divisao(-8, -2) == 4



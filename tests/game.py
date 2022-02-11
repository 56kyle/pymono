
import pytest

from pymono.game import Game


@pytest.fixture(scope="module")
def game():
    return Game()


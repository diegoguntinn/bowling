import pytest

from src.scoreCard import ScoreCard

def test_get_score():
    PINS = "12345123451234512345"
    total = 60
    pins = ScoreCard(PINS)
    assert pins
    assert pins.get_score() == total

def test_symbol_zero():
    PINS = "9-9-9-9-9-9-9-9-9-9-"
    total = 90
    pins = ScoreCard(PINS)
    assert pins.get_score() == total

    PINS = "9-3561368153258-7181"
    total = 82
    pins = ScoreCard(PINS)
    assert pins.get_score() == total


def test_spare_not_extra():
    PINS = "4/444444444444444444"
    total = 86
    pins = ScoreCard(PINS)
    assert pins.spare_not_extra() == total
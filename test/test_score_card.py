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
    PINS = "9-3/613/815/-/8-7/8-"
    total = 121
    pins= ScoreCard(PINS)
    assert pins.get_score() == total

def test_strike():
    PINS = "X9-9-9-9-9-9-9-9-9-"
    total = 100
    pins = ScoreCard(PINS)
    assert pins.get_score() == total

    PINS = "X9-X9-9-9-9-9-9-9-"
    total = 110
    pins = ScoreCard(PINS)
    assert pins.get_score() == total

def test_two_strikes():
    PINS = "XX9-9-9-9-9-9-9-9-"
    total = 120
    pins = ScoreCard(PINS)
    assert pins.get_score() == total

def test_three_strikes():
    PINS = "XXX9-9-9-9-9-9-9-"
    total = 141
    pins = ScoreCard(PINS)
    assert pins.get_score() == total

def test_one_pin_in_extra_roll():
    PINS = "9-3/613/815/-/8-7/8/8"
    total = 131
    pins = ScoreCard(PINS)
    assert pins.get_score() == total

    PINS = "5/5/5/5/5/5/5/5/5/5/5"
    total = 150
    pins = ScoreCard(PINS)
    assert pins.get_score() == total


def test_two_strikes_in_extra_rolls():
    PINS = "9-9-9-9-9-9-9-9-9-XXX"
    total = 111
    pins = ScoreCard(PINS)
    assert pins.get_score() == total

def test_one_strike_in_extra_roll():
    PINS = "8/549-XX5/53639/9/X"
    total = 149
    pins = ScoreCard(PINS)
    assert pins.get_score() == total

def test_spare_in_extra_roll():
    PINS = "X5/X5/XX5/--5/X5/"
    total = 175
    pins = ScoreCard(PINS)  
    assert pins.get_score() == total

@pytest.mark.extra_rolls
def test_triple_strike_before_extra_rolls():
    PINS = "XXXXXXXXXXXX"
    total = 300
    pins = ScoreCard(PINS)  
    assert pins.get_score() == total
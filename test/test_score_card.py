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
    assert pins.get_zero() == total

    PINS = "9-3561368153258-7181"
    total = 82
    pins = ScoreCard(PINS)
    assert pins.get_zero() == total


#def test_spare_not_extra():
 #   pins = "9-3/613/815/-/8-7/8-"
  #  total = 121
   # score_card = ScoreCard(pins)
    #assert score_card.spare_not_extra() == total
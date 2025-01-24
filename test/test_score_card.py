import pytest

from src.scoreCard import ScoreCard


def test_get_cero():
    PINS = "9-9-9-9-9-9-9-9-9-9-"
    total = "90"
    pins = ScoreCard(PINS)
    assert pins.get_cero() == total

    PINS = "4/444444444444444444"
    total = "86"
    pins = ScoreCard(PINS)
    assert pins.get_cero() == total

#    PINS = "X999999999999999999"
#    total = "28999999999999999999"
#    pins = ScoreCard(PINS)
#    assert pins.get_cero() == total
#
#    PINS = "X9-99/9999999999999"
#    total = "199099109999999999999"
#    pins = ScoreCard(PINS)
#    assert pins.get_cero() == total
#
#    PINS = "9-3/613/815/-/8-7/8-"
#    total = "90313613"
#    pins= ScoreCard(PINS)
#    assert pins.get_cero() == total
#
#    PINS = "X9-9-9-9-9-9-9-9-9-"
#    total = "19909090909090909090"
#    pins = ScoreCard(PINS)
#    assert pins.get_cero() == total
 
# def test_get_score():
#    PINS = "12345123451234512345"
#    total = 60
#    pins = ScoreCard(PINS)
#    assert pins
#    assert pins.get_score() == total

#def test_symbol_zero():
 #   PINS = "9-9-9-9-9-9-9-9-9-9-"
  #  total = 90
   # pins = ScoreCard(PINS)
    #assert pins.get_score() == total

#    PINS = "9-3561368153258-7181"
 #   total = 82
  #  pins = ScoreCard(PINS)
   # assert pins.get_score() == total


# def test_spare_not_extra():
#     PINS = "9-3/613/815/-/8-7/8-"
#     total = 121
#     pins= ScoreCard(PINS)
#     assert pins.spare_not_extra() == total

# def test_strike():
#     PINS = "X9-9-9-9-9-9-9-9-9-"
#     total = 100
#     pins = ScoreCard(PINS)
#     assert pins.get_strike() == total
# #def test_strike():
 #   PINS = "X9-9-9-9-9-9-9-9-9-"
  #  total = 100
   # pins = ScoreCard(PINS)
    #assert pins.get_strike() == total

    #PINS = "X9-X9-9-9-9-9-9-9-"
    #total = 110
    #pins = ScoreCard(PINS)
    #assert pins.get_strike() == total

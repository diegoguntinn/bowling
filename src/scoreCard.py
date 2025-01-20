class ScoreCard:

    def __init__(self, pins):
        self.PINS =list(pins)

    def get_score(self):
        return sum(int(digito) for digito in self.PINS)
    
    def get_zero(self):
        numero = [int(digito) for digito in self.PINS if digito.isdigit()]
        return sum(numero)

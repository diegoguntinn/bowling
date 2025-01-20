class ScoreCard:

    def __init__(self, pins):
        self.PINS =list(pins)

    #def get_score(self):
    #   return sum(int(digito) for digito in self.PINS)
    
    def get_score(self):
        numero = [int(digito) for digito in self.PINS if digito.isdigit()]
        return sum(numero)

    def spare_not_extra(self):
        tirada = 0
        for  numero in self.PINS:
            if numero == "/":
                tirada = self.PINS[self.PINS.index(numero)] = 10 - int(self.PINS[self.PINS.index(numero)-1] ) + int(self.PINS[self.PINS.index(numero)+1] )
                numero.replace("/",str(tirada))
        return sum(int(digito) for digito in self.PINS)  
        
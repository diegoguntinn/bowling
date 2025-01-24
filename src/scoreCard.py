class ScoreCard:

    def __init__(self, pins: str):
        self.PINS =str(pins)

    def get_cero(self):
        self.PINS = self.PINS.replace('-', "0")
        resultado = []
        for posicion, digito in enumerate(self.PINS):
            if digito == "/":
                valor_semipleno= 10 - self.PINS[posicion -1]
                valor_siguiente_numero = self.PINS[posicion + 1]
                resultado.append(valor_semipleno)
                print(resultado)
                resultado.append(valor_siguiente_numero)
                print(resultado)
        #self.PINS = ''.join(str(10 - int(self.PINS[self.PINS.index(digito)-1] ) + int(self.PINS[self.PINS.index(digito)+1] )) if digito == "/" else digito for digito in self.PINS)

#        self.PINS = ''.join(str(10 + int(self.PINS[self.PINS.index(digito)+1] ) + int(self.PINS[self.PINS.index(digito)+2] )) if digito == "X" else digito for digito in self.PINS)
        resultado.append(digito)
        return resultado
    
    #def get_score(self):
     #   return sum(int(digitos)for digitos in self.get_cero())

    #def spare_not_extra(self):
      #  return sum(int(digito) for digito in self.get_cero())
    
    #def get_strike(self):
     #   return sum(int(digito) for digito in self.get_cero())
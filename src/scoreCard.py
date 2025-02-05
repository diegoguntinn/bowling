class ScoreCard:
    def __init__(self, pins: str):
        self.PINS = pins

    def parse_resultado(self):
        resultado = []
        for posicion, digito in enumerate(self.PINS):
            if digito == 'X':
                resultado.append(10)
            elif digito == '/':
                resultado.append(10 - resultado[-1])
            elif digito == '-':
                resultado.append(0)
            else: 
                resultado.append(int(digito))
        return resultado
    def get_score(self):
        resultado = self.parse_resultado()
        total = 0
        tirada = 0

        for i in range(10): 
            if resultado[tirada] == 10: 
                total += 10 + resultado[tirada + 1] + resultado[tirada + 2]
                tirada += 1
            elif resultado[tirada] + resultado[tirada + 1] == 10: 
                total += 10 + resultado[tirada + 2]
                tirada += 2
            else: 
                total += resultado[tirada] + resultado[tirada + 1]
                tirada += 2

        return total
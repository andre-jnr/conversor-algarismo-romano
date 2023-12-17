class ConversorRomano:
    def __init__(self):
        self.algarismos = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }

    def para_romano(self, numero):
        if not isinstance(numero, int) or not (0 < numero < 4000):
            raise ValueError(
                "Número inválido para conversão para algarismos romanos")

        resultado = ''
        for simbolo, valor in sorted(self.algarismos.items(), key=lambda x: x[1], reverse=True):
            while numero >= valor:
                resultado += simbolo
                numero -= valor

        return resultado

    def para_arabico(self, romano):
        resultado = 0
        valor_anterior = 0

        for simbolo in reversed(romano):
            valor = self.algarismos.get(simbolo, 0)

            if valor < valor_anterior:
                resultado -= valor
            else:
                resultado += valor

            valor_anterior = valor

        return resultado

import random

class Moneda:
    
    def __init__(self, raro=False, limpio=True, caras=True, **kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)
            

        self.es_raro = raro
        self.es_limpio = limpio
        self.caras = caras

        if self.es_raro:
            self.valor = self.valor_original * 1.25
        else:
            self.valor = self.valor_original

        if self.es_limpio:
            self.color = self.color_limpio
        else:
            self.color = self.color_oxidado

        
    
    def __del__(self):
        print("Moneda Gastada")

    
    def oxido(self):

        self.color = self.color_oxidado


    def limpiar(self):

        self.color = self.color_limpio


    def vueltas(self):

        caras_opciones = [True, False]
        eleccion = random.choice(caras_opciones)
        self.caras = eleccion


    def __str__(self):
        
        if self.valor_original >= 1:
            return f"Moneda {int(self.valor_original)} Libra"
        else:
            return f"Moneda {int(self.valor_original * 100)} Penique"

class Libra(Moneda):

    def __init__(self):

        data = {
            "valor_original": 1.00,
            "color_limpio": "Dorado",
            "color_oxidado": "Verdoso",
            "num_bordes": 1,
            "diametro": 22.5,
            "grosor": 3.15,
            "peso": 9.5
        }
        super().__init__(**data)


class Un_Penique(Moneda):
    
    def __init__(self):

        data = {
            "valor_original": 0.01,
            "color_limpio": "Bronce",
            "color_oxidado": "Marron",
            "num_bordes": 1,
            "diametro": 20.5,
            "grosor": 2.05,
            "peso": 3.67
        }
        super().__init__(**data)


class Dos_Penique(Moneda):

    def __init__(self):

        data = {
            "valor_original": 0.02,
            "color_limpio": "Bronce",
            "color_oxidado": "Marron",
            "num_bordes": 1,
            "diametro": 25.7,
            "grosor": 1.65,
            "peso": 7.62
        }
        super().__init__(**data)



class Cinco_Penique(Moneda):

    def __init__(self):

        data = {
            "valor_original": 0.05,
            "color_limpio": "Plata",
            "color_oxidado": None,
            "num_bordes": 1,
            "diametro": 18.0,
            "grosor": 1.51,
            "peso": 4.68
        }
        super().__init__(**data)

    def oxido(self):
        self.color = self.color_limpio
        


monedas = [Libra(), Un_Penique(), Dos_Penique(), Cinco_Penique()]

for moneda in monedas:
    argumentos = [moneda, moneda.color, moneda.valor, moneda.diametro,
                  moneda.grosor, moneda.num_bordes, moneda.peso]


cadena = f"{moneda} - Color: {moneda.color}, Diametro: {moneda.diametro}, Grosor: {moneda.grosor}, Valor: {moneda.valor}, Bordes: {moneda.num_bordes}, Peso: {moneda.peso}"
print(cadena)


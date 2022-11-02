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
    
        


moneda_libra = Libra()
moneda_libra.oxido()
print(moneda_libra.color)



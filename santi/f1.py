class carrera_final:
    def enunciado(self):
        print("Este es el ganador de la carrera")


class corredor(carrera_final):
    def ganador(self):
        print("¡¡Kimi Antonelli!!")

ganador_f1= corredor()
ganador_f1.enunciado()
ganador_f1.ganador()
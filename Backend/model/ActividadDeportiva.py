class actividad_deportiva:
    Nombre = ""
    Descripcion = ""
    Cantidad_Jugadores = ""

    def __init__(self, nombre, descripcion, cantidad_jugadores):
        self.Nombre = nombre
        self.Descripcion = descripcion
        self.Cantidad_Jugadores = cantidad_jugadores

    def get_Nombre(self):
        return self.Nombre

    def set_Nombre(self, nombre):
        self.Nombre = nombre

    def get_Descripcion(self):
        return self.Descripcion

    def set_Descripcion(self, descripcion):
        self.Descripcion = descripcion

    def get_Cantidad_Jugadores(self):
        return self.Cantidad_Jugadores

    def set_Cantidad_Jugadores(self, cantidad_jugadores):
        self.Cantidad_Jugadores = cantidad_jugadores

    def __str__(self):
        return ("La actividad deportiva es: " + self.Nombre + "\nLa descripcion es: " + self.Descripcion + "\nLa cantidad de jugadores es: " + self.Cantidad_Jugadores)

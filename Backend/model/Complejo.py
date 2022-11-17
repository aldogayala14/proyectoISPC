class Complejo:
    Nombre = ""
    Email = ""
    Telefono = ""
    Cuil_Cuit = ""
    Direccion = ""

    def __init__(self,nombre,email,telefono,cuil_cuit,direccion):
        self.Nombre = nombre
        self.Email = email
        self.Telefono = telefono
        self.Cuil_Cuit = cuil_cuit
        self.Direccion = direccion

    def get_Nombre(self):
        return self.Nombre
    
    def set_Nombre(self,nombre):
        self.Nombre = nombre
    
    def get_Email(self):
        return self.Email
    
    def set_Email(self,email):
        self.Email = email
    
    def get_Telefono(self):
        return self.Telefono
    
    def set_Telefono(self,telefono):
        self.Telefono = telefono

    def get_Cuil_Cuit(self):
        return self.Cuil_Cuit
    
    def set_Cuil_Cuit(self, cuil_cuit):
        self.Cuil_Cuit = cuil_cuit
    
    def get_Direccion(self):
        return self.Direccion
    
    def set_Direccion(self,direccion):
        self.Direccion = direccion
    
    def __str__(self):
        return ("El complejo es: " + self.Nombre + "\nEl email es: " + self.Email + "\nEl telefono es: " +self.Telefono)
        
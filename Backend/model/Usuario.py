class Usuario:
    Nombre = ""
    Apelllido = ""
    DNI = ""
    Email = ""
    Password = ""
    Habilitado = True
    Fecha_creacion = ""
    Fecha_update = ""
    Direccion = ""

    def _init_(self,nombre,apellido,dni,email,password,habilitado,
                fecha_creacion,fecha_update,direccion):
                self.Nombre = nombre
                self.Apelllido = apellido
                self.DNI = dni
                self.Email = email
                self.Password = password
                self.Habilitado = habilitado
                self.Fecha_creacion = fecha_creacion
                self.Fecha_update = fecha_update
                self.Direccion = direccion
    
    def get_Nombre(self):
        return self.Nombre

    def set_Nombre(self,nombre):
        self.Nombre = nombre
    
    def get_Apellido(self):
        return self.Apelllido
    
    def set_Apellido(self,apellido):
        self.Apelllido = apellido

    def get_DIN(self):
        return self.DNI
    
    def set_DNI(self,dni):
        self.DNI = dni
    
    def get_Email(self):
        return self.DNI
    
    def set_Email(self, email):
        self.Email = email
   
    def get_Password(self):
        return self.Password
    
    def set_Passsword(self, password):
        self.Password = password
   
    def get_Habilitado(self):
        return self.Habilitado

    def set_Habilitado(self,habilitado):
        self.Habilitado = habilitado
    

    def get_Fecha_creacion(self):
        return self.Fecha_creacion

    def set_Fecha_creacion(self, fecha_creacion):
        self.Fecha_creacion = fecha_creacion
    
    def get_Fecha_update(self):
        return self.Fecha_update
    
    def set_Fecha_update(self, fecha_update):
        self.Fecha_update = fecha_update
   
    def get_Direccion(self):
        return self.Direccion

    def set_Direccion(self, direccion):
        self.Direccion = direccion
    
    def __str__(self):
        return ("El nombre es: " + self.Nombre + " \nEl apellido es :" + self.Apelllido + "\nEl Email es: " + self.Email)
        


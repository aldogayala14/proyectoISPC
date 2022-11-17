class MedioPago:
    
    Entidad_Bancaria = ""
    Nombre = ""
    Is_Credito = False
    Cantidad_Cuotas = 0
    Monto = 0
    Fecha_Vencimiento = ""
    Descripcion =""


    def __init__(self,entidad_bancaria,nombre,is_credito,cantidad_cuotas,monto,fecha_vencimiento,descripcion):
        self.Entidad_Bancaria = entidad_bancaria
        self.Nombre = nombre
        self.Is_Credito = is_credito
        self.Cantidad_Cuotas = cantidad_cuotas
        self.Monto = monto
        self.Fecha_Vencimiento = fecha_vencimiento
        self.Descripcion = descripcion
    
    def get_Entidad_Bancaria(self):
        return self.Entidad_Bancaria
    
    def set_Entidad_Bancaria(self, entidad_bancaria):
        self.Entidad_Bancaria = entidad_bancaria
    
    def get_Nombre(self):
        return self.Nombre
    
    def set_Nombre(self,nombre):
        self.Nombre = nombre
    
    def get_Is_Credito(self):
        return self.Is_Credito 
    
    def set_Is_Credito(self, is_credito):
        self.Is_Credito = is_credito
    
    def get_Cantidad_Cuotas(self):
        return self.Cantidad_Cuotas

    def set_Cantidad_Cuotas(self,cantidad_cuotas):
        self.Cantidad_Cuotas = cantidad_cuotas
    
    def get_Monto(self):
        return self.Monto
    
    def set_Monto(self,monto):
        self.Monto = monto
    
    def get_Fecha_Vencimiento(self):
        return self.Fecha_Vencimiento
    
    def set_Fecha_Vencimiento(self,fecha_vencimiento):
        self.Fecha_Vencimiento = fecha_vencimiento

    def get_Descripcion(self):
        return self.Descripcion
    
    def set_Descricpion(self, descripcion):
        self.Descripcion = descripcion
    
    def __str__(self):
        return ("La entidad es: " + self.Entidad_Bancaria + "\nEl nombre es: " + self.Nombre + "\nEl monto es: " + self.Monto)

class Persona:
    def __init__(self, nombre, telefono) -> None:
        self.nombre = nombre
        self.telefono = telefono
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre} Telefono: {self.telefono}'
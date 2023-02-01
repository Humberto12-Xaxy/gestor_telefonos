from persona import Persona

class Directorio:
    def __init__(self) -> None:
        self.directorio = []

    def crear_directorio(self, nombre, telefono):
        persona = Persona(nombre, telefono)
        self.directorio.append(persona)

    def obtner_persona_por_nombres(self, nombre:str):
        con = 0
        for persona in self.directorio:
            con = 0
            for indice, letra in enumerate(nombre):
                if len(nombre) > len(persona.nombre):
                    break
                if letra == persona.nombre[indice]:
                    con += 1
                    if con > 1:
                        print(persona)
                        break
                    
            
            

if __name__ == '__main__':
    directorio = Directorio()
    while True:
        opcion = int(input('Agregar un nuevo registro [1] Buscar registro [2] Salir[cualquier numero] '))
        if opcion == 1:
            nombre = input('Escribe el nombre: ')
            numero = input('Escribe el numero de teléfono: ')
            directorio.crear_directorio(nombre, numero)
        elif opcion == 2:
            nombre = input('Introduce el nombre a buscar: ')
            directorio.obtner_persona_por_nombres(nombre)
        
        else:
            break
        

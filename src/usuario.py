# usuario.py
# Edición realizada por Víctor Figueroa
# Clase que representa a un usuario y su peso, con método corregido para actualizarlo correctamente

class Usuario:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

    def get_nombre(self):
        return self.nombre

    def get_peso(self):
        return self.peso

    def actualizar_peso(self, nuevo_peso):
        # Corregí este método para asignar el nuevo peso ingresado correctamente
        self.peso = nuevo_peso

    def mostrar_informacion(self):
        print(f"Usuario: {self.nombre}, Peso Actual: {self.peso} kg")

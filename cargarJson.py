import json

class cargadorJson:

    def __init__(self):
        self.data = {}

    def cargarJson(self, nombre, apellido, edad, altura):
        if not(nombre in self.data): 
            self.data[nombre] = {
                    'apellido' : apellido,
                    'edad' : edad,
                    'altura' : altura
                    }

    def crearYCargarJson(self):
        with open('data.json', 'w') as file:
            json.dump(self.data, file, indent=4)
    
    def mostrarJson(self):
        print(self.data)

    def leerJson(self):
        try:
            with open('data.json') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print("archivo no encontrado")
    
        
    def updateJson(self, nombre, apellido):
        if nombre in self.data:
            print(self.data[nombre]['apellido'])
            self.data[nombre]['apellido'] = apellido
            print(self.data[nombre]['apellido'])
            print("cliente " + nombre + " actualizado!")
        else:
            print("no existe cliente")

    def eliminar(self, nombre):
        if nombre in self.data:
            self.data.pop(nombre) 
            print("usuario eliminado")
        else:
            print("usuario no encontrado")


# ALTA, BAJA, MODIFICACIONES

c = cargadorJson()
c.leerJson()
c.updateJson('juan','rosales')
c.updateJson('ivan','rosales')
# c.cargarJson('juan','natello','33', '1.69')
c.eliminar('juan')
# c.cargarJson('ivan','natello','31', '1.69')
# c.mostrarJson()
# print(c.data)
c.crearYCargarJson()
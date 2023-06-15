from ClaseAgenteUniversitario import AgenteUniversitario
class PersonalApoyo(AgenteUniversitario):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.categoria = categoria

    def calcular_sueldo(self):
        porcentaje_antiguedad = self.antiguedad * 0.01
        sueldo = self.sueldo_basico + self.sueldo_basico * porcentaje_antiguedad
        return sueldo

    def mostrar_datos(self):
        print(f"Personal de Apoyo - Apellido: {self.apellido}, Nombre: {self.nombre}, Categoría: {self.categoria}")


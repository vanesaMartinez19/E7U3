from ClaseAgenteUniversitario import AgenteUniversitario
class Investigador(AgenteUniversitario):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.area_investigacion = area_investigacion
        self.tipo_investigacion = tipo_investigacion

    def calcular_sueldo(self):
        porcentaje_antiguedad = self.antiguedad * 0.01
        sueldo = self.sueldo_basico + self.sueldo_basico * porcentaje_antiguedad
        return sueldo

    def mostrar_datos(self):
        print(f"Investigador - Apellido: {self.apellido}, Nombre: {self.nombre}, Área de Investigación: {self.area_investigacion}, Tipo de Investigación: {self.tipo_investigacion}")


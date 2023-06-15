from ClaseAgenteUniversitario import AgenteUniversitario
class Docente(AgenteUniversitario):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.carrera = carrera
        self.cargo = cargo
        self.catedra = catedra

    def calcular_sueldo(self):
        porcentaje_antiguedad = self.antiguedad * 0.01
        porcentaje_cargo = 0.1 if self.cargo == "simple" else 0.2 if self.cargo == "semiexclusivo" else 0.5
        sueldo = self.sueldo_basico + self.sueldo_basico * porcentaje_antiguedad + self.sueldo_basico * porcentaje_cargo
        return sueldo

    def mostrar_datos(self):
        print(f"Docente - Apellido: {self.apellido}, Nombre: {self.nombre}, Carrera: {self.carrera}, Cargo: {self.cargo}, Cátedra: {self.catedra}")

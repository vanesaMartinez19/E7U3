class AgenteUniversitario(ABC):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad):
        self.cuil = cuil
        self.apellido = apellido
        self.nombre = nombre
        self.sueldo_basico = sueldo_basico
        self.antiguedad = antiguedad

    @abstractmethod
    def calcular_sueldo(self):
        porcentaje_antiguedad = self.antiguedad * 0.01
        porcentaje_cargo = 0.1 if self.cargo == "simple" else 0.2 if self.cargo == "semiexclusivo" else 0.5
        sueldo = self.sueldo_basico + self.sueldo_basico * porcentaje_antiguedad + self.sueldo_basico * porcentaje_cargo
        return sueldo

    @abstractmethod
    def mostrar_datos(self):
        print(
            f"Docente - Apellido: {self.apellido}, Nombre: {self.nombre}, Carrera: {self.carrera}, Cargo: {self.cargo}, Cátedra: {self.catedra}")

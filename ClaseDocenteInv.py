from ClaseInvestigador import Investigador
from ClaseDocente import Docente
class DocenteInvestigador(Docente, Investigador):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion, categoria, importe_extra):
        Docente.__init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra)
        Investigador.__init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion)
        self.categoria = categoria
        self.importe_extra = importe_extra

    def calcular_sueldo(self):
        sueldo_docente = Docente.calcular_sueldo(self)
        sueldo_investigador = Investigador.calcular_sueldo(self)
        sueldo = sueldo_docente + sueldo_investigador + self.importe_extra
        return sueldo

    def mostrar_datos(self):
        print(f"Docente Investigador - Apellido: {self.apellido}, Nombre: {self.nombre}, Carrera: {self.carrera}, Cargo: {self.cargo}, Cátedra: {self.catedra}, Área de Investigación: {self.area_investigacion}, Tipo de Investigación: {self.tipo_investigacion}")


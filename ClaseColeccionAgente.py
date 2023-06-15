import json
from collections.abc import Iterable
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClasePersonalApoyo import PersonalApoyo
from ClaseDocenteInv import DocenteInvestigador
from abc import ABC, abstractmethod

class ColeccionAgentes(Iterable):
    def __init__(self):
        self.agentes = []

    def __iter__(self):
        return iter(self.agentes)

    def insertarElemento(self, agente, posicion):
        if posicion < 0 or posicion > len(self.agentes):
            raise ValueError("La posición de inserción no es válida.")
        self.agentes.insert(posicion, agente)

    def agregarElemento(self, agente):
        self.agentes.append(agente)

    def mostrarElemento(self, posicion):
        if posicion < 0 or posicion >= len(self.agentes):
            raise IndexError("La posición especificada está fuera del rango válido.")
        agente = self.agentes[posicion]
        if isinstance(agente, Docente):
            return "Docente"
        elif isinstance(agente, PersonalApoyo):
            return "Personal de Apoyo"
        elif isinstance(agente, Investigador):
            return "Investigador"
        elif isinstance(agente, DocenteInvestigador):
            return "Docente Investigador"

    def obtener_docentes_investigadores(self):
        docentes_investigadores = []
        for agente in self.agentes:
            if isinstance(agente, DocenteInvestigador):
                docentes_investigadores.append(agente)
        docentes_investigadores.sort(key=lambda x: x.nombre)
        return docentes_investigadores

    def contar_agentes_por_area(self, area_investigacion):
        cantidad_docentes_investigadores = 0
        cantidad_investigadores = 0
        for agente in self.agentes:
            if isinstance(agente, DocenteInvestigador):
                cantidad_docentes_investigadores += 1
            elif isinstance(agente, Investigador) and agente.area_investigacion == area_investigacion:
                cantidad_investigadores += 1
        return cantidad_docentes_investigadores, cantidad_investigadores

    def listar_datos_agentes(self):
        agentes_ordenados = sorted(self.agentes, key=lambda x: x.apellido)
        for agente in agentes_ordenados:
            print(f"{agente.apellido}, {agente.nombre}, Tipo de Agente: {type(agente).__name__}, Sueldo: {agente.calcular_sueldo()}")

    def listar_docentes_investigadores_por_categoria(self, categoria):
        docentes_investigadores_categoria = []
        total_importe_extra = 0
        for agente in self.agentes:
            if isinstance(agente, DocenteInvestigador) and agente.categoria == categoria:
                docentes_investigadores_categoria.append(agente)
                total_importe_extra += agente.importe_extra
        docentes_investigadores_categoria.sort(key=lambda x: x.apellido)
        for agente in docentes_investigadores_categoria:
            print(f"{agente.apellido}, {agente.nombre}, Importe Extra: {agente.importe_extra}")
        print(f"Total a solicitar al Ministerio: {total_importe_extra}")

    def almacenar_datos_en_archivo(self, archivo):
        data = []
        for agente in self.agentes:
            if isinstance(agente, Docente):
                data.append({
                    "tipo": "Docente",
                    "cuil": agente.cuil,
                    "apellido": agente.apellido,
                    "nombre": agente.nombre,
                    "sueldo_basico": agente.sueldo_basico,
                    "antiguedad": agente.antiguedad,
                    "carrera": agente.carrera,
                    "cargo": agente.cargo,
                    "catedra": agente.catedra
                })
            elif isinstance(agente, PersonalApoyo):
                data.append({
                    "tipo": "Personal de Apoyo",
                    "cuil": agente.cuil,
                    "apellido": agente.apellido,
                    "nombre": agente.nombre,
                    "sueldo_basico": agente.sueldo_basico,
                    "antiguedad": agente.antiguedad,
                    "categoria": agente.categoria
                })
            elif isinstance(agente, Investigador):
                data.append({
                    "tipo": "Investigador",
                    "cuil": agente.cuil,
                    "apellido": agente.apellido,
                    "nombre": agente.nombre,
                    "sueldo_basico": agente.sueldo_basico,
                    "antiguedad": agente.antiguedad,
                    "area_investigacion": agente.area_investigacion,
                    "tipo_investigacion": agente.tipo_investigacion
                })
            elif isinstance(agente, DocenteInvestigador):
                data.append({
                    "tipo": "Docente Investigador",
                    "cuil": agente.cuil,
                    "apellido": agente.apellido,
                    "nombre": agente.nombre,
                    "sueldo_basico": agente.sueldo_basico,
                    "antiguedad": agente.antiguedad,
                    "carrera": agente.carrera,
                    "cargo": agente.cargo,
                    "catedra": agente.catedra,
                    "area_investigacion": agente.area_investigacion,
                    "tipo_investigacion": agente.tipo_investigacion,
                    "categoria": agente.categoria,
                    "importe_extra": agente.importe_extra
                })
        with open(archivo, "w") as file:
            json.dump(data, file)






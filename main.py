import json
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClasePersonalApoyo import PersonalApoyo
from ClaseDocenteInv import DocenteInvestigador
from ClaseColeccionAgente import ColeccionAgentes


def print_hi(name):

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



if __name__ == '__main__':
    # Ejemplo de uso
    coleccion_agentes = ColeccionAgentes()

    # Leer y procesar el archivo "personal.json"
    with open("personal.json", "r") as file:
        data = json.load(file)
        for item in data:
            tipo_agente = item["tipo"]
            cuil = item["cuil"]
            apellido = item["apellido"]
            nombre = item["nombre"]
            sueldo_basico = item["sueldo_basico"]
            antiguedad = item["antiguedad"]

            if tipo_agente == "Docente":
                carrera = item["carrera"]
                cargo = item["cargo"]
                catedra = item["catedra"]
                agente = Docente(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra)
            elif tipo_agente == "Personal de Apoyo":
                categoria = item["categoria"]
                agente = PersonalApoyo(cuil, apellido, nombre, sueldo_basico, antiguedad, categoria)
            elif tipo_agente == "Investigador":
                area_investigacion = item["area_investigacion"]
                tipo_investigacion = item["tipo_investigacion"]
                agente = Investigador(cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion,
                                      tipo_investigacion)
            elif tipo_agente == "Docente Investigador":
                carrera = item["carrera"]
                cargo = item["cargo"]
                catedra = item["catedra"]
                area_investigacion = item["area_investigacion"]
                tipo_investigacion = item["tipo_investigacion"]
                categoria = item["categoria"]
                importe_extra = item["importe_extra"]
                agente = DocenteInvestigador(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra,
                                             area_investigacion, tipo_investigacion, categoria, importe_extra)

            coleccion_agentes.agregarElemento(agente)

    # Ejemplo de uso del menú de opciones
    while True:
        print("Menú de Opciones:")
        print("1. Insertar agente en la colección")
        print("2. Agregar agente a la colección")
        print("3. Mostrar tipo de agente en una posición")
        print("4. Listar docentes investigadores por carrera")
        print("5. Contar docentes investigadores e investigadores por área de investigación")
        print("6. Listar datos de todos los agentes ordenados por apellido")
        print("7. Listar docentes investigadores por categoría")
        print("8. Almacenar datos de los agentes en el archivo 'personal.json'")
        print("9. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            cuil = input("Ingrese el CUIL: ")
            apellido = input("Ingrese el apellido: ")
            nombre = input("Ingrese el nombre: ")
            sueldo_basico = float(input("Ingrese el sueldo básico: "))
            antiguedad = int(input("Ingrese la antigüedad: "))
            carrera = input("Ingrese la carrera: ")
            cargo = input("Ingrese el cargo: ")
            catedra = input("Ingrese la cátedra: ")
            agente = Docente(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra)
            posicion = int(input("Ingrese la posición de inserción: "))
            coleccion_agentes.insertarElemento(agente, posicion)
            print("Agente insertado correctamente.")

        elif opcion == "2":
            cuil = input("Ingrese el CUIL: ")
            apellido = input("Ingrese el apellido: ")
            nombre = input("Ingrese el nombre: ")
            sueldo_basico = float(input("Ingrese el sueldo básico: "))
            antiguedad = int(input("Ingrese la antigüedad: "))
            carrera = input("Ingrese la carrera: ")
            cargo = input("Ingrese el cargo: ")
            catedra = input("Ingrese la cátedra: ")
            agente = Docente(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra)
            coleccion_agentes.agregarElemento(agente)
            print("Agente agregado correctamente.")

        elif opcion == "3":
            posicion = int(input("Ingrese la posición del agente: "))
            try:
                tipo_agente = coleccion_agentes.mostrarElemento(posicion)
                print(f"El tipo de agente en la posición {posicion} es: {tipo_agente}")
            except IndexError:
                print("La posición especificada está fuera del rango válido.")

        elif opcion == "4":
            carrera = input("Ingrese la carrera: ")
            docentes_investigadores_carrera = coleccion_agentes.obtener_docentes_investigadores_por_carrera(carrera)
            print(f"Docentes Investigadores de la carrera {carrera}:")
            for docente in docentes_investigadores_carrera:
                docente.mostrar_datos()

        elif opcion == "5":
            area_investigacion = input("Ingrese el área de investigación: ")
            cantidad_docentes_investigadores, cantidad_investigadores = coleccion_agentes.contar_agentes_por_area(
                area_investigacion)
            print(
                f"Cantidad de Docentes Investigadores en el área {area_investigacion}: {cantidad_docentes_investigadores}")
            print(f"Cantidad de Investigadores en el área {area_investigacion}: {cantidad_investigadores}")

        elif opcion == "6":
            coleccion_agentes.listar_datos_agentes()

        elif opcion == "7":
            categoria = input("Ingrese la categoría: ")
            coleccion_agentes.listar_docentes_investigadores_por_categoria(categoria)

        elif opcion == "8":
            archivo = input("Ingrese el nombre del archivo: ")
            coleccion_agentes.almacenar_datos_en_archivo(archivo)
            print("Datos almacenados correctamente.")

        elif opcion == "9":
            break

        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")



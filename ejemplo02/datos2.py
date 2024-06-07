from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_tablas import Establecimiento, Parroquia, Canton, Provincia

# Todos los establecimientos de la provincia de Bolivar.

# Crear el enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def establecimiento_provincia(provincia):
    establecimientos = session.query(Establecimiento).join(Parroquia).join(Canton).join(Provincia).filter(
        Provincia.nombre == provincia
    # session.query(Establecimiento): Inicia una consulta para obtener datos de la tabla Establecimiento.
    # .join(Parroquia): Realiza una unión (JOIN) con la tabla Parroquia a través de la relación definida en el modelo.
    # .join(Canton): Realiza una unión (JOIN) con la tabla Canton.
    # .join(Provincia): Realiza una unión (JOIN) con la tabla Provincia.
    # .filter(Provincia.nombre == provincia): Filtra los resultados para incluir solo aquellos establecimientos que están en la provincia especificada.
    # .all(): Ejecuta la consulta y devuelve todos los resultados.
    ).all()
    return establecimientos

# Ejemplo de uso
provincia = "BOLIVAR"
establecimientos = establecimiento_provincia(provincia)
for establecimiento in establecimientos:
    print(establecimiento)

session.close()

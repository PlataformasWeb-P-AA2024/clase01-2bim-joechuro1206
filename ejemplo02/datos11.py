from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_tablas import Establecimiento

# Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 090112.

# Crear el enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def establecimientos_sostenimiento_codigoDistrito():
    establecimientos = session.query(Establecimiento).filter(
        Establecimiento.codigo_distrito == '02D04'  # Prueba con el código correcto
    ).order_by(Establecimiento.sostenimiento).all()
    return establecimientos

establecimientos = establecimientos_sostenimiento_codigoDistrito()
if establecimientos:
    for establecimiento in establecimientos:
        print(f"Sostenimiento: {establecimiento.sostenimiento} | Establecimiento: {establecimiento.nombre} | Código Distrito: {establecimiento.codigo_distrito}")
else:
    print("No se encontraron establecimientos con el código de distrito especificado.")

session.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_tablas import Establecimiento

# Los establecimientos que tienen como parte de nombre la cadena "UNIDOS"

# Crear el enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def establecimientos_cadena(cadena):
    establecimientos = session.query(Establecimiento).filter(
        Establecimiento.nombre.like(f"%{cadena}%")
    ).all()
    return establecimientos

cadena = "UNIDOS"
establecimientos = establecimientos_cadena(cadena)
for establecimiento in establecimientos:
    print(establecimiento)

for establecimiento in establecimiento:
    print(f"Establecimiento: {establecimiento.nombre} | Provincia: {establecimiento.parroquia.canton.provincia.nombre}")

session.close()

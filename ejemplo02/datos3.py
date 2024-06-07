from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_tablas import Establecimiento, Parroquia, Canton

# Todos los establecimientos del cantón de Guayaquil.

# Crear el enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def establecimientos_canton(canton):
    establecimientos = session.query(Establecimiento).join(Parroquia).join(Canton).filter(
        Canton.nombre == canton
    ).all()
    return establecimientos

canton = "GUAYAS" # Prueba con CALUMA
establecimientos = establecimientos_canton(canton)

if establecimientos:
    for establecimiento in establecimientos:
        print(establecimiento)
else:
    print(f"No existen establecimientos en el cantón: {canton}")

session.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_tablas import Establecimiento, Parroquia, Canton

# Todos los establecimientos del cantón de Urdaneta y Vinces.

# Crear el enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def establecimiento_2cantones(cantones):
    establecimientos = session.query(Establecimiento).join(Parroquia).join(Canton).filter(
        Canton.nombre.in_(cantones)
    ).all()
    return establecimientos


cantones = ["URDANETA", "VINCENS"] 
establecimientos = establecimiento_2cantones(cantones)
for establecimiento in establecimientos:
    print(establecimiento)

session.close()

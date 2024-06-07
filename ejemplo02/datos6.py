from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_tablas import Establecimiento, Parroquia, Canton

# Los cantones que tiene establecimientos como número de estudiantes tales como: 1, 74, 100

# Crear el enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Ejemplo de uso
cantones = session.query(Canton).filter(Establecimiento.numero_estudiantes.in_([1, 74, 100])).all()

for canton in cantones:
    print(f"Canton: {canton.nombre} | Provincia {canton.provincia.nombre}")
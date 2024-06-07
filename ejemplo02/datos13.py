from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_tablas import Establecimiento

# Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores y régimen escolar igual Costa.

# Crear el enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def filtrar_nEstudiantes_nDocentes_regimen():
    establecimientos = session.query(Establecimiento).filter(
        Establecimiento.numero_docentes > 100,
        Establecimiento.regimen_escolar == 'COSTA'
    ).order_by(Establecimiento.numero_docentes).all()
    return establecimientos

establecimientos = filtrar_nEstudiantes_nDocentes_regimen()
for establecimiento in establecimientos:
    print(f"Establecimiento: {establecimiento.nombre} | Profesores: {establecimiento.numero_docentes} | Régimen Escolar: {establecimiento.regimen_escolar}")

session.close()

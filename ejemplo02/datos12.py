from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_tablas import Establecimiento

# Los establecimientos ordenados por número de estudiantes; 
# que tengan más de 100 profesores y régimen escolar igual Sierra.

# Crear el enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def filtrar_nEstudiantes_nDocentes_regimen():
    establecimientos = session.query(Establecimiento).filter(
        Establecimiento.numero_docentes > 100, # probar con 10
        Establecimiento.regimen_escolar == 'SIERRA'
    ).order_by(Establecimiento.numero_estudiantes).all()
    return establecimientos

establecimientos = filtrar_nEstudiantes_nDocentes_regimen()
if establecimientos:
    for establecimiento in establecimientos:
        print(f"Establecimiento: {establecimiento.nombre} | Estudiantes: {establecimiento.numero_estudiantes} | Profesores: {establecimiento.numero_docentes} | Régimen Escolar: {establecimiento.regimen_escolar}")
else:
    print("No se encontraron datos")

session.close()

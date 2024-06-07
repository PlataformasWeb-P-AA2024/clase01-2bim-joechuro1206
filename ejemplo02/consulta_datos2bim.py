from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from crear_tablas import Canton, Provincia, Parroquia

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()
cantones = session.query(Canton).all()

cantones = session.query(Canton).all()
for c in cantones:
    print(f"Cantón: {c.nombre} | Número de estudiantes: {c.obtener_numero_estudiantes()}")

print("----------------")

provincias = session.query(Provincia).all()
for p in provincias:
    print(f"Provincia: {p.nombre} | Número de docentes: {p.obtener_numero_docentes()}")

print("----------------")

parroquias = session.query(Parroquia).all()
for parroquia in parroquias:
    print(f"Parroquia: {parroquia.nombre} | Número de establecimientos: {parroquia.obtener_numero_establecimientos()}")

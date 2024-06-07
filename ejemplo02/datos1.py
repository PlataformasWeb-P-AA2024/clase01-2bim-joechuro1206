from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from crear_tablas import Establecimiento, Parroquia

# Todos los establecimientos que pertenecen al Código División 
# Política Administrativa Parroquia con valor 020151 y 020153

# Crear el enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def establecimiento_codigoParroquia(codigo1, codigo2):
    # Definimos una función que toma dos códigos como parámetros.
    establecimientos = session.query(Establecimiento).join(Parroquia).filter(
        (Parroquia.codigo_division == codigo1) | (Parroquia.codigo_division == codigo2)
    # Realizamos una consulta sobre la tabla Establecimiento y hace un join con la tabla Parroquia,
    # Aplica un filtro para seleccionar solo aquellos establecimientos que están en parroquias con los códigos codigo1 o codigo2
    ).all()
    return establecimientos

codigo1 = 20151
codigo2 = 20153
establecimientos = establecimiento_codigoParroquia(codigo1, codigo2)
for establecimiento in establecimientos:
    print(establecimiento)

session.close()
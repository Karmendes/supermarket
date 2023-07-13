from src.etl.etl_prix import ETLPrix
from src.etl.etl_zonasul import ETLZonaSul

def create_etl(etl_name):

    factory = {
        "zona_sul": ETLZonaSul(),
        "prix":ETLPrix()
    }

    if etl_name in factory:
        return factory[etl_name]
    return None

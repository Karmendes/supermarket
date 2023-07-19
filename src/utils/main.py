from os import getenv
from dotenv import load_dotenv
load_dotenv()


def generate_list(config_dict):
    routes = []
    for chave, valores in config_dict.items():
        for valor in valores:
            routes.append(f"{chave}/{valor}")
    return routes

def generate_credentials():
    return getenv("USER"),getenv("USER"),getenv("HOST"),getenv("PORT"),getenv("DATABASE")
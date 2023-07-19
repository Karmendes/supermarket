def generate_list(config_dict):
    routes = []
    for chave, valores in config_dict.items():
        for valor in valores:
            routes.append(f"{chave}/{valor}")
    return routes
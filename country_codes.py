from pygal_maps_world import i18n

def get_country_code(country_name):
    """Devolve o código de duas letras do Pygal para um país, dado o seu nome."""
    for code, name in i18n.COUNTRIES.items():
        if name == country_name:
            return code
    # Se o país não foi encontrado, devolve None
    return None
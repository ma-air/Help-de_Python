def saludo(idioma):
    def saludo_es():
        print("HOLA")
    def saludo_en():
        print("HI")
    idioma_func = {"es": saludo_es,
                    "en": saludo_en}
    return idioma_func[idioma]

saludar=saludo("es")
saludar()

saludar=saludo("en")
saludar()
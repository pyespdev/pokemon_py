debilidades = {
    "Agua": {
        "débil": ["Eléctrico", "Planta"],
        "resistente": ["Agua", "Fuego", "Hielo"],
        "inmune": []
    },
    "Bicho": {
        "débil": ["Fuego", "Roca", "Veneno", "Volador"],
        "resistente": ["Lucha", "Planta", "Tierra"],
        "inmune": []
    },
    "Dragón": {
        "débil": ["Dragón", "Hielo"],
        "resistente": ["Agua", "Eléctrico", "Fuego", "Planta"],
        "inmune": []
    },
    "Eléctrico": {
        "débil": ["Tierra"],
        "resistente": ["Eléctrico", "Volador"],
        "inmune": []
    },
    "Fantasma": {
        "débil": ["Fantasma"],
        "resistente": ["Veneno"],
        "inmune": ["Lucha", "Normal"]
    },
    "Fuego": {
        "débil": ["Agua", "Roca", "Tierra"],
        "resistente": ["Bicho", "Fuego", "Planta"],
        "inmune": []
    },
    "Hielo": {
        "débil": ["Fuego", "Lucha", "Roca"],
        "resistente": ["Hielo"],
        "inmune": []
    },
    "Lucha": {
        "débil": ["Psíquico", "Volador"],
        "resistente": ["Bicho", "Roca"],
        "inmune": []
    },
    "Normal": {
        "débil": ["Lucha"],
        "resistente": [],
        "inmune": ["Fantasma"]
    },
    "Planta": {
        "débil": ["Bicho", "Fuego", "Hielo", "Veneno", "Volador"],
        "resistente": ["Agua", "Eléctrico", "Planta", "Tierra"],
        "inmune": []
    },
    "Psíquico": {
        "débil": ["Bicho"],
        "resistente": ["Lucha", "Psíquico"],
        "inmune": ["Fantasma"]
    },
    "Roca": {
        "débil": ["Agua", "Lucha", "Planta", "Tierra"],
        "resistente": ["Fuego", "Normal", "Veneno", "Volador"],
        "inmune": []
    },
    "Tierra": {
        "débil": ["Agua", "Hielo", "Planta"],
        "resistente": ["Roca", "Veneno"],
        "inmune": ["Eléctrico"]
    },
    "Veneno": {
        "débil": ["Bicho", "Psíquico", "Tierra"],
        "resistente": ["Lucha", "Planta", "Veneno"],
        "inmune": []
    },
    "Volador": {
        "débil": ["Eléctrico", "Hielo", "Roca"],
        "resistente": ["Bicho", "Lucha", "Planta"],
        "inmune": ["Tierra"]
    },
}
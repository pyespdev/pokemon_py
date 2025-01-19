efectos = {
    "SIN_EFECTO_ADICIONAL": {
        "nombre": "SIN_EFECTO_ADICIONAL",
        "efecto": []
    },
    "ATAQUE_BAJA1_EFECTO": {
        "nombre": "ATAQUE_BAJA1_EFECTO",
        "efecto": ["ataque", "bajar", 1]
    },
    "DEFENSA_BAJA1_EFECTO": {
        "nombre": "DEFENSA_BAJA1_EFECTO",
        "efecto": ["defensa", "bajar", 1]
    },
    "DEFENSA_BAJA2_EFECTO": {
        "nombre": "DEFENSA_BAJA2_EFECTO",
        "efecto": ["defensa", "bajar", 2]
    },
    "PRECISION_BAJA1_EFECTO": {
        "nombre": "PRECISION_BAJA1_EFECTO",
        "efecto": [],
        "efecto_ataque": ["precision", "bajar", 1]
    },
    "PRECISION_SUBE1_EFECTO": {
        "nombre": "PRECISION_SUBE1_EFECTO",
        "efecto": [],
        "efecto_ataque": ["precision", "subir", 1]
    },
    "ATAQUE_PRECISION_SUBE1_EFECTO": {
    },
    "ATAQUE_DEFENSA_SUBE1_EFECTO": {
    },
    "ATAQUE_SUBE2_EFECTO": {
        "nombre": "ATAQUE_SUBE2_EFECTO",
        "efecto": ["ataque", "subir", 2],
        "efecto_ataque": ["ataque", "subir", 1]
    },
    "ATAQUE_DEFENSA_SUBE1_EFECTO": {
    }
}

# Se debería indicar si afecta al usuario o al oponente
# con un atributo "objetivo" por ejemplo
# no se si aquí o en Ataques.py

# Se deberían introducir las características de:
#  "precision" -> Ataques
#  "evasion" -> Pokemon

# Se deberían introducir los cambios de estado (Persistentes)
# "Paralizado", "Envenenado", "Congelado", "Dormido", "Quemado"

# Se deberían introducir los cambios de estado (Efímeros)
# "Confuso", "Maldito", "Enamorado", "Atrapado", "Drenado", "Canto Mortal"

"""
TODOS LOS EFECTOS POSIBLES

    PRECISION_BAJA1
    ARMADURA_ACIDA
    ATAQUE_PRECISION_SUBE1
    ATAQUE_DEFENSA_SUBE1
    ATAQUE_BAJA_SIDE
    ATAQUE_BAJA1
    ATAQUE_ESPECIAL_VELOCIDAD_SUBE1
    ATAQUE_2VECES
    ATAQUE_SUBE_SIDE
    ATAQUE_SUBE2
    HUESOMERANG
    QUEMAR_SIDE1
    QUEMAR_SIDE2
    CARGA
    CONFUSION_GRANDE_SIDE
    CONFUSION
    CONFUSION_SIDE
    CONVERSION
    RIZO_DEFENSA
    DEFENSA_BAJA_SIDE
    DEFENSA_BAJA1
    DEFENSA_BAJA2
    DEFENSA_SUBE1
    DEFENSA_SUBE2
    ANULACION
    DRENAR_VIDA
    COMESUEÑOS
    EVASION_SUBE1
    EXPLOTAR
    CORTAFUEGOS
    RETROCEDER_SIDE1
    RETROCEDER_SIDE2
    VOLAR
    FOCO_ENERGIA
    CONGELAR_SIDE
    DESARROLLO
    NEBLINA
    CURAR
    HIPERRAYO
    PATADA_SALTO
    DRENADORAS
    PANTALLA_LUZ
    METRONOMO
    IMITACION
    MOV_ESPEJO
    NIEBLA
    KO
    PARALIZAR
    PARALIZAR_SIDE1
    PARALIZAR_SIDE2
    DIA_PAGO
    ENVENENAR
    ENVENENAR_SIDE1
    ENVENENAR_SIDE2
    RETROCEDER
    REFLEJO
    DORMIR
    DAÑO_ESPECIAL
    ESPECIAL_BAJA_SIDE
    ESPECIAL_SUBE2
    VELOCIDAD_BAJA_SIDE
    VELOCIDAD_BAJA1
    VELOCIDAD_SUBE2
    SALPICADURA
    SUSTITUTO
    SUPERDIENTE
    RAPIDEZ
    TELETRANSPORTE
    GOLPE_DANZA_PETALO
    TRANSFORMACION
    ATRAPAR
    TRIATAQUE
    DOBLE_ATAQUE
    2_3_ATAQUES
    2_A_5_ATAQUES
    REFUGIO
"""
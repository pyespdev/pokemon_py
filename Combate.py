"""
 Importamos la funcion random para el ataque del Pokemon Oponente
"""
import random
"""
 Importamos la Pokedex, archivo donde están los Pokemon (nombres y tipos)
"""
from Pokedex import pokemon_dict
"""
 Creamos la clase Ataque con los atributos nombre que guardará el nombre del ataque
 y poder que guardará los puntos de daño de los ataques
"""
class Ataque:
    def __init__(self, nombre: str, poder: int) -> None:
        self.nombre = nombre
        self.poder = poder
"""
 Creamos la clase Pokemon con los atributos nombre, vida y ataques
 y los métodos para agregar, elegir y recibir ataques
"""
class Pokemon:
    def __init__(self, nombre: str, vida: int) -> None:
        self.nombre = nombre
        self.vida = vida
        self.ataques = {}

    def agregar_ataque(self, nombre: str, poder: int):
        self.ataques[nombre] = Ataque(nombre, poder)

    def elegir_ataque(self, nombre_ataque: str):
        return self.ataques.get(nombre_ataque)

    def recibir_ataque(self, ataque: Ataque):
        self.vida -= ataque.poder
        if self.vida < 0:
            self.vida = 0
"""
 Creamos la clase Combate que contendrá el Pokemon del jugador y del oponente
 y los turnos de ataque de jugador y oponente. Empezará atacando el oponente.
"""
class Combate:
    def __init__(self, jugador: Pokemon, oponente: Pokemon) -> None:
        self.jugador = jugador
        self.oponente = oponente
        self.pulsa_para_continuar = "\nPulsa ENTER/INTRO para continuar...\n"

    def turno_atacar_oponente(self):
        ataque_oponente = random.choice(list(self.oponente.ataques.values()))
        print(f"{self.oponente.nombre} usa {ataque_oponente.nombre} y causa {ataque_oponente.poder} puntos de daño.")
        self.jugador.recibir_ataque(ataque_oponente)
        print(f"Te quedan {self.jugador.vida} puntos de vida.")

    def turno_atacar_jugador(self):
        print("\nAhora es tu turno para atacar. Puedes elegir entre los 3 ataques que tienes disponibles.")
        ataques_posibles = list(self.jugador.ataques.values())
        elegir_ataque = int(input("Elige que ataque quieres hacer\n"
                                  f"1- {ataques_posibles[0].nombre}\n"
                                  f"2- {ataques_posibles[1].nombre}\n"
                                  f"3- {ataques_posibles[2].nombre}\n"
                                  "Tu opción --> "))
        if 1 <= elegir_ataque <= len(ataques_posibles):
            ataque_jugador = ataques_posibles[elegir_ataque - 1]
            print(f"¡Lanzas un ataque {ataque_jugador.nombre} y causas {ataque_jugador.poder} puntos de daño a {self.oponente.nombre}!.")
            self.oponente.recibir_ataque(ataque_jugador)
            print(f"A {self.oponente.nombre} le quedan {self.oponente.vida} puntos de vida.")
        else:
            print("¡Has perdido el turno! No elegiste un ataque válido.")

 # Elegimos los Pokemon del Oponente y del Jugador desde la Pokedex eligiendo un número del 1 al 151
    def elegir_pokemon_oponente():
        # Elegir Pokémon oponente con validación
        while True:
            try:
                elegir_pokemon_oponente = int(input("Elige un pokemon para tu oponente. Del 1 al 151.\n"))
                # Comprobar si el número está dentro del rango válido
                if 1 <= elegir_pokemon_oponente <= 151:
                    break  # Salir del bucle si el número es válido
                else:
                    print("¡Número fuera de rango! Elige un número entre 1 y 151.")
            except ValueError:
                # Si el usuario introduce algo que no es un número
                print("¡Por favor ingresa un número válido entre 1 y 151.")
        # Usar zfill para agregar ceros a la izquierda y crear la cadena con #
        elegir_pokemon_oponente = f"#{str(elegir_pokemon_oponente).zfill(3)}"
        pokemon_oponente = Pokemon(pokemon_dict[elegir_pokemon_oponente]['nombre'], 130)
        pokemon_oponente.agregar_ataque("Placaje", 40)
        pokemon_oponente.agregar_ataque("Gruñido", 0)
        pokemon_oponente.agregar_ataque("Látigo Cepa", 45)
        return pokemon_oponente
    
    def elegir_pokemon_jugador():
        while True:
            try:
                elegir_pokemon_jugador = int(input("¡Muy bien!, ahora elige tu Pokemon. Del 1 al 151.\n"))
                # Comprobar si el número está dentro del rango válido
                if 1 <= elegir_pokemon_jugador <= 151:
                    break  # Salir del bucle si el número es válido
                else:
                    print("¡Número fuera de rango! Elige un número entre 1 y 151.")
            except ValueError:
                # Si el usuario introduce algo que no es un número
                print("¡Por favor ingresa un número válido entre 1 y 151.")
        # Usar zfill para agregar ceros a la izquierda y crear la cadena con #
        elegir_pokemon_jugador = f"#{str(elegir_pokemon_jugador).zfill(3)}"
        pokemon_jugador = Pokemon(pokemon_dict[elegir_pokemon_jugador]['nombre'], 130)
        pokemon_jugador.agregar_ataque("Arañazo", 40)
        pokemon_jugador.agregar_ataque("Gruñido", 0)
        pokemon_jugador.agregar_ataque("Ascuas", 40)
        return pokemon_jugador

# Explicación del juego, componentes y dinámica
    def jugar(self):
        print(f"** COMBATE POKEMON -- {self.oponente.nombre} contra {self.jugador.nombre} **")
        print(f"Te reto a un combate entre personajes Pokemon. Yo controlo a {self.oponente.nombre} y tú a {self.jugador.nombre}.")
        print("Combatimos mientras ambos tengamos vida.\n")
        input(self.pulsa_para_continuar)

        while self.jugador.vida > 0 and self.oponente.vida > 0:
            self.turno_atacar_oponente()
            if self.jugador.vida == 0:
                break
            input(self.pulsa_para_continuar)
            self.turno_atacar_jugador()
            if self.oponente.vida == 0:
                break
            input(self.pulsa_para_continuar)
            print("\nResumen del combate:")
            print(f"Te quedan {self.jugador.vida} puntos de vida.")
            print(f"A {self.oponente.nombre} le quedan {self.oponente.vida} puntos de vida.")
        if self.jugador.vida == 0:
            print(f"\nLo siento, pero {self.oponente.nombre} te ha ganado.")
        if self.oponente.vida == 0:
            print(f"\n¡ENHORABUENA! Has derrotado a {self.oponente.nombre}.")
        print("\nEspero volver a verte pronto.")
"""
 Creamos un nuevo Combate con dos nuevos Pokemon:
 El primer Pokemon que pasamos como argumento es el del jugador y el segundo el del oponente
"""
combate = Combate(Combate.elegir_pokemon_jugador(), Combate.elegir_pokemon_oponente())
combate.jugar()

"""
 Siguientes Commits propuestos:
  - Cambiar en el método elegir_ataque() las opciones puestas a mano,
  - Controlar la entrada del usuario de modo que se garantice que el jugador elija un número válido entre 1 y 151
"""
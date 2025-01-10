import random                       # Para el ataque del Pokemon Oponente (de momento)
from Pokedex import pokedex         # Archivo donde están los Pokemon (id, nombre y tipos)
from Datos.Ataques import ataques   # Archivo donde estarán todos los Ataques y sus características

# Clase Ataque con los atributos nombre, tipo y poder
class Ataque:
    def __init__(self, nombre: str, tipo: str, poder: int) -> None:
        self.nombre = nombre
        self.tipo = tipo
        self.poder = poder

# Clase Pokemon con los atributos nombre, stats y ataques
# y los métodos para agregar, elegir y recibir ataques
class Pokemon:
    def __init__(self, nombre: str, tipos: str, stats: str) -> None:
        self.nombre = nombre
        self.tipos = tipos
        self.vida = stats['vida']
        self.ataque = stats['ataque']
        self.defensa = stats['defensa']
        self.velocidad = stats['velocidad']
        self.especial = stats['especial']
        self.ataques = {}

    def agregar_ataque(self, nombre: str, tipo: str, poder: int):
        self.ataques[nombre] = Ataque(nombre, tipo, poder)

    def elegir_ataque(self, nombre_ataque: str):
        return self.ataques.get(nombre_ataque)

    def recibir_ataque(self, ataque: Ataque):
        self.comparar_tipo_defensor(ataque)
        self.vida -= ataque.poder
        if self.vida < 0:
            self.vida = 0
    """
    Introducimos la comparación de tipos entre Pokemon y Ataque para posteriormente
    calcular la Fórmula del daño directo, que será algo como esto:
        
    Daño = P1 * (P2 / P3 + 2)

        P1 = 0.01 * $B * $E *V
        P2 = (0.2 * $N + 1) * $A * $P
        P3 = 25 / $D

        $B = Bonificación
        $E = Efectividad
        $V = Variación
        $N = Nivel
        $A = Ataque / Especial
        $P = Poder de Ataque
        $D = Defensa / Especial

    Para saber la clase del Ataque (Físico o Especial), vale con saber el tipo.
    tipos = ["Agua", "Bicho", "Dragón", "Eléctrico", "Fantasma", "Fuego", "Hielo", "Lucha", "Normal", "Planta", "Psíquico", "Roca", "Tierra", "Veneno", "Volador"]
    ataques_fisicos = ["Bicho", "Fantasma", "Lucha", "Normal", "Roca", "Tierra", "Veneno", "Volador"]
    ataques_especiales = ["Agua", "Dragón", "Eléctrico", "Fuego", "Hielo", "Planta", "Psíquico"]
    """
    
    # P1 (Primera parte de la Fórmula del daño directo)
    # P1 = 0.01 * bonificacion * efectividad * variacion

    # $B
    # Bonificación: si el ataque es del mismo tipo que el Pokemon que lo lanza toma un valor de 1,5
    # si el ataque es de un tipo diferente que el Pokemon que lo lanza toma un valor de 1.
    def comparar_tipo_atacante(self, ataque: Ataque):
        if self.tipos[0] == ataque.tipo :
            print(f"{self.nombre}, que realiza el ataque es de tipo {self.tipos[0]}; {ataque.nombre} es de tipo {ataque.tipo}.")
            bonificacion = 1.5
        else:
            print(f"{self.nombre}, que realiza el ataque es de tipo {self.tipos[0]}; {ataque.nombre} es de tipo {ataque.tipo}.")
            bonificacion = 1
        return bonificacion

    # $E
    # Efectividad que podrá tener los valores 0, 0.25, 0.5, 1, 2 y 4
    # en función de la Relación entre Tipos (Archivo Debilidades)
    def comparar_tipo_defensor(self, ataque: Ataque):
        if ataque.tipo == self.tipos[0] :
            print(f"{self.nombre}, que recibe el ataque es de tipo {self.tipos[0]}; {ataque.nombre} es de tipo {ataque.tipo}.")
        else:
            print(f"{self.nombre}, que recibe el ataque es de tipo {self.tipos[0]}; {ataque.nombre} es de tipo {ataque.tipo}.")

    # $V
    # Variación que tendrá un valor entre 85 y 100 (incluidos)
    variacion = random.randint(85,100)
    print(f"El Número de Variación ha sido {variacion}.")

    # P2 (Segunda parte de la Fórmula del daño directo)
    # P2 = (0.2 * nivel + 1) * clase_Ataque * Poder_ataque
    def comparar_tipo_ataque(self, ataque: Ataque):
        ataques_fisicos = ["Bicho", "Fantasma", "Lucha", "Normal", "Roca", "Tierra", "Veneno", "Volador"]
        if ataque.tipo in ataques_fisicos:
            clase_ataque = "Físico"
            print(f"{self.nombre}, realiza un ataque es de clase {clase_ataque}, ya que es de tipo {ataque.tipo}.")
        else:
        # ataques_especiales = ["Agua", "Dragón", "Eléctrico", "Fuego", "Hielo", "Planta", "Psíquico"]
            clase_ataque = "Especial"
            print(f"{self.nombre}, realiza un ataque es de clase {clase_ataque}, ya que es de tipo {ataque.tipo}.")
        return clase_ataque
    # P3 (Tercera parte de la Fórmula del daño directo)
    # P3 = 25 / tipo_Defensa
    # Sera Defensa / Especial según el tipo de Ataque, se debería implentar en comparar_tipo_ataque()

# Clase Combate donde se desarrolla el juego
# Se eligen los Pokemon de Jugador y Oponente y sus turnos
class Combate:
    def __init__(self, jugador: Pokemon, oponente: Pokemon) -> None:
        self.jugador = jugador
        self.oponente = oponente
        self.pulsa_para_continuar = "\nPulsa ENTER/INTRO para continuar...\n"

    def turno_atacar_oponente(self):
        ataque_oponente = random.choice(list(self.oponente.ataques.values()))
        self.oponente.comparar_tipo_atacante(ataque_oponente)
        print(f"{self.oponente.nombre} usa {ataque_oponente.nombre} y causa {ataque_oponente.poder} puntos de daño.")
        self.jugador.recibir_ataque(ataque_oponente)
        print(f"Te quedan {self.jugador.vida} puntos de vida.")

    def turno_atacar_jugador(self):
        print("\nAhora es tu turno para atacar. Puedes elegir entre los ataques que tienes disponibles.")
        ataques_posibles = list(self.jugador.ataques.values())
        mensaje_ataques = "Elige qué ataque quieres hacer:\n"
        # Usando enumerate para obtener tanto el índice como el nombre del ataque
        for index, ataque in enumerate(ataques_posibles):
            mensaje_ataques += f"{index+1}- {ataque.nombre}\n"

        elegir_ataque = int(input(mensaje_ataques + "Tu opción --> "))        

        if 1 <= elegir_ataque <= len(ataques_posibles):
            ataque_jugador = ataques_posibles[elegir_ataque - 1]
            self.jugador.comparar_tipo_atacante(ataque_jugador)
            print(f"¡Lanzas un ataque {ataque_jugador.nombre} y causas {ataque_jugador.poder} puntos de daño a {self.oponente.nombre}!.")
            self.oponente.recibir_ataque(ataque_jugador)
            print(f"A {self.oponente.nombre} le quedan {self.oponente.vida} puntos de vida.")
        else:
            print("¡Has perdido el turno! No elegiste un ataque válido.")

    # Elegimos los Pokemon del Oponente y del Jugador desde la Pokedex eligiendo un número del 1 al 151
    def elegir_pokemon_oponente():
        while True:
            try:
                elegir_pokemon_oponente = int(input("Elige un pokemon para tu oponente. Del 1 al 151.\n"))
                if 1 <= elegir_pokemon_oponente <= 151:
                    break  # Salir del bucle si el número es válido
                else:
                    print("¡Número fuera de rango! Elige un número entre 1 y 151.")
            except ValueError:
                # Si el usuario introduce algo que no es un número
                print("¡Por favor ingresa un número válido entre 1 y 151.")
        # Usar zfill para agregar ceros a la izquierda y crear la cadena con #
        elegir_pokemon_oponente = f"#{str(elegir_pokemon_oponente).zfill(3)}"
        pokedex_oponente = pokedex[elegir_pokemon_oponente]['nombre']

        # Importar dinámicamente el Pokemon del Oponente usando __import__
        module = __import__(f"Datos.Pokemon.Stats_base.{pokedex_oponente}", fromlist=[pokedex_oponente])
        # Acceder a la clase dentro del módulo importado
        poke_oponente = getattr(module, pokedex_oponente)
        pokemon_oponente = Pokemon(poke_oponente["nombre"], poke_oponente["tipos"], poke_oponente["stats"])

        # Recorrer el array de ataques del Oponente
        for ataque_nombre in poke_oponente["ataques"]:
            # Obtener los detalles del ataque desde el diccionario `ataques`
            ataque = ataques[ataque_nombre]
            # Llamar al método agregar_ataque con el nombre, tipo y poder del ataque
            pokemon_oponente.agregar_ataque(ataque["nombre"], ataque["tipo"], ataque["poder"])
        
        return pokemon_oponente
    
    def elegir_pokemon_jugador():
        while True:
            try:
                elegir_pokemon_jugador = int(input("¡Muy bien!, ahora elige tu Pokemon. Del 1 al 151.\n"))
                if 1 <= elegir_pokemon_jugador <= 151:
                    break  # Salir del bucle si el número es válido
                else:
                    print("¡Número fuera de rango! Elige un número entre 1 y 151.")
            except ValueError:
                # Si el usuario introduce algo que no es un número
                print("¡Por favor ingresa un número válido entre 1 y 151.")
        # Usar zfill para agregar ceros a la izquierda y crear la cadena con #
        elegir_pokemon_jugador = f"#{str(elegir_pokemon_jugador).zfill(3)}"
        pokedex_jugador = pokedex[elegir_pokemon_jugador]['nombre']

        # Importar dinámicamente el Pokemon del Jugador usando __import__
        module = __import__(f"Datos.Pokemon.Stats_base.{pokedex_jugador}", fromlist=[pokedex_jugador])
        # Acceder a la clase dentro del módulo importado
        poke_jugador = getattr(module, pokedex_jugador)
        pokemon_jugador = Pokemon(poke_jugador["nombre"], poke_jugador["tipos"], poke_jugador["stats"])

        # Recorrer el array de ataques del Jugador
        for ataque_nombre in poke_jugador["ataques"]:
            # Obtener los detalles del ataque desde el diccionario `ataques`
            ataque = ataques[ataque_nombre]
            # Llamar al método agregar_ataque con el nombre, tipo y poder del ataque
            pokemon_jugador.agregar_ataque(ataque["nombre"], ataque["tipo"], ataque["poder"])
        
        return pokemon_jugador

    # Explicación del juego, componentes y dinámica
    def jugar(self):
        print(f"** COMBATE POKEMON -- {self.oponente.nombre} contra {self.jugador.nombre} **")
        print(f"Te reto a un combate entre personajes Pokemon. Yo controlo a {self.oponente.nombre} y tú a {self.jugador.nombre}.")
        print("Combatimos mientras ambos tengamos vida.\n")
        input(self.pulsa_para_continuar)
        # Empezará atacando el oponente.
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

# Generamos el Combate
combate = Combate(Combate.elegir_pokemon_jugador(), Combate.elegir_pokemon_oponente())
combate.jugar()

"""
Propuesta de Siguientes Commits:
- Terminar de Implementar los Tipos (Efectividad entre ellos)
- Implementar los Efectos Especiales de los Ataques
"""
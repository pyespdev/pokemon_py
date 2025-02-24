import random
from Pokedex import pokedex         # Archivo donde están los Pokemon (id, nombre y tipos)
from Datos.Ataques import ataques   # Archivo donde estarán todos los Ataques y sus características
from Datos.Debilidades import debilidades   # Debilidades de cada Tipo
from Datos.Efectos import efectos   # Archivo donde estarán los efectos especiales de los Ataques

class Ataque:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.tipo = ataques[nombre]['tipo']
        self.poder = ataques[nombre]['poder']
        self.efecto = ataques[nombre]['efecto']
        self.precision = ataques[nombre]['precision']

class Pokemon:
    def __init__(self, nombre: str, tipos: str, stats: str, nivel: int) -> None:
        self.nombre = nombre
        self.nivel = nivel
        self.tipos = tipos
        self.vida = self.calcular_stats(stats,'vida')
        self.ataque = self.calcular_stats(stats,'ataque')
        self.defensa = self.calcular_stats(stats,'defensa')
        self.velocidad = self.calcular_stats(stats,'velocidad')
        self.especial = self.calcular_stats(stats,'especial')
        self.evasion = 100
        self.ataques = {}

    def agregar_ataque(self, nombre: str):
        self.ataques[nombre] = Ataque(nombre)

    def comprobar_precision(self, ataque: Ataque):
        precision = ataque.precision
        aleatorio = random.randint(1,100)
        print(f"La precisión del Ataque {ataque.nombre} es de {ataque.precision}")
        print(f"El número aleatorio es {aleatorio}")
        if aleatorio > precision:
            print(f"El número aleatorio {aleatorio} es mayor que {ataque.precision}, la precisión del Ataque {ataque.nombre}")
        else:
            print(f"la precisión del Ataque {ataque.nombre} ({ataque.precision}), es mayor que el número aleatorio {aleatorio}")
    
    def elegir_ataque(self, nombre_ataque: str):
        return self.ataques.get(nombre_ataque)

    def recibir_ataque(self, ataque: Ataque):
        daño = self.calcular_daño_total(self.comparar_tipo_atacante(ataque), self.comparar_tipo_defensor(ataque), 
        self.variacion, self.nivel, self.comparar_tipo_ataque_defensa(ataque), ataque.poder)
        self.comprobar_efecto(ataque)
        self.vida -= daño
        if self.vida < 0:
            self.vida = 0

    def comprobar_efecto(self, ataque: Ataque):
        efecto = efectos[ataque.efecto]['efecto']
        if not efecto:
            return
        # Comprobar si el atributo corresponde a uno de los posibles y es válido
        atributo = efecto[0]  # Puede ser 'ataque', 'defensa', 'velocidad', o 'especial'
        # Verificar si el atributo existe en la clase y es válido
        if hasattr(self, atributo):
            valor_atributo = getattr(self, atributo)  # Obtener el valor actual del atributo dinámicamente
            print(f"El atributo {atributo} antes de {efecto[1]} era de {valor_atributo}")
            if efecto[1] == 'bajar':
                nuevo_valor = valor_atributo - efecto[2]
                setattr(self, atributo, nuevo_valor)  # Asignar el nuevo valor al atributo
            elif efecto[1] == 'subir':
                nuevo_valor = valor_atributo + efecto[2]
                setattr(self, atributo, nuevo_valor)  # Asignar el nuevo valor al atributo
            else:
                print(f"Algo falló en la operación para {atributo}")
            # Imprimir el nuevo valor del atributo
            valor_actualizado = getattr(self, atributo)
            print(f"El atributo {atributo} después de {efecto[1]} es de {valor_actualizado}")
        else:
            print(f"El atributo {atributo} no existe en esta clase.")

    """
    Estadísticas por nivel
    Vamos a Obviar IVs, EVs y Naturaleza por el momento
    PS = 10 + (Nivel / 100 * (base_vida * 2)) + Nivel
    Resto_stats = 5 + (Nivel / 100 * (base_stat * 2))
    """
    def calcular_stats(self, stats:str, nombre_stat: str):
        if nombre_stat == 'vida':
            stat = 10 + (self.nivel / 100 * (stats[nombre_stat] * 2)) + self.nivel
        else:
            stat = 5 + (self.nivel / 100 * (stats[nombre_stat] * 2))
        stat = round(stat)
        print(f"La cantidad de {nombre_stat} de {self.nombre}, es de {stat} puntos")
        return stat

    """
    Fórmula del daño directo:
        Daño = P1 * (P2 / P3 + 2)

        P1 = 0.01 * $B * $E *V
        P2 = (0.2 * $N + 1) * $A * $P
        P3 = 25 * $D

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
        #print(f"{self.nombre} (tipo {self.tipos[0]}), realiza el ataque {ataque.nombre} que es de tipo {ataque.tipo}.")
        print(f"realiza el ataque {ataque.nombre} que es de tipo {ataque.tipo}.")
        if self.tipos[0] == ataque.tipo :
            bonificacion = 1.5
        else:
            bonificacion = 1
        return bonificacion

    # $E
    # Efectividad que podrá tener los valores 0, 0.5, 1 y 2.
    # en función de la Relación entre Tipos (Archivo Debilidades)
    def comparar_tipo_defensor(self, ataque: Ataque):
        print(f"{self.nombre} (tipo {self.tipos[0]}), recibe el ataque {ataque.nombre} que es de tipo {ataque.tipo}.")
        if ataque.tipo in debilidades[self.tipos[0]]["débil"] :
            print(f"Es muy efectivo. El daño es (x2)")
            efectividad = 2
        elif ataque.tipo in debilidades[self.tipos[0]]["resistente"] :
            print(f"No es muy efectivo. El daño es (x 0,5)")
            efectividad = 0.5
        elif ataque.tipo in debilidades[self.tipos[0]]["inmune"] :
            print(f"No afecta. El daño es 0")
            efectividad = 0
        else: 
            print(f"El daño es normal  (x1)")
            efectividad = 1
        return efectividad
    
    # $V
    # Variación que tendrá un valor entre 85 y 100 (incluidos)
    variacion = random.randint(85,100)
    print(f"El Número de Variación ha sido {variacion}.")

    # P2 (Segunda parte de la Fórmula del daño directo)
    # P2 = (0.02 * nivel + 1) * clase_Ataque * Poder_ataque
    # Será Ataque / Especial según el tipo de Ataque
    # P3 (Tercera parte de la Fórmula del daño directo)
    # P3 = 25 * tipo_Defensa
    # Será Defensa / Especial según el tipo de Ataque
    def comparar_tipo_ataque_defensa(self, ataque: Ataque):
        ataques_fisicos = ["Bicho", "Fantasma", "Lucha", "Normal", "Roca", "Tierra", "Veneno", "Volador"]
        if ataque.tipo in ataques_fisicos:
            clase_stats = "Físicas (Ataque/Defensa)"
            clase_ataque = self.ataque
            clase_defensa = self.defensa
        else:
        # ataques_especiales = ["Agua", "Dragón", "Eléctrico", "Fuego", "Hielo", "Planta", "Psíquico"]
            clase_stats = "Especiales (Especial)"
            clase_ataque = self.especial
            clase_defensa = self.especial
        print(f"Se utilizan las stats {clase_stats}, ya que {ataque.nombre} es de tipo {ataque.tipo}.")
        return clase_ataque, clase_defensa

    def calcular_daño_total (self, bonificacion, efectividad, variacion, nivel, clase_ataque_defensa, poder_ataque):
        if poder_ataque == 0:
            daño_total = 0
        else: 
            p1 = 0.01 * bonificacion * efectividad * variacion
            p1 = round(p1)
            p2 = 0.2 * (nivel + 1) * clase_ataque_defensa[0] * poder_ataque
            p2 = round(p2) 
            p3 = 25 * clase_ataque_defensa[1]
            p3 = round(p3)
            daño_total = p1 * (p2 / p3 + 2)
            daño_total = round(daño_total)
            print(f"Daño Total = {p1} * ({p2} / {p3} + 2) = {daño_total}")
        return daño_total

# Clase Combate donde se desarrolla el juego
# Se eligen los Pokemon de Jugador y Oponente y sus turnos
class Combate:
    def __init__(self, jugador: Pokemon, oponente: Pokemon) -> None:
        self.jugador = jugador
        self.oponente = oponente
        self.pulsa_para_continuar = "\nPulsa ENTER/INTRO para continuar...\n"

    def turno_atacar_oponente(self):
        ataque_oponente = random.choice(list(self.oponente.ataques.values()))
        print(f"El {self.oponente.nombre} enemigo ataca.")
        if self.oponente.comprobar_precision(ataque_oponente):
            print(f"PRUEBA")
        else:
            if 'mejora_propia' in efectos[ataque_oponente.efecto]:
                #print("EL EFECTO ES PARA EL POKEMON QUE ATACA (NO IMPLEMENTADO)")
                self.oponente.recibir_ataque(ataque_oponente)
            else:
                self.jugador.recibir_ataque(ataque_oponente)
            print(f"Te quedan {self.jugador.vida} puntos de vida.")

    def turno_atacar_jugador(self):
        print("\nAhora es tu turno para atacar. Puedes elegir entre los ataques que tienes disponibles.")
        ataques_posibles = list(self.jugador.ataques.values())
        mensaje_ataques = "Elige qué ataque quieres hacer:\n"
        # Usando enumerate para obtener tanto el índice como el nombre del ataque
        for index, ataque in enumerate(ataques_posibles):
            mensaje_ataques += f"{index+1}- {ataque.nombre}\n"
        while True:
            try:
                elegir_ataque = int(input(mensaje_ataques + "Tu opción --> "))        
                if 1 <= elegir_ataque <= len(ataques_posibles):
                    ataque_jugador = ataques_posibles[elegir_ataque - 1]
                    print(f"Tu {self.jugador.nombre} ataca.")
                    if self.jugador.comprobar_precision(ataque_jugador):
                        print(f"PRUEBA")
                    else:
                        if 'mejora_propia' in efectos[ataque_jugador.efecto]:
                            #print("EL EFECTO ES PARA EL POKEMON QUE ATACA (NO IMPLEMENTADO)")
                            self.jugador.recibir_ataque(ataque_jugador)
                        else:
                            self.oponente.recibir_ataque(ataque_jugador)
                            print(f"A {self.oponente.nombre} le quedan {self.oponente.vida} puntos de vida.")
                        break
            except ValueError:
                # Si el usuario introduce algo que no es un número válido
                print(f"¡Por favor ingresa un número válido entre 1 y {len(ataques_posibles)}")

    # Elegimos los Pokemon del Oponente y del Jugador desde la Pokedex eligiendo un número del 1 al 151
    def elegir_pokemon_oponente():
        while True:
            try:
                elegir_pokemon_oponente = int(input("Elige un pokemon para tu oponente. Del 1 al 151.\n"))
                if 1 <= elegir_pokemon_oponente <= 151:
                    try:
                        elegir_nivel_oponente = int(input("Elige un nivel para tu oponente. Del 1 al 100.\n"))
                        if 1 <= elegir_nivel_oponente <= 100:
                            nivel_oponente = elegir_nivel_oponente
                            break
                        else:
                            print("¡Número fuera de rango! Elige un número entre 1 y 100.")
                    except ValueError:
                        # Si el usuario introduce algo que no es un número
                        print("¡Por favor ingresa un número válido entre 1 y 100.")
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
        pokemon_oponente = Pokemon(poke_oponente["nombre"], poke_oponente["tipos"], poke_oponente["stats"], nivel_oponente)

        # Recorrer el array de ataques del Oponente
        for ataque_nombre in poke_oponente["ataques"]:
            ataque = ataques[ataque_nombre]
            pokemon_oponente.agregar_ataque(ataque["nombre"])
        
        return pokemon_oponente
    
    def elegir_pokemon_jugador():
        while True:
            try:
                elegir_pokemon_jugador = int(input("¡Muy bien!, ahora elige tu Pokemon. Del 1 al 151.\n"))
                if 1 <= elegir_pokemon_jugador <= 151:
                    try:
                        elegir_nivel_jugador = int(input("Elige un nivel para tu Pokemon. Del 1 al 100.\n"))
                        if 1 <= elegir_nivel_jugador <= 100:
                            nivel_jugador = elegir_nivel_jugador
                            break
                        else:
                            print("¡Número fuera de rango! Elige un número entre 1 y 100.")
                    except ValueError:
                        # Si el usuario introduce algo que no es un número
                        print("¡Por favor ingresa un número válido entre 1 y 100.")
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
        pokemon_jugador = Pokemon(poke_jugador["nombre"], poke_jugador["tipos"], poke_jugador["stats"], nivel_jugador)

        # Recorrer el array de ataques del Jugador
        for ataque_nombre in poke_jugador["ataques"]:
            ataque = ataques[ataque_nombre]
            pokemon_jugador.agregar_ataque(ataque["nombre"])
        
        return pokemon_jugador

    # Explicación del juego, componentes y dinámica
    def jugar(self):
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")
        print(f"** COMBATE POKEMON -- {self.oponente.nombre} (Nivel {self.oponente.nivel}) contra {self.jugador.nombre} (Nivel {self.jugador.nivel}) **")
        print(f"Te reto a un combate entre personajes Pokemon. Yo controlo a {self.oponente.nombre} y tú a {self.jugador.nombre}.")
        print("Combatimos mientras ambos tengamos vida.\n")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")
        input(self.pulsa_para_continuar)
        # Empezará atacando el oponente.
        while self.jugador.vida > 0 and self.oponente.vida > 0:
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")
            self.turno_atacar_oponente()
            if self.jugador.vida == 0:
                break
            input(self.pulsa_para_continuar)
            self.turno_atacar_jugador()
            if self.oponente.vida == 0:
                break
            input(self.pulsa_para_continuar)
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")
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
    CONTINUAR AQUÍ: 1:49:00 (CHARACTERS) Empezamos Character
    https://youtu.be/fo4e3njyGy0?si=7KkKwD5Nyi4xpGdq&t=5771

    DESCARGAR TILESETS
    Por ejemplo de https://eeveeexpo.com/resources/1631/

    DESCARGAR PROYECTOS DE TILED: .tmx
"""
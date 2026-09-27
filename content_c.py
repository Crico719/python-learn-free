# -*- coding: utf-8 -*-
"""Teoria + quizzes: lecciones 61-90"""

T = {}

T[61] = """## Tuplas y listas

Convertir entre **tuplas y listas**:

```python
# Lista a tupla
lista = [1, 2, 3]
tupla = tuple(lista)
print(tupla)                 # (1, 2, 3)

# Tupla a lista
tupla = (4, 5, 6)
lista = list(tupla)
print(lista)                 # [4, 5, 6]

# Desempaquetar (tuple unpacking)
a, b, c = (1, 2, 3)
print(a, b, c)               # 1 2 3

primero, *resto = (10, 20, 30, 40)
print(primero)               # 10
print(resto)                 # [20, 30, 40]
```

**Desempaquetar en bucles (muy util):**

```python
puntos = [(1, "Ana"), (2, "Luis"), (3, "Mia")]
for posicion, nombre in puntos:
    print(posicion, nombre)
```

**Por que elegir tupla:** es mas rapida y protege los datos de cambios."""

T[62] = """## Tuplas de regreso

Funciones que **devuelven tuplas**:

```python
def minimo_maximo(numeros):
    return min(numeros), max(numeros)

bajo, alto = minimo_maximo([3, 1, 4, 1, 5])
print(f"Min: {bajo}, Max: {alto}")     # Min: 1, Max: 5
```

**Varios valores a la vez:**

```python
def resumen(notas):
    return max(notas), min(notas), sum(notas) / len(notas)

alta, baja, promedio = resumen([80, 90, 70])
print(f"{alta} {baja} {promedio:.1f}")
```

**Devolver un diccionario:**

```python
def estadisticas(datos):
    return {"min": min(datos), "max": max(datos),
            "promedio": sum(datos) / len(datos)}

r = estadisticas([1, 2, 3])
print(r["max"])     # 3
```

Las tuplas son ideales para **empaquetar** varios resultados relacionados."""

T[63] = """## Creacion de diccionarios

Los **diccionarios** guardan pares **clave: valor**:

```python
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Lima"
}

print(persona["nombre"])        # Ana
persona["edad"] = 26            # modificar
persona["pais"] = "Peru"        # agregar
```

**Acceso seguro con `.get()`:**

```python
print(persona.get("email"))         # None
print(persona.get("email", "N/A"))  # N/A
persona["edad"]                     # KeyError si no existe!
```

**Metodos:**

```python
print(persona.keys())        # claves
print(persona.values())      # valores
print(persona.items())       # pares

del persona["pais"]          # eliminar clave
persona.pop("edad")          # elimina y devuelve
```

**Anidados:**

```python
inventario = {"frutas": {"manzana": 5}, "verduras": {}}
inventario["frutas"]["manzana"] += 1
```"""

T[64] = """## Uso de diccionarios

Recorrer **diccionarios**:

```python
estudiante = {"nombre": "Ana", "edad": 22, "ciudad": "Lima"}

for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")

for clave in estudiante.keys():
    print(clave)

for valor in estudiante.values():
    print(valor)

for i, (clave, valor) in enumerate(estudiante.items(), 1):
    print(f"{i}. {clave} = {valor}")
```

**Contar con diccionarios:**

```python
palabras = ["a", "b", "a", "c", "b", "a"]
conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1
print(conteo)     # {'a': 3, 'b': 2, 'c': 1}
```

**Buscar y filtrar:**

```python
notas = {"Ana": 90, "Luis": 65, "Mia": 78}
aprobados = {k: v for k, v in notas.items() if v >= 70}
print(aprobados)     # {'Ana': 90, 'Mia': 78}
```"""

T[65] = """## Tuplas, diccionarios y conjuntos 1

```python
# Tuplas para datos fijos
coordenada = (15, 25)
print(f"Latitud: {coordenada[0]}, Longitud: {coordenada[1]}")

# Diccionarios para registros
empleados = {
    "Ana": {"puesto": "Dev", "salario": 5000},
    "Luis": {"puesto": "QA", "salario": 4000}
}
print(empleados["Ana"]["puesto"])     # Dev

# Conjuntos para eliminar duplicados
notas = [90, 85, 90, 78, 85, 90]
unicas = set(notas)
print(unicas)                    # {78, 85, 90}
print(len(unicas))               # 3
```

**Los tres juntos:**

```python
def resumen_alumnos(alumnos):
    aprobados = {n for n, c in alumnos.items() if c["nota"] >= 70}
    return len(aprobados), sorted(aprobados)

alumnos = {"Ana": {"nota": 90}, "Luis": {"nota": 60}, "Mia": {"nota": 78}}
cant, lista = resumen_alumnos(alumnos)
print(f"{cant} aprobados: {lista}")
```"""

T[66] = """## Robar una carta - Parte 1

```python
import random

palos = ["Corazones", "Diamantes", "Treboles", "Picas"]
valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# Crear la baraja: tuplas (valor, palo)
baraja = [(valor, palo) for palo in palos for valor in valores]
print(f"Baraja creada: {len(baraja)} cartas")   # 52

# Barajar
random.shuffle(baraja)
print("Baraja mezclada")

# Robar una carta
carta = baraja.pop()          # quita y devuelve la ultima
print(f"Robaste: {carta[0]} de {carta[1]}")
print(f"Quedan {len(baraja)} cartas")
```

**Lo que usas:**
- `random.shuffle()` para mezclar
- `baraja.pop()` para quitar
- **Comprension de listas** con dos bucles
- **Tuplas** para guardar valor y palo juntos"""

T[67] = """## Creacion de conjuntos

Los **conjuntos (sets)** son listas sin orden ni duplicados:

```python
colores = {"rojo", "azul", "verde"}
print(len(colores))       # 3

# No hay duplicados
numeros = {1, 2, 2, 3, 3, 3}
print(numeros)            # {1, 2, 3}
print(len(numeros))       # 3
```

**Operaciones basicas:**

```python
colores.add("amarillo")       # agregar
colores.discard("azul")       # quitar si existe
print("rojo" in colores)       # True
```

**Crear desde una lista:**

```python
lista = [1, 2, 2, 3, 3, 3, 4]
unico = set(lista)
print(unico)                  # {1, 2, 3, 4}
print(list(unico))            # [1, 2, 3, 4] (orden variable)
```

**Sets vacios:** usa `set()` — nunca `{}` que es un diccionario vacio."""

T[68] = """## Uso de conjuntos

Las **operaciones de conjuntos**:

```python
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

union = a | b
interseccion = a & b
diferencia = a - b
simetrica = a ^ b

print(union)          # {1,2,3,4,5,6,7}
print(interseccion)   # {3,4,5}
print(diferencia)     # {1,2}
print(simetrica)      # {1,2,6,7}
```

**Con palabras:**

```python
matematicas = {"Ana", "Luis", "Carlos"}
arte = {"Luis", "Carlos", "Diana"}

print(matematicas & arte)      # {'Luis', 'Carlos'}
print(matematicas | arte)      # todos
print(matematicas - arte)      # solo matematicas
print(arte - matematicas)      # solo arte
```

**Comparar conjuntos:**

```python
print(a == {1, 2, 3, 4, 5})       # True
print(a.issubset({1,2,3,4,5,6}))  # True
```"""

T[69] = """## Conjuntos y listas

Convertir entre **conjuntos y listas**:

```python
lista = [1, 2, 2, 3, 3, 3, 4, 4]

# Lista a set (elimina duplicados)
unico = set(lista)
print(unico)                 # {1, 2, 3, 4}

# Set a lista
vuelta = list(unico)
vuelta.sort()
print(vuelta)                # [1, 2, 3, 4]

# Eliminar duplicados sin set
sin_repetidos = []
for numero in lista:
    if numero not in sin_repetidos:
        sin_repetidos.append(numero)
print(sin_repetidos)         # [1, 2, 3, 4]
```

**Ordenar un set:**

```python
unico = set(lista)
ordenado = sorted(unico)
print(ordenado)              # [1, 2, 3, 4]
```

**Lista a set ordenado:**

```python
frutas = ["mango", "uva", "kiwi", "uva"]
unicas = sorted(set(frutas))
print(unicas)                # ['kiwi', 'mango', 'uva']
```"""

T[70] = """## Operaciones de set

Usar **operaciones de conjuntos** para analizar datos:

```python
matematicas = {"Ana", "Luis", "Carlos", "Mia"}
arte = {"Luis", "Carlos", "Diana"}

print("En ambas:", matematicas & arte)          # {'Luis', 'Carlos'}
print("Solo matematicas:", matematicas - arte)  # {'Ana', 'Mia'}
print("Solo arte:", arte - matematicas)          # {'Diana'}
print("Al menos una:", matematicas | arte)      # los 5
print("En solo una:", matematicas ^ arte)       # {'Ana', 'Mia', 'Diana'}
```

**Comparar sets:**

```python
a = {1, 2}
b = {2, 3}

print(a == b)                 # False
print(a.issubset({1,2,3}))    # True
print(b.issuperset({2}))      # True
print(len(a & b))             # 1
```

**Ejemplo real:**

```python
compraron_a = {"Ana", "Luis", "Mia"}
comproron_b = {"Luis", "Mia", "Diana"}
ambos = compraron_a & comproron_b
print(f"Compraron ambos: {len(ambos)} clientes")
```"""

T[71] = """## Robar una carta - Parte 2

Jugar con puntos:

```python
import random

palos = ["Corazones", "Diamantes", "Treboles", "Picas"]
valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

puntos = {"A": 11, "J": 10, "Q": 10, "K": 10}
for n in range(2, 11):
    puntos[str(n)] = n

baraja = [(v, p) for p in palos for v in valores]
random.shuffle(baraja)

mano = []
total = 0
for i in range(3):
    carta = baraja.pop()
    mano.append(carta)
    valor = puntos[carta[0]]
    total += valor
    print(f"Carta {i+1}: {carta[0]} de {carta[1]} = {valor} puntos")

print(f"\\nTotal: {total} puntos")
print(f"Quedan {len(baraja)} cartas")

print("\\nTu mano:")
for valor, palo in mano:
    print(f"  {valor} de {palo}")
```

**Lo nuevo:** diccionario de puntos, `for i in range(3)`, `enumerate()`."""

T[72] = """## Modulos

Los **modulos** son archivos de Python que ya trae listos para usar:

```python
import random
print(random.randint(1, 100))
print(random.choice(["a", "b", "c"]))

import math
print(math.sqrt(16))            # 4.0
print(math.pi)                  # 3.14159...

import os
print(os.getcwd())              # carpeta actual
print(os.listdir("."))          # archivos de la carpeta

import datetime
print(datetime.date.today())
```

**Importar solo lo que necesitas (mejor):**

```python
from random import randint, choice
print(randint(1, 10))
```

**Con alias:**

```python
import datetime as dt
print(dt.date.today())
```

Standard library: `random`, `math`, `os`, `datetime`, `json`, `csv`, `re`, `sys`."""

T[73] = """## Modulos - Practica

```python
import random
import math

# Random
print(random.randint(1, 6))         # dado
print(random.uniform(0, 1))         # flotante 0-1
print(random.sample([1,2,3,4,5], 3))

# Math
print(math.sqrt(144))      # 12.0
print(math.ceil(3.2))      # 4   (redondea arriba)
print(math.floor(3.8))     # 3   (redondea abajo)
print(math.pi)

# Entrada y azar juntos
numeros = [random.randint(1, 100) for _ in range(5)]
print(numeros)
print("Mayor:", max(numeros))
print("Promedio:", round(sum(numeros)/len(numeros), 2))
```

**Importar funciones especificas:**

```python
from math import sqrt, pi, ceil
from random import randint, choice

print(sqrt(25))
print(choice(["Python", "Java", "JS"]))
```

Si olvidaste importar, da `NameError: name 'sqrt' is not defined`."""

T[74] = """## Creando tus propios modulos

**archivo `saludos.py`:**

```python
def saludar(nombre):
    return f"¡Hola, {nombre}!"

def despedir(nombre):
    return f"Adiós, {nombre}"

VERSION = "1.0"
```

**archivo `main.py`:**

```python
from saludos import saludar, despedir
import saludos

print(saludar("Ana"))
print(despedir("Luis"))
print(saludos.VERSION)
```

**Nombres alternativos:**

```python
import saludos as s
print(s.saludar("Mia"))
```

**Importar todo:**

```python
from saludos import *
print(saludar("Todos"))
```

**Buena practica:** evita `import *`, importa solo lo que usas. Los archivos deben estar en la **misma carpeta**."""

T[75] = """## Organizacion multi-archivo

```
mi_app/
    main.py          # punto de entrada
    datos.py         # datos y constantes
    funciones.py     # logica
    utiles.py        # helpers
```

**`datos.py`**
```python
VERSION = "2.0"
USUARIOS = ["Ana", "Luis", "Mia"]
```

**`utiles.py`**
```python
def es_par(n):
    return n % 2 == 0

def saludar(nombre):
    return f"Hola {nombre}"
```

**`funciones.py`**
```python
from utiles import es_par
from datos import USUARIOS

def mostrar_aprobados():
    return [u for u in USUARIOS if len(u) % 2 == 0]
```

**`main.py`**
```python
from datos import VERSION
from utiles import saludar
from funciones import mostrar_aprobados

print("App version", VERSION)
print(saludar("Ana"))
print(mostrar_aprobados())
```

Ejecutas **solo** `main.py`. Los demas se importan."""

T[76] = """## Entendiendo los paquetes

```
mi_paquete/
    __init__.py       # hace que sea un paquete
    utiles.py
    calculos.py
```

**`__init__.py`** convierte la carpeta en un paquete importable. Puede estar vacio:

```python
# mi_paquete/__init__.py
__version__ = "1.0"
```

**Importar el paquete completo:**

```python
import mi_paquete
print(mi_paquete.__version__)

import mi_paquete.utiles
print(mi_paquete.utiles.es_par(4))
```

**Importar desde el `__init__`:**

```python
# mi_paquete/__init__.py
from .utiles import es_par, saludar
from .calculos import area_rectangulo
```

**Uso:**

```python
from mi_paquete import es_par, area_rectangulo
print(es_par(4))                     # True
print(area_rectangulo(3, 5))         # 15
```

El punto en `from .utiles` significa "desde **este** paquete"."""

T[77] = """## Modulos de Python - Practica

```python
import os
import sys
import math
import random
import datetime

print("Version Python:", sys.version.split()[0])
print("Carpeta actual:", os.getcwd())
print("Archivos:", len(os.listdir(".")))
print("Ejecutable:", os.path.basename(sys.executable))

print("Raiz de 144:", math.sqrt(144))
print("PI:", round(math.pi, 4))
print("Aleatorio:", random.randint(1, 100))

hoy = datetime.date.today()
print("Hoy es:", hoy)
print("Formato:", hoy.strftime("%d/%m/%Y"))
print("Hace 7 dias:", hoy - datetime.timedelta(days=7))
```

**Modulos clave para tu dia a dia:** `os`, `sys`, `math`, `random`, `datetime`, `json`, `re`, `collections`."""

T[78] = """## Instalacion de paquetes de terceros

Con `pip`:

```powershell
pip install requests          # instalar un paquete
pip install requests pandas numpy   # varios
pip list                      # ver lo instalado
pip upgrade requests          # actualizar
pip uninstall requests        # desinstalar
```

**Usar un paquete instalado:**

```python
import requests

respuesta = requests.get("https://api.github.com/repos/python/cpython")
datos = respuesta.json()
print(datos["name"], datos["stargazers_count"])
```

**Paquetes utiles:**

| Paquete | Para que sirve |
|---------|----------------|
| `requests` | llamar APIs |
| `matplotlib` | graficos |
| `pandas` | analisis de datos |
| `numpy` | calculo numerico |
| `flask` | crear web apps |

**Entorno virtual (recomendado):**

```powershell
python -m venv mi_entorno
mi_entorno\\Scripts\\activate
pip install requests
```"""

T[79] = """## Gestion de versiones de paquetes

```python
import requests
print(requests.__version__)         # 2.31.0

import sys
print(sys.version)
print(sys.version_info)            # (3, 12, 1, ...)
```

**Ver requisitos de un proyecto:**

```powershell
pip freeze > requirements.txt      # guarda todo instalado
pip install -r requirements.txt    # reinstala desde el archivo
```

**Instalar version especifica:**

```powershell
pip install requests==2.28.0
pip install requests>=2.25,<3.0
```

**Buena practica: siempre un `requirements.txt`:**

```
requests==2.31.0
flask==3.0.0
```

**Comprobar conflictos:**

```powershell
pip check
pip show requests
```"""

T[80] = """## Dependencias de Python - Practica

**`requirements.txt`**
```
requests==2.31.0
```

**Uso en el codigo:**

```python
import requests

API = "https://api.github.com"
usuario = "python"

r = requests.get(f"{API}/users/{usuario}")
datos = r.json()

print(datos["name"])
print(datos["public_repos"], "repos publicos")
```

**Verificar la respuesta:**

```python
if r.status_code == 200:
    print("Todo bien")
else:
    print("Error", r.status_code)
```

**Con parameters (query):**

```python
r = requests.get(f"{API}/search/repositories",
                 params={"q": "python tutorial", "sort": "stars"})
print(r.json()["total_count"], "resultados")
```

**Regla de oro:** si tu proyecto usa paquetes, incluye `requirements.txt`."""

T[81] = """## Calculadora de danos - Parte 1

```python
import random

def calcular_dano(ataque, defensa, critico=False):
    base = ataque - defensa
    if base < 0:
        base = 0
    variacion = random.randint(-3, 3)
    dano = base + variacion
    if critico:
        dano = int(dano * 1.5)
    return max(0, dano)

# Simular combate
jugador = {"nombre": "Heroe", "ataque": 25, "defensa": 10, "vida": 100}
enemigo = {"nombre": "Goblin", "ataque": 18, "defensa": 8, "vida": 60}

ronda = 1
while enemigo["vida"] > 0 and jugador["vida"] > 0:
    critico = random.random() < 0.25
    dano = calcular_dano(jugador["ataque"], enemigo["defensa"], critico)
    enemigo["vida"] -= dano
    print(f"Ronda {ronda}: {jugador['nombre']} hace {dano} de dano")
    ronda += 1

if enemigo["vida"] <= 0:
    print(f"¡Victoria! {enemigo['nombre']} fue derrotado")
else:
    print("Derrota...")
```

**Lo nuevo:** `random.random()` para probabilidad, diccionarios para personajes, `while` con dos condiciones."""

T[82] = """## Errores y excepciones

Manejar **errores** con `try / except`:

```python
try:
    numero = int(input("Numero: "))
    print(f"Es numero: {numero}")
except ValueError:
    print("Eso no es un numero valido")
```

**Varias excepciones:**

```python
try:
    resultado = 10 / int(input("Divisor: "))
    print(resultado)
except ValueError:
    print("Entrada no valida")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
```

**`try / except / else / finally`:**

```python
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
else:
    print("Leido con exito")
finally:
    print("Siempre se ejecuta esto")
```

**Capturar el error (`as`):**

```python
try:
    int("abc")
except ValueError as error:
    print(f"Ocurrio este error: {error}")
```

**Nunca escribas `except:` a secas** — captura errores de verdad."""

T[83] = """## Levantando excepciones

**Levantar excepciones** propias con `raise`:

```python
def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

try:
    print(dividir(10, 2))      # 5.0
    print(dividir(10, 0))      # lanza el error
except ValueError as error:
    print(f"Error: {error}")
```

**Crear tus propias excepciones:**

```python
class EdadInvalidaError(Exception):
    pass

def registrar(edad):
    if edad < 0:
        raise EdadInvalidaError(f"La edad no puede ser {edad}")
    return f"Registrado: {edad} anos"
```

**Jerarquia de excepciones comunes:**

| Excepcion | Cuando ocurre |
|-----------|---------------|
| `ValueError` | valor con tipo correcto pero contenido malo |
| `TypeError` | tipo de dato incorrecto |
| `IndexError` | indice fuera de rango |
| `KeyError` | clave no existe en un dict |
| `ZeroDivisionError` | division entre cero |
| `FileNotFoundError` | archivo no existe |

`raise` **detiene** la funcion inmediatamente."""

T[84] = """## Errores y excepciones - Practica

```python
def calculadora(a, b, operacion):
    try:
        a = float(a)
        b = float(b)

        if operacion == "sumar":
            return a + b
        elif operacion == "restar":
            return a - b
        elif operacion == "dividir":
            if b == 0:
                raise ZeroDivisionError("division entre cero")
            return a / b
        else:
            raise ValueError(f"Operacion desconocida: {operacion}")

    except ZeroDivisionError as e:
        return f"Error: {e}"
    except ValueError as e:
        return f"Error de valor: {e}"
    except TypeError:
        return "Error de tipo"

print(calculadora("10", "5", "sumar"))      # 15.0
print(calculadora("10", "0", "dividir"))    # Error: division entre cero
print(calculadora("abc", "5", "sumar"))     # Error de valor
```

**Punto clave:** `raise` dentro del `try` lo atrapa su propio `except`."""

T[85] = """## Manejo de multiples tipos de excepcion

```python
def procesar_archivo(nombre):
    try:
        with open(nombre, "r") as archivo:
            contenido = archivo.read()
            numero = int(contenido.strip())
            return numero * 2
    except FileNotFoundError:
        print("Error: el archivo no existe")
    except PermissionError:
        print("Error: sin permisos")
    except ValueError:
        print("Error: el contenido no es un numero")
    except IsADirectoryError:
        print("Error: eso es una carpeta")
    except Exception as error:
        print(f"Error inesperado: {error}")
    finally:
        print("Operacion finalizada")
    return None
```

**`finally` siempre se ejecuta**, haya error o no.

**`else` solo si no hubo error:**

```python
try:
    n = int(input("Numero: "))
except ValueError:
    print("No es un numero")
else:
    print(f"Numero valido: {n * 2}")
```

**Varias excepciones en un `except`:**

```python
except (ValueError, TypeError):
    print("Entrada invalida")
```"""

T[86] = """## Trabajando con mensajes de excepcion

```python
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, retiro):
        self.saldo = saldo
        self.retiro = retiro
        super().__init__(
            f"Saldo insuficiente: tienes {saldo} pero pides {retiro}"
        )

class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

    def retirar(self, monto):
        if monto > self.saldo:
            raise SaldoInsuficienteError(self.saldo, monto)
        self.saldo -= monto
        return f"Retiro OK. Nuevo saldo: {self.saldo}"

cuenta = Cuenta(100)
try:
    print(cuenta.retirar(50))
    print(cuenta.retirar(80))     # error
except SaldoInsuficienteError as e:
    print(e)
    print(f"Faltan: {e.retiro - e.saldo}")
```

**Mensajes utiles:**

```python
raise ValueError(f"Edad invalida: {edad}. Debe estar entre 0 y 150")
```

Un buen mensaje **dice que paso y como arreglarlo**."""

T[87] = """## Manejo de excepciones - Practica

```python
def leer_notas(archivo):
    try:
        with open(archivo, "r") as f:
            notas = [float(linea.strip()) for linea in f if linea.strip()]
        return notas
    except FileNotFoundError:
        print(f"No se encontro {archivo}")
    except ValueError:
        print("El archivo tiene valores no numericos")
    except PermissionError:
        print("No tienes permiso para leer")
    finally:
        print("Fin de la lectura")
    return []

def calcular_promedio(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

notas = leer_notas("notas.txt")
print(f"Promedio: {calcular_promedio(notas):.2f}")
```

**Combinando todo:** comprehension con `try` dentro, `finally` para limpieza, funciones que manejan sus propios errores."""

T[88] = """## Mejores practicas en manejo de errores

```python
# 1. Captura excepciones ESPECIFICAS, nunca genericas
try:
    ...
except FileNotFoundError:      # BIEN
    ...
except:                       # MAL - oculta bugs reales
    ...

# 2. Usa Exception como ultimo recurso
except Exception as e:
    logger.error(f"Inesperado: {e}")

# 3. No captures lo que puedes evitar
n = int("abc")     # MAL, esto falla y lo sabes
try:
    n = int(texto) # BIEN, el texto viene del usuario
except ValueError:
    pass

# 4. finally para limpiar
try:
    archivo = open("datos.txt")
    datos = archivo.read()
except IOError as e:
    print("Error de E/S:", e)
finally:
    archivo.close()      # SIEMPRE se cierra

# 5. "raise ... from" para encadenar
def procesar():
    try:
        return int("abc")
    except ValueError as e:
        raise ValueError("Formato de numero invalido") from e

# 6. with para recursos
with open("datos.txt") as f:   # cierra solo
    contenido = f.read()
```

**Regla de oro:** `try` lo mas pequeño posible, alrededor solo de lo que puede fallar."""

T[89] = """## Excepciones - Practica

```python
class ProductoNoEncontradoError(Exception):
    pass

class Inventario:
    def __init__(self, productos):
        self.productos = productos

    def buscar(self, nombre):
        if nombre not in self.productos:
            raise ProductoNoEncontradoError(f"No existe: {nombre}")
        return self.productos[nombre]

    def descontar(self, nombre, cantidad):
        stock = self.buscar(nombre)        # puede lanzar error
        if cantidad > stock:
            raise ValueError(
                f"Stock insuficiente de {nombre}: "
                f"hay {stock}, pides {cantidad}"
            )
        self.productos[nombre] = stock - cantidad
        return f"Nuevo stock de {nombre}: {stock - cantidad}"

try:
    inv = Inventario({"pan": 10, "leche": 3})
    print(inv.descontar("pan", 4))
    print(inv.descontar("queso", 1))       # ProductoNoEncontradoError
    print(inv.descontar("leche", 10))      # Stock insuficiente
except ProductoNoEncontradoError as e:
    print(f"No encontrado: {e}")
except ValueError as e:
    print(f"Problema de stock: {e}")
```

**Cadena:** una funcion llama a otra, y los errores se propagan hacia arriba."""

T[90] = """## Validador de lecturas de sensores - Parte 1

```python
import random

class LecturaInvalidaError(Exception):
    pass

LIMITE_MIN = 0
LIMITE_MAX = 40

def leer_sensor():
    valor = random.uniform(-10, 50)
    if valor < LIMITE_MIN or valor > LIMITE_MAX:
        raise LecturaInvalidaError(
            f"Lectura fuera de rango: {valor:.1f} "
            f"(permitido {LIMITE_MIN}-{LIMITE_MAX})"
        )
    return valor

def leer_muestras(cantidad):
    lecturas = []
    errores = 0

    for i in range(cantidad):
        try:
            valor = leer_sensor()
            lecturas.append(valor)
            print(f"  [{i+1:2}] OK: {valor:.2f}")
        except LecturaInvalidaError as error:
            errores += 1
            print(f"  [{i+1:2}] ERROR: {error}")

    return lecturas, errores

print("=== VALIDANDO SENSORES ===")
lecturas, errores = leer_muestras(10)

print(f"\\nValidas: {len(lecturas)}/10")
if lecturas:
    print(f"Promedio: {sum(lecturas)/len(lecturas):.2f}")
    print(f"Min: {min(lecturas):.2f}, Max: {max(lecturas):.2f}")
```

**Lo nuevo:** clase de excepcion propia, constantes, validacion, acumulacion de errores sin que el programa se caiga."""

Q = {}

Q[61] = [
 ("Como conviertes una lista a tupla?", ["tuple(lista)", "list(tupla)", "(lista)"], 0),
 ("Que hace *resto?", ["Captura el resto", "Multiplica", "Nada"], 0),
 ("Como desempaquetas en un for?", ["for a, b in pares:", "for par in pares:", "for a in pares:"], 0),
 ("Que ventaja tiene la tupla?", ["Inmutable y rapida", "Mas metodos", "Ninguna"], 0),
 ("Que devuelve list(tupla)?", ["Una lista", "Una tupla", "Nada"], 0),
]

Q[62] = [
 ("Que hace return?", ["Devuelve y sale", "Imprime", "Repite"], 0),
 ("Como desempaquetas varios valores?", ["a, b = f()", "a = f()", "[a,b] = f()"], 0),
 ("Que ventaja tiene devolver tupla?", ["Varios valores en una", "Mas rapido", "Ninguna"], 0),
 ("Que hace sorted()?", ["Ordena sin modificar", "Ordena in-place", "Invierte"], 0),
 ("Cual es la diferencia con sort()?", ["sort no crea nueva", "Iguales", "sort crea nueva"], 0),
]

Q[63] = [
 ("Como se define un set?", ["{}", "[]", "()"], 0),
 ("Que hace .add()?", ["Agrega", "Quita", "Ordena"], 0),
 ("Que hace | entre sets?", ["Union", "Interseccion", "Diferencia"], 0),
 ("Que hace & entre sets?", ["Interseccion", "Union", "Diferencia"], 0),
 ("Como quitas duplicados?", ["set(lista)", "dict()", "unique()"], 0),
]

Q[64] = [
 ("Como recorres un set?", ["for x in set", "for i, x in set", "while"], 0),
 ("Que operacion es la union?", ["|", "&", "-"], 0),
 ("Cual es la interseccion?", ["&", "|", "-"], 0),
 ("Como quitas duplicados de una lista?", ["set(lista)", "dict()", "unique()"], 0),
 ("Como conviertes set a lista?", ["list(set)", "set(list)", "tuple(set)"], 0),
]

Q[65] = [
 ("Que es un conjunto?", ["Elementos unicos sin orden", "Lista ordenada", "Diccionario"], 0),
 ("Como accedes a un diccionario anidado?", ["d['a']['b']", "d.a.b", "d[0][1]"], 0),
 ("Como creas un set con comprehension?", ["{n for n in lista if ...}", "set(list)", "[set()]"], 0),
 ("Que hace len(set(lista))?", ["Cuantos unicos hay", "Total de elementos", "Nada"], 0),
 ("Que es mas eficiente para contar unicos?", ["set()", "sorted()", "list()"], 0),
]

Q[66] = [
 ("Cuantas cartas tiene una baraja?", ["52", "48", "13"], 0),
 ("Que hace random.shuffle()?", ["Mezcla la lista", "Elige una", "Crea una"], 0),
 ("Que hace pop() en una lista?", ["Quita y devuelve el ultimo", "Solo quita", "Agrega"], 0),
 ("Como se crea la baraja?", ["Comprension de listas con dos bucles", "Dos listas", "random"], 0),
 ("Que tipo de dato guarda cada carta?", ["Tupla", "Lista", "Diccionario"], 0),
]

Q[67] = [
 ("Que tiene un set que no tiene una lista?", ["No admite duplicados", "Es mas rapido", "Es ordenada"], 0),
 ("Como creas un set vacio?", ["set()", "{}", "()"], 0),
 ("Que hace .discard(x)?", ["Quita si existe", "Lanza error si no", "Agrega"], 0),
 ("Que hace `in` con sets?", ["True si existe", "Agrega", "Nada"], 0),
 ("Que valor tiene {1,1,2}?", ["{1,2}", "{1,1,2}", "Error"], 0),
]

Q[68] = [
 ("Que operacion da elementos en ambos?", ["a & b", "a | b", "a - b"], 0),
 ("Que operacion da elementos en solo uno?", ["a ^ b", "a & b", "a | b"], 0),
 ("Como comparas si un set es subconjunto?", ["issubset()", "==", "in"], 0),
 ("Que hace a.issuperset(b)?", ["a contiene a b", "a es subconjunto", "Nada"], 0),
 ("Que imprime len(a & b)?", ["Cuantos coinciden", "Total", "Nada"], 0),
]

Q[69] = [
 ("Como eliminas duplicados de una lista?", ["set(lista)", "del", "pop()"], 0),
 ("Como ordenas un set?", ["sorted()", "sort()", "order()"], 0),
 ("Que hace list(set(...))?", ["Convierte a lista", "Elimina", "Ordena"], 0),
 ("Como eliminas duplicados sin set?", ["if x not in lista", "if x in lista", "count()"], 0),
 ("Que hace sorted(set(frutas))?", ["Unicas y ordenadas", "Con duplicados", "Sin ordenar"], 0),
]

Q[70] = [
 ("Que significa A - B?", ["Solo los de A", "Solo los de B", "Todos"], 0),
 ("Que significa A ^ B?", ["En solo uno", "En ambos", "Todos"], 0),
 ("Como sabes cuantos hay en comun?", ["len(a & b)", "len(a | b)", "len(a)"], 0),
 ("Que devuelve issubset()?", ["True o False", "Una lista", "Nada"], 0),
 ("Que aplicacion tiene esto?", ["Clientes que compraron dos productos", "Ordenar", "Contar"], 0),
]

Q[71] = [
 ("Que hace puntos[carta[0]]?", ["Busca el valor de la carta", "Agrega", "Nada"], 0),
 ("Como barajas la baraja?", ["random.shuffle()", "random.choice()", "sort()"], 0),
 ("Que hace pop() aqui?", ["Roba una carta", "Agrega", "Nada"], 0),
 ("Que imprime el total?", ["Suma de los puntos", "Numero de cartas", "Nada"], 0),
 ("Que son los puntos?", ["Un diccionario", "Una lista", "Un set"], 0),
]

Q[72] = [
 ("Que hace import random?", ["Carga el modulo random", "Genera numeros", "Nada"], 0),
 ("Como usas solo una funcion?", ["from math import sqrt", "import math.sqrt", "use sqrt"], 0),
 ("Que modulo da la carpeta actual?", ["os", "sys", "math"], 0),
 ("Que modulo da la version de Python?", ["sys", "os", "platform"], 0),
 ("Que hace math.ceil(3.2)?", ["4", "3", "3.2"], 0),
]

Q[73] = [
 ("Que hace math.floor(3.8)?", ["3", "4", "3.8"], 0),
 ("Que hace random.randint(1, 6)?", ["Numero del 1 al 6", "Decimal", "Lista"], 0),
 ("Que hace random.uniform(0,1)?", ["Decimal entre 0 y 1", "Entero", "Nada"], 0),
 ("Que error da si no importas?", ["NameError", "TypeError", "ValueError"], 0),
 ("Que hace random.sample(lista, 3)?", ["3 elementos al azar", "Los 3 primeros", "Nada"], 0),
]

Q[74] = [
 ("Que palabra define un modulo propio?", ["def", "class", "module"], 0),
 ("Como se importa una funcion propia?", ["from saludos import saludar", "import saludar()", "use saludos"], 0),
 ("Donde debe estar el archivo?", ["En la misma carpeta", "En site-packages", "En /"], 0),
 ("Que se recomienda evitar?", ["import *", "import os", "from x import y"], 0),
 ("Que es una constante en un modulo?", ["Una variable en mayusculas", "Una funcion", "Una clase"], 0),
]

Q[75] = [
 ("Cual es el punto de entrada?", ["main.py", "datos.py", "utiles.py"], 0),
 ("Que archivo tiene los datos?", ["datos.py", "main.py", "utiles.py"], 0),
 ("Que hace un import entre archivos?", ["Carga el modulo\", \"Nada", "Ejecuta el archivo"], 0),
 ("Que archivo ejecutas?", ["Solo main.py", "Todos", "Ninguno"], 0),
 ("Cual es la ventaja de dividir?", ["Codigo mas organizado", "Mas rapido", "Menos memoria"], 0),
]

Q[76] = [
 ("Que archivo hace que una carpeta sea paquete?", ["__init__.py", "main.py", "setup.py"], 0),
 ("Que significa el punto en from .utiles?", ["Desde este paquete", "Carpeta actual", "Nada"], 0),
 ("Como se importa un paquete completo?", ["import mi_paquete", "from mi_paquete", "use mi_paquete"], 0),
 ("Que puede contener __init__.py?", ["Codigo que se ejecuta al importar", "Solo comentarios", "Nada"], 0),
 ("Que es un paquete?", ["Carpeta con modulos", "Un archivo", "Una funcion"], 0),
]

Q[77] = [
 ("Que modulo da la version de Python?", ["sys.version", "os.version", "platform.version"], 0),
 ("Que modulo lista archivos?", ["os.listdir()", "sys.listdir()", "math.listdir()"], 0),
 ("Que modulo da la fecha de hoy?", ["datetime", "time", "os"], 0),
 ("Que hace timedelta(days=7)?", ["Resta 7 dias", "Suma 7 dias", "Nada"], 0),
 ("Como se formatea una fecha?", ["strftime()", "format()", "date()"], 0),
]

Q[78] = [
 ("Que comando instala un paquete?", ["pip install", "pip get", "python install"], 0),
 ("Que paquete sirve para llamar APIs?", ["requests", "math", "random"], 0),
 ("Que sirve para crear graficos?", ["matplotlib", "requests", "flask"], 0),
 ("Que es un entorno virtual?", ["python -m venv", "pip venv", "venv install"], 0),
 ("Que comando lo activa en Windows?", ["mi_entorno\\Scripts\\activate", "source activate", "pip activate"], 0),
]

Q[79] = [
 ("Que comando guarda los requisitos?", ["pip freeze > requirements.txt", "pip save", "pip list > req.txt"], 0),
 ("Como instalas desde requirements.txt?", ["pip install -r requirements.txt", "pip load", "pip read"], 0),
 ("Como ves la version de un paquete?", ["requests.__version__", "requests.version()", "get_version()"], 0),
 ("Como instalas una version exacta?", ["pip install x==1.0", "pip install x=1.0", "pip install x 1.0"], 0),
 ("Que hace pip check?", ["Verifica conflictos", "Instala", "Borra"], 0),
]

Q[80] = [
 ("Que codigo da el cuerpo de una respuesta JSON?", ["r.json()", "r.text()", "r.data()"], 0),
 ("Como se envia un query param?", ["params={...}", "query={...}", "data={...}"], 0),
 ("Que codigo verifica el exito?", ["r.status_code == 200", "r.ok()", "r == 200"], 0),
 ("Que archivo debe tener un proyecto?", ["requirements.txt", "config.txt", "deps.txt"], 0),
 ("Que hace pip freeze?", ["Lista todo instalado", "Instala", "Borra"], 0),
]

Q[81] = [
 ("Que hace random.random()?", ["Decimal entre 0 y 1", "Entero", "Lista"], 0),
 ("Como se calcula el dano?", ["ataque - defensa", "ataque + defensa", "ataque * defensa"], 0),
 ("Que hace max(0, dano)?", ["Evita dano negativo", "Suma", "Nada"], 0),
 ("Que porcentaje es 0.25?", ["25%", "2.5%", "0.25%"], 0),
 ("Que condicion termina el combate?", ["vida > 0 de ambos", "ronda == 3", "Nada"], 0),
]

Q[82] = [
 ("Que hace try?", ["Intenta ejecutar el bloque", "Repite", "Valida"], 0),
 ("Que hace except?", ["Captura el error", "Lanza el error", "Ignora"], 0),
 ("Que hace finally?", ["Siempre se ejecuta", "Solo si hay error", "Nunca"], 0),
 ("Que hace else en try?", ["Se ejecuta si no hay error", "Se ejecuta siempre", "Nunca"], 0),
 ("Por que no usar except: a secas?", ["Oculta bugs", "Es mas rapido", "No funciona"], 0),
]

Q[83] = [
 ("Que palabra levanta una excepcion?", ["raise", "throw", "error"], 0),
 ("Como se crea una excepcion propia?", ["class X(Exception)", "def X()", "X = Exception"], 0),
 ("Que hace raise dentro de una funcion?", ["Sale de la funcion", "Continua", "Repite"], 0),
 ("Que error da dividir entre cero?", ["ZeroDivisionError", "ValueError", "TypeError"], 0),
 ("Que error da convertir 'hola' a int?", ["ValueError", "TypeError", "NameError"], 0),
]

Q[84] = [
 ("Que hace raise dentro de try?", ["Lo atrapa su propio except", "Se ignora", "Repite"], 0),
 ("Que hace float('abc')?", ["ValueError", "TypeError", "Nada"], 0),
 ("Cuales except son obligatorios?", ["Ninguno", "try", "return"], 0),
 ("Como se llama el bloque que puede fallar?", ["try", "except", "else"], 0),
 ("Que imprime calculadora('10','0','dividir')?", ["Error: division entre cero", "0", "infinito"], 0),
]

Q[85] = [
 ("Que hace finally?", ["Siempre se ejecuta", "Solo sin error", "Nunca"], 0),
 ("Cual es el error de un archivo inexistente?", ["FileNotFoundError", "ValueError", "TypeError"], 0),
 ("Como capturas varios errores?", ["except (A, B):", "except A and B:", "except A, B"], 0),
 ("Que hace else en un try?", ["Se ejecuta si no hubo error", "Siempre", "Nunca"], 0),
 ("Que hace Exception como ultimo recurso?", ["Captura lo no previsto", "Nada", "Repite"], 0),
]

Q[86] = [
 ("Que hace super().__init__()?", ["Inicializa la clase padre", "Nada", "Repite"], 0),
 ("Que guarda self.saldo?", ["El saldo de la instancia", "Nada", "La clase"], 0),
 ("Que es un buen mensaje de error?", ["Dice que paso y como arreglarlo", "Solo el error", "Vacio"], 0),
 ("Como se accede a e.retiro?", ["Atributo de la excepcion", "Variable global", "Nada"], 0),
 ("Que clase base usan las excepciones?", ["Exception", "Object", "Error"], 0),
]

Q[87] = [
 ("Que hace el bloque else del try?", ["Se ejecuta si no hubo error", "Siempre", "Nunca"], 0),
 ("Que metodo abre un archivo?", ["open()", "file()", "read()"], 0),
 ("Que se necesita para leer lineas?", ["with open()", "try/except", "for"], 0),
 ("Que hace if linea.strip() en la comprehension?", ["Ignora lineas vacias", "Borra", "Nada"], 0),
 ("Que hace finally en la lectura?", ["Siempre imprime fin", "Solo errores", "Nada"], 0),
]

Q[88] = [
 ("Que se debe evitar?", ["except: sin tipo", "try/except", "finally"], 0),
 ("Que se usa para limpiar recursos?", ["finally o with", "else", "return"], 0),
 ("Cual es la regla de oro?", ["try lo mas pequeño posible", "try en todo el codigo", "Sin try"], 0),
 ("Que hace raise ... from e?", ["Encadena el error original", "Nada", "Repite"], 0),
 ("Que se recomienda para archivos?", ["with open()", "open() sin cerrar", "try/except"], 0),
]

Q[89] = [
 ("Que hace return dentro de un metodo?", ["Sale del metodo", "Repite", "Nada"], 0),
 ("Cual es el orden de los except?", ["Mas especificos primero", "Aleatorio", "El ultimo primero"], 0),
 ("Que hace una clase vacia con pass?", ["Es un marcador", "No hace nada", "Error"], 0),
 ("Que se propaga hacia arriba?", ["Las excepciones", "Las variables", "Los prints"], 0),
 ("Que ventaja tiene usar clases?", ["Codigo organizado", "Menos rapido", "Nada"], 0),
]

Q[90] = [
 ("Que hace raise dentro de leer_sensor()?", ["Salta al except", "Imprime", "Repite"], 0),
 ("Que es LIMITE_MAX?", ["Una constante", "Una funcion", "Un parametro"], 0),
 ("Que hace finally en este proyecto?", ["Nada, es buen ejemplo", "Imprime resumen", "Borra"], 0),
 ("Que hace if lecturas: al final?", ["Evita error si esta vacia", "Nada", "Imprime"], 0),
 ("Que hace :.1f en el mensaje?", ["1 decimal", "1 entero", "Nada"], 0),
]

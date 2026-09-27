# -*- coding: utf-8 -*-
"""Teoria + quizzes: lecciones 31-60"""

T = {}

T[31] = """## Piedra, papel o tijera - Parte 2

Al mejor de tres rondas:

```python
import random

opciones = ["piedra", "papel", "tijera"]
victorias = 0
derrotas = 0

for ronda in range(1, 4):        # 3 rondas
    pc = random.choice(opciones)
    jugador = input(f"Ronda {ronda} - piedra/papel/tijera: ").lower()

    if jugador == pc:
        print("Empate!\\n")
    elif (jugador == "piedra" and pc == "tijera") or \\
         (jugador == "papel" and pc == "piedra") or \\
         (jugador == "tijera" and pc == "papel"):
        victorias += 1
        print("Ganaste la ronda!\\n")
    else:
        derrotas += 1
        print("Perdiste la ronda!\\n")

print(f"RESULTADO: {victorias} victorias, {derrotas} derrotas")
if victorias > derrotas:
    print("¡Ganaste el juego!")
elif victorias < derrotas:
    print("Perdiste el juego")
else:
    print("Empate")
```

**Lo nuevo:** contador de victorias/derrotas y `print` con salto de linea."""

T[32] = """## Agrupacion de datos en listas

Las **listas** agrupan varios valores en una sola variable:

```python
frutas = ["manzana", "banana", "cereza"]
numeros = [10, 20, 30]
mixto = ["Ana", 25, True, 3.14]     # puede mezclar tipos

print(frutas[0])     # manzana   (empieza en 0)
print(frutas[-1])    # cereza    (-1 es el ultimo)
print(frutas[1:3])   # ['banana', 'cereza']  (rebanada)
```

**El indice 0 es el primero:**

```python
lista = ["a", "b", "c"]
#  indices: 0   1   2
```

**Agregar y consultar:**

```python
frutas.append("uva")           # agrega al final
frutas.insert(0, "mango")      # agrega al inicio
print(len(frutas))             # cuantas hay
print("banana" in frutas)       # True o False
```

Las listas son **mutables**: se pueden cambiar despues de crearlas."""

T[33] = """## Cambio de datos en listas

Para **cambiar** datos se asigna al indice:

```python
frutas = ["manzana", "banana", "cereza"]

frutas[0] = "durazno"
print(frutas)     # ['durazno', 'banana', 'cereza']
```

**Rebanada (slicing):**

```python
numeros = [0, 1, 2, 3, 4, 5]

print(numeros[1:4])    # [1, 2, 3]     del 1 al 3
print(numeros[:3])     # [0, 1, 2]     desde el inicio
print(numeros[3:])     # [3, 4, 5]     hasta el final
print(numeros[::2])    # [0, 2, 4]     de 2 en 2
```

**Ojo:** `numeros[1:4]` incluye el indice 1 pero **no** el 4. El final es exclusivo.

**Error clasico:** `numeros[10] = 5` da `IndexError` si la lista es corta."""

T[34] = """## Actualizacion de listas

Metodos para **agregar y quitar**:

```python
frutas = ["manzana", "banana"]

frutas.append("cereza")          # ['manzana', 'banana', 'cereza']
frutas.insert(1, "mango")        # ['manzana', 'mango', 'banana', 'cereza']
frutas.remove("banana")          # ['manzana', 'mango', 'cereza']
fruta = frutas.pop()             # quita y devuelve el ultimo
fruta = frutas.pop(0)            # quita el primero

del frutas[1]                    # elimina por indice
frutas.clear()                   # vacia la lista
```

| Metodo | Que hace |
|--------|----------|
| `append(x)` | agrega al final |
| `insert(i, x)` | agrega en posicion i |
| `remove(x)` | borra el primer x |
| `pop()` | quita y devuelve el ultimo |
| `pop(i)` | quita y devuelve el i |
| `clear()` | vacia todo |

**Seguridad:** `remove` y `pop` dan error si el elemento no existe."""

T[35] = """## Organizacion de datos 1

**Ordenar** datos en listas:

```python
numeros = [42, 7, 19, 3, 88, 25]

numeros.sort()             # [3, 7, 19, 25, 42, 88]
numeros.sort(reverse=True) # descendente
numeros.reverse()          # invierte el orden
copia = numeros.copy()     # copia independiente
```

**Ordenar sin modificar el original:**

```python
numeros = [42, 7, 19]
ordenado = sorted(numeros)      # devuelve nueva lista
print(numeros)                  # [42, 7, 19]  intacto
print(ordenado)                 # [7, 19, 42]
```

**Ordenar por clave en diccionarios:**

```python
notas = {"Ana": 90, "Luis": 65, "Mia": 78}
ranking = sorted(notas.items(), key=lambda x: x[1], reverse=True)
```

**Tambien:** `max()`, `min()`, `sum()`, `len()` funcionan con listas de numeros."""

T[36] = """## Looping sobre listas

Recorrer listas con `for`:

```python
numeros = [10, 20, 30, 40, 50]

for n in numeros:
    print(n)

# Transformar la misma lista
for i in range(len(numeros)):
    numeros[i] = numeros[i] * 2

# Acumular
total = 0
for n in numeros:
    total += n
print("Suma:", total)

# Con indice
for indice, valor in enumerate(numeros):
    print(indice, valor)

# Sobre strings
for letra in "Python":
    print(letra)
```

**Comprension de listas (forma compacta):**

```python
dobles = [n * 2 for n in numeros]
```

Mismo resultado que el `for`, pero en **una sola linea**."""

T[37] = """## Decidir con listas

El operador `in` comprueba si un valor esta en la lista:

```python
frutas = ["manzana", "banana", "cereza"]

print("banana" in frutas)      # True
print("durazno" in frutas)     # False
print("man" in frutas)         # False (busca el texto completo)
```

**Con condiciones:**

```python
buscar = input("Que fruta buscas: ").lower()

if buscar in frutas:
    indice = frutas.index(buscar)
    print(f"Encontrada en la posicion {indice}")
else:
    print("No la tenemos")

if buscar not in frutas:
    print("Podriamos pedirla")
```

**Funciona con cadenas, diccionarios, tuplas y rangos:**

```python
print(3 in [1, 2, 3])            # True
print("a" in "palabra")           # True
print("llave" in {"llave": 1})    # True (revisa las claves)
print(5 in range(1, 10))         # True
```"""

T[38] = """## Organizacion de datos 2

Combinacion de operaciones:

```python
numeros = [42, 7, 19, 3, 88, 25, 3, 7]

# Eliminar duplicados
unicos = list(set(numeros))
unicos.sort()
print(unicos)              # [3, 7, 19, 25, 42, 88]

# Contar duplicados
from collections import Counter
veces = Counter(numeros)
print(veces.most_common(2))    # [(7, 2), (3, 2)]
```

**Ordenar cadenas:**

```python
nombres = ["Zoe", "ana", "Luis"]
print(sorted(nombres))                    # mayusculas primero
print(sorted(nombres, key=str.lower))     # ['ana', 'Luis', 'Zoe']
```

**Invertir y ordenar:**

```python
palabras = ["python", "es", "genial"]
palabras.reverse()
print(palabras)                  # ['genial', 'es', 'python']
```"""

T[39] = """## Lista de tareas - Parte 1

```python
tareas = []

while True:
    tarea = input("Nueva tarea (o 'salir'): ").lower()

    if tarea == "salir":
        break              # termina el bucle

    if tarea not in tareas:
        tareas.append(tarea)
        print("Agregada:", tarea)
    else:
        print("Esa tarea ya existe")

print(f"\\nTareas pendientes: {len(tareas)}")
for i, tarea in enumerate(tareas, 1):
    print(f"  {i}. {tarea}")
```

**Lo que aprendiste:**
- Crear una lista vacia: `tareas = []`
- `append()` para agregar
- `in` para evitar duplicados
- `break` para salir del `while`
- `enumerate(lista, 1)` para numerar desde 1

Este patron (`while True` + `input` + `break`) es la base de todo menu."""

T[40] = """## Encontrando datos extremos

Valores **extremos** y resumenes:

```python
notas = [45, 78, 92, 60, 88, 55, 73]

print(max(notas))              # 92
print(min(notas))              # 45
print(sum(notas))              # 491
print(len(notas))              # 7
print(sum(notas) / len(notas)) # 70.14...  (promedio)
```

**Redondear el promedio:**

```python
promedio = sum(notas) / len(notas)
print(round(promedio, 2))      # 70.14
print(f"{promedio:.1f}")        # 70.1
```

**Los extremos por indice:**

```python
mayor = notas.index(max(notas))
print(f"La mejor nota es {max(notas)} (posicion {mayor})")
```

**Top 3:**

```python
top3 = sorted(notas, reverse=True)[:3]
print("Top 3:", top3)          # [92, 88, 78]
```"""

T[41] = """## Ordenacion de datos

```python
nombres = ["Carlos", "Ana", "Luis", "Maria"]

nombres.sort()
print(nombres)                    # ['Ana', 'Carlos', 'Luis', 'Maria']

nombres.sort(reverse=True)
print(nombres)                    # descendente
```

**Por longitud:**

```python
nombres.sort(key=len)
print(nombres)                    # ['Ana', 'Luis', 'Carlos', 'Maria']
```

**Diccionarios por valor:**

```python
notas = {"Ana": 90, "Luis": 65, "Mia": 78}

ranking = sorted(notas.items(), key=lambda par: par[1], reverse=True)
for nombre, nota in ranking:
    print(f"{nombre}: {nota}")

for nombre in sorted(notas.keys()):
    print(nombre)
```

**`lambda`** es una funcion anonima de una linea: `lambda par: par[1]` significa "toma `par` y devuelve `par[1]`"."""

T[42] = """## Usando listas 1

Analisis completo de una lista:

```python
compras = ["leche", "pan", "leche", "huevos", "queso", "leche"]

print(len(compras))                      # 6 en total
print(compras.count("leche"))            # 3 veces aparece
print("leche" in compras)                # True
print(list(set(compras)))                # sin duplicados
print(len(set(compras)))                 # 3 unicos
```

**Contar cada elemento:**

```python
from collections import Counter
conteo = Counter(compras)
for producto, cantidad in conteo.items():
    print(f"{producto}: {cantidad}")

print(conteo.most_common(2))     # [('leche', 3), ('pan', 1)]
```

**Lista de la compra — validar:**

```python
print("Falta comprar:", [p for p in set(compras)
                         if conteo[p] == 1])
```"""

T[43] = """## Listas de incorporacion

Agregar elementos de una lista a otra:

```python
a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)             # [1, 2, 3, 4, 5, 6]
a += b                  # lo mismo
a = a + [7, 8]          # con el operador +
```

**Diferencia clave:**

```python
x = [1, 2]
x.append([3, 4])        # [1, 2, [3, 4]]  <- anidada (error comun)
x.extend([3, 4])        # [1, 2, 3, 4]    <- correcta
```

**Insertar en el medio:**

```python
a.insert(2, "nuevo")    # inserta en la posicion 2
```

**Unir varias listas:**

```python
compras1 = ["pan", "leche"]
compras2 = ["queso"]
todas = compras1 + compras2     # crea una nueva
```

**Trucazo con comprehension:**

```python
a, b = [1, 2, 3], [4, 5, 6]
combinada = [x + y for x, y in zip(a, b)]
print(combinada)      # [5, 7, 9]
```"""

T[44] = """## Conteo de elementos

Contar elementos de varios formas:

```python
colores = ["rojo", "azul", "rojo", "verde", "rojo", "azul"]

# Metodo count()
print(colores.count("rojo"))     # 3
print(colores.count("azul"))     # 2

# Con bucle y diccionario
conteo = {}
for color in colores:
    conteo[color] = conteo.get(color, 0) + 1
print(conteo)     # {'rojo': 3, 'azul': 2, 'verde': 1}

# Con Counter (lo mas rapido)
from collections import Counter
print(Counter(colores))

# Contar algo que no existe
print(colores.count("morado"))   # 0
```

**Contar letras de una palabra:**

```python
palabra = "banana"
for letra in set(palabra):
    print(letra, palabra.count(letra))
# a 3, n 2, b 1
```

**Conprehension:**

```python
for color in set(colores):
    print(color, colores.count(color))
```"""

T[45] = """## Uso de listas 2

Filtrar y transformar con **comprensiones de listas**:

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar
pares = [n for n in numeros if n % 2 == 0]
print(pares)                     # [2, 4, 6, 8, 10]

mayores = [n for n in numeros if n > 5]
print(mayores)                   # [6, 7, 8, 9, 10]

# Transformar
dobles = [n * 2 for n in numeros]
print(dobles)                    # [2, 4, 6, ..., 20]

# Filtrar y transformar
dobles_pares = [n * 2 for n in numeros if n % 2 == 0]
print(dobles_pares)              # [4, 8, 12, 16, 20]

# Con cadenas
palabras = ["sol", "luna", "estrella", "planeta"]
largas = [p for p in palabras if len(p) > 5]
print(largas)                    # ['estrella', 'planeta']
```

**Equivalente con for (mas verboso):**

```python
dobles = []
for n in numeros:
    if n % 2 == 0:
        dobles.append(n * 2)
```

La comprehension hace lo mismo en **una linea**."""

T[46] = """## Lista de tareas - Parte 2

Menu completo:

```python
tareas = []

def mostrar():
    if not tareas:
        print("No hay tareas pendientes")
        return
    for i, tarea in enumerate(tareas, 1):
        print(f"  {i}. {tarea}")

while True:
    print("\\n--- MENU ---")
    print("1. Agregar tarea")
    print("2. Completar tarea")
    print("3. Eliminar tarea")
    print("4. Ver tareas")
    print("5. Salir")

    opcion = input("Elige: ")

    if opcion == "1":
        tarea = input("Nueva tarea: ")
        if tarea:
            tareas.append(tarea)
            print("Agregada")

    elif opcion == "2":
        mostrar()
        pos = int(input("Numero a completar: ")) - 1
        if 0 <= pos < len(tareas):
            tareas[pos] = "[x] " + tareas[pos]
            print("Completada")

    elif opcion == "3":
        pos = int(input("Numero a eliminar: ")) - 1
        if 0 <= pos < len(tareas):
            tareas.pop(pos)
            print("Eliminada")

    elif opcion == "4":
        mostrar()

    elif opcion == "5":
        print("Adiós!")
        break

    else:
        print("Opción no válida")
```

**Lo nuevo:** `def mostrar()` (funcion), menu con `elif`, validacion `0 <= pos < len(lista)`."""

T[47] = """## Reutilizando codigo con funciones

Las **funciones** empaquetan codigo reutilizable:

```python
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

saludar("Ana")      # ¡Hola, Ana!
saludar("Luis")     # ¡Hola, Luis!
```

**Con `return` para devolver un valor:**

```python
def sumar(a, b):
    resultado = a + b
    return resultado

total = sumar(5, 3)
print(total)         # 8
```

**Anatomia:**

```python
def nombre(parametro):    # definicion
    cuerpo                # indentado
    return valor          # opcional
```

**Sin `return` la funcion devuelve `None`:**

```python
def saludar(nombre):
    print("Hola", nombre)     # imprime, no devuelve

x = saludar("Ana")
print(x)      # None
```

**Regla clave:** `def` crea la funcion, la llamada usa parentesis `()`."""

T[48] = """## Creacion de parametros

Los **parametros** son los valores que recibe una funcion:

```python
def saludar(nombre, edad):
    print(f"{nombre} tiene {edad} anos")

saludar("Ana", 25)
```

**Parametro por defecto:**

```python
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

saludar("Ana")              # Hola, Ana!
saludar("Luis", "Buenas")   # Buenas, Luis!
```

**Parametros con nombre (keywords):**

```python
def saludar(nombre, edad):
    print(f"{nombre} - {edad}")

saludar(edad=25, nombre="Ana")   # el orden da igual
```

**Cantidad variable de argumentos:**

```python
def sumar(*numeros):
    return sum(numeros)

print(sumar(1, 2, 3, 4))     # 10
```

**Devolver varios valores:**

```python
def dividir(a, b):
    return a // b, a % b

cociente, resto = dividir(17, 5)
print(cociente, resto)     # 3 2
```"""

T[49] = """## Valores de retorno

Los **valores de retorno** con `return`:

```python
def calcular(notas):
    mayor = max(notas)
    menor = min(notas)
    promedio = sum(notas) / len(notas)
    return mayor, menor, promedio

notas = [80, 90, 70, 85]
alta, baja, prom = calcular(notas)
print(f"Max: {alta}, Min: {baja}, Promedio: {prom:.1f}")
```

**`return` termina la funcion:**

```python
def validar(edad):
    if edad < 0:
        return "Edad invalida"     # sale aqui
    if edad >= 18:
        return "Mayor"
    return "Menor"                 # si no hubo return antes
```

**Return vs Print:**
- `print()` **muestra** en pantalla, no guarda nada
- `return` **guarda** el valor para usarlo despues

**Return vacio = None:**

```python
def nada():
    return       # igual que return None
print(nada())    # None
```"""

T[50] = """## Uso de multiples parametros

Funciones con **varios parametros**:

```python
def crear_usuario(nombre, edad, ciudad="Desconocida", activo=True):
    estado = "activo" if activo else "inactivo"
    return f"{nombre} ({edad}, {ciudad}) - {estado}"

print(crear_usuario("Ana", 25))
print(crear_usuario("Luis", 30, "Lima"))
print(crear_usuario("Mia", 22, activo=False))
```

**`*args` y `**kwargs`:**

```python
def sumar(*args):
    return sum(args)

def perfil(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

sumar(1, 2, 3)                  # 6
perfil(nombre="Ana", edad=25)   # nombre: Ana, edad: 25
```

**Buena practica:** muchos parametros → pasar un diccionario:

```python
def procesar(usuario):
    print(usuario["nombre"])

procesar({"nombre": "Ana", "edad": 25})
```"""

T[51] = """## Comprension de las funciones

El **alcance (scope)** de una variable:

```python
x = 10              # variable global

def mostrar():
    x = 5           # variable LOCAL (dentro de la funcion)
    print("Dentro:", x)    # 5

mostrar()
print("Fuera:", x)         # 10  (la global no cambio)
```

**Reglas:**
- Las variables creadas **dentro** de una funcion son **locales**
- Para leer una global dentro de una funcion no necesitas nada especial
- Para **modificar** una global necesitas `global`

```python
contador = 0

def incrementar():
    global contador      # usamos la global
    contador += 1

incrementar()
incrementar()
print(contador)     # 2
```

**Buena practica:** evita `global`, pasa y devuelve valores:

```python
def incrementar(n):
    return n + 1

contador = 0
contador = incrementar(contador)     # mucho mas claro
```"""

T[52] = """## Funciones 1 - Practica

```python
# 1. Es un palindromo?
def es_palindromo(palabra):
    limpio = palabra.lower().replace(" ", "")
    return limpio == limpio[::-1]

print(es_palindromo("Anita lava la tina"))   # True
print(es_palindromo("hola"))                 # False

# 2. Fahrenheit a Celsius
def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9

print(fahrenheit_a_celsius(100))   # 37.77...

# 3. Contar vocales
def contar_vocales(texto):
    resultado = 0
    for letra in texto.lower():
        if letra in "aeiou":
            resultado += 1
    return resultado

# 4. Factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)     # recursividad
```

**Conceptos:** `s[::-1]` invierte, `return` devuelve, `in` busca, hay recursividad."""

T[53] = """## Sistema de pedidos de alimentos - Parte 1

```python
menu = {
    "pizza": 10.50,
    "pasta": 8.75,
    "ensalada": 6.00
}

print("=== MENU ===")
for plato, precio in menu.items():
    print(f"{plato:12} ${precio:.2f}")

pedido = input("Que quieres pedir? ").lower()

if pedido in menu:
    cantidad = int(input("Cuantos? "))
    total = menu[pedido] * cantidad
    print(f"Total: ${total:.2f}")
else:
    print("No tenemos ese plato")
    print("Opciones:", ", ".join(menu.keys()))
```

**Lo que usas:**
- **Diccionario** plato → precio
- `.items()` para recorrer clave y valor
- `in` para validar
- `f"{precio:.2f}"` para formato con 2 decimales
- `", ".join()` para unir claves"""

T[54] = """## Funciones y alcance de variables

```python
def obtener_datos(nombre, edad, ciudad="Lima"):
    # estas son variables LOCALES, solo existen aqui
    completo = f"{nombre}, {edad} años, {ciudad}"
    return completo

info = obtener_datos("Ana", 25)
print(info)
```

**Listas mutadas dentro de funciones (OJO):**

```python
def agregar(mi_lista):
    mi_lista.append("nuevo")     # modifica la original

datos = ["a"]
agregar(datos)
print(datos)        # ['a', 'nuevo']  <- si se modifico!
```

**Para evitarlo, devuelve una copia:**

```python
def agregar_seguro(mi_lista):
    return mi_lista + ["nuevo"]

datos = ["a"]
resultado = agregar_seguro(datos)
print(datos)        # ['a']  intacta
```

Esta es una de las trampas mas comunes de Python."""

T[55] = """## Decidir con funciones

Funciones que **deciden** con `return`:

```python
def nivel(edad):
    if edad < 0:
        return "Edad invalida"
    elif edad >= 18:
        return "Mayor de edad"
    elif edad >= 13:
        return "Adolescente"
    else:
        return "Nino"

edad = int(input("Edad: "))
print(nivel(edad))
```

**Validar y devolver (patron comun):**

```python
def dividir(a, b):
    if b == 0:
        return None           # no se puede dividir
    return a / b

resultado = dividir(10, 2)
if resultado is None:
    print("Error: division entre cero")
else:
    print(resultado)
```

**Importante:** el `return` dentro de un `if` **sale** de la funcion inmediatamente."""

T[56] = """## Funciones con listas

```python
def duplicar(lista):
    return [n * 2 for n in lista]

def agregar(lista, nuevo):
    return lista + [nuevo]

def eliminar(lista, valor):
    return [x for x in lista if x != valor]

print(duplicar([1, 2, 3]))          # [2, 4, 6]
print(agregar([1, 2], 3))           # [1, 2, 3]
print(eliminar([1, 2, 2, 3], 2))    # [1, 3]
```

**Devolver siempre una lista nueva es la practica segura.**

**Con comprehensions dentro de la funcion:**

```python
def solo_pares(lista):
    return [n for n in lista if n % 2 == 0]

def cuadrados(lista):
    return [n ** 2 for n in lista]

print(solo_pares([1, 2, 3, 4]))     # [2, 4]
print(cuadrados([1, 2, 3]))         # [1, 4, 9]
```

Este patron es **super usado** en el trabajo real con Python."""

T[57] = """## Funciones con bucles

```python
def contar_hasta(n):
    for i in range(1, n + 1):
        print(i)

def sumar_hasta(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

def buscar(lista, objetivo):
    for indice, valor in enumerate(lista):
        if valor == objetivo:
            return indice     # sale al encontrarlo
    return -1                 # no lo encontro

contar_hasta(5)
print(sumar_hasta(10))          # 55
print(buscar([4, 8, 15], 15))   # 2
```

**Un `return` dentro del bucle es una forma elegante de `break`:**

```python
def validar_lista(lista):
    for n in lista:
        if n < 0:
            return False       # sale si encuentra negativo
    return True                # si llego aqui, todo esta bien
```"""

T[58] = """## Funciones 2 - Practica

```python
# 1. Factorial con recursion
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# 2. Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 3. Es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 4. Fusionar dos listas ordenadas
def fusionar(a, b):
    return sorted(a + b)

# 5. Contar palabras
def palabras(texto):
    return len(texto.split())

print(factorial(5))              # 120
print(fibonacci(10))             # 55
print(es_primo(17))              # True
print(fusionar([1,3,5], [2,4]))  # [1,2,3,4,5]
print(palabras("hola mundo python"))  # 3
```

**Conceptos:** recursion, `range`, `%`, `sorted`, `split()`."""

T[59] = """## Sistema de pedidos - Parte 2

Multiples cocinas con diccionarios anidados:

```python
cocinas = {
    "italiana": {"pizza": 10.50, "pasta": 8.75},
    "mexicana": {"taco": 5.00, "burrito": 7.50},
    "japonesa": {"sushi": 12.00, "ramen": 10.50}
}

for cocina, platos in cocinas.items():
    print(f"\\n{cocina.upper()}")
    for plato, precio in platos.items():
        print(f"   {plato:12} ${precio:.2f}")

pedido = []
while True:
    opcion = input("Pedir plato (o 'salir'): ").lower()
    if opcion == "salir":
        break
    for cocina, platos in cocinas.items():
        if opcion in platos:
            cantidad = int(input(f"Cuantos {opcion}? "))
            pedido.append((opcion, cantidad, platos[opcion] * cantidad))
            break
    else:
        print("No encontrado")

total = sum(p[2] for p in pedido)
print(f"\\nTotal: ${total:.2f}")
```

**Lo nuevo:** diccionarios anidados, `for...else`, tuplas, `sum()` con generador."""

T[60] = """## Creacion de tuplas

Las **tuplas** son como listas pero **inmutables** (no se pueden cambiar):

```python
coordenadas = (10, 20)
print(coordenadas[0])        # 10
print(coordenadas[-1])       # 20

# No se puede modificar:
coordenadas[0] = 99          # TypeError
```

**Crear tuplas:** con parentesis o sin ellos (comas):

```python
a = (1, 2, 3)
b = 1, 2, 3                 # igual
c = ("singleton",)          # con coma para 1 solo elemento
```

**Metodos (solo lectura):**

```python
t = (3, 1, 4, 1, 5)
print(t.count(1))       # 2
print(t.index(4))       # 2
print(max(t), min(t))   # 5 1
print(len(t))           # 5
```

**Para que sirve:** cuando los datos no deben cambiar, como coordenadas, fechas o claves de diccionario."""

Q = {}

Q[31] = [
 ("Como juegas al mejor de tres?", ["for i in range(3)", "while True", "input x3"], 0),
 ("Que variable cuenta victorias?", ["victorias", "win", "puntos"], 0),
 ("Que imprime f'\\n'?", ["Salto de linea", "La letra n", "nada"], 0),
 ("Que hace la barra \\ al final de linea?", ["Continua la linea", "Comenta", "Nada"], 0),
 ("Que imprime al final si victorias == derrotas?", ["Ganaste", "Perdiste", "Empate"], 2),
]

Q[32] = [
 ("Como se crea una lista?", ["[]", "{}", "()"], 0),
 ("Que indice tiene el primer elemento?", ["0", "1", "-1"], 0),
 ("Que hace [-1]?", ["El ultimo", "Error", "El primero"], 0),
 ("Que hace append()?", ["Agrega al final", "Quita", "Ordena"], 0),
 ("Que hace `in` con listas?", ["Comprueba pertenencia", "Agrega", "Nada"], 0),
]

Q[33] = [
 ("Como cambias un elemento?", ["lista[0] = x", "lista.add(x)", "lista[0].add(x)"], 0),
 ("Que hace lista[1:4]?", ["Indices 1,2,3", "Indices 1,2,3,4", "Indices 0,1,2"], 0),
 ("El final del slice es inclusivo?", ["Si", "No", "Depende"], 1),
 ("Que hace lista[::2]?", ["De 2 en 2", "Los ultimos 2", "Nada"], 0),
 ("Que error da indice fuera de rango?", ["IndexError", "ValueError", "KeyError"], 0),
]

Q[34] = [
 ("Que hace append(x)?", ["Agrega al final", "Quita", "Ordena"], 0),
 ("Que hace pop()?", ["Quita y devuelve el ultimo", "Solo quita", "Agrega"], 0),
 ("Que hace remove(x)?", ["Quita la primera coincidencia", "Quita el ultimo", "Nada"], 0),
 ("Que hace clear()?", ["Vacia la lista", "Ordena", "Agrega"], 0),
 ("Que hace insert(i, x)?", ["Inserta en posicion i", "Agrega al final", "Quita"], 0),
]

Q[35] = [
 ("Que hace sort()?", ["Ordena la lista en sitio", "Devuelve nueva lista", "Invierte"], 0),
 ("Como ordenas sin modificar el original?", ["sorted()", "sort()", "reverse()"], 0),
 ("Que hace sorted(reverse=True)?", ["Descendente", "Ascendente", "Error"], 0),
 ("Como ordenas un dict por valor?", ["key=lambda x: x[1]", "key=len", "sort()"], 0),
 ("Que hace copy()?", ["Copia la lista", "Borra", "Ordena"], 0),
]

Q[36] = [
 ("Que hace enumerate()?", ["Indice y valor", "Cuenta", "Enumera"], 0),
 ("Que hace range(len(lista))?", ["Indices validos", "Valores", "Nada"], 0),
 ("Que es una list comprehension?", ["Crear listas en una linea", "Un bucle", "Una funcion"], 0),
 ("Como recorres un string con for?", ["for letra in texto", "for i in range()", "while"], 0),
 ("Que hace [n*2 for n in lista]?", ["Duplica cada elemento", "Suma 2", "Nada"], 0),
]

Q[37] = [
 ("Que hace `in`?", ["Comprueba si esta", "Agrega", "Quita"], 0),
 ("Como buscas el indice?", [".index()", ".find()", ".get()"], 0),
 ("Que significa `not in`?", ["Que NO esta", "Que no existe el metodo", "Nada"], 0),
 ("`in` con diccionarios revisa...", ["Las claves", "Los valores", "No funciona"], 0),
 ("Que da 5 in range(1,10)?", ["True", "False", "Error"], 0),
]

Q[38] = [
 ("Como eliminas duplicados?", ["set()", "del", "pop()"], 0),
 ("Como ordenas un set?", ["sorted()", "sort()", "order()"], 0),
 ("Que hace Counter?", ["Cuenta frecuencias", "Ordena", "Suma"], 0),
 ("Como ordenas ignorando mayusculas?", ["key=str.lower", "key=str", "key=len"], 0),
 ("Que hace most_common(2)?", ["Los 2 mas comunes", "Los 2 primeros", "Nada"], 0),
]

Q[39] = [
 ("Como creas lista vacia?", ["tareas = []", "tareas = {}", "tareas = ()"], 0),
 ("Como evitas duplicados?", ["if tarea not in tareas", "if tarea in tareas", "count()"], 0),
 ("Como sales del while?", ["break", "stop", "exit"], 0),
 ("Que hace enumerate(l, 1)?", ["Numera desde 1", "Empieza en 0", "Cuenta"], 0),
 ("Que patron base es este?", ["while True + input + break", "for + if", "def + return"], 0),
]

Q[40] = [
 ("Que funcion da el maximo?", ["max()", "top()", "big()"], 0),
 ("Como calculas promedio?", ["sum/len", "avg()", "mean/total"], 0),
 ("Que hace round(x, 2)?", ["2 decimales", "Redondea a 2", "Nada"], 0),
 ("Que hace f'{x:.1f}'?", ["1 decimal", "Redondea a 1", "Nada"], 0),
 ("Como sacas el top 3?", ["sorted(reverse=True)[:3]", "top(3)", "max x3"], 0),
]

Q[41] = [
 ("Como ordenas por longitud?", ["key=len", "key=size", "key=count"], 0),
 ("Que hace reverse=True?", ["Descendente", "Invierte", "Nada"], 0),
 ("Como ordenas un dict por nota?", ["key=lambda p: p[1]", "key=notas", "sort()"], 0),
 ("Que es lambda?", ["Funcion anonima de una linea", "Un bucle", "Una clase"], 0),
 ("Que metodo ordena sin crear nueva lista?", ["sort()", "sorted()", "order()"], 0),
]

Q[42] = [
 ("Como cuentas elementos?", ["len()", "count()", "size()"], 0),
 ("Como cuentas uno especifico?", [".count(x)", ".index(x)", ".find(x)"], 0),
 ("Como sabes cuantos son unicos?", ["len(set())", "len(unique)", "set(len)"], 0),
 ("Que hace most_common()?", ["Los mas frecuentes", "Los primeros", "Nada"], 0),
 ("Como recorres contando con dict?", [".get(x, 0) + 1", "count[x]", "sum[x]"], 0),
]

Q[43] = [
 ("Que hace extend()?", ["Agrega los de otra lista", "Agrega anidada", "Quita"], 0),
 ("Cual es la diferencia clave de append()?", ["append anida, extend no", "Iguales", "append quita"], 0),
 ("Como unes dos listas?", ["lista1 + lista2", "lista1.join()", "merge(lista1)"], 0),
 ("Que hace insert(2, x)?", ["Inserta en posicion 2", "Agrega al final", "Quita"], 0),
 ("Que hace zip()?", ["Empareja elemento a elemento", "Comprime", "Divide"], 0),
]

Q[44] = [
 ("Como cuentas con dict?", ["conteo[x] = conteo.get(x,0)+1", "count[x]", "sum[x]"], 0),
 ("Que hace Counter?", ["Cuenta frecuencias", "Ordena", "Suma"], 0),
 ("Como recorres sin repetir?", ["set()", "range()", "list()"], 0),
 ("Que devuelve count() si no existe?", ["0", "-1", "None"], 0),
 ("Como cuentas letras de una palabra?", ["palabra.count(letra)", "len(letra)", "str.count()"], 0),
]

Q[45] = [
 ("Que es una list comprehension?", ["Crear listas en una linea", "Un bucle", "Una clase"], 0),
 ("Como filtras en una comprehension?", ["if dentro de [n for n in ...]", "filter()", "where"], 0),
 ("Que hace [n*2 for n in lista]?", ["Transforma", "Filtra", "Ordena"], 0),
 ("Que hace [p for p in palabras if len(p) > 5]?", ["Filtra las largas", "Transforma", "Ordena"], 0),
 ("Cual es mas eficiente?", ["Comprehension", "Bucle largo", "Igual"], 0),
]

Q[46] = [
 ("Como defines una funcion?", ["def mostrar():", "func mostrar()", "function mostrar()"], 0),
 ("Como validas un indice de lista?", ["0 <= pos < len(lista)", "pos > 0", "pos < lista"], 0),
 ("Que hace pop(pos)?", ["Quita y devuelve en pos", "Solo quita", "Agrega"], 0),
 ("Como sales del menu?", ["break", "stop", "exit"], 0),
 ("Como marcas una tarea completada?", ["Prefijo [x]", "Borrarla", "Moverla"], 0),
]

Q[47] = [
 ("Que palabra define una funcion?", ["def", "function", "fun"], 0),
 ("Que hace return?", ["Devuelve un valor", "Imprime", "Nada"], 0),
 ("Que pasa sin return?", ["Devuelve None", "Devuelve 0", "Falta"], 0),
 ("Como llamas una funcion?", ["nombre()", "nombre", "call nombre"], 0),
 ("Cual es la diferencia clave?", ["print muestra, return guarda", "Iguales", "return imprime"], 0),
]

Q[48] = [
 ("Que es un parametro?", ["Valor que recibe la funcion", "Valor que devuelve", "Un bucle"], 0),
 ("Como se define un parametro por defecto?", ["def f(x=5):", "def f(5):", "def f(x:5)"], 0),
 ("Que son los argumentos con nombre?", ["Llamar con x=5", "Parametros", "Variables"], 0),
 ("Que hace *args?", ["Argumentos variables", "Multiplica", "Puntero"], 0),
 ("Como devuelves dos valores?", ["return a, b", "return [a, b]", "return a + b"], 0),
]

Q[49] = [
 ("Que hace return?", ["Termina y devuelve", "Solo imprime", "Repite"], 0),
 ("Como desempaquetas dos valores?", ["a, b = f()", "a = f()", "[a,b] = f()"], 0),
 ("Que pasa si solo hay return en una rama?", ["Sale ahi", "Sigue", "Error"], 0),
 ("Cual es la diferencia con print?", ["return guarda, print muestra", "Iguales", "print devuelve"], 0),
 ("Que devuelve return sin valor?", ["None", "0", "Vacio"], 0),
]

Q[50] = [
 ("Que hace **kwargs?", ["Argumentos con nombre", "Multiplica", "Potencia"], 0),
 ("Cuando conviene un diccionario?", ["Muchos parametros", "Un parametro", "Nunca"], 0),
 ("Como haces un valor condicional en f-string?", ["f\"{x if cond else y}\"", "f\"{x?y}\"", "f\"{x or y}\""], 0),
 ("Que es f-string anidada?", ["f dentro de f", "Un string de f", "Nada"], 0),
 ("Cual es el orden de precedencia?", ["or, and, not", "not, and, or", "and, or, not"], 1),
]

Q[51] = [
 ("Cual es el scope de una variable dentro de una funcion?", ["Local", "Global", "Ninguno"], 0),
 ("Que hace global?", ["Usa la variable global", "Crea una nueva", "Nada"], 0),
 ("Que se imprime arriba?", ["La global intacta", "La local", "Error"], 0),
 ("Por que no usar global?", ["Es mala practica", "No funciona", "Es lento"], 0),
 ("Como lo evitas?", ["Devolver valores", "Usar global", "print"], 0),
]

Q[52] = [
 ("Como inviertes un string?", ["s[::-1]", "reverse(s)", "s.rev()"], 0),
 ("Como comparas ignorando espacios?", ["s.replace(' ','')", "s.strip()", "s.join()"], 0),
 ("Que hace round(x, 2)?", ["2 decimales", "Redondea a 2", "Nada"], 0),
 ("Como limpias una cadena para comparar?", ["strip y lower", "upper", "split"], 0),
 ("Cual es la forma compacta de return?", ["return a + b", "print(a+b)", "a += b"], 0),
]

Q[53] = [
 ("Como se define un diccionario?", ["{}", "[]", "()"], 0),
 ("Como recorres clave y valor?", [".items()", ".keys()", ".values()"], 0),
 ("Como accedes de forma segura?", [".get()", "[key]", ".find()"], 0),
 ("Como formateas un precio?", ["f'{p:.2f}'", "f'{p:2}'", "str(p)"], 0),
 ("Que hace round(3.14159, 2)?", ["3.14", "3.1", "3"], 0),
]

Q[54] = [
 ("Cual es el error comun con globales?", ["Asumir que existe fuera", "Usarla mal", "Nada"], 0),
 ("Que hace `global`?", ["Accede a la global", "Crea global", "Nada"], 0),
 ("Que pasa si una funcion muta una lista?", ["Se modifica la original", "Nada", "Error"], 0),
 ("Como lo evitas?", ["Devolver copia", "Modificar directo", "global"], 0),
 ("Que pueden hacer las funciones anidadas?", ["Acceden a la externa", "No pueden", "Dan error"], 0),
]

Q[55] = [
 ("Que peligro tienen las listas mutables?", ["Se modifican fuera", "Dan error", "Nada"], 0),
 ("Como lo evitas?", ["Devolver copia", "Modificar directo", "global"], 0),
 ("Que hace return dentro de un if?", ["Sale de la funcion", "Repite el if", "Nada"], 0),
 ("Como evitas el error de los 8 espacios?", ["Usar 4 espacios", "Usar tabs", "Cualesquiera"], 0),
 ("Que es una funcion anidada?", ["def dentro de def", "if dentro de for", "class dentro de def"], 0),
]

Q[56] = [
 ("Como recorres una lista en una funcion?", ["for item in lista", "while", "if"], 0),
 ("Que hace return en una funcion?", ["Devuelve el resultado", "Imprime", "Nada"], 0),
 ("Como acumulas en un bucle?", ["resultado += x", "resultado = x", "sum += x"], 0),
 ("Que hace `in` en un for?", ["Recorre la lista", "Agrega", "Elimina"], 0),
 ("Cual es el parametro mas comun?", ["lista", "nombre", "edad"], 0),
]

Q[57] = [
 ("Que hace return dentro de un bucle?", ["Sale y devuelve", "Repite", "Nada"], 0),
 ("Que devuelve buscar() si no encuentra?", ["-1", "0", "None"], 1),
 ("Como se acumula un total?", ["total += n", "total = n", "sum = n"], 0),
 ("Que tipo de bucle usarias para recorrer?", ["for", "while", "if"], 0),
 ("Que hace enumerate() en una funcion?", ["Da indice y valor", "Cuenta", "Enumera"], 0),
]

Q[58] = [
 ("Que es recursion?", ["Una funcion que se llama a si misma", "Un bucle", "Una clase"], 0),
 ("Que es un numero primo?", ["Solo divisible entre 1 y si mismo", "Par", "Mayor que 10"], 0),
 ("Como sabes si n es primo?", ["Revisar divisores hasta sqrt(n)", "n % 2", "n > 10"], 0),
 ("Que hace split()?", ["Divide un string en lista", "Junta", "Quita"], 0),
 ("Que hace sorted()?", ["Ordena sin modificar", "Ordena en sitio", "Invierte"], 0),
]

Q[59] = [
 ("Que es un diccionario anidado?", ["Dict dentro de dict", "Lista dentro de dict", "Tupla"], 0),
 ("Que hace for...else?", ["Else si no hubo break", "Siempre", "Nunca"], 0),
 ("Como sumas los totales?", ["sum(p[2] for p in pedido)", "sum(pedido)", "total = 0"], 0),
 ("Como recorres 两 niveles?", ["for anidado", "while", "if"], 0),
 ("Que hace f'{precio:.2f}'?", ["2 decimales", "Precio", "Nada"], 0),
]

Q[60] = [
 ("Que es una tupla?", ["Secuencia inmutable", "Lista mutable", "Diccionario"], 0),
 ("Que error da cambiar una tupla?", ["TypeError", "ValueError", "IndexError"], 0),
 ("Como se crea una tupla de 1 elemento?", ["('x',)", "('x')", "[x]"], 0),
 ("Que hace .index() en tupla?", ["Posicion del elemento", "El elemento", "Nada"], 0),
 ("Que indice es -1?", ["El ultimo", "El primero", "Error"], 0),
]

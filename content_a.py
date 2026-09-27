# -*- coding: utf-8 -*-
"""Teoria + quizzes: lecciones 1-30"""

T = {}

T[1] = """## Variables

Las **variables** son cajas con nombre donde guardas informacion para usarla despues.

En Python creas una variable con el signo `=`:

```python
nombre = "Ana"
edad = 25
altura = 1.70
activo = True
```

Python detecta solo el tipo de dato, no necesitas declararlo.

**Reglas para nombres:**
- Solo letras, numeros y `_`
- No pueden empezar con numero
- No pueden ser palabras reservadas (`if`, `while`, `for`)
- Python distingue mayusculas: `edad` != `Edad`

```python
mi_edad = 25      # correcto
2edad = 25         # MAL
```

**Tipos basicos:** `int` (entero), `float` (decimal), `str` (texto), `bool` (True/False)."""

T[2] = """## Usar variables

Las variables se pueden **usar, operar y reasignar**:

```python
x = 10
y = 5
print(x + y)    # 15
print(x - y)    # 5
print(x * y)    # 50
print(x / y)    # 2.0   division siempre da decimal
print(x // y)   # 2     division entera
print(x % y)    # 0     modulo: el resto
print(x ** y)   # 100000 potencia
```

**Reasignar** cambia el valor:

```python
puntaje = 10
puntaje = puntaje + 5   # ahora 15
puntaje += 5            # forma corta, ahora 20
```

**El error mas comun:** usar un solo `=` cuando querias comparar. Para comparar se usa `==`."""

T[3] = """## Verdadero y falso

Los **booleanos** solo tienen dos valores: `True` y `False` (con mayuscula).

```python
print(5 > 3)     # True
print(5 < 3)     # False
print(5 == 5)    # True
print(5 != 5)    # False
```

Tambien puedes asignarlos:

```python
es_mayor = 18 > 17
print(es_mayor)   # True
```

En Python todo valor puede evaluarse como verdadero o falso:
- **Falso:** `0`, `""`, `[]`, `{}`, `None`, `False`
- **Verdadero:** todo lo demas

Son la base de todas las condiciones `if`."""

T[4] = """## Igualdad y verificacion

Los **operadores de comparacion** devuelven booleanos:

| Operador | Significado | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `==`     | igual a       | `5 == 5`| `True`  |
| `!=`     | diferente de  | `5 != 5`| `False` |
| `>`      | mayor que     | `5 > 3` | `True`  |
| `<`      | menor que     | `3 < 5` | `True`  |
| `>=`     | mayor o igual | `5 >= 5`| `True`  |
| `<=`     | menor o igual | `3 <= 5`| `True`  |

**El error mas comun:** usar un solo `=` para comparar.

```python
if edad = 18:    # MAL: asigna
if edad == 18:   # BIEN: compara
```

Combinacion de condiciones:

```python
if 5 > 3 and 2 < 4:   # True
if 5 > 3 or 2 > 4:    # True
if not (5 > 3):       # False
```"""

T[5] = """## Cadenas de formato

Las **f-strings** permiten meter variables dentro de texto (Python 3.6+):

```python
nombre = "Ana"
edad = 25

print(f"Hola, me llamo {nombre} y tengo {edad} anos")
```

Dentro de las llaves `{}` puedes poner **expresiones completas**:

```python
print(f"El doble de 7 es {7 * 2}")     # El doble de 7 es 14
print(f"{3.14159:.2f}")                # 3.14  (2 decimales)
print(f"{10 * 2} anos")                # 20 anos
```

Otras formas mas antiguas:

```python
"Mi nombre es " + nombre
"Mi nombre es {} y tengo {}".format(nombre, edad)
"Nombre: %s" % nombre
```

**Tip:** las comillas van dentro o fuera, pero no pueden ser las dos iguales."""

T[6] = """## Conceptos basicos de Python

```python
# Variables y tipos
nombre = "Ana"      # str
edad = 25            # int
altura = 1.70        # float
activo = True        # bool

# Ver el tipo
print(type(edad))          # <class 'int'>
print(type(nombre))        # <class 'str'>

# Convertir entre tipos
print(int("25") + 5)       # 30
print(str(25) + " anos")   # 25 anos
print(float(25))           # 25.0

# Operadores
print(10 + 3, 10 - 3, 10 * 3, 10 / 3)
print(10 // 3, 10 % 3, 10 ** 2)

# Concatenar
print("Hola" + " " + "Ana")
print(f"Hola {nombre}")
```

**Ojo:** `input()` **siempre devuelve texto**, aunque escribas numeros. Hay que convertirlo con `int()`."""

T[7] = """## Bot - Parte 1

Un **bot** es un programa que simula una conversacion.

```python
nombre = input("Bot: ¿Como te llamas? ")
print(f"Bot: Hola {nombre}, mucho gusto!")
print("Bot: Soy tu bot en Python. ¿En que te puedo ayudar?")
```

**Conceptos que usas:**
- `print()` para mostrar texto
- `input()` para recibir la respuesta del usuario
- f-strings para insertar el nombre

**Detalle importante:** el bot escribe `Bot:` antes de cada mensaje, asi se sabe quien habla. Eso se llama **prefijo de rol** y es un patron muy usado en chatbots."""

T[8] = """## Comparando numeros

Comparar **numeros** para tomar decisiones:

```python
nota = int(input("Tu nota: "))

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Bien")
elif nota >= 60:
    print("Suficiente")
else:
    print("Reprobado")
```

Se evalua **de arriba hacia abajo** y se detiene en la primera condicion verdadera.

**Combinaciones:**

```python
edad = 25
if edad >= 18 and edad < 65:
    print("Adulto en edad laboral")
```

**Recuerda:** convierte `input()` con `int()` antes de comparar."""

T[9] = """## Comparando cuerdas

Se pueden comparar **cadenas** con los mismos operadores:

```python
respuesta = input("Color favorito: ")

if respuesta.lower() == "azul":
    print("Es mi favorito tambien!")
elif respuesta.lower() == "rojo":
    print("Clasico")
else:
    print(f"Interesante: {respuesta}")
```

**Metodos utiles:**

| Metodo | Que hace | Ejemplo |
|--------|----------|---------|
| `.lower()` | a minusculas | `"AB".lower()` → `"ab"` |
| `.upper()` | a mayusculas | `"ab".upper()` → `"AB"` |
| `.strip()` | quita espacios | `" hola ".strip()` → `"hola"` |
| `.startswith("a")` | empieza con | `"abc".startswith("a")` → `True` |

**Importante:** Python diferencia mayusculas, `"Ana" != "ana"`. Por eso usamos `.lower()`."""

T[10] = """## Descubriendo tipos

`type()` te dice que tipo tiene un valor:

```python
print(type(10))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hola"))    # <class 'str'>
print(type(True))      # <class 'bool'>
print(type([1,2]))     # <class 'list'>
```

**Convertir entre tipos (type casting):**

```python
print(int("42"))       # 42      texto → entero
print(float("3.5"))    # 3.5     texto → decimal
print(str(100))        # "100"   numero → texto
print(bool(0))         # False
```

**Errores comunes:**

```python
int("hola")    # ValueError: invalid literal for int()
```

`int()` trunca decimales: `int(3.9)` → `3`. Para redondear usa `round(3.9)` → `4`."""

T[11] = """## Tipos y comparaciones

Combinar **tipos** con **comparaciones** correctamente.

El error clasico: comparar texto con numero.

```python
# MAL - input devuelve texto
edad = input("Edad: ")
if edad >= 18:        # TypeError

# BIEN - convierte primero
edad = int(input("Edad: "))
if edad >= 18:
    print("Puedes votar")
```

**Comprobar si algo es convertible:**

```python
texto = "123"
if texto.isdigit():          # True, todo son numeros
    print(int(texto) * 2)    # 246

if texto.isalpha():          # False, hay digitos
    print("Es solo texto")
```

Metodos: `.isdigit()`, `.isalpha()`, `.isspace()`, `.isupper()`, `.islower()`.

**El flujo correcto:** pedir → convertir → comparar → mostrar."""

T[12] = """## Entrada

`input()` **siempre devuelve una cadena de texto**:

```python
nombre = input("Nombre: ")     # str
edad = input("Edad: ")         # str  <- aunque escribas 25
precio = input("Precio: ")     # str
```

Por eso los numeros fallan al comparar:

```python
edad = input("Edad: ")
print(edad > 18)     # TypeError
```

**Solucion: convierte el resultado**

```python
edad = int(input("Edad: "))         # ok
precio = float(input("Precio: "))   # con decimales
cantidad = int(input("Cantidad: ")) + 1
```

**Buena practica:** maneja el error si el usuario escribe letras.

```python
try:
    edad = int(input("Edad: "))
except ValueError:
    print("Eso no es un numero")
```"""

T[13] = """## Bot - Parte 2

Ahora el bot **responde** segun lo que dice el usuario:

```python
print("Bot: ¡Hola! Soy tu bot en Python.")

nombre = input("Bot: ¿Como te llamas? ")
print(f"Bot: Mucho gusto, {nombre}!")

animo = input("Bot: ¿Como te sientes? ")
if animo.lower() in ["bien", "good", "feliz"]:
    print("Bot: ¡Me alegra tu buena vibra!")
elif animo.lower() in ["mal", "triste"]:
    print("Bot: Que mal, espero que mejoras pronto.")
else:
    print("Bot: Entiendo.")

print(f"Bot: Adiós {nombre}, fue un gusto platicar.")
```

**Lo nuevo respecto a la parte 1:**
- `if / elif / else` para reaccionar
- `in` con lista para aceptar varias palabras
- `.lower()` para no depender de mayusculas

Este es el esqueleto basico de cualquier chatbot."""

T[14] = """## Toma de decisiones

Las **decisiones** controlan que codigo se ejecuta, con `if`:

```python
edad = int(input("Tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

**La estructura:**
- `if condicion:` seguido de codigo **indentado** (4 espacios)
- El bloque solo se ejecuta si la condicion es `True`
- `else:` ejecuta lo contrario

**El error mas comun:** olvidar los dos puntos `:`.

```python
if edad >= 18      # MAL
    print("Mayor")

if edad >= 18:     # BIEN
    print("Mayor")
```

**En Python los espacios importan.** Si no indentes, da `IndentationError`."""

T[15] = """## Uso de condiciones

Las condiciones se combinan con operadores logicos:

```python
edad = int(input("Edad: "))
estudiante = input("Eres estudiante? (si/no): ").lower() == "si"

if edad >= 18 and estudiante:
    print("Puedes entrar con descuento")
elif edad >= 65 or edad < 0:
    print("Revisa el dato ingresado")
else:
    print("Precio normal")
```

| Operador | Significado | Ejemplo |
|----------|-------------|---------|
| `and`    | las dos True | `a > 0 and a < 10` |
| `or`     | al menos una True | `a == 0 or a == 1` |
| `not`    | invierte | `not es_mayor` |

**Prioridad** (mayor a menor): `not` → `and` → `or`."""

T[16] = """## Enunciados condicionales 1

Practica de condicionales combinando todo:

```python
usuario = input("Usuario: ")
clave = input("Clave: ")

if usuario == "admin" and clave == "1234":
    print("¡Acceso permitido!")
elif usuario == "admin":
    print("Clave incorrecta")
else:
    print("Usuario no registrado")
```

**Puntos clave:**
- `and` exige que **ambas** condiciones sean True
- Se evalua de arriba hacia abajo, gana la primera True
- Siempre hay un `else` para el resto

**Pro tip:** compara con `.lower()` si el usuario puede escribir de cualquier forma."""

T[17] = """## Sentencias else

`else` cubre **todo lo que no se cumplio** antes.

```python
# Sin else: no pasa nada si no cumple
if nota >= 60:
    print("Aprobado")

# Con else: siempre hay respuesta
if nota >= 60:
    print("Aprobado")
else:
    print("Reprobado")
```

**Calculadora completa:**

```python
op = input("Operacion (+ - * /): ")
a = float(input("Numero 1: "))
b = float(input("Numero 2: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("No se puede dividir entre cero")
else:
    print("Operacion no valida")
```

**Buena practica:** mete las validaciones dentro del bloque."""

T[18] = """## Incorporacion de elif

`elif` = "else if" en otros lenguajes. Encadena muchas condiciones:

```python
nota = int(input("Nota: "))

if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muy bien")
elif nota >= 70:
    print("Bien")
else:
    print("Reprobado")
```

**Como funciona:** Python revisa de arriba hacia abajo y **se detiene en la primera condicion verdadera**. Solo una rama se ejecuta.

**El orden importa:**

```python
if nota >= 60:      print("Pasa")       # el 95 entra aqui
elif nota >= 90:    print("Excelente")  # nunca se ejecuta
```

Pon siempre **de mayor a menor**."""

T[19] = """## Decisiones complejas

Multiples variables combinadas:

```python
temp = int(input("Temperatura: "))
lluvia = input("Esta lloviendo? (si/no): ").lower() == "si"
fin = input("Es fin de semana? (si/no): ").lower() == "si"

if temp > 30 and not lluvia:
    print("Calor seco, perfecta para salir")
elif lluvia or temp < 5:
    print("Mal dia para salir")
elif fin:
    print("Descansa en casa")
else:
    print("Buen dia normal")
```

**Prioridad de operadores** (de mayor a menor):
1. `not`
2. `and`
3. `or`

Usa parentesis para clarity:

```python
if (temp > 30 and not lluvia) or (temp < 0 and lluvia):
    print("Clima extremo")
```"""

T[20] = """## Enunciados condicionales 2

Practica avanzada de condicionales:

```python
nota = float(input("Nota final: "))
asistencia = int(input("Asistencias (de 20): "))

if nota >= 70 and asistencia >= 15:
    print("Aprobaste con honores")
elif nota >= 70 and asistencia < 15:
    print("Aprobaste pero con baja asistencia")
elif nota >= 60:
    print("Reprobaste por poco")
else:
    print("Reprobaste")
```

**Logica de este ejemplo:**
- Aprobado **y** asistio bien → honores
- Aprobado **pero** falto → aprobado normal
- Reprobado → no aprobado

Sirve para practicar `and`, `or` y la cadena de decisiones."""

T[21] = """## Piedra, papel o tijera - Parte 1

La logica del juego:

```python
import random

opciones = ["piedra", "papel", "tijera"]
pc = random.choice(opciones)
jugador = input("piedra/papel/tijera: ").lower()

print("PC eligio:", pc)

if jugador == pc:
    print("Empate!")
elif (jugador == "piedra" and pc == "tijera") or \\
     (jugador == "papel" and pc == "piedra") or \\
     (jugador == "tijera" and pc == "papel"):
    print("¡Ganaste!")
else:
    print("Perdiste")
```

**Las reglas de victoria:**
- Piedra vence a Tijera
- Papel vence a Piedra
- Tijera vence a Papel

`random.choice()` elige un elemento **al azar** de la lista."""

T[22] = """## Autoasignacion y operadores

Los **operadores de asignacion compuesta** abrevian operaciones:

```python
x = 10

x += 5      # x = x + 5    → 15
x -= 3      # x = x - 3    → 12
x *= 2      # x = x * 2    → 24
x /= 4      # x = x / 4    → 6.0
x **= 2     # x = x ** 2   → 36.0
x //= 5     # x = x // 5   → 7.0
x %= 3      # x = x % 3    → 1.0
```

Sirven mucho en bucles:

```python
total = 0
for numero in [5, 10, 15]:
    total += numero    # en vez de total = total + numero
```

**Tambien con cadenas:**

```python
saludo = "Hola"
saludo += " Mundo"
print(saludo)     # Hola Mundo
saludo *= 2
print(saludo)     # Hola MundoHola Mundo
```"""

T[23] = """## Bucles while

El bucle `while` **repite mientras** la condicion sea `True`:

```python
contador = 1
while contador <= 5:
    print(contador)
    contador += 1      # ¡importante! si no, nunca termina
```

Salida: 1, 2, 3, 4, 5

**El peligro del bucle infinito:**

```python
while True:
    print("infinito")   # no para nunca

i = 1
while i <= 5:
    print(i)            # ¡falta i += 1!
```

**Menu tipico** (lo veras en proyectos):

```python
opcion = ""
while opcion != "salir":
    opcion = input("Menu: ")
    if opcion == "1":
        print("Hola")
```

Usa `while` cuando **no sabes cuantas veces** se repite."""

T[24] = """## Parando bucles while

`break` **sale** del bucle; `continue` **salta** a la siguiente iteracion:

```python
# break: termina el bucle
while True:
    cmd = input("Comando: ")
    if cmd == "salir":
        break            # aqui termina el while
    print("Hiciste:", cmd)
print("Ya salimos del bucle")

# continue: ignora el resto de esta vuelta
for i in range(1, 6):
    if i == 3:
        continue         # salta el 3
    print(i)             # imprime 1, 2, 4, 5
```

**Combinados (impares hasta 7):**

```python
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue         # salta los pares
    if i > 7:
        break            # ya no sigue
    print(i)             # 1, 3, 5, 7
```

**En `for` funcionan igual.**"""

T[25] = """## Bucles 1 - Practica

Practica de bucles while:

```python
# Suma del 1 al 10
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print("Suma:", total)     # 55

# Tabla de multiplicar
n = int(input("Tabla del: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1

# Contar hacia atras
cuenta = int(input("Cuenta atras desde: "))
while cuenta > 0:
    print(cuenta)
    cuenta -= 1
```

**Leva en cuenta:**
- Inicializar la variable de control
- La condicion en el `while`
- Actualizar la variable dentro del bucle

Si falta el ultimo paso → bucle infinito."""

T[26] = """## Control de bucles while

**`break` en busqueda temprana:**

```python
numeros = [4, 8, 15, 16, 23, 42]
objetivo = 15

for n in numeros:
    if n == objetivo:
        print("Encontrado en", numeros.index(n))
        break        # no hace falta seguir buscando
```

**`continue` para filtrar datos:**

```python
datos = ["Ana", "", "Carlos", None, "Diana"]

for dato in datos:
    if not dato:              # None, "" o 0 -> salta
        continue
    print("Hola", dato)

# Imprime: Hola Ana, Hola Carlos, Hola Diana
```

**`for ... else`** — el `else` se ejecuta solo si el bucle **no** se rompio con `break`:

```python
for n in range(1, 5):
    if n == 3:
        break
    print(n)
else:
    print("No se encontro el 3")   # NO se imprime
```

Sirve para **buscar** algo y saber si lo encontraste."""

T[27] = """## Bucles for

El bucle `for` **recorre** una secuencia elemento por elemento:

```python
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)

for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    print(i)

for indice, fruta in enumerate(frutas):
    print(indice, fruta)
```

**Ventaja sobre `while`:** no necesitas un contador manual ni arriesgarte al bucle infinito.

**`for` funciona con todo lo iterable:** listas, cadenas, diccionarios, rangos, archivos."""

T[28] = """## Bucles 2 - Practica

```python
# Maximo de una lista
numeros = [34, 7, 92, 15, 6, 89]
maximo = numeros[0]

for n in numeros:
    if n > maximo:
        maximo = n

print("Maximo:", maximo)     # 92

# Suma de una lista
total = 0
for n in numeros:
    total += n
print("Suma:", total)

# Numeros pares
pares = []
for n in range(1, 11):
    if n % 2 == 0:
        pares.append(n)
print(pares)     # [2, 4, 6, 8, 10]

# Promedio
print("Promedio:", sum(numeros) / len(numeros))
```

**Tip:** Python trae `max()`, `min()`, `sum()`, `len()` listas para usar. Pero saber el bucle te da control total."""

T[29] = """## Control avanzado de bucles

**`break` y `continue` en bucles anidados:**

```python
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
objetivo = 5
encontrado = False

for fila in matriz:
    for numero in fila:
        if numero == objetivo:
            print("Encontrado")
            encontrado = True
            break        # sale del for interno
    if encontrado:
        break            # sale del for externo
```

**Enumerar con indice y salto:**

```python
for i, fruta in enumerate(["uva", "pera", "mango", "kiwi"]):
    if i % 2 == 0:
        print(i, fruta)     # indices 0 y 2
```

**`zip()`** para recorrer dos listas a la vez:

```python
nombres = ["Ana", "Luis", "Mia"]
notas = [90, 85, 95]

for nombre, nota in zip(nombres, notas):
    print(f"{nombre}: {nota}")
```"""

T[30] = """## Bucles 3 - Practica

```python
# Tabla de multiplicar completa (bucles anidados)
for i in range(1, 6):
    linea = ""
    for j in range(1, 11):
        linea += f"{i*j:4}"
    print(linea)
```

**Filtro con `continue`:**

```python
numeros = [5, 12, 8, 3, 20, 7, 15]
mayores = []

for n in numeros:
    if n < 10:
        continue      # ignora los menores a 10
    mayores.append(n)

print(mayores)     # [12, 20, 15]
```

**`return` dentro de un bucle** actua como `break` y ademas devuelve:

```python
def buscar(lista, objetivo):
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i          # sale de la funcion
    return -1                 # no lo encontro
```"""

# Quizzes: (pregunta, [opciones], indice correcto)
Q = {}

Q[1] = [
 ("¿Para que usan los ordenadores las variables?", ["Para almacenar informacion para su uso posterior", "Para mostrar la informacion en pantalla", "Para apagar el equipo"], 0),
 ("Como se crea una variable en Python?", ["nombre = 5", "variable nombre = 5", "5 = nombre"], 0),
 ("Que tipo tiene la variable `edad = 25`?", ["str", "int", "float"], 1),
 ("Cual de estos NO es un nombre de variable valido?", ["mi_edad", "_edad", "2edad"], 2),
 ("Que imprime `type(3.14)`?", ["<class 'int'>", "<class 'float'>", "<class 'str'>"], 1),
]

Q[2] = [
 ("Cuanto es `7 // 2`?", ["3.5", "3", "4"], 1),
 ("Cuanto es `7 % 2`?", ["1", "2", "3.5"], 0),
 ("Que hace `x += 5`?", ["x = 5", "x = x + 5", "x = x * 5"], 1),
 ("Cual es el error en `if edad = 18:`?", ["Falta el dos puntos", "Un solo = asigna en vez de comparar", "No hay error"], 1),
 ("Cuanto es `2 ** 5`?", ["10", "25", "32"], 2),
]

Q[3] = [
 ("Cuales son los dos valores booleanos?", ["1 y 0", "True y False", "Si y No"], 1),
 ("Que devuelve `5 > 3`?", ["5", "True", "1"], 1),
 ("Cual de estos es FALSO?", ["5", "'hola'", "0"], 2),
 ("Como asignas un booleano?", ["activo = si", "activo = True", "activo = true"], 1),
 ("Que devuelve `not True`?", ["True", "False", "None"], 1),
]

Q[4] = [
 ("Que operador compara igualdad?", ["=", "==", "=>"], 1),
 ("Que devuelve `5 != 5`?", ["True", "False", "0"], 1),
 ("Que operador significa 'mayor o igual'?", [">", ">=", "<="], 1),
 ("Que combinacion da True? (5>3 y 2<4)", ["and", "or", "not"], 0),
 ("Que hace `!=`?", ["Igual", "Diferente", "Mayor"], 1),
]

Q[5] = [
 ("Como se escribe una f-string?", ["f'hola {nombre}'", "'f hola {nombre}'", "format('hola', nombre)"], 0),
 ("Que imprime f'{7*2}'?", ["7*2", "14", "{14}"], 1),
 ("Cual es el resultado de f'{3.14159:.2f}'?", ["3.14159", "3.14", "3.1"], 1),
 ("Cual de estos NO es una f-string valida?", ["f'hola'", "f'{x}'", "f hola {x}"], 2),
 ("Como concatenas con signo +?", ["'a' + 'b' = 'ab'", "'a' + 'b'", "concat('a','b')"], 1),
]

Q[6] = [
 ("Que devuelve type(10)?", ["str", "int", "float"], 1),
 ("Como conviertes '25' a numero?", ["int('25')", "num('25')", "'25'.int()"], 0),
 ("Que imprime int(3.9)?", ["4", "3", "3.9"], 1),
 ("Para que sirve input()?", ["Leer archivos", "Pedir datos al usuario", "Imprimir"], 1),
 ("Que error da int('hola')?", ["TypeError", "ValueError", "NameError"], 1),
]

Q[7] = [
 ("Para que sirve input()?", ["Imprimir texto", "Pedir datos al usuario", "Borrar datos"], 1),
 ("Que hace print()?", ["Muestra texto en pantalla", "Guarda en archivo", "Pide datos"], 0),
 ("Como se inserta una variable en texto?", ["f'{nombre}'", "'{f nombre}'", "{f'{nombre}'}"], 0),
 ("Que tipo devuelve input()?", ["int", "str", "float"], 1),
 ("Por que el bot escribe 'Bot:' antes?", ["Para saber quien habla", "Es decorativo", "Obligatorio"], 0),
]

Q[8] = [
 ("Que hace `if`?", ["Repite codigo", "Decide si un bloque se ejecuta", "Nada"], 1),
 ("Es obligatorio el `:` al final de un if?", ["No", "Si", "Solo si es largo"], 1),
 ("Que error da si no indentas?", ["NameError", "IndentationError", "SyntaxError"], 1),
 ("Que compara `elif nota >= 80`?", ["Igualdad", "Nota mayor o igual a 80", "Nota igual a 80"], 1),
 ("Como se combinan condiciones?", ["and / or / not", "+ / -", "* / /"], 0),
]

Q[9] = [
 ("Como comparas sin importar mayusculas?", ["== directo", ".lower()", ".strip()"], 1),
 ("Que hace .upper()?", ["A minusculas", "A mayusculas", "Sin espacios"], 1),
 ("Que devuelve 'Ana' == 'ana'?", ["True", "False", "None"], 1),
 ("Para que sirve .strip()?", ["Quitar espacios", "Cambiar case", "Nada"], 0),
 ("Que hace 'hola'.startswith('h')?", ["True", "False", "'h'"], 0),
]

Q[10] = [
 ("Para que sirve type()?", ["Convertir", "Ver el tipo", "Validar"], 1),
 ("Que devuelve type(True)?", ["str", "bool", "int"], 1),
 ("Que hace float('3.5')?", ["'3.5'", "3.5", "35"], 1),
 ("Que hace str(100)?", ["100", "'100'", "[100]"], 1),
 ("int() redondea o trunca?", ["Redondea", "Trunca", "Da error"], 1),
]

Q[11] = [
 ("Por que falla `input() >= 18`?", ["input devuelve texto", "Falta int()", "No se puede"], 0),
 ("Como lo corriges?", ["edad = int(input())", "edad = str(input())", "edad = input(int())"], 0),
 ("Que hace '123'.isdigit()?", ["True", "False", "123"], 0),
 ("Cual es el orden correcto?", ["Comparar, convertir, pedir", "Pedir, convertir, comparar", "Convertir, pedir, comparar"], 1),
 ("Como manejas texto no numerico?", ["try/except", "if/else", "while"], 0),
]

Q[12] = [
 ("Que devuelve input() siempre?", ["int", "str", "float"], 1),
 ("Como pides un numero entero?", ["n = input()", "n = int(input())", "n = float(input())"], 1),
 ("Que pasa si comparas texto con numero?", ["Funciona", "TypeError", "ValueError"], 1),
 ("Que metodo de str quita espacios?", [".strip()", ".lower()", ".upper()"], 0),
 ("Como manejas error de input?", ["try/except", "print", "while"], 0),
]

Q[13] = [
 ("Que hace `in` con una lista?", ["Comprueba pertenencia", "Agrega", "Elimina"], 0),
 ("Como haces que el bot acepte varias palabras?", ["or / elif", "in [lista]", "add()"], 1),
 ("Por que usamos .lower()?", ["Para acortar", "Para ignorar mayusculas", "Para validar"], 1),
 ("Que estructura permite reaccionar?", ["if/elif/else", "for", "while"], 0),
 ("Que imprime una f-string con {nombre}?", ["El valor de nombre", "{nombre}", "Error"], 0),
]

Q[14] = [
 ("Que palabra introduce una condicion?", ["if", "else", "elif"], 0),
 ("Que hace `else`?", ["Repite", "Ejecuta si nada mas se cumplio", "Nada"], 1),
 ("Que es obligatorio en Python?", ["El `:`", "Los parentesis", "El `;`"], 0),
 ("Por que importa la indentacion?", ["Es estilo", "Define que codigo pertenece al bloque", "Es opcional"], 1),
 ("Cual es el error comun?", ["if edad >= 18 (sin :)", "print(18)", "edad = 18"], 0),
]

Q[15] = [
 ("Que hace `and`?", ["Al menos una True", "Las dos True", "Invierte"], 1),
 ("Que hace `or`?", ["Las dos True", "Al menos una True", "Invierte"], 1),
 ("Que hace `not`?", ["Las dos True", "Al menos una", "Invierte el valor"], 2),
 ("Cual es el orden de precedencia?", ["or, and, not", "not, and, or", "and, or, not"], 1),
 ("Como clasificas una nota con elif?", ["De mayor a menor", "De menor a mayor", "Al azar"], 0),
]

Q[16] = [
 ("Que combinacion da acceso?", ["or", "and", "not"], 1),
 ("Como comparas sin mayusculas?", ["== directo", ".lower() ==", "len()"], 1),
 ("Que se ejecuta si nada cumple?", ["if", "elif", "else"], 2),
 ("Como se evalua la cadena?", ["De abajo hacia arriba", "De arriba hacia abajo", "Al azar"], 1),
 ("Cuantas ramas se ejecutan?", ["Todas", "Solo una", "Ninguna"], 1),
]

Q[17] = [
 ("Que cubre `else`?", ["Solo un caso", "Todo lo no cumplido antes", "Nada"], 1),
 ("Como haces una calculadora?", ["if/elif/else", "for", "while"], 0),
 ("Donde validas division entre cero?", ["Antes del if", "Dentro del elif", "Despues"], 1),
 ("Que hace float() aqui?", ["Convierte a numero decimal", "Redondea", "Nada"], 0),
 ("Que pasa si la operacion no existe?", ["Sale else", "Falla", "Repite"], 0),
]

Q[18] = [
 ("Que es `elif`?", ["else + if", "if + else", "while"], 0),
 ("Cuantas ramas se ejecutan?", ["Todas", "Solo la primera verdadera", "Ninguna"], 1),
 ("Por que importa el orden?", ["Estetico", "La primera True gana", "Sintaxis"], 1),
 ("Como se ordenan las notas?", ["De menor a mayor", "De mayor a menor", "Al azar"], 1),
 ("Que palabra viene despues de if?", ["elif", "else", "done"], 0),
]

Q[19] = [
 ("Cual tiene mayor precedencia?", ["or", "and", "not"], 2),
 ("Como clarificas condiciones?", ["Con parentesis", "Con comentarios", "No se puede"], 0),
 ("Que significa `not lluvia`?", ["Si llueve", "Si no llueve", "No llueve mucho"], 1),
 ("Como comparas si el usuario dijo si?", ["== 'si'", ".lower() == 'si'", "in 'si'"], 1),
 ("Cuantas condiciones admite un if?", ["Solo una", "Varias con and/or", "Ninguna"], 1),
]

Q[20] = [
 ("Que logica usa este ejemplo?", ["and / or combinados", "Solo if", "for"], 0),
 ("Que necesita para honores?", ["Nota y asistencia", "Solo nota", "Solo asistencia"], 0),
 ("Que pasa si aprobado pero falta?", ["Aprobado con honores", "Aprobado normal", "Reprobado"], 1),
 ("Como decides la rama final?", ["else", "elif", "if"], 0),
 ("Que porcentaje es 15 de 20?", ["50%", "75%", "100%"], 1),
]

Q[21] = [
 ("Que funcion elige al azar?", ["random.randint", "random.choice", "random.shuffle"], 1),
 ("Que vence a la tijera?", ["Piedra", "Papel", "Ninguno"], 0),
 ("Como detectas empate?", ["if jugador == pc", "if jugador != pc", "else"], 0),
 ("Que hace elif?", ["Ejecuta si la anterior fallo", "Repite", "Nada"], 0),
 ("Que hace .lower()?", ["A minusculas", "A mayusculas", "Quita espacios"], 0),
]

Q[22] = [
 ("Que hace `-=`?", ["x = x - n", "x = -n", "Nada"], 0),
 ("Que hace `**= 2`?", ["x = x ** 2", "x = 2 ** x", "Nada"], 0),
 ("Funciona += con cadenas?", ["Si", "No", "Solo numeros"], 0),
 ("Donde es mas util +=?", ["Bucles", "Print", "Input"], 0),
 ("Que hace `/=`?", ["Divide", "Multiplica", "Modulo"], 0),
]

Q[23] = [
 ("Que repite while?", ["Mientras la condicion sea True", "Un numero de veces", "Nada"], 0),
 ("Que causa bucle infinito?", ["Olvida incrementar la variable", "Usar while", "Usar print"], 0),
 ("Cual es su equivalente?", ["for", "if", "def"], 0),
 ("Cuando usas while?", ["Cuando no sabes cuantas veces", "Siempre", "Nunca"], 0),
 ("Que palabra sale del while?", ["break", "continue", "return"], 0),
]

Q[24] = [
 ("Que hace break?", ["Salta a la siguiente vuelta", "Sale del bucle", "Repite"], 1),
 ("Que hace continue?", ["Sale del bucle", "Salta a la siguiente vuelta", "Termina"], 1),
 ("Como sales de while True?", ["break", "stop", "exit()"], 0),
 ("Como saltas los pares?", ["continue con if n%2==0", "break", "else"], 0),
 ("Con continue en 3, que imprime?", ["1 2 3 4 5", "1 2 4 5", "4 5"], 1),
]

Q[25] = [
 ("Cual es la suma del 1 al 10?", ["45", "50", "55"], 2),
 ("Que falta en un while correcto?", ["La condicion", "Actualizar el contador", "Los parentesis"], 1),
 ("Como generas la tabla?", ["while con i", "print directo", "input"], 0),
 ("Que se necesita al inicio?", ["Inicializar la variable de control", "Nada", "El resultado"], 0),
 ("Como cuentas hacia atras?", ["i += 1", "i -= 1", "i = 1"], 1),
]

Q[26] = [
 ("Que hace break en un for?", ["Sale del bucle", "Salta una vuelta", "Repite"], 0),
 ("Para que sirve continue?", ["Filtrar datos", "Terminar", "Nada"], 0),
 ("Que se imprime si el for termina normal?", ["break", "else", "continue"], 1),
 ("Que da .index()?", ["El indice", "El valor", "El tipo"], 0),
 ("Que hace zip()?", ["Recorre dos listas a la vez", "Zipea archivos", "Nada"], 0),
]

Q[27] = [
 ("Que recorre for?", ["Una secuencia elemento a elemento", "Un numero de veces", "Nada"], 0),
 ("Que genera range(5)?", ["0 1 2 3 4", "1 2 3 4 5", "5 valores"], 0),
 ("Que genera range(1, 6)?", ["0 1 2 3 4 5", "1 2 3 4 5", "6 valores"], 1),
 ("Que hace enumerate?", ["Da indice y valor", "Cuenta", "Enumera"], 0),
 ("Que ventaja tiene for sobre while?", ["No tiene bucle infinito", "Es mas rapido", "Usa mas memoria"], 0),
]

Q[28] = [
 ("Como encuentras el maximo con for?", ["max()", "Bucle con if", "sort()"], 1),
 ("Cual es el promedio?", ["sum / len", "max", "min"], 0),
 ("Como agregas pares a una lista?", ["append dentro de if", "add()", "push()"], 0),
 ("Que funcion da el total?", ["sum()", "total()", "count()"], 0),
 ("Que hace range(0, 10, 2)?", ["0 2 4 6 8", "2 4 6 8", "0 1 2"], 0),
]

Q[29] = [
 ("Como sales de dos bucles anidados?", ["break en ambos", "Flag + break en externo", "continue"], 1),
 ("Que hace enumerate()?", ["Indice y valor", "Cuenta", "Enumera"], 0),
 ("Que hace zip()?", ["Recorre dos listas juntas", "Comprime", "Divide"], 0),
 ("Que hace else en un bucle?", ["Se ejecuta si no hubo break", "Siempre", "Nunca"], 0),
 ("Como recorres un diccionario?", [".items()", "[0]", "len()"], 0),
]

Q[30] = [
 ("Cuantos bucles necesita una tabla?", ["2 anidados", "1", "3"], 0),
 ("Como agregas texto sin salto?", ["end=''", "sin salto", "-n"], 1),
 ("Que hace continue al filtrar?", ["Salta lo que no cumple", "Termina", "Repite"], 0),
 ("Que ventaja tiene return en un bucle?", ["Sale y devuelve", "Repite", "Nada"], 0),
 ("Que devuelve buscar() si no encuentra?", ["0", "-1", "None"], 1),
]

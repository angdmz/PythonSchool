# en la mayoría de los lenguajes, tenés alguna API de colecciones que tienen 3 interfaces suuuuper comunes

s = set()
d = dict()
l = list()

# tanto set como dict están implementados sobre tabla de hash por defecto en python,
# y list está implementado sobre array dinámico

# hablemos primero, un poco sobre sets...

for i in range(10):
    s.add(i)

print(len(s))
print(str(s))
print(f"esta el 1? {1 in s}")
print(f"esta el 9349? {9349 in s}")

# los sets no tienen ni orden ni repetidos, son el análogo del objeto matemático conjunto
# si no tienen orden entonces...
s2 = set()

for i in reversed(range(10)):
    s2.add(i)

print(len(s2))
print(str(s2))

# seran iguales?
print(f"son iguales loko? {s == s2}")
# se pueden sacar cosas también tipo
s.remove(5)
print(f"s quedo así: {s}")

# claro, en s y s2 insertamos las mismas cosas pero al no tener orden entonces no distingue que
# haya puesto un 10 o un 1 primero, entonces estamos bien como vamos
# si no tienen repetidos entonces...

s = set()
s2 = set()

# che loko, tan famoso es python para inicializar variables de forma fácil, no hay algún truquito para no hacer esas
# 2 líneas?

s = s2 = set()

s.add(1)

s2.add(1)
s2.add(1)
s2.add(1)

# seran iguales?
print(f"son iguales loko? {s == s2}")

# estamos perfectos!

# che loko, antes dijiste que los sets son de hecho conjuntos matemáticos entonces...
# si, tenemos las operaciones propias de teoría de conjuntos

s = {1, 2, 3}  # ah si, de paso esto es análogo a hacer set() y add(1) add(2) add(3), python lindo y coso
s2 = {2, 3, 4}

print(f"s: {s}")
print(f"s2: {s2}")
print(f"la intersección: {s.intersection(s2)}")
print(f"la unión: {s.union(s2)}")
print(f"la diferencia simétrica: {s.symmetric_difference(s2)}")
print(f"y de hecho las diferencia de izquierda: {s.difference(s2)} COMO LA LOGICA DE LOS JOINS DE SQL LOKO")

# y podemos digamos hacer esta boludez, que es basicamente sumar conjuntos
s.update(s2)
print(f"esto debería ser igual que la union: {s}")
# y podemos sacar también
s.difference_update(s2)
print(f"esto debería ser igual que la diferencia: {s}")

# ok bueno hablemos un poco de listas ahora, pero poco nomás porque esto es lo que ya conocemos no?

l = list()
l.append(1)
l.append(1)
l.append(1)
print(f"no tiene muchas ciencia {l}")
print(f"accedo al iésimo {l[1]}")
l2 = [1, 2, 3, 4]  # de nuevo, sintaxis corta
print(f"esta el 4? {4 in l2}")
l2.remove(4)  # sacamo el cuatro
print(f"l2: {l2}")

# bueno ya, suficiente con las listas :v, no hay mucho más interesante para contar que no se pueda gugliar

# pasemo a los diccionarios

d = dict()

d["cecii"] = "buen humor"
d["cecilia"] = "enojado"
d["MARIA CECILIA"] = "del orto"

print(f"diccionario de cecis? {d}")
print(f"esta cecii? {'cecii' in d}")
# a cualquier diccionario decente le podemos sacar las claves y los valores, no?
print(d.keys())
print(d.values())

d.pop("MARIA CECILIA")

print(f"sacamos a MARIA CECILIA porque no estamos del orto: {d}")

del d["cecilia"]

print(f"y sacamos a cecilia porque enojados tampoco: {d}")

# cheeee y como mierda iteramos estas cosas?
l = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7]
s = {1, 2, 3, 4, 5, 6, 7}
d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7}

# iteremos listas
i = 0
while i < len(l):
    print(l[i])
    i += 1

# obviamente hay algo mejor!
for e in l:
    print(e)

# si queremos el indice también
for i, e in enumerate(l):
    print(f"i: {i} e:{e}")

# iteremos sets
for e in s:
    print(e)

# y finalmente diccionarios, pero para, los diccionarios son colecciones de pares clave valor... que onda?

for par in d:  # que pasa si hago esto?
    print(par)
# me iteraste las claves Y los valores, una verga loko
# ahh pero si puedo obtener las claves...

for k in d.keys():
    print(f"k: {k} v: {d[k]}")

# bueno, es una mejora, pero no hay algo MAS PIOLA???!?!?
for k, v in d.items():
    print(f"k: {k} v:{v}")

# muito mais melhor mano


# la magoya esta era para mostrar que boludeces copadas podemos escribir en python, porque hasta ahora lo tenemos
# muuuy parecido a otros lenguajes no? osea que tiene de piola python entonces?

# supongamos que queremos una lista de números pares...

l = [2 * i for i in range(11)]  # listas por comprensión capoooo
print(l)

# y si quiero numeros pares que no sean multiplos de 5? como mierda hacemos?
l = [2 * i for i in range(11) if i % 5 != 0]  #listas por comprension con condicional
print(l)


# esto es análogo a los sets!

s = {2 * i for i in range(11)}  # sets por comprensión capoooo
print(s)

# y si quiero numeros pares que no sean multiplos de 5? como mierda hacemos?
s = {2 * i for i in range(11) if i % 5 != 0}  #sets por comprension con condicional
print(s)


# y con los diccionarios?

inflacion_2019_paises = [
    {'pais': "Argentina", 'inflacion': 50},
    {'pais': "Ecuador", 'inflacion': 0.1},
    {'pais': "Estados Unidos", 'inflacion': 2},
    {'pais': "Venezuela", 'inflacion': 1000000},
]
print(inflacion_2019_paises)

inflacion_2019_paises_dict = {par["pais"]: par["inflacion"] for par in inflacion_2019_paises}
# osea {clave: valor for elemento in cosaiterable}
print(inflacion_2019_paises_dict)

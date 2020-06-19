from collections import namedtuple
from functools import partial
from attrdict import AttrDict

Elemento = namedtuple("Elemento", "peso valor")

class Mochila:
    cosas = set()

    def agregar_elemento(self, elemento):
        self.cosas.add(elemento)

    def __str__(self):
        return f"<Mochila cosas={self.cosas}>"

MochiTupla = namedtuple("MochiTupla", "cosas")

e1 = Elemento(10, 10)
e2 = Elemento(1, 1)
mochitupla = MochiTupla(cosas=set())
Mochila.agregar_elemento(mochitupla, e1)
mochi = Mochila()
mochi.agregar_elemento(e2)

print(f"Mochila: {mochi}")
print(f"Mochitupla: {mochitupla}")

def agregar_cosas_a_mochila(mochila, cant):
    cosas = [Elemento(i, i) for i in range(cant)]
    for c in cosas:
        mochila.agregar_elemento(c)

agregar_cosas_a_mochila(mochi, 10)
print (f"Mochila despues de agregar: {mochi.cosas}")


# ah pero y si jugamos un poco más con el chequeo dinámico de tipos y duck typing?
partialized = partial(Mochila.agregar_elemento, mochitupla)
motrucha = AttrDict(agregar_elemento=partialized)

agregar_cosas_a_mochila(motrucha, 10)
print(f"Mochitrucha: {motrucha}")

# claro, motrucha tiene agregar_elemento como atributo, que como es una función, se puede ejecutar, pero esa función
# tiene como parámetro a self, que en el contexto de objeto instanciado, self es la propia instancia, pero fuera, tiene
# que ser provista
try:
    print(f"cosas de mochitrucha: {motrucha.cosas}")
except AttributeError as ke:
    print(f"reventamos eh: {ke}")

# claro, motrucha es un AttrDict, su unico elemento es esa función agregar_elemento, que la hicimos parcializando
# la función Mochila.agregar_elemento con mochitupla! por lo que no tiene un atributo cosas
# podremos hacer un mecanismo para hacer "objetos con propiedades privadas"?

def crear_objeto_trucho(propiedades_privadas, propiedades_publicas):
    truchoself = AttrDict(propiedades_privadas)
    truchobjeto = AttrDict({k: partial(v,truchoself) for k, v in propiedades_publicas.items()})
    return truchobjeto

# tratemos de hacer una mochitrucha con este metodo!
otra_mochitrucha = crear_objeto_trucho({'cosas':set()},{'agregar_elemento': Mochila.agregar_elemento})
print(f"nuestra mochitrucha: {otra_mochitrucha}")

# probemos hacer cosas como las de antes!
agregar_cosas_a_mochila(otra_mochitrucha, 20)
print(f"mochitrucha: {otra_mochitrucha}")

#ahh pero si tratamos de ver esa propiedad que propusimos privada?
try:
    print(otra_mochitrucha.cosas)
except AttributeError as ae:
    print(f"La cagamos de nuevo eh: {ae}")

# podremos agregar el __str__?
def probemos_a_ver_si_anda(self):
    return f"<Mochitrucha hecha en mi funcion adhoc cosas={self.cosas}>"

metodos_publicos = {'agregar_elemento': Mochila.agregar_elemento,'__repr__': probemos_a_ver_si_anda}
yet_another_mochitrucha = crear_objeto_trucho({'cosas':set()}, metodos_publicos)

# habrá andado? hagamos print!
print(f"Andara el __repr__ de nuestra mochitrucha?: {yet_another_mochitrucha}")

# y claro... no... porque mochitrucha es un attrdict! osea que nuestro mamarracho anda, peeeero es eso, un mamarracho
# pero y si overrideamos la función __str__ de attrdict en esa instancia particular?

def crear_objeto_trucho_mejorado(propiedades_privadas, propiedades_publicas):
    truchobjeto = crear_objeto_trucho(propiedades_privadas, propiedades_publicas)
    truchobjeto.__repr__ = propiedades_publicas.get("__repr__", truchobjeto.__repr__)
    return truchobjeto

try:
    mochitrucha_mejorada = crear_objeto_trucho_mejorado({'cosas':set()}, metodos_publicos)
    # habrá andado? hagamos print!
    print(f"Andara el __str__ de nuestra mochitrucha mejorada?: {mochitrucha_mejorada}")
except TypeError as te:
    print(f"yyyy no anduvo che...: {te}")


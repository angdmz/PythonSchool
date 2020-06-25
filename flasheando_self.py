from collections import namedtuple
from functools import partial
from attrdict import AttrDict

#no hacia falta hacer esto, pero lo pense como para flashear hacer algo con el problema de la mochila https://es.wikipedia.org/wiki/Problema_de_la_mochila
Elemento = namedtuple("Elemento", "peso valor")

# una clase super boluda, lo que hiciera falta para nuestro ejemplito
class Mochila:
    cosas = set()

    def agregar_elemento(self, elemento):
        self.cosas.add(elemento)

    def __str__(self):
        return f"<Mochila cosas={self.cosas}>"

# una tupla nombrada que se comporte parecido a una instancia de mochila, porque tiene una componente cosas
# como acceder a la componente de una tupla nombrada es igual a acceder al atributo de un objeto
# puede pasar por objeto
MochiTupla = namedtuple("MochiTupla", "cosas")

e1 = Elemento(10, 10)
e2 = Elemento(1, 1)

# así trataríamos regularmente el objeto mochi de clase Mochila
mochi = Mochila()
mochi.agregar_elemento(e2)

#instanciar una MochiTupla con un set para la componente cosas
mochitupla = MochiTupla(cosas=set())
# me mando a la función agregar_elemento de la clase Mochila, haciendo pasar la mochitupla como un objeto de clase Mochila
# cosa posible gracias al duck typing habilitandonos el polimorfismo!
Mochila.agregar_elemento(mochitupla, e1)

# todo esto funcó gracias a que mochi.agregar_elemento(e2) es exactamente igual a hacer Mochila.agregar_elemento(mochi,e2)
# porque python nos hace el partial de Mochila.agregar_elemento con el objeto mochi de prepo, porque claramente es más piola
# escribirlo así que con todo el coso largo!

print(f"Mochila: {mochi}")
print(f"Mochitupla: {mochitupla}")

# me invento una funcioncita que espera algo que se comporte como una mochila, no importa qué hace la función, 
# sólo importa que espera que el parámetro mochila tenga agregar_elemento
def agregar_cosas_a_mochila(mochila, cant):
    cosas = [Elemento(i, i) for i in range(cant)]
    for c in cosas:
        mochila.agregar_elemento(c)


# claro, esto debe andar trank porque mochi es una instancia de Mochila, va todo bien        
agregar_cosas_a_mochila(mochi, 10)
print (f"Mochila despues de agregar: {mochi.cosas}")


# ah pero y si jugamos un poco más con el chequeo dinámico de tipos y duck typing?

#paraaaaaaaa wachin, qué es esto?
partialized = partial(Mochila.agregar_elemento, mochitupla)
# ok, explico, partial es una funcion práctica que nos provee python, que recibe una funcion F y un valor cualquiera X
# y devuelve una nueva funcion G tal que la funcion G es de hecho F con el valor X que se manda de parámetro siempre
# o sea que partialized es ahora una variable que es una función que en su primer parámetro le mete de prepo mochitupla!
# con esta jugarreta hacemos por nuestra cuenta el sugar syntax que python nos da nativamente que comenté en las lineas 36 37 y 38


# bueno bueno bueno, y qué es este AttrDict falopa?
# ok, es cierto que podría haber usado de nuevo una namedtuple peeero queria usar AttrDict
# pero qué es?
# ok, un AttrDict es un diccionario pero que le podés acceder a las claves como si fueran atributos
# AAAAAAAAAAAAAAAH
motrucha = AttrDict(agregar_elemento=partialized)
# entonces motrucha es de hecho un attrdict, osea un diccionario que se le pueden acceder las claves como atributos
# osea queeee tiene comportamiento de objeto, y además le definimos la clave agregar_elemento con el significado partialized
# y partialized era la función esa que hicimos antes!
# osea que motrucha.agregar_elemento() es algo que tiene que andar gracias a que las funciones son de alto orden en python!

agregar_cosas_a_mochila(motrucha, 10)
print(f"Mochitrucha: {motrucha}")


# claro, motrucha es un AttrDict, su unica clave es esa función agregar_elemento, que la hicimos parcializando
# la función Mochila.agregar_elemento con mochitupla! por lo que no tiene una clave cosas
# podremos hacer un mecanismo para hacer "objetos con propiedades privadas"?
try:
    print(f"cosas de mochitrucha: {motrucha.cosas}")
except AttributeError as ke:
    print(f"reventamos eh: {ke}")


# podremos hacer una función que haga objetos truchos con las ideas de antes?
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
# genial, cayó en la excepción! osea que anduvo la falopeada que inventé

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


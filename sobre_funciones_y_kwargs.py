from collections import namedtuple


def funcion_de_mierda_con_muchos_parametros(a, b, c, d, e, f, g, h, i):
    print(a, b, c, d, e, f, g, h, i)


# esta funcion es un culo, tiene muchos parametros
funcion_de_mierda_con_muchos_parametros(1, 2, 3, 4, 5, 6, 7, 8, 9)


# tuve mucha suerte, qué pasa si le pifio al orden de los parámetros mientras codeo? esto no tiene chequeo estático...


# bueeeno, podemos refactorizar la función y que reciba un objeto, a priori, no?
def funcion_de_mierda_2(objetoloco):
    print(objetoloco.a, objetoloco.b, objetoloco.c, objetoloco.d, objetoloco.e, objetoloco.f, objetoloco.g,
          objetoloco.h, objetoloco.i)


# no voy a hacer una clase para esto, uso una namedtuple y fue
MiTuplaLoca = namedtuple("ClaseLoca", ["a", "b", "c", "d", "e", "f", "g", "h", "i"])  # defino la tupla nombrada
coso = MiTuplaLoca(1, 2, 3, 4, 5, 6, 7, 8, 9)  # la instancia de la tupla
funcion_de_mierda_2(coso)

# pero para eso tuve que justamente modificar la función yyyyy medio que capaz no tira ni en pedo hacer eso
# PYTHON SALVAME
funcion_de_mierda_con_muchos_parametros(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9)

# eee ok, vemos que con esto nos guiamos de ojo al menos, pero ke onda
funcion_de_mierda_con_muchos_parametros(d=4, e=5, f=6, g=7, h=8, i=9, a=1, b=2, c=3, )
# ahh mirá, es conmutativo, bueno, va mejor, pero a qué viene esto?

d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9}

funcion_de_mierda_con_muchos_parametros(**d)
# AAA ok, puedo mandar los parámetros como diccionario poniendo los asteriscos esos, buena onda


def funcion_de_negocio_loca(a,b,c, *args, **kwargs):
    print(a,b,c)
    print(args)
    print(kwargs)

# benvenute a los keyword arguments, un feature bastaaante peoli de python

funcion_de_negocio_loca(1,2,3,4,5,65,76,55,425,56,56,7)
# ahhh, tipo, args tiene los valores de los parámetros en el orden que se ingresaron que no son parte de la firma de la función

def otra_funcion_de_negocio_loca(*args, **kwargs):
    for k, v in kwargs.items():
        print(k, v)

otra_funcion_de_negocio_loca(algun_parametro_flashero=123, y_metamos_otro_porque_si=coso)

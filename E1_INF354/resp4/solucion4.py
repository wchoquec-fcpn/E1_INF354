# 4. Con el uso de librerÃ­as en PYTHON, construya la dependencia de 
# Abuelos, tios, padres, primos e hijos de su familia.

from kanren import run, var, eq, Relation, facts
a = var()
b = var()


abuelo = Relation()
facts(abuelo, ("abueloPat","hijo1"),("abueloMat","hijo1"))
print(abuelo.facts)

tio = Relation()
facts(tio, ("tio1","hijo1"),("tio1","hijo2"))
print(tio.facts)


padre = Relation()
facts(padre, ("papa","hijo1"),("papa","hijo2"),("abuelo","papa"))
print(padre.facts)

primos = Relation()
facts(primos, ("primos1","hijo1"),("primos2","hijo1"))
print(primos.facts)


#¿Quien es el papa de hijo2?
print(run(1,a,padre(a,"hijo2")))
#¿el papa que  hijos tiene?
print(run(2,b,padre("papa",b)))
#¿QuiÃ©n es el abuelo de hijo1?
print(run(1, a, padre(a, b),padre(b, 'hijo1')))

# =============================================================================
# {('abueloPat', 'hijo1'), ('abueloMat', 'hijo1')}
# {('tio1', 'hijo1'), ('tio1', 'hijo2')}
# {('papa', 'hijo2'), ('papa', 'hijo1'), ('abuelo', 'papa')}
# {('primos2', 'hijo1'), ('primos1', 'hijo1')}
# ('papa',)
# ('hijo2', 'hijo1')
# ('abuelo',)
# =============================================================================

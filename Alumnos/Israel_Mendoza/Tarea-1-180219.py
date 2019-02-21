############################################################ Tarea 18/02/2019 ################################################

##Ejercicio 1##

print("Hello World!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print('Yay! Printing.')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')


## Ejecicio 2##

#Un comentario, es algo que puedes leer después#
#Cualquier cosa posterior a# es ignorada por Python#

print("I could have code like this.") # el comentario posterior será ignorado
# Tambien se puede usar un comentario para "deshabilitar" o dejar comentarios fuera del codigo:

# print("This won't run.")

print("This will run.")


## Ejecicio 3##

print("Ahora contare mis pollos:") #Escribe el texto

print("Gallinas",25+30/6) #Escribe el texto y realiza la operación
print("Gallos", 100-25*3%4)

print ("Ahora contare los huevos:") #Escribe el texto

print(3+2+1-5+4%2-1/4+6) #Realiza la operación

print("Es correcto 3+2<5-7?") #Escribe el texto

print(3+2<5-7) #Realiza la operación

print("Resultado de 3 + 2?", 3 + 2) #Escribe el texto y realiza la operación
print("Resultado de 5 - 7?", 5 - 7) #Escribe el texto y realiza la operación

print("Ah, por eso es Falso.") #Escribe el texto

print("Un poco mas.") #Escribe el texto

print("Es mayor?", 5 > -2) #Escribe el texto y realiza la operación
print("Es mayor o igual?", 5 >= -2) #Escribe el texto y realiza la operación
print("Es menor igual?", 5 <= -2) #Escribe el texto y realiza la operación


## Ejercicio 4##

autos=100
lugares_por_auto=4
conductores=30
pasajeros=90
autos_detenidos=autos-conductores
autos_movimiento=conductores
capacidad_autos=autos_movimiento*lugares_por_auto
pasajeros_promedio_auto=pasajeros/autos_movimiento

print("Hay",autos,"autos disponibles")
print("Sólo hay",conductores,"conductores")
print("Tendremos",autos_detenidos,"autos vacios hoy")
print("Podemos transportar",capacidad_autos,"personas el día de hoy")
print("Tenemos",pasajeros,"pasajeros a transportar")
print("Necesitamos meter",pasajeros_promedio_auto,"pasajeros en cada auto")


## Ejercicio 5#

mi_nombre='Israel Mendoza'
mi_edad=41
mi_peso=69 #Kgs
mi_estatura=163 #Cms
mis_ojos='Cafe'
mis_dientes='Blancos'
mi_cabello='Negro'

print(f"Hablemos de {mi_nombre}.")
print(f"El mide {mi_estatura} cms de altura.")
print(f"Pesa {mi_peso}kgs. de músculo")
print("De hecho, no es muy gordo")
print(f"Tiene ojos {mis_ojos} y su cabello es {mi_cabello}.")
print(f"Sus dientes normalmente son {mis_dientes}, dependiendo del cafe.")

#Linea engañosa#
total=mi_edad+mi_peso+mi_estatura
print(f"Si sumo {mi_edad}, {mi_peso}, {mi_estatura} obtengo {total}")


## Ejercicio 6#

clases_personas=10
x=f"Hay {clases_personas} clases de personas."

binary="binarios"
do_not="no lo son"
y=f"Sabremos quienes son {binary} y quienes {do_not}"

print(x)
print(y)

print(f"Yo dije: {x}")
print(f"Tambien dije: '{y}'")

hilariuos=False

evaluacion_broma="Es una broma divertida? {}"

print(evaluacion_broma.format(hilariuos))

w="Este es el lado izquierdo de..."
e="una cadena con lado derecho."

print(w+e)



## Ejercicio 7#

print("Mary tiene un corderito.")
print("Tiene lana blanca como la {}.".format('nieve'))
print("Y va a dónde ella va")
print("."*10) #Que hace?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#Observa la coma la final, quitala y ve que pasa

print(end1 + end2 + end3 + end4 + end5 + end6 , end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)


##Ejercicio 8#

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("uno", "dos", "tres", "cuatro"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Prueba tu",
"Propio texto aqui",
"Quiza un poema",
"O una cancion sobre el miedo"
))


##Ejercicio 9#

dias="Lun Mar Mie Jue Vie Sab Dom"
meses="Ene\nFeb\nMar\nAbr\nMay\nJun\nJul\nAgo\nSep\nOct\nNov\nDic"

print("Estos son los dias", dias)
print("Estos son los meses", meses)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")


##Ejercicio 10#

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


##Ejercicio 11#

print("Que edad tienes?",end=' ')
edad=input()
print("Cuanto mides?",end=' ')
estatura=input()
print("Cuanto pesas?",end=' ')
peso=input()

print(f"Entonces, tienes {edad} años, mides {estatura} cms y pesas {peso} kgs." )

######      x = input("Como te llamas:") #########
######      print("Hello, " + x) #################


##Ejercicio 12#

edad=input("Que edad tienes? ")
estatura=input("Cuanto mides? ")
peso=input("Cuanto pesas? ")
print(f"Entonces, tienes {edad} años, mides {estatura} cms y pesas {peso} kgs." )



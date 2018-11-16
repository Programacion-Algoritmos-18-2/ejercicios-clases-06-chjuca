from paquete.model import *			# Se importa todo el archivo modelado
# p=PersonaEquipo("Luis")
f=Futbolista("Antonio")				# Se crea el Objeto Futbolista y le enviamos un parametro
m=MedicoEquipo("Ramon")				# Se crea el Objeto Medico y le enviamos un parametro
p=PresidenteEquipo("Francisco") 	# Se crea el Objeto Presidente y le enviamos un parametro
e=Entrenador("Jose")				# Se crea el Objeto Entrenador y le enviamos un parametro
lista=[f,m,p,e]						# Se crea una lista que almacena los objetos creados anteriormente
for l in lista:						# Recorremos los objetos presentes en la lista
	l.entrenar()					# Llamamos al metodo entrenar de cada uno de los objetos
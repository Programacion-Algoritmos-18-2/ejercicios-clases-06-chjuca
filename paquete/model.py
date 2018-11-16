import abc

class PersonaEquipo(metaclass=abc.ABCMeta):			# Se define la clase abstracta

	def __init__(self,nom):							# Metodo __init__ de la clase abstracta
		self.nombre = nom 							# Atributo de la clase abstracta

	@abc.abstractmethod		
	def entrenar(self):						# Metodo Abstacto de la clase
		pass

	def setNombre(self,nombre):						# Funcion que da valor al atributo de la clase
		self.nombre=nombre

	def getNombre(self):							# Funcion que devuelve el valor del atributo de la clase
		return self.nombre

class Entrenador(PersonaEquipo):					# Se define la clase Entrenador que es una PersonaEquipo

	def __init__(self,n):							# Metodo __init__ de la clase Entrenador
		super(Entrenador, self).__init__(n)			# Se heredan los atributo de Persona Equipo
		self.codigoEntrenado=""						# Atributo de la clase

	def setCodigoEntrenador(self,codigoEntrenado):	# Funcion que da valor al atributo de la clase
		self.codigoEntrenado=codigoEntrenado

	def getCodigoEntrenador(self):					# Funcion que devuelve el valor del atributo de la clase			
		return self.codigoEntrenado

	def entrenar(self):						# Funcion que sobreescribe el metodo abstracto
		print("Yo %s, Entrenador, soy el director del entrenamiento "%(self.getNombre()))


class Futbolista(PersonaEquipo):					# Se define la clase Entrenador que es una PersonaEquipo

	def __init__(self,n):							# Metodo __init__ de la clase Futbolista
		super(Futbolista, self).__init__(n)			# Se heredan los atributo de PersonaEquipo
		self.posicionCampo=""						# Atributo de la clase

	def setPosicionCampo(self,posicionCampo):		# Funcion que devuelve el valor del atributo de la clase
		self.posicionCampo=posicionCampo

	def getPosicionCampo(self):						# Funcion que devuelve el valor del atributo de la clase
		return self.posicionCampo

	def entrenar(self):								# Funcion que sobreescribe el metodo abstracto
		print("Yo %s, Futbolista, hago Practica en el entrenamiento "%(self.getNombre()))


class MedicoEquipo(PersonaEquipo):					# Se define la clase MedicoEquipo que es una PersonaEquipo

	def __init__(self,n):							# Metodo __init__ de la clase Futbolista					
		super(MedicoEquipo, self).__init__(n)		# Se heredan los atributo de PersonaEquipo
		self.titulo=""								# Atributo de la clase

	def setTitulo(self,titulo):						# Funcion que devuelve el valor del atributo de la clase
		self.titulo=titulo

	def getTitulo(self):							# Funcion que devuelve el valor del atributo de la clase
		return self.titulo

	def entrenar(self):								# Funcion que sobreescribe el metodo abstracto
		print("Yo %s, Medico, atiendo a los jugadores del entrenamiento "%(self.getNombre()))

class PresidenteEquipo(PersonaEquipo):				# Se define la clase MedicoEquipo que es una PersonaEquipo

	def __init__(self,n):							# Metodo __init__ de la clase PresidenteEquipo
		super(PresidenteEquipo, self).__init__(n)	# Se heredan los atributo de PersonaEquipo
		self.numeroPropiedades=""					# Atributo de la clase

	def setNumeroPropiedades(self,num):				# Funcion que devuelve el valor del atributo de la clase
		self.numeroPropiedades=num

	def getNumeroPropiedades(self):					# Funcion que devuelve el valor del atributo de la clase		
		return self.numeroPropiedades

	def entrenar(self):								# Funcion que sobreescribe el metodo abstracto
		print("Yo %s, Presidente, Pongo dinero para el entrenamiento"%(self.getNombre()))

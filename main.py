#! /usr/bin/env python3
class Serie():
    titulo = ''
    genero = ''
    creador = ''
    temporadas = 3
    entregado = False
    def __init__(self, titulo, genero, creador, temporadas):
        self.titulo = titulo
        self.genero = genero
        self.creador = creador
        self.temporadas = temporadas

    # Defino los getters
    def get_titulo(self):
        return self.titulo
    def get_genero(self):
        return self.genero
    def get_creador(self):
        return self.creador
    def get_temporadas(self):
        return self.temporadas

    # Defino los setters
    def set_titulo(self, titulo):
        self.titulo = titulo
    def set_genero(self, genero):
        self.genero = genero
    def set_creador(self, creador):
        self.creador = creador
    def set_temporadas(self, temporadas):
        self.temporadas = temporadas

    # Reescribo el metodo __str__ para devolver el objeto como string
    def __str__(self):
        return 'Serie 📼 Titulo: '+self.titulo +' | Genero: '+self.genero+' | Creador: '+self.creador+' | Temporadas: '+ str(self.temporadas) + ' | Entregado: ' + str(self.entregado)

    def __gt__(self, serie):
        return self.temporadas > serie.temporadas
    def __lt__(self, serie):
        return self.temporadas < serie.temporadas
    def __eq__(self, serie):
        return self.temporadas == serie.temporadas
    def __ne__(self, serie):
        return self.temporadas != serie.temporadas

# Clase Videojuego (heredamos titulo y genero, renombramos creador a company)
class Videojuego(Serie):
    company = ''
    horas = 10 #default 10
    entregado = False
    def __init__(self, titulo, genero, company, horas):
        super().__init__(titulo, genero, company, horas)
        self.company = company
        self.horas = horas
    # Hereda getters
    def get_titulo(self):
        titulo = super().get_titulo()
        return titulo
    def get_genero(self):
        genero = super().get_genero()
        return genero
    def get_company(self):
        #company = get_creador()
        return company
    def get_horas(self):
        #horas = get_horas()
        return horas
    #hereda setters
    def set_titulo(self):
        titulo = super().set_titulo()
        self.titulo = titulo
    def set_genero(self):
        genero = super().set_genero()
        self.genero = genero
    def set_creador(self):
        creador = super().set_creador()
        self.creador = creador
    def set_horas(self):
        temporadas = super().set_temporadas()
        self.horas = temporadas
    def __str__(self):
        return 'Videojuego 💾 Titulo: '+self.titulo +' | Genero: '+self.genero+' | Compañia: '+self.company +' | Horas: '+ str(self.horas) + ' | Entregado: ' + str(self.entregado)

# Datos
s1 = Serie('Black Books', 'Sitcom', 'Dylan Moran', 3)
s2 = Serie('The IT Crowd', 'Sitcom', 'Graham Linehan', 4)
s3 = Serie('The Ofice', 'Sitcom', 'Greg Daniels', 9)
s4 = Serie('Breaking Bad', 'Drama', 'Vince Gilligan', 5)
s5 = Serie("The Wire", "Drama", "David Simon", 5)
v1 = Videojuego('Maniac Mansion', 'Aventura grafica', 'LucasArts', 10)
v2 = Videojuego('Monkey Island', 'Aventura grafica', 'LucasArts', 10)
v3 = Videojuego('Loom', 'Aventura grafica', 'LucasArts', 15)
v4 = Videojuego('Leisure Suite Larry', 'Aventura grafica', 'LucasArts', 15)
v5 = Videojuego('Day of Tentacle', 'Aventura grafica', 'LucasArts', 20)
series = [s1, s2, s3, s4, s5]
videojuegos = [v1, v2, v3, v4, v5]


# Parte 3. Interfaz entregable
class interfazEntregable():
    videojuegos = videojuegos
    items = series + videojuegos
    #items = series

    def listar_items(self):
        for item in self.items:
            print(item)

    def listar_series(self):
        for serie in series:
            print(serie)

    def listar_juegos(self):
        for juego in videojuegos:
            print(juego)

    def entregar(self, item):
        item.entregado = True

    def devolver(self, item):
        item.entregado = False

    def isEntregado(self, item):
        if (item.entregado == True):
            print(item.titulo + ': Entregado')
        elif (item.entregado == False):
            print(item.titulo + ': No entregado')

    def cuentaEntregados(self, tipo):
        if tipo == 'videojuegos':
            items = self.videojuegos
        elif tipo == 'series':
            items = self.series
        else:
            items = self.items
        cuenta = 0

        #print(tipo)
        print('==================================')
        print(str(tipo).upper() + ':')
        for item in items:
            if item.entregado == True:
                print(item)
                cuenta = cuenta+1
            else:
                pass
        print(str(cuenta) + ' entregados')
        print('----------------------------------')

    def compareTo(self, serie1, serie2):
        if (serie1.temporadas > serie2.temporadas):
            print(serie1.titulo + ' mayor duracion que ' + serie2.titulo)
        if (serie1.temporadas < serie2.temporadas):
            print(serie1.titulo + ' menos que ' + serie2.titulo)

    def itemsNumber(self):
        print(len(self.items))

interfaz = interfazEntregable()

#Entregamos algunos titulos
interfaz.entregar(s2)
interfaz.entregar(s4)
interfaz.entregar(v1)
interfaz.entregar(v2)

#interfaz.isEntregado(s1)
#interfaz.isEntregado(s2)
#interfaz.isEntregado(interfaz.items[1])
#interfaz.cuentaEntregados(all)
#interfaz.cuentaEntregados('series')
#interfaz.cuentaEntregados('videojuegos')

#Comparar
#interfaz.compareTo(series[1], videojuegos[2]) #Funciona!!



### Ejecutable
def ejecutable():
    while True:
        print('---------------------------------------------')
        print('Bienvenido al videoclub. ¿Que deseas hacer?')
        print('[1]:Listar series [2]:Listar videojuegos [3]:Entregar [4]:Listar entregados [5]:Listar los de mayor duracion [6]:Comparar')
        x = input()
        if int(x) == 1:
            interfaz.listar_series()
        if int(x) == 2:
            interfaz.listar_juegos()
        if int(x) == 3:
            print('Que quieres entregar?')
            y = input()
            interfaz.entregar(str(y))
            #print y.isEntregado()
            print(str(y) + ' entregado!')
        if int(x) == 4:
            print('[1]:Series [2]:Videojuegos [3]:Todos')
            z = input()
            if int(z) == 1:
                interfaz.cuentaEntregados('series')
            if int(z) == 2:
                interfaz.cuentaEntregados('videojuegos')
            if int(z) == 3:
                interfaz.cuentaEntregados(all)
            else:
                pass
        if int(x) == 5:
            pass

ejecutable()
import pygame
import os
class Cancion:
    def __init__(self, id:str, titulo:str, artista:str, duracion:int,genero:str, archivo_mp3:str):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion
        self.genero = genero
        self.archivo_mp3 = archivo_mp3
        
    def __str__(self):
        return (f"{self.id}) {self.titulo} - {self.artista} ({self.duracion}s) [{self.genero}] -> {self.archivo_mp3}")
    
    def reproducir (self):
        """Reproduce el archivo MP3 usando pygame"""
        try:
            if not os.path.exists(self.archivo_mp3):
                print(f"L Error: El archivo {self.archivo_mp3} no existe")
                return False
            
            pygame.mixer.init()
            pygame.mixer.music.load(self.archivo_mp3)
            pygame.mixer.music.play()
            self.reproduciendo = True
            return True
            
        except pygame.error as e:
            print(f"L Error al reproducir {self.titulo}: {e}")
            return False
        except Exception as e:
            print(f"L Error inesperado: {e}")
            return False
    
    def detener(self):
        """Detiene la reproducción"""
        pygame.mixer.music.stop()
        self.reproduciendo = False

class ListaReproduccion:
    def __init__ ( self, nombre:str):
        self.nombre=nombre
        self.canciones: List[int] = []
        
    def __str__(self):
        return f"Lista: {self.nombre} ({len(self.canciones)} canciones)"    
        
    def anadir_canciones(self, id_cancion:int):
        if id_cancion not in self.canciones:
            self.canciones.append(id_cancion)
            return True
        else:
            print("⚠️ La canción ya está en la lista.")
            return False

    def quitar_canciones(self, id_cancion:int):
        if id_cancion in self.canciones:
            self.canciones.remove(id_cancion)
            return True
        return False    
    
class PlataformaMusical:
    def __init__(self):
        self.canciones : list[Cancion] = []
        self.listas : list[ListaReproduccion] = []
        self.id_actual = 1
        
    def registrar_cancion(self, titulo:str, artista:str, duracion:int,genero:str, archivo:str):
        for song in self.canciones:
            if song.titulo.lower() == titulo.lower() and song.artista.lower() == artista.lower():
                print ("La canción ya está registrada :(")
                return False
            
        cancion_registrada = Cancion(self.id_actual,titulo,artista,duracion,genero,archivo)
        self.canciones.append(cancion_registrada)
        self.id_actual +=1
        return True
    
    def editar_cancion(self,id_cancion, titulo=None, artista=None, duracion=None, genero=None, archivo_mp3=None):
        for song in self.canciones:
            if song.id == id_cancion:
                if titulo:
                    song.titulo = titulo
                if artista:
                    song.artista = artista
                if duracion:
                    song.duracion = duracion
                if genero:
                    song.genero = genero
                if archivo_mp3:
                    song.archivo_mp3 = archivo_mp3
                return True
        return False
    
    def eliminar_cancion(self, id_e:int):
        for c in self.canciones:
            if c.id == id_e:
                self.canciones.remove(c)
                return True  
        return False 
    
    def listar_canciones(self):
        
        if not self.canciones:
            print("No hay canciones registradas :(")
            return
        print ('\n --- Lista de Canciones')
        for song in self.canciones:
            print (song)
        print(f"Total : {len(self.canciones)} canciones")
    
    def crear_lista(self,nombre):
        for lista in self.listas:
            if lista.nombre.lower() == nombre.lower():
                print("Ya existe esta playlist")
                return False
            
        nueva_lista = ListaReproduccion(nombre)
        self.listas.append(nueva_lista)
        return True
    
    def borrar_lista(self, nombre:str):
        for i, lista in enumerate(self.listas):
            if lista.nombre.lower() == nombre.lower():
                del self.listas[i]
                return True
        return False
    
    def obtener_lista(self, nombre:str):
        for lista in self.listas:
            if lista.nombre.lower() == nombre.lower():
                return lista
        return None
    
    def listar_listas(self):
        return self.listas
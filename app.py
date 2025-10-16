#!/usr/bin/env python3
"""Interfaz por consola para la PlataformaMusical (parte 1)."""
from musica.plataforma import PlataformaMusical, Cancion
import os
import pygame

#### Pedir int ####

def pedir_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, introduce un número entero válido.")

#### Gestionar canciones ####

def menu_canciones(plataforma):
    while True:
        print('\n--- Gestión de canciones ---')
        print('1) Añadir canción')
        print('2) Modificar canción')
        print('3) Eliminar canción')
        print('4) Listar canciones')
        print('0) Volver')
        opc = pedir_int('> ')
        if opc == 1:
            print("opcion1")
            anadir_cancion(plataforma)
        elif opc == 2:
            print("opcion2")
            modificar_cancion(plataforma)
        elif opc == 3:
            print("opcion3")
            eliminar_cancion(plataforma)
        elif opc == 4:
            listar_canciones(plataforma)
        elif opc == 0:
            print('Volviendo...')
            return
        else:
            print('Opción inválida') 

def anadir_cancion(plataforma):
    print('\n --- Añadir canción ---')
    titulo = input('Título: ')
    artista = input('Artista: ')
    duracion = int(input('Duración (segundos): '))
    genero = input('Género: ')
    
    print('\n Archivos disponibles en biblioteca:')
    biblioteca_path = "musica/biblioteca"
    if os.path.exists(biblioteca_path):
        archivos = os.listdir(biblioteca_path)
        for archivo in archivos:
            if archivo.endswith('.mp3'):
                print(f"  - {archivo}")

    archivo = input('Nombre del archivo MP3: ').strip()
    ruta_completa = os.path.join(biblioteca_path, archivo)
    
    if not os.path.exists(ruta_completa):
        print("❌ No se encontró el archivo especificado.")
        return
    
    registro = plataforma.registrar_cancion(titulo,artista,duracion,genero,ruta_completa)
    
    if registro:
        print("Canción añadida correctamente. :)")
    else:
        print("No se pudo añadir la canción. :(")
        
def modificar_cancion(plataforma):
    print('\n --- Modificar canción ---')
    print(' Canciones disponibles')
    
    for song in plataforma.canciones:
        print (f"{song.id}) {song.titulo} - {song.artista} ({song.duracion}s) ")
        
    id_seleccion = pedir_int("\nSelecciona número de la canción (0 para cancelar): ")        
    
    if id_seleccion == 0:
        return

    nuevo_titulo = input("Nuevo título (enter para dejar): ").strip() or None
    nuevo_artista = input("Nuevo artista (enter para dejar): ").strip() or None
    nueva_duracion = input("Nueva duración (enter para dejar): ").strip()
    nueva_duracion = int(nueva_duracion) if nueva_duracion else None
    nuevo_genero = input("Nuevo género (enter para dejar): ").strip() or None
    nueva_ruta = input("Nueva ruta MP3 (enter para dejar): ").strip() or None

    if plataforma.editar_cancion(id_seleccion, nuevo_titulo, nuevo_artista, nueva_duracion, nuevo_genero, nueva_ruta):
        print("Canción modificada correctamente.")
    else:
        print("No se encontró la canción.")

def eliminar_cancion(plataforma):
    print('\n --- Eliminar canción ---')
    print(' Canciones disponibles')
    
    for song in plataforma.canciones:
        print (f"{song.id}) {song.titulo} - {song.artista} ({song.duracion}s) ")
        
    id_seleccion = pedir_int("\nSelecciona número de la canción (0 para cancelar): ")        
    
    if id_seleccion == 0:
        return  
     
    if plataforma.eliminar_cancion(id_seleccion):
        print("Eliminada.")
    else:
        print("No se encontró la canción")

def listar_canciones(plataforma):
    
    if not plataforma.canciones:
        print("No hay canciones registradas :(")
        return
    print ('\n --- Lista de Canciones')
    for song in plataforma.canciones:
        print (song)
    print(f"Total : {len(plataforma.canciones)} canciones")
        
#### Gestionar listas ####

def menu_listas(plataforma):
    while True: 
        print('\n --- Gestión de listas ---')
        print('1) Crear lista')
        print('2) Eliminar lista')
        print('3) Ver contenido de lista')
        print('4) Añadir canciones a lista')
        print('5) Eliminar canción de lista')
        print('0) Volver')
        opc = pedir_int('> ')
        if opc == 1:
            crear_lista(plataforma)
        elif opc == 2:
            eliminar_lista(plataforma)
        elif opc == 3:
            mostrar_lista(plataforma)
        elif opc == 4:
            anadir_cancion_lista(plataforma)
        elif opc == 5:
            eliminar_cancion_lista(plataforma)
        elif opc == 0:
            print('Volviendo...')
            return
        else:
            print('Opción inválida') 

def crear_lista(plataforma):
    print('\n --- Crear lista ---')
    nombre = input("Nombre de la lista: ")
    
    if nombre:
        plataforma.crear_lista(nombre)
        print("Creada")
        
    else: print("El nombre no puede estar vacío")

def anadir_cancion_lista(plataforma):
    print('\n --- Añadir canciones a una lista ---')
    
    print('Listas disponibles:')
    if not plataforma.listas:
        print("No hay listas creadas, crea alguna lista e intentelo de nuevo")
        return
    
    for i, lista in enumerate(plataforma.listas, 1):
        print(f"{i}) {lista.nombre} ({len(lista.canciones)} canciones)")
    
    id_lista = pedir_int('Selecciona número de la lista (0 para cancelar): ')
    
    if id_lista == 0:
        return       
    
    # validar lista seleccionada
    if id_lista < 1 or id_lista > len(plataforma.listas):
        print("Número de lista inválido.")
        return
    
    #seleccionamos la lista que ha seleccionado el usuario         
    lista_seleccionada = plataforma.listas[id_lista-1]   
    
    print('Canciones disponibles para añadir:')
    if not plataforma.canciones:
        print ("No hay canciones registradas")
        return
    
    for song in plataforma.canciones:
        print(f"{song.id}) {song.titulo} - {song.artista}")
    
    id_seleccionado=pedir_int('Selecciona número de la canción a añadir (0 para cancelar): ') 
    if id_seleccionado == 0:
        return
    
    cancion_encontrada = None
    for cancion in plataforma.canciones:
        if cancion.id == id_seleccionado:
            cancion_encontrada = cancion
            break
    
    if cancion_encontrada:
        lista_seleccionada.anadir_canciones(id_seleccionado)
        if lista_seleccionada.anadir_canciones:
            print(f"Canción '{cancion_encontrada.titulo}' añadida a la lista '{lista_seleccionada.nombre}'")
        else:
            print(" No se encontró la canción.")

def mostrar_lista(plataforma):
    print('\n --- Ver contenido de una lista ---')
    listas = plataforma.listas
    print('Listas disponibles:')
    if not listas:
        print("No hay listas disponibles")
        return
    for i, lista in enumerate(listas, 1):
        print(f"{i}) {lista.nombre} ({len(lista.canciones)} canciones)")
    
    id_lista = pedir_int('Selecciona número de la lista (0 para cancelar): ')
    
    if id_lista == 0:
        return       
    
    # validar lista seleccionada
    if id_lista < 1 or id_lista > len(plataforma.listas):
        print("Número de lista inválido.")
        return
    
    #seleccionamos la lista que ha seleccionado el usuario         
    lista_seleccionada = plataforma.listas[id_lista-1]   
    
    # Mostrar canciones de la lista
    if not lista_seleccionada.canciones:
        print("Esta lista está vacía.")
    else:
        for id_cancion in lista_seleccionada.canciones:
            # Buscar la canción en todas las canciones de la plataforma
            for cancion in plataforma.canciones:
                if cancion.id == id_cancion:
                    print(f"{cancion.id}) {cancion.titulo} - {cancion.artista} ({cancion.duracion}s)")
                    break
                
def eliminar_lista(plataforma):
    print('\n --- Eliminar una lista ---')
    
    print('Listas disponibles:')
    if not plataforma.listas:
        print("No hay listas disponibles")
        return
    
    for i, lista in enumerate(plataforma.listas, 1):
        print(f"{i}) {lista.nombre} ({len(lista.canciones)} canciones)")
    
    id_lista = pedir_int('Selecciona número de la lista (0 para cancelar): ')
    
    if id_lista == 0:
        return       
    
    # validar lista seleccionada
    if id_lista < 1 or id_lista > len(plataforma.listas):
        print("Número de lista inválido.")
        return
    
    #seleccionamos la lista que ha seleccionado el usuario         
    lista_seleccionada = plataforma.listas[id_lista-1]
    nombre_lista = lista_seleccionada.nombre 
    
    lista_verificada = plataforma.obtener_lista(nombre_lista)
    if not lista_verificada:
        print("La lista no existe.")
        return
    plataforma.borrar_lista(nombre_lista)
    print("Eliminada")

def eliminar_cancion_lista(plataforma):
    print('\n --- Eliminar canción de una lista ---')
    
    print('Listas disponibles:')
    if not plataforma.listas:
        print("No hay listas disponibles")
        return
    for i, lista in enumerate(plataforma.listas, 1):
        print(f"{i}) {lista.nombre} ({len(lista.canciones)} canciones)")
    
    id_lista = pedir_int('Selecciona número de la lista (0 para cancelar): ')
    
    if id_lista == 0:
        return       
    
    # validar lista seleccionada
    if id_lista < 1 or id_lista > len(plataforma.listas):
        print("Número de lista inválido.")
        return
    
    #seleccionamos la lista que ha seleccionado el usuario         
    lista_canciones = plataforma.listas[id_lista-1]   
    
    print('Canciones disponibles para eliminar:')
    if not lista_canciones.canciones:
        print ("No hay canciones")
        return
    
    for song in plataforma.canciones:
        print(f"{song.id}) {song.titulo} - {song.artista}")
    
    id_seleccionado=pedir_int('Selecciona número de la canción a eliminar (0 para cancelar): ') 
    if id_seleccionado == 0:
        return
    
    # Eliminar canción de la lista
    if lista_canciones.quitar_canciones(id_seleccionado):
        print("Canción eliminada de la lista.")
    else:
        print("La canción no está en esta lista.")

#### menu reproduccion ####
def menu_reproduccion(plataforma):
    print('\n --- Reproducción ---')
    
    listas = plataforma.listas
    print('Listas disponibles:')
    if not listas:
        print("No hay listas disponibles")
        return
    
    for i, lista in enumerate(listas, 1):
        print(f"{i}) {lista.nombre} ({len(lista.canciones)} canciones)")
    print('0) Volver')
    
    id_lista = pedir_int('Selecciona lista: ')
    
    if id_lista == 0:
        return
    
    # validar lista seleccionada
    if id_lista < 1 or id_lista > len(listas):
        print("Número de lista inválido.")
        return
    
    lista_seleccionada = listas[id_lista-1]
    
    if not lista_seleccionada.canciones:
        print ("No hay canciones para reproducir")
        return
    
    indice_actual = 0
    cancion_actual = None
    
    while True:
        id_cancion_actual = lista_seleccionada.canciones[indice_actual]
        
        for cancion in plataforma.canciones:
            if cancion.id == id_cancion_actual:
                cancion_actual = cancion
                break
            
        if cancion_actual:
            print(f"Reproduciendo: {cancion_actual.titulo} - {cancion_actual.artista} ({cancion_actual.duracion})s")
            print("n) siguiente, p) Anterior, s) Salir reproducción")
            
            cancion_actual.reproducir()
            
            while True:
                opcion= input('>').strip().lower()
                
                if opcion == 'n':
                    indice_actual = (indice_actual + 1) % len(lista_seleccionada.canciones)
                    break
                elif opcion == 'p':
                    indice_actual = (indice_actual - 1) % len(lista_seleccionada.canciones)
                    break
                elif opcion == 's': 
                    pygame.mixer.quit()
                    return
        else:
            print("Error: Cancion no encontrada")
            break
                
#### Main ####
        
def main():
    plataforma = PlataformaMusical()
    while True:
        print('\n=== Plataforma Musical ===')
        print('1) Gestionar canciones')
        print('2) Gestionar listas')
        print('3) Reproducción')
        print('0) Salir')
        opc = pedir_int('> ')
        if opc == 1:
            print("opcion1")
            menu_canciones(plataforma)
        elif opc == 2:
            print("opcion2")
            menu_listas(plataforma)
        elif opc == 3:
            print("opcion3")
            menu_reproduccion(plataforma)
        elif opc == 0:
            print('Hasta luego')
            break
        else:
            print('Opción inválida')

if __name__ == '__main__':
    main()


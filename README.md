# INFORMÁTICA 2
# Trabajo Final

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de una aplicación en Python que permite gestionar una biblioteca de música. La aplicación permite al usuario dar de alta canciones, organizarlas en listas de reproducción, editarlas o eliminarlas, y finalmente reproducir las listas creadas.

##  Funcionalidades Principales

### Gestión de Canciones
- **Añadir canciones**: Registrar nuevas canciones con información completa (título, artista, duración, género, archivo MP3)
- **Modificar canciones**: Editar los datos de canciones existentes
- **Eliminar canciones**: Quitar canciones de la biblioteca
- **Listar canciones**: Visualizar todas las canciones registradas

### Gestión de Listas de Reproducción
- **Crear listas**: Crear nuevas listas de reproducción con nombre personalizado
- **Eliminar listas**: Borrar listas de reproducción existentes
- **Añadir canciones a listas**: Agregar canciones específicas a las listas
- **Eliminar canciones de listas**: Quitar canciones específicas de las listas
- **Ver contenido de listas**: Mostrar todas las canciones contenidas en una lista

### Sistema de Reproducción
- **Reproducir listas**: Ejecutar listas de reproducción completas
- **Navegación entre canciones**: Moverse entre anterior y siguiente canción
- **Control de reproducción**: Pausar, reanudar y detener la reproducción
  
##  Tecnologías Utilizadas

- **Python 3**: Lenguaje de programación principal, usando programación orientada a objetos
- **Pygame**: Librería para reproducción de audio MP3

## Instalación y Configuración

1. **Clonar o descargar** el proyecto
2. **Instalar dependencias**:
   ```bash
   pip install pygame

3. **Crear carpetas/**
    ```bash

    ├── app.py
    ├── musica/
    │   ├── __init__.py
    │   ├── plataforma.py
    │   └── biblioteca/
    │       ├── cancion1.mp3
    │       ├── cancion2.mp3
    │       └── ...

4. **Ejecutar la aplicación:**
    ```bash
    python3 app.py

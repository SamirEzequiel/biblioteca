from django.db import models

"""
Este módulo define los modelos principales de la aplicación de biblioteca.
Contiene las clases Editor, Autor y Libro que representan las entidades principales del sistema.
"""

class Editor(models.Model):
    """
    Modelo que representa a una editorial de libros.
    Almacena información básica de contacto y ubicación de la editorial.
    """
    nombre = models.CharField(max_length=30, help_text="Nombre de la editorial")
    direccion = models.CharField(max_length=50, help_text="Dirección física de la editorial")
    ciudad = models.CharField(max_length=60, help_text="Ciudad donde se encuentra la editorial")
    estado = models.CharField(max_length=30, help_text="Estado o provincia")
    pais = models.CharField(max_length=30, help_text="País de origen")
    website = models.URLField(help_text="Sitio web oficial de la editorial")

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Editores"

    def __str__(self):
        return f"{self.nombre}"

class Autor(models.Model):
    """
    Modelo que representa a un autor de libros.
    Almacena información personal y de contacto del autor.
    """
    nombre = models.CharField(max_length=30, help_text="Nombre del autor")
    apellidos = models.CharField(max_length=40, help_text="Apellidos del autor")
    email = models.EmailField('Email', blank=True, help_text="Correo electrónico de contacto")

    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Libro(models.Model):
    """
    Modelo que representa un libro en la biblioteca.
    Contiene información detallada del libro y sus relaciones con autores y editores.
    """
    titulo = models.CharField(max_length=100, help_text="Título del libro")
    autores = models.ManyToManyField(Autor, help_text="Autores del libro")
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE, help_text="Editorial que publicó el libro")
    fecha_publicacion = models.DateField(blank=True, null=True, help_text="Fecha de publicación del libro")
    portada = models.ImageField(upload_to="portadas", null=True, help_text="Imagen de la portada del libro")
    precio = models.DecimalField(max_digits=12, decimal_places=2, null=True, help_text="Precio del libro")

    class Meta:
        ordering = ["titulo"]
        verbose_name_plural = "Libros"

    def __str__(self):
        return self.titulo

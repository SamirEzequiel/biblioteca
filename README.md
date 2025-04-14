# 📚 Biblioteca Digital

¡Bienvenido a nuestro Sistema de Biblioteca Digital! Esta aplicación te permite gestionar tu biblioteca de manera fácil y eficiente, desarrollada con Django para brindarte la mejor experiencia.

## 🚀 ¿Qué necesitas para empezar?

- Python 3.8 o más reciente
- pip instalado en tu sistema
- Git para clonar el repositorio

## 📥 Guía de Instalación Rápida

### 1️⃣ Obtén el código
```bash
git clone <URL_del_repositorio>
cd biblioteca
```

### 2️⃣ Prepara tu entorno
Si usas Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Si usas Linux o macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instala todo lo necesario
```bash
pip install -r requirements.txt
```

### 4️⃣ Configura la base de datos
```bash
python manage.py migrate
```

### 5️⃣ Crea tu usuario administrador
```bash
python manage.py createsuperuser
```

### 6️⃣ ¡Pon todo en marcha!
```bash
python manage.py runserver
```

¡Listo! 🎉 Ahora puedes acceder a:
- Aplicación principal: http://127.0.0.1:8000/
- Panel de administración: http://127.0.0.1:8000/admin

## 🛠️ Herramientas que usamos

- Django 4.2.7 - El framework web que hace la magia
- Django REST Framework 3.14.0 - Para nuestra potente API
- Django Filter 23.3 - Búsquedas y filtrados avanzados
- Pillow 10.1.0 - Manejo de imágenes

## 📁 ¿Cómo está organizado?

El proyecto está estructurado de manera simple y clara:
- `Biblioteca/` - El corazón del proyecto
- `libros/` - Donde gestionamos todos los libros
- `manage.py` - El centro de control de Django
- `requirements.txt` - Lista de todo lo que necesitas instalar

## 💡 Consejos importantes

- Siempre usa un entorno virtual para mantener tu proyecto aislado y limpio
- Asegúrate de tener todo instalado antes de iniciar
- Si agregas nuevas dependencias, no olvides actualizar el requirements.txt

¿Tienes dudas? ¡No dudes en abrir un issue en el repositorio! 🤝

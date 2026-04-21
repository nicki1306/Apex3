# 🚗 Apex - Sistema de Gestión de Flota

Una aplicación Full-Stack desarrollada para la administración y control de vehículos. Este proyecto demuestra la implementación de una arquitectura web moderna, separando el cliente de la API RESTful, y gestionando la persistencia de datos en una base de datos relacional.

## 🛠️ Stack Tecnológico

**Frontend:**
* **Angular:** Construido utilizando la nueva arquitectura de Componentes Standalone.
* **TypeScript:** Para un tipado estricto y código más seguro.
* **HTML5 & LESS:** Para el maquetado y estilos.
* **HttpClient & FormsModule:** Para el consumo de la API y el manejo reactivo de formularios.

**Backend:**
* **Python:** Lenguaje principal de la lógica de servidor.
* **FastAPI:** Framework de alto rendimiento para la creación de la API REST.
* **SQLAlchemy:** ORM utilizado para interactuar con la base de datos de forma programática.
* **Uvicorn:** Servidor ASGI para la ejecución rápida y asíncrona.

**Base de Datos:**
* **PostgreSQL:** Motor de base de datos relacional para almacenamiento persistente.

## ⚙️ Características (Features)

* **Arquitectura Basada en Componentes:** Aplicación del principio de Responsabilidad Única mediante componentes modulares (`vehicle-list` y `vehicle-form`).
* **Operaciones CRUD:**
  * **Create:** Carga de nuevos vehículos (Marca, Modelo, Patente) desde la interfaz de usuario.
  * **Read:** Consumo y renderizado en tiempo real de los datos almacenados en PostgreSQL.
  * **Delete:** Eliminación de registros con actualización dinámica del DOM sin recargar la página.
* **API Documentada:** Documentación automática e interactiva provista de forma nativa por FastAPI mediante Swagger UI (disponible en `/docs`).
* **CORS Configurado:** Middleware habilitado para permitir la comunicación fluida y segura entre los puertos de desarrollo del cliente y el servidor.

## 🚀 Cómo ejecutar el proyecto localmente

### 1. Levantar el Backend (FastAPI)
Abrir una terminal en el directorio del backend y ejecutar:
```bash
cd backend
# Activar el entorno virtual (venv)
uvicorn main:app --reload

La API estará escuchando en http://localhost:8000

2. Levantar el Frontend (Angular)
Abrir una segunda terminal en el directorio del frontend y ejecutar:
cd apex-frontend
# Instalar dependencias si es la primera vez
npm install
# Compilar y abrir el servidor de desarrollo
ng serve -o
La aplicación web se abrirá automáticamente en http://localhost:4200

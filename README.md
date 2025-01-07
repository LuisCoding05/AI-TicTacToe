# Proyecto de 3 en raya con IA

## Prerrequisitos

### Etapa 1: Configuración del servidor  
Asegúrate de que el servidor Flask esté habilitado,  
junto con su intérprete de Python y el servicio MySQL.  

> **ℹ️ Info:** Flask es un microframework para Python. Si aún no lo has instalado, puedes hacerlo con el siguiente comando:  
> ```bash
> pip install Flask
> ```  
> Asegúrate de que MySQL esté en ejecución.

---

### Etapa 2: Configuración de la base de datos  
En la carpeta `database`, encontrarás un archivo `.sql`.    

> **ℹ️ Info:** Puedes importar archivos `.sql` utilizando la herramienta que tu tengas o la línea de comandos de MySQL.  
> Ejemplo para la línea de comandos:  
> ```bash
> mysql -u nombre_usuario -p nombre_base_de_datos < ruta/al/archivo.sql
> ```

---

### Etapa 3: Configuración de la conexión a la base de datos  
Abre el archivo `config.py` y asegúrate de que la configuración de conexión coincida con tu entorno.  

> **ℹ️ Info:** Actualiza los siguientes valores en `config.py`:
> - **Host:** El nombre del host (generalmente `localhost` para desarrollo local).
> - **Nombre de usuario y contraseña:** Tus credenciales de MySQL.
> - **Nombre de la base de datos:** El nombre de la base de datos que importaste anteriormente.(La mia la llamé pythonflask)
> - **¡¡¡IMPORTANTE!!!** Todas o casi todas las contraseñas cifradas del backup son: "1234", si quieres cambiarlas puedes usar el passGenerator.py y asignar la que desees

---

### Etapa 4: Instalación de dependencias  
Instala las dependencias necesarias para el proyecto utilizando el archivo `requirements.txt`.  

> **ℹ️ Info:** Puedes instalar las dependencias con el siguiente comando:  
> ```bash
> pip install -r requirements.txt
> ```

---

### Etapa 5: Detalles extra
> **ℹ️ Info:** En routes tienes las configuraciones del servidor para las distintas rutas y la mayoría de funciones que hacen que funcione el proyecto.

> **ℹ️ Info:** En el archivo passGenerator.py puedes crear contraseñas cifradas y comparar contraseñas para ver si coinciden.

> **ℹ️ Info:** En el archivo models.py tienes los modelos de la base de datos transformados en objetos.

> **ℹ️ Info:** En el archivo IA_algorithm.py tienes el algoritmo de la IA.

> **ℹ️ Info:** En el archivo config.py creamos la conexión con la base de datos.

> **ℹ️ Info:** En el archivo app.py enlazamos las conexiones con la aplicación.
---

## Nota Final  
¡Eso es todo! Todo debería funcionar sin problemas, pero avísame si encuentras algún error o problema. 😊
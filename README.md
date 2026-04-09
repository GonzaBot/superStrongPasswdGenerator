**Password Fortress**
 
 ![Python](https://img.shields.io/badge/Python-3.12-blue)

**Password Fortress** es una herramienta de escritorio diseñada para combatir uno de los eslabones más débiles de la cadena de seguridad: las contraseñas predecibles. No solo genera claves, sino que audita la seguridad de las existentes y aplica técnicas de inyección de entropía.

---

## 🚀 Funcionalidades
* **Generación Criptográficamente Segura:** Utiliza el módulo `secrets` de Python (basado en fuentes de aleatoriedad del sistema operativo) para garantizar que las claves no sigan patrones predecibles.
* **Analizador de Fuerza Reala:** Evalúa la combinación de caracteres (mayúsculas, minúsculas, números y símbolos) para calcular el tiempo estimado de crackeo mediante fuerza bruta.
* **Motor de Fortalecimiento:** Permite al usuario ingresar una base "memorable" y el script la expande con sufijos aleatorios de alta complejidad.
* **Interfaz Gráfica (GUI):** Desarrollada íntegramente en Tkinter con un enfoque de "Modo Oscuro" para una mejor experiencia de usuario.

## 🛠️ Instalación y Uso

### Requisitos
* Python 3.10 o superior.
* Sistema operativo con soporte de interfaz gráfica (Windows, macOS o Linux con X11/Wayland).

### Cómo ejecutar
1.  Descarga el archivo `main.py`.
2.  Abre una terminal y dirígete al directorio donde se encuentra el archivo.
3.  Ejecuta la aplicación:
    ```bash
    python main.py
    ```

## 🛡️ Conceptos de Ciberseguridad Aplicados
En este proyecto del Día 1, se aplicaron los siguientes principios:
1.  **Entropía de Información:** Cuánta incertidumbre hay en una contraseña. A mayor entropía, mayor resistencia a ataques de diccionario.
2.  **Uso de `secrets` vs `random`:** En ciberseguridad, la aleatoriedad estándar (como `random.py`) es pseudo-aleatoria y predecible. Aquí se utilizó `secrets` para cumplir con estándares de seguridad industrial.
3.  **Auditoría de Fuerza Bruta:** Cálculo basado en la potencia de cómputo de GPUs masivas modernas ($10^{12}$ intentos por segundo).

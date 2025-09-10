# 📊 Generador de Números Pseudoaleatorios con Pruebas Estadísticas

Este proyecto implementa un **sistema generador de números pseudoaleatorios** con interfaz gráfica (**GUI en Tkinter**), que permite generar secuencias mediante diferentes algoritmos clásicos y aplicar pruebas estadísticas para evaluar su validez.  

Incluye los siguientes **algoritmos de generación**:

- ✅ **Cuadrados Medios** (*Middle Square Method*)  
- ✅ **Multiplicación de Semillas** (*Product of Seeds Method*)  
- ✅ **Multiplicador Constante con Semilla Fija** (*Constant Multiplier Method*)  

Y las siguientes **pruebas estadísticas**:  

- 📌 **Prueba de Uniformidad (Chi²)**  
- 📌 **Prueba de Medias**  
- 📌 **Prueba de Varianza**  

El programa muestra los resultados en **tablas detalladas** y genera **histogramas de distribución**.  

---

## 📂 Estructura de Carpetas

El proyecto se organiza de la siguiente forma:  

proyecto-pseudoaleatorios/
│
├── src/
│ ├── main.py # Archivo principal: GUI y ejecución
│ ├── generadores.py # Algoritmos de generación de números
│ ├── pruebas.py # Funciones de pruebas estadísticas
│ ├── utils.py # Funciones auxiliares (ej. exportar CSV)
│
├── data/
│ └── resultados/ # Carpeta donde se guardarán las exportaciones CSV
│
├── README.md # Documentación del proyecto
└── requirements.txt # Dependencias del proyecto



---

## ⚙️ Dependencias

El programa está desarrollado en **Python 3.8+** y requiere las siguientes librerías:  

```bash
pip install matplotlib scipy


Dependencias principales:

Tkinter → Interfaz gráfica (incluido en la instalación estándar de Python).

Matplotlib → Gráficas e histogramas.

SciPy → Cálculos estadísticos (Chi², límites de pruebas).

CSV (módulo estándar) → Exportación de resultados.

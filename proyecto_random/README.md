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

```
proyecto-pseudoaleatorios/
│
├── src/
│   ├── main.py                # Archivo principal: GUI y ejecución
│   ├── generadores.py         # Algoritmos de generación de números
│   ├── pruebas.py             # Funciones de pruebas estadísticas
│   ├── utils.py               # Funciones auxiliares (ej. exportar CSV)
│
├── data/
│   └── resultados/            # Carpeta donde se guardarán las exportaciones CSV
│
├── README.md                  # Documentación del proyecto
└── requirements.txt           # Dependencias del proyecto
```

---

## ⚙️ Dependencias

El programa está desarrollado en **Python 3.8+** y requiere las siguientes librerías:  

```bash
pip install matplotlib scipy
```

Dependencias principales:

- **Tkinter** → Interfaz gráfica (incluido en la instalación estándar de Python).  
- **Matplotlib** → Gráficas e histogramas.  
- **SciPy** → Cálculos estadísticos (Chi², límites de pruebas).  
- **CSV** (módulo estándar) → Exportación de resultados.  

---

## ▶️ Ejecución del Programa

1. Clonar el repositorio o descargar el proyecto:  

   ```bash
   git clone https://github.com/Argos71/Calculadora-de-Numeros-Pseudoaleatorios-y-Pruebas.git
   cd proyecto_random
   ```

2. Instalar las dependencias:  

   ```bash
   pip install -r ../requirements.txt
   ```

3. Ejecutar el programa desde `main.py`:  

   ```bash
   python main.py
   ```

---

## 🖥️ Funcionamiento del Programa

### 1. Selección de Algoritmo
Desde la interfaz gráfica, el usuario puede elegir entre:  
- **Cuadrados Medios**: Se eleva al cuadrado la semilla y se toman los dígitos centrales.  
- **Multiplicación de Semillas**: Dos semillas iniciales se multiplican y se extraen los dígitos centrales.  
- **Multiplicador Constante**: Una semilla fija se multiplica iterativamente con otra semilla cambiante, extrayendo los dígitos centrales en cada paso.  

### 2. Generación de Números
- Se introducen las semillas y la cantidad de números a generar.  
- Se muestran en una **tabla interactiva** con índice y valor.  
- Opcional: Se exportan los resultados en **CSV**.  

### 3. Pruebas Estadísticas
El usuario selecciona qué prueba aplicar:  

#### 🔹 **Prueba de Uniformidad (Chi²)**
Divide los números generados en intervalos y compara la **frecuencia observada** vs la **frecuencia esperada**.  
- Tabla con intervalos, frecuencias, diferencia cuadrática y suma total.  
- Determina si la distribución es uniforme.  

#### 🔹 **Prueba de Medias**
Evalúa si la media de los números está dentro del rango esperado:  

\[
LI = \frac{1}{2} - Z_{\alpha/2}\left(\frac{1}{\sqrt{12n}}\right)
\]  
\[
LS = \frac{1}{2} + Z_{\alpha/2}\left(\frac{1}{\sqrt{12n}}\right)
\]  

Donde:  
- \( n \) = cantidad de números generados.  
- \( Z_{\alpha/2} \) = valor crítico (1.96 para 95%).  

La tabla muestra: media obtenida, límite inferior, límite superior y resultado (si cumple o no).  

#### 🔹 **Prueba de Varianza**
Evalúa si la varianza de la secuencia cae dentro de los límites esperados:  

\[
LI = \frac{X^2_{1-\alpha/2,n-1}}{12(n-1)}
\]  
\[
LS = \frac{X^2_{\alpha/2,n-1}}{12(n-1)}
\]  

La tabla muestra: varianza obtenida, límites y decisión.  

### 4. Histogramas
Para cada secuencia generada, el programa dibuja un **histograma de distribución** en Matplotlib.  

---

## 📋 Ejemplo de Uso

1. Ingresar semilla **1234**, cantidad de números **20**, seleccionar **Cuadrados Medios**.  
2. Se genera una tabla:  

| Índice | Número Aleatorio |
|--------|------------------|
| 1      | 0.4356           |
| 2      | 0.8765           |
| …      | …                |

3. Seleccionar **Prueba de Uniformidad** → Se muestra tabla de frecuencias:  

| Intervalo | F. Observada | F. Esperada | Dif² |
|-----------|--------------|-------------|------|
| 0.0-0.1   | 3            | 2.0         | 0.5  |
| 0.1-0.2   | 1            | 2.0         | 0.5  |
| …         | …            | …           | …    |

4. Se genera el **histograma** automáticamente.  

---

## 📌 Consideraciones

- El algoritmo de **Multiplicador Constante** mantiene la **primera semilla fija** y va multiplicando sucesivamente por el resultado obtenido, extrayendo siempre los **dígitos centrales**.  
- Se recomienda usar semillas de al menos 4 dígitos para evitar ciclos cortos.  
- El número de intervalos en la prueba de Chi² puede ajustarse en la interfaz.  

---

## Bitácora

📓 Bitácora del Proyecto

Clase 1 - 13/08/2025: Presentación de la materia y explicación de los objetivos del proyecto de generadores pseudoaleatorios.

Clase 2 - 20/08/2025: Desarrollo de los algoritmos de cuadrados medios y productos medios.

Clase 3 - 27/08/2025: Desarrollo del algoritmo de multiplicador constante y aplicación de las pruebas de medias y pruebas de varianza.

Clase 4 - 03/09/2025: Ejecución de pruebas de uniformidad para validar la distribución de los números generados.


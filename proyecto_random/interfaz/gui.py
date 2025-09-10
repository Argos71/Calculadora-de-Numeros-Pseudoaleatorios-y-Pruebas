import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import matplotlib.pyplot as plt
import csv
import math
from scipy.stats import chi2

# ---------------- GENERADORES ----------------
def cuadrados_medios(semilla, n, digitos=4):
    numeros = []
    x = semilla
    for _ in range(n):
        x2 = x*x
        x2_str = str(x2).zfill(digitos*2)
        start = (len(x2_str)-digitos)//2
        centro = int(x2_str[start:start+digitos])
        numeros.append(round(centro/(10**digitos),4))
        x = centro
    return numeros

def multiplicador_constante(semilla_fija, semilla_variable, n, digitos=4):
    """
    Multiplicador constante usando la misma lógica de dígitos centrales
    que el cuadrado medio.
    """
    numeros = []
    x = semilla_variable
    for _ in range(n):
        mult = semilla_fija * x
        mult_str = str(mult).zfill(digitos*2)
        start = (len(mult_str)-digitos)//2
        centro = int(mult_str[start:start+digitos])
        u = round(centro/(10**digitos),4)
        numeros.append(u)
        x = centro
    return numeros

def multiplicacion_semillas(x0, y0, n):
    numeros = []
    x = x0
    y = y0
    for _ in range(n):
        z = (x*y) % 10000
        numeros.append(round(z/10000,4))
        x = z
    return numeros

# ---------------- PRUEBAS ----------------
def prueba_medias(numeros, confianza=0.95):
    n = len(numeros)
    media = sum(numeros)/n
    z = 1.96
    std_error = 1 / math.sqrt(12*n)
    li = round(0.5 - z*std_error,4)
    ls = round(0.5 + z*std_error,4)
    resultado = "Aceptado" if li <= media <= ls else "Rechazado"
    tabla = [{"nombre":"Media","valor":round(media,4),"limite_inferior":li,"limite_superior":ls,"diferencia":round(media-0.5,4),"resultado":resultado}]
    return {"valor":media,"resultado":resultado,"tabla":tabla}

def prueba_varianza(numeros, confianza=0.95):
    n = len(numeros)
    media = sum(numeros)/n
    varianza = sum((x-media)**2 for x in numeros)/n
    alfa = 1-confianza
    chi2_inf = chi2.ppf(alfa/2,df=n-1)
    chi2_sup = chi2.ppf(1-alfa/2,df=n-1)
    li = round((n-1)*varianza/chi2_sup,4)
    ls = round((n-1)*varianza/chi2_inf,4)
    resultado = "Aceptado" if li <= varianza <= ls else "Rechazado"
    tabla = [{"nombre":"Varianza","valor":round(varianza,4),"limite_inferior":li,"limite_superior":ls,"diferencia":round(varianza-1/12,4),"resultado":resultado}]
    return {"valor":varianza,"resultado":resultado,"tabla":tabla}

def prueba_uniformidad(numeros,k=10):
    n = len(numeros)
    intervalos = [0]*k
    for x in numeros:
        idx = min(int(x*k),k-1)
        intervalos[idx] +=1
    freq_esp = n/k
    chi2_val = sum((f-freq_esp)**2/freq_esp for f in intervalos)
    resultado = "Aceptado" if chi2_val<16.92 else "Rechazado"
    tabla = []
    for i in range(k):
        li = i/k
        ls = (i+1)/k
        tabla.append({"intervalo":f"[{li:.2f}-{ls:.2f})","frecuencia_observada":intervalos[i],"frecuencia_esperada":freq_esp,"diferencia_cuadratica":(intervalos[i]-freq_esp)**2})
    return {"chi2":chi2_val,"resultado":resultado,"tabla":tabla}

# ---------------- GUI ----------------
class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Generador y Pruebas de Números Pseudoaleatorios")
        self.geometry("1000x600")
        self.numeros=[]
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)
        self._crear_frame_generadores()
        self._crear_frame_pruebas()
        self._crear_frame_tabla()
        self._crear_frame_resultados()

    # ---------- FRAMES ----------
    def _crear_frame_generadores(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Generadores")
        ttk.Label(frame,text="Semilla 1 (X0):").grid(row=0,column=0,padx=5,pady=5)
        self.semilla_entry=ttk.Entry(frame)
        self.semilla_entry.grid(row=0,column=1,padx=5,pady=5)
        ttk.Label(frame,text="Semilla 2 (Y0 / Segunda semilla):").grid(row=1,column=0,padx=5,pady=5)
        self.segunda_semilla_entry=ttk.Entry(frame)
        self.segunda_semilla_entry.grid(row=1,column=1,padx=5,pady=5)
        ttk.Label(frame,text="Cantidad de números (n):").grid(row=2,column=0,padx=5,pady=5)
        self.n_entry=ttk.Entry(frame)
        self.n_entry.grid(row=2,column=1,padx=5,pady=5)
        ttk.Button(frame,text="Generar Cuadrados Medios",command=self.generar_cuadrados).grid(row=3,column=0,columnspan=2,pady=5)
        ttk.Button(frame,text="Generar Multiplicador Constante",command=self.generar_multiplicador).grid(row=4,column=0,columnspan=2,pady=5)
        ttk.Button(frame,text="Generar Multiplicación Semillas",command=self.generar_multiplicacion_semillas).grid(row=5,column=0,columnspan=2,pady=5)
        ttk.Button(frame,text="Exportar Tabla a CSV",command=self.exportar_csv).grid(row=6,column=0,columnspan=2,pady=5)

    def _crear_frame_pruebas(self):
        frame=ttk.Frame(self.notebook)
        self.notebook.add(frame,text="Pruebas")
        ttk.Label(frame,text="k (intervalos Chi²):").pack(pady=5)
        self.k_entry=ttk.Entry(frame)
        self.k_entry.insert(0,"10")
        self.k_entry.pack(pady=5)
        self.var_medias=tk.BooleanVar(value=True)
        self.var_varianza=tk.BooleanVar(value=True)
        self.var_uniformidad=tk.BooleanVar(value=True)
        ttk.Checkbutton(frame,text="Prueba de Medias",variable=self.var_medias).pack(pady=2)
        ttk.Checkbutton(frame,text="Prueba de Varianza",variable=self.var_varianza).pack(pady=2)
        ttk.Checkbutton(frame,text="Prueba de Uniformidad",variable=self.var_uniformidad).pack(pady=2)
        ttk.Button(frame,text="Realizar Pruebas Seleccionadas",command=self.realizar_pruebas_seleccionadas).pack(pady=10)

    def _crear_frame_tabla(self):
        frame=ttk.Frame(self.notebook)
        self.notebook.add(frame,text="Tabla de Números")
        self.tree=ttk.Treeview(frame,columns=("i","u"),show="headings")
        self.tree.heading("i",text="Índice")
        self.tree.heading("u",text="Número Aleatorio")
        self.tree.pack(fill="both",expand=True)

    def _crear_frame_resultados(self):
        frame=ttk.Frame(self.notebook)
        self.notebook.add(frame,text="Resultados Pruebas")
        self.tree_pruebas=ttk.Treeview(frame,columns=("prueba","valor","resultado"),show="headings")
        self.tree_pruebas.heading("prueba",text="Prueba")
        self.tree_pruebas.heading("valor",text="Valor / Detalle")
        self.tree_pruebas.heading("resultado",text="Resultado")
        self.tree_pruebas.pack(fill="both",expand=True)

    # ---------- GENERADORES ----------
    def generar_cuadrados(self):
        try:
            semilla=int(self.semilla_entry.get())
            n=int(self.n_entry.get())
            self.numeros=cuadrados_medios(semilla,n)
            self.llenar_tabla()
            self.mostrar_histograma("Cuadrados Medios")
        except Exception as e:
            messagebox.showerror("Error",str(e))

    def generar_multiplicador(self):
        try:
            semilla_fija=int(self.semilla_entry.get())
            semilla_variable=int(self.segunda_semilla_entry.get())
            n=int(self.n_entry.get())
            self.numeros=multiplicador_constante(semilla_fija,semilla_variable,n)
            self.llenar_tabla()
            self.mostrar_histograma("Multiplicador Constante")
        except Exception as e:
            messagebox.showerror("Error",str(e))

    def generar_multiplicacion_semillas(self):
        try:
            x0=int(self.semilla_entry.get())
            y0=int(self.segunda_semilla_entry.get())
            n=int(self.n_entry.get())
            self.numeros=multiplicacion_semillas(x0,y0,n)
            self.llenar_tabla()
            self.mostrar_histograma("Multiplicación Semillas")
        except Exception as e:
            messagebox.showerror("Error",str(e))

    # ---------- TABLA ----------
    def llenar_tabla(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for idx,val in enumerate(self.numeros,start=1):
            self.tree.insert("", "end", values=(idx,val))

    def exportar_csv(self):
        if not self.numeros:
            return messagebox.showwarning("Atención","Primero genere números.")
        file=filedialog.asksaveasfilename(defaultextension=".csv",filetypes=[("CSV files","*.csv")])
        if file:
            with open(file,"w",newline="") as f:
                writer=csv.writer(f)
                writer.writerow(["Índice","Número Aleatorio"])
                for idx,val in enumerate(self.numeros,start=1):
                    writer.writerow([idx,val])
            messagebox.showinfo("Éxito",f"Tabla exportada a {file}")

    # ---------- PRUEBAS ----------
    def realizar_pruebas_seleccionadas(self):
        if not self.numeros:
            return messagebox.showwarning("Atención","Primero genere números.")
        for i in self.tree_pruebas.get_children():
            self.tree_pruebas.delete(i)
        k=int(self.k_entry.get())
        # Medias
        if self.var_medias.get():
            res=prueba_medias(self.numeros)
            self.tree_pruebas.insert("", "end", values=("Media",f"{res['valor']:.4f}",res['tabla'][0]['resultado']))
            det=res['tabla'][0]
            self.tree_pruebas.insert("", "end", values=(f"  Límites: {det['limite_inferior']}-{det['limite_superior']}, Dif={det['diferencia']:.4f}","",""))
        # Varianza
        if self.var_varianza.get():
            res=prueba_varianza(self.numeros)
            self.tree_pruebas.insert("", "end", values=("Varianza",f"{res['valor']:.4f}",res['tabla'][0]['resultado']))
            det=res['tabla'][0]
            self.tree_pruebas.insert("", "end", values=(f"  Límites: {det['limite_inferior']}-{det['limite_superior']}, Dif={det['diferencia']:.4f}","",""))
        # Uniformidad
        if self.var_uniformidad.get():
            res=prueba_uniformidad(self.numeros,k=k)
            self.tree_pruebas.insert("", "end", values=("Uniformidad (Chi²)",f"{res['chi2']:.4f}",res['resultado']))
            for fila in res['tabla']:
                self.tree_pruebas.insert("", "end", values=(f"  {fila['intervalo']}",f"{fila['frecuencia_observada']}/{fila['frecuencia_esperada']:.2f}",f"Dif²={fila['diferencia_cuadratica']:.2f}"))

    # ---------- HISTOGRAMA ----------
    def mostrar_histograma(self,titulo):
        plt.hist(self.numeros,bins=10,edgecolor="black")
        plt.title(f"Histograma - {titulo}")
        plt.xlabel("Intervalos")
        plt.ylabel("Frecuencia")
        plt.show()

if __name__=="__main__":
    app=Aplicacion()
    app.mainloop()

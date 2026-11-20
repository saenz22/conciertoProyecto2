# Ubicador de concierto — Proyecto 2, Análisis y Diseño de Algoritmos (2026-2)

Entrega y sustentación: **7 de diciembre de 2026**.
Este README explica de qué trata el proyecto, qué hay en esta carpeta y qué le toca a cada quien. Léanlo completo antes de tocar código.

---

## 1. De qué trata el proyecto

Benito-Bad dará un concierto en el Valle del Cauca. El departamento se modela como un cuadrado de N×N km con ciudades en coordenadas enteras. Hay que escoger **en qué punto entero (x, y)** queda el concierto, bajo estas reglas:

- La distancia entre puntos es **Manhattan**: `|x − xᵢ| + |y − yᵢ|`.
- El concierto **no puede quedar sobre una ciudad**.
- El concierto **no puede favorecer** a una ciudad sobre otra. El enunciado no define "favorecer": **lo definimos nosotros** y lo justificamos (es el corazón del informe y de la sustentación).

### Lo más importante: qué se entrega y qué NO

El programa **no resuelve el problema**. Es un **generador de código**: lee la entrada y produce texto con un **modelo MiniZinc** que el usuario copia y ejecuta aparte. El enunciado prohíbe expresamente mostrar el resultado dentro de la aplicación.

| Entregable | Qué es |
|---|---|
| Informe PDF (formato IEEE) | Modelo formal, explicación de la implementación (sin código), pruebas con datos concretos, **análisis de pruebas** (la parte más importante), conclusiones |
| Aplicación con GUI | TextArea de entrada, vista de cómo se interpretó la entrada, botón "Solucionar", campo de texto con el código MiniZinc |
| Sustentación individual | Nota de 0 a 1 que **multiplica** la nota del proyecto. **Todos deben poder explicar todo el modelo.** |

Formato de la entrada (TextArea):

```
12
5
Palmira 2 3
Cali 10 2
Buga 11 0
Tulua 0 3
RioFrio 1 2
```

Línea 1: N. Línea 2: M. Siguientes M líneas: `nombre x y`.

> **Aviso:** el enunciado dice que los grupos son de **máximo 3 personas** y somos 4. Hay que confirmar con el profesor.

---

## 2. Cómo funciona (flujo de datos)

```
TextArea → parsear_entrada → validar → generar_minizinc → campo de código
            (entrada.py)    (validacion.py)  (generador.py)      (gui.py)
```

El modelo MiniZinc vive en una **plantilla** (`plantillas/modelo.mzn.tpl`): MiniZinc normal con marcadores `__N__`, `__M__`, `__CX__`, `__CY__`, `__NOMBRES__` donde cambian los datos. El generador reemplaza esos marcadores con los valores de la entrada. El resto del modelo no cambia entre entradas.

---

## 3. Estructura de la carpeta

```
concierto/
├── main.py                      # punto de entrada
├── gui.py                       # interfaz tkinter (HECHA, ver estado)
├── tema.py                      # paleta de colores (constantes)
├── entrada.py                   # Ciudad, Instancia, parsear_entrada
├── validacion.py                # reglas de validación
├── generador.py                 # arma el código MiniZinc desde la plantilla
├── plantillas/
│   └── modelo.mzn.tpl           # EL MODELO (lo escribe el equipo)
├── casos/                       # entradas de prueba (.txt)
└── tests/                       # tests unitarios (unittest)
```

Opcional (no es requisito del enunciado): `herramientas/verificador.py`, un script de fuerza bruta que prueba los (N+1)² puntos para **comprobar** las respuestas de MiniZinc. Nunca se importa desde la app.

**Tecnología:** Python 3 + tkinter (viene incluido con Python). Tests con `unittest`.

---

## 4. Estado actual

| Módulo | Estado |
|---|---|
| `gui.py`, `tema.py`, `main.py` | Hechos. Falta ajustes menores de la revisión (botón "Limpiar" con posición fija, fuentes por sistema operativo, scrollbar en la tabla) |
| `entrada.py`, `validacion.py`, `generador.py` | **Stubs provisionales** para que la GUI abra. Hay que reemplazarlos por las versiones reales |
| `plantillas/modelo.mzn.tpl` | **Pendiente**: el modelo MiniZinc |
| `casos/`, `tests/` | Pendientes |

### Cómo ejecutar

Desde la carpeta raíz (importante, porque la plantilla se carga con ruta relativa):

```
python main.py        # en macOS/Linux: python3 main.py
```

Pulse **Cargar ejemplo** y luego **Solucionar** (o `Ctrl+Enter`).

---

## 5. Reparto de trabajo

| Persona | Responsabilidad | Revisa a |
|---|---|---|
| **A — Modelo** | `plantillas/modelo.mzn.tpl`: criterio de equidad, restricciones y objetivo, probados en el IDE de MiniZinc | D |
| **B — Aplicación** | `gui.py`, `main.py`, pulido de interfaz | A (que el código generado sea correcto) |
| **C — Núcleo** | `entrada.py`, `validacion.py`, `generador.py` y sus tests | B |
| **D — Pruebas e informe** | `casos/`, ejecución de pruebas, tablas, análisis, formato IEEE | C |

Si finalmente el grupo es de 3: C absorbe el verificador (si se hace) y D mantiene `casos/` e informe.

**Regla del equipo:** como la sustentación es individual, nadie "se especializa" al punto de no entender el resto. Cada persona revisa el trabajo de otra (columna "Revisa a") y, antes del 7 de diciembre, hacemos un ensayo de preguntas cruzadas.

---

## 6. Decisiones pendientes (hay que tomarlas como grupo)

1. **Criterio de "equitativo".** Hipótesis de trabajo: **minimizar la distancia máxima** (nadie queda muy lejos) y, como desempate, **minimizar el rango** `max(d) − min(d)` (las distancias son parecidas). Alternativas a comparar: suma de distancias, solo rango, varianza. Hay que probarlas en un mismo ejemplo y buscar casos donde **discrepen**; ese material alimenta el análisis del informe.
2. **Nombres con espacios** en la entrada: ¿se aceptan o se rechazan con mensaje claro?
3. **Líneas en blanco** en la entrada: ¿se ignoran o son error?
4. **Bordes del cuadrado:** ¿el concierto puede quedar en x=0, x=N, y=0, y=N? (Hipótesis: sí, `0..N`.)
5. **Verificador de fuerza bruta:** ¿lo hacemos? Recomendación: una versión mínima para N pequeño, para poder responder "¿cómo saben que su modelo es correcto?".

Todo lo que decidamos debe quedar escrito como **supuesto** en el informe.

---

## 7. Casos extraños que debemos cubrir

El profesor advierte que preguntará por qué el concierto queda en un punto y no en otro. Conviene tener casos de prueba para:

- M = 1 y M = 2.
- Ciudades colineales, o en las esquinas del cuadrado.
- Una ciudad aislada lejos de las demás.
- El punto óptimo coincide con una ciudad (hay que tomar el mejor punto libre).
- Varios puntos óptimos empatados.
- N pequeño con casi todos los puntos ocupados, o todos (problema infactible).
- Entradas inválidas: ciudades fuera del cuadrado, repetidas, M que no coincide con las líneas.

---

## 8. Ruta de trabajo (hasta el 7 de diciembre)

**Hasta el 25 nov — entender y decidir**
- Todos instalan MiniZinc IDE y hacen ejercicios pequeños (una variable con dominio, `forall`, `abs`/`max`/`min`, un `solve minimize`).
- A modela el ejemplo del enunciado y compara criterios de equidad.
- C implementa `entrada.py` primero (los demás dependen de `Instancia`).
- Acordar nombres y firmas de funciones.

**26 nov – 2 dic — construir**
- Integración completa: GUI → parsear → validar → generar.
- Ejecutar todos los casos en MiniZinc y registrar resultados y tiempos.
- Borrador del informe: modelo, implementación y pruebas.

**3 – 7 dic — analizar y ensayar**
- Análisis de resultados y conclusiones, revisión cruzada.
- **Congelar el código el 4 o 5 de diciembre.**
- Ensayo de sustentación.

---

## 9. Convenciones

- Docstrings en todas las funciones públicas (qué hace, args, returns, raises).
- Colores solo desde `tema.py`, nunca valores sueltos en `gui.py`.
- La GUI **nunca** calcula ni muestra el resultado del problema.
- Si hay errores de entrada, el panel de código debe quedar vacío (nadie copia un modelo roto).
- Cambios de firmas de funciones: avisar al grupo.

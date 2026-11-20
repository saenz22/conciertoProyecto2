# Base del informe técnico

Este archivo sirve como base editable del informe IEEE. Deben agregarse autores,
institución, fecha y los resultados reales obtenidos con MiniZinc.

## Resumen

Se presenta un generador de modelos MiniZinc para seleccionar una ubicación
equitativa de un concierto dentro de un cuadrado con ciudades en coordenadas
enteras. La aplicación valida la entrada y no calcula la solución.

## I. Modelo del problema

**Datos**

- `N`: lado del cuadrado.
- `M`: número de ciudades.
- `(cx[i], cy[i])`: posición de la ciudad `i`.

**Variables**

- `conciertoX ∈ {0, ..., N}`.
- `conciertoY ∈ {0, ..., N}`.
- `distancia[i] = |conciertoX-cx[i]| + |conciertoY-cy[i]|`.

**Restricciones**

```text
conciertoX != cx[i] o conciertoY != cy[i], para toda ciudad i.
```

**Objetivo**

Primero se minimiza la distancia máxima:

```text
min max(distancia)
```

Luego se minimiza el rango:

```text
min (max(distancia)-min(distancia))
```

La implementación combina los objetivos como:

```text
min max(distancia)*(2*N+2)+(max(distancia)-min(distancia))
```

## II. Supuestos

- Las coordenadas válidas están entre `0` y `N`, incluyendo los bordes.
- Los nombres son campos únicos sin espacios.
- Las líneas en blanco son inválidas.
- Las ciudades tienen posiciones diferentes.
- Debe existir al menos un punto libre.
- El criterio minimax con rango define la equidad.

## III. Implementación

El parser convierte el texto en objetos `Ciudad` e `Instancia`. El validador
revisa las reglas de negocio. El generador reemplaza marcadores en la plantilla
MiniZinc. La interfaz usa `tkinter` y permite copiar el modelo generado.

## IV. Pruebas

Ejecutar y documentar al menos:

| Caso | Datos | Objetivo |
|---|---|---|
| Ejemplo | N=12, M=5 | Comparar modelo y verificador |
| Una ciudad | N variable | Confirmar simetría |
| Dos esquinas | M=2 | Analizar empates |
| Colineales | M>2 | Analizar el criterio |
| Cuadrado completo | M=(N+1)^2 | Confirmar infactibilidad |
| Fuera de rango | X>N o Y<0 | Confirmar validación |

Agregar resultados reales con punto obtenido, máximo, mínimo, rango, tiempo
y número de soluciones óptimas.

## V. Análisis

Analizar variación según `N` y `M`, concentración de ciudades, empates,
comparación con suma de distancias y tiempos de resolución.

## VI. Conclusiones

Redactar las conclusiones después de ejecutar las pruebas reales. Deben indicar
el comportamiento observado, la justificación del criterio y las limitaciones.

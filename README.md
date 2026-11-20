# Ubicador de concierto

Proyecto 2 de Análisis y Diseño de Algoritmos, periodo 2026-2.

La aplicación lee una instancia del problema y genera código MiniZinc.
No calcula ni muestra la ubicación óptima dentro de Python.

## Criterio de equidad

Se eligió optimización lexicográfica:

1. Minimizar la distancia Manhattan máxima desde el concierto a una ciudad.
2. Entre soluciones empatadas, minimizar el rango entre la distancia máxima
   y la distancia mínima.

Las coordenadas permitidas están en `0..N` en ambos ejes. El punto no puede
coincidir con ninguna ciudad.

## Ejecución

Desde la raíz del repositorio:

```bash
python3 proyecto2/main.py
```

## Entrada

```text
12
5
Palmira 2 3
Cali 10 2
Buga 11 0
Tulua 0 3
RioFrio 1 2
```

Los nombres no admiten espacios. Las líneas en blanco son inválidas.

## Estructura

```text
proyecto2/
├── main.py
├── gui.py
├── tema.py
├── entrada.py
├── validacion.py
├── generador.py
├── plantillas/modelo.mzn.tpl
├── pruebas/
└── tools/solucionVoraz.py
```

El verificador de fuerza bruta no se importa desde la GUI. Se usa
exclusivamente para comprobar ejemplos pequeños.

## Pruebas

```bash
python3 -m unittest discover -s proyecto2/pruebas -p 'test*.py'
```

Las pruebas cubren parser, validación, generación y fuerza bruta.

## Documentos

- [Preguntas de sustentación](Preguntas_sustentacion.md)
- [Base del informe técnico](Informe_proyecto.md)

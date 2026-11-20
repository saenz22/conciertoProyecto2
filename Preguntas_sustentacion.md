# Preguntas de sustentación y respuestas

## 1. ¿Qué problema resuelve el proyecto?

Recibe el lado `N` del Valle y una lista de `M` ciudades con coordenadas
enteras. Genera un modelo MiniZinc que selecciona una posición válida para el
concierto.

## 2. ¿Qué significa que el concierto sea equitativo?

El enunciado no define una medida exacta. Se decidió minimizar primero la
distancia Manhattan máxima y, después, el rango entre la máxima y la mínima.

## 3. ¿Por qué se usa distancia Manhattan?

La distancia horizontal se suma a la vertical:
`abs(x-cx) + abs(y-cy)`.

## 4. ¿Cuál es el modelo formal?

Las variables son `conciertoX` y `conciertoY`, ambas entre `0` y `N`. Para
cada ciudad se calcula su distancia. Ninguna posición puede coincidir con una
ciudad. Se minimiza `max(distancia)` y luego
`max(distancia)-min(distancia)`.

## 5. ¿Cómo se asegura la optimización lexicográfica?

La función objetivo usa
`max(distancia)*(2*N+2)+(max(distancia)-min(distancia))`. El rango máximo
válido es `2*N`, por lo que el factor separa completamente el objetivo
principal.

## 6. ¿Por qué las coordenadas llegan hasta `N`?

La representación incluye las posiciones enteras del borde. Cada eje tiene
`N+1` posiciones desde `0` hasta `N`.

## 7. ¿Qué ocurre si la posición óptima coincide con una ciudad?

Se excluye con una restricción disyuntiva. Debe cumplirse
`conciertoX != ciudadX` o `conciertoY != ciudadY`.

## 8. ¿Qué ocurre si todas las posiciones están ocupadas?

La aplicación devuelve un error. La validación calcula `(N+1)^2` posiciones
y compara ese número con `M`.

## 9. ¿Qué ocurre con nombres o posiciones repetidas?

Se reporta el nombre repetido y la posición repetida. Ambas situaciones no
están permitidas.

## 10. ¿Por qué se rechazan nombres con espacios y líneas en blanco?

El formato exige tres campos por ciudad. Rechazar nombres con espacios hace
que el parser sea determinista y las líneas vacías no producen datos ambiguos.

## 11. ¿Qué valida el parser y qué valida el validador?

El parser valida estructura y tipos. El validador valida rangos, nombres,
duplicados y disponibilidad de un punto libre.

## 12. ¿Cómo se evita copiar código generado desde una entrada inválida?

Se limpia la salida antes de procesar. Si falla el parser o la validación,
el área MiniZinc permanece vacía y se muestra el error.

## 13. ¿Por qué la aplicación no muestra la solución?

El enunciado prohíbe resolver dentro de la aplicación. Python genera el
modelo y MiniZinc realiza la optimización.

## 14. ¿Por qué existe un verificador de fuerza bruta?

Permite comprobar ejemplos pequeños evaluando todas las posiciones libres.
Es una comparación independiente del modelo.

## 15. ¿Cuál es la complejidad del verificador?

Es `O(M(N+1)^2)`, porque analiza `(N+1)^2` puntos y `M` distancias por punto.

## 16. ¿Cuál es la complejidad del generador?

Es aproximadamente `O(M+L)`, donde `L` es la longitud de la plantilla.

## 17. ¿Puede haber empates?

Sí. Varios puntos pueden compartir distancia máxima y rango óptimos. El
verificador conserva todos los puntos óptimos.

## 18. ¿Qué son los otros criterios del verificador?

Permite comparar `minimax`, `rango`, `suma` y `minimax_rango`. Esto ayuda a
demostrar por qué se eligió el criterio lexicográfico.

## 19. ¿Qué pruebas deben ejecutarse antes de entregar?

Debe ejecutarse el ejemplo del enunciado, una ciudad, esquinas, ciudades
colineales, empates, cuadrado completo e entradas inválidas.

## 20. ¿Qué limitaciones tiene este enfoque?

El dominio crece con `(N+1)^2` y el modelo calcula una distancia por ciudad.
Para valores grandes puede aumentar el tiempo de resolución.

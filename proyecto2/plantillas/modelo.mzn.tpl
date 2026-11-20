% Modelo generado por el proyecto Ubicador de concierto.
% Criterio: minimizar la distancia maxima y, luego, el rango.

int: N = __N__;
int: M = __M__;

array[1..M] of int: ciudadX = __CX__;
array[1..M] of int: ciudadY = __CY__;
array[1..M] of string: nombres = __NOMBRES__;

var 0..N: conciertoX;
var 0..N: conciertoY;
array[1..M] of var 0..(2 * N): distancia;
var 0..(2 * N): distanciaMaxima;
var 0..(2 * N): distanciaMinima;
var 0..(2 * N): rango;

constraint
  forall(i in 1..M)(
    distancia[i] = abs(conciertoX - ciudadX[i])
                  + abs(conciertoY - ciudadY[i])
  );

constraint
  forall(i in 1..M)(
    not (conciertoX = ciudadX[i] /\ conciertoY = ciudadY[i])
  );

constraint distanciaMaxima = max(distancia);
constraint distanciaMinima = min(distancia);
constraint rango = distanciaMaxima - distanciaMinima;

solve minimize (distanciaMaxima * (2 * N + 2)) + rango;

output [
  "concierto = (", show(conciertoX), ", ", show(conciertoY), ")\n",
  "distancia maxima = ", show(distanciaMaxima), "\n",
  "rango = ", show(rango), "\n",
  "distancias = ", show(distancia), "\n"
];
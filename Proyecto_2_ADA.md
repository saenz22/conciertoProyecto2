## AN´ALISIS Y DISE˜NO DE ALGORITMOS Segundo proyecto - Optimizaci´on

## Miguel ´Angel Askar Rodr´ıguez, Mg * 2026-2

Para este proyecto debe entregarse un informe en PDF a trav´es del campus virtual. Este proyecto debe ser sustentado, la nota de sustentaci´on estar´a entre 0 y 1 de acuerdo a su desempe˜no individual en la misma, esta nota se multiplicar´a por la nota obtenida en el proyecto. La sustentaci´on se ejecutar´a de manera individual y la nota no se entregar´a inmediata- mente dado que se deben revisar las sustentaciones

de cada uno. Se aceptan grupos de m´aximo 3 personas.

Fecha de entrega y sustentaci´on: 7 de diciem- bre de 2026

- El modelo del problema: Descripci´on formal.

- Explicaci´on de su implementaci´on. Sin incluir c´ odigo.

- Pruebas: descripci´on de las pruebas realiza- das con datos espec´ıficos.

- An´alisis de las pruebas realizadas. Explique las variaciones de acuerdo al tama˜no y natu- raleza de su entrada. Esta es una de las partes m´as importantes del informe, por favor sean cuidadosos.

- Conclusiones, deben ser conclusiones de bue- na calidad, que evidencien que ya casi son ingenieros.

- 2. Una implementaci´on en un lenguaje deseado:

- Debe poder cargarse la entrada dentro de un TextArea que tendr´a el siguiente formato:

- La primera l´ınea un entero N indicando el tama˜no del cuadrado que representa al Valle

- La segunda l´ınea un entero M indicando el n´umero de ciudades

- Las siguientes M l´ıneas contienen la ubi- caci´on de las ciudades. Cada fila contiene 3 datos separados por un espacio. El pri- mer espacio es el nombre de ciudad, el segundo su posici´on en X y el tercero su posici´on en Y.

Una entrada de ejemplo es

## 1. ¿D´onde pongo mi concierto?

El cantante Benito-Bad va a cantar en el Valle del Cauca y su concierto es muy apetecido. Cada ciudad quiere que el concierto quede lo m´as cerca posible de ellos. La gobernaci´on ha decidido medir la distancia entre dos ciudades como la distancia Manhattan, que

es la distancia en el eje X m´as en el eje Y.

Nuestro departamento (Valle del Cauca), para efectos de simplificaci´on, se representa como un cuadrado perfecto de N km por N km., siendo un plano donde X e Y son positivas; la esquina inferior izquierda marca la posici´on (0,0). En este sistema las ciudades est´an situadas sobre las intersecciones, es decir siempre tienen posiciones enteras. Por ejemplo,

si N = 10 una entrada posible ser´ıa:

Cuadro 1: Entrada de ejemplo

Sin embargo, con el fin de no alentar los duelos a muerte entre alcaldes, el concierto no puede quedar directamente dentro de una ciudad. As´ı mismo, tampoco puede quedar “favoreciendo” a una ciudad m´as que a otra, es decir que el concierto debe quedar

a una distancia donde sea relativamente equitativo

*miguel.askar@correounivalle.edu.co

desplazarse, relativamente hablando.

Nota: Se recomienda analizar posibles casos ex- tra˜nos y particulares, ya que en la sustentaci´on se puede preguntar la raz´on de porqu´e el concierto queda en cierto punto y no en otro. Adem´as, depende de su ingenio determinar qu´e podr´ıa ser “favorecer”m´as a

una ciudad que a otra y c´ omo lo evitar´ıa.

- 1. Debe entregar un informe en PDF en formato IEEE que contenga:

```
12
5
Palmira 2 3
Ca l i 10 2
Buga 11 0
Tulua 0 3
RioFr io 1 2
```


- Se debe tener una interfaz gr´afica mostran- do c´ omo es la entrada, un bot´on de solucio- nar problema y un campo de texto donde se genere c´ odigo que pueda copiar y pegar en MiniZinc.

- Ojo, no se aceptan soluciones que den el re- sultado dentro de la aplicaci´on, esto es debido a que generar el c´ odigo de MiniZinc implica conocer bien c´ omo se crea el modelo del pro- blema.

- Por otra parte, no se recomienda crear en la GUI un plano cartesiano para representar a las ciudades, esto no dar´a puntos extra.
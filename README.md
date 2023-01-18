# Awars

## Integrantes

- Jesús Aldair Alfonso Pérez C-312
- Mauro Bolado Vizoso C-311

## Resumen

Awar es un simulador de modos de batalla, donde las unidades (agentes) involucradas se enfrentan para salir victoriosos sobre el enemigo con las condiciones que presente el enfrentamiento.

## Simulación

La simulación se llevó a cabo con el concepto de agentes y lógica difusa para lograr un ligero acercamiento a la realidad, para llevar a cabo la simulación son necesarias las unidades implicadas, un modo de batalla o simulación. Indistintamente de como se distribuyen las unidades, que es a definir por el usuario.

El Simulador, dada su estructura, permite ejecutar en él cualquier problema de unidades (agentes) en un mapa. Esto es posible dado que para cada problema se reduce a definir correctamente el modo de simulación de acorde al problema que se quiere simular. El objetivo de esta arquitectura es hacer cada paso lo más extensible posible para futuras mejoras.

### Modo de Simulación

El modo de simulación determina bajo que condiciones se lleva a cabo la simulación, es este el que sabe generar un mapa, a través de un generador de mapas que es posible definirlo a su vez, lleva el control de como ejecutar cada acción sobre la simulación y cuando esta es válida o no en el contexto, el modo debe tener en cuenta cada uno de los modificadores de bonificaciones y penalizaciones que brinde el mapa y él mismo.

#### Modo Normal

Este modo de simulación no tiene en cuenta modificadores del terreno, para bonificaciones o penalizaciones de ataque, precisión, movimiento o armadura.

#### Modo Difícil

El modo difícil de simulación tiene en cuenta bonificaciones y penalizaciones del terreno para llevar a cabo la ejecución de las acciones y a la hora de validarlas. Para este modo tanto la precisión, la capacidad de movimiento, el ataque, la defensa y la visión están afectadas por las condiciones de la simulación.

#### Modo Ajedrez

El modo de ajedrez está pensado para la ejecución del ajedrez, validando cada movida y llevando a cabo la ejecución de la misma con las condiciones del ajedrez.

#### Generador de mapas

La idea detrás de tener un generador de mapas es que en un mismo modo puedan ser utilizados muchos mapas distintos que cumplan con las especificaciones del modo de simulación, con el objetivo de hacer el modo lo más extensible posible.

### Unidad

Las unidades (agentes) son las que llevan a cabo cada acción en la simulación a través de una toma de decisiones simple, toma de decisiones que es representada por su estrategia resolviendo ademas un problema de CSP y utilizando un MiniMax para obtener un mejor resultado en cada momento, cada unidad toma las deciciones enteramente dado el contexto en el que se encuentre.

#### Tipos de unidad

Las unidades, dependiendo del problema a simular pueden presentar caraterísticas variables, en la implementación actual del proyecto se notan varias definiciones de este concepto: unidades básicas, unidades armadas y unidades de ajedrez. Para cada uno de los distintos tipos de unidad se resaltan las características relevantes de la misma de acorde al problema para el que están diseñadas.

##### Unidad Básica

La unidad básica no es más que una dónde no se tiene en cuenta equipamiento alguno, armadas a ¨mano limpia¨ son en la práctica ¨boxeadores¨ sin guantes. Cuyo comportamiento está definido claramente al combate cuerpo a cuerpo.

Cabe mencionar que las unidades básicas pueden estar equipadas con armamento de cualquier tipo, pero no cuentan con un equipamiento defensivo

##### Unidad Armada

La unidad armada puede contar con un equipamento defensivo adicional que le proporciona defensa de acorede a la situación, queda a manos de la implementación la efectividad de dicho equipamento respecto a cada arma. Para la actual implementación del proyecto la efectivada es pareja para todo tipo de armas, aspecto que no necesariamente tiene por que ser de esta manera y es una posibilidad más a evaluar en futuras versiones, incluyendo que la unidad pùdiera trazar su estrategia también dependiendo de que tan efectiva sea su armadura para las armas de los oponentes.

##### Unidad de Ajedrez

La diferencia de las unidades de ajedrez respecto a las básicas es que estas a su vez controlan unidades (agentes), en resumidas cuentas son una capa intermedia, son las que controlan las piezas del tablero, estas unidades llevan un registro de las piezas que estan en su pertenencia en cada momento de la simulación y evalúan cada situación de acorde a cuanto afecta una jugada para sus piezas y el resultado en sí.

#### Estrategias de las unidades

Para definir el comportamiento de las unidades estas traen incormporadas un conjunto de estrategias, las cuales son las encargadas de resolver el problema de evaluar cada acción en el contexto dado para el agente, por consiguiente, el problema fue atacado con los algoritmos de CSP para resolver las restricciones que pueda presentar el entorno y las limitaciones del agente y a su vez se utilizó un minimax clásico para obtener un comportamiento más detallado a profundidad de la embergadura de cada acción.

Cabe mencionar que las estrategias van desde las muy simples (Aleatorio, Goloso, Atacante) hasta unas un poco más elaboradas (las antes mencionadas con minimax y CSP, incluso estrategias con lógica difusa para hacer no determinista la toma de decisiones).

### Entorno

El entorno de simulación o mapa va a estar determinado por un generador, generador que como bien antes mencionado será manejado por el modo de simulación, el mapa puede abarcar conceptos como clima, obstáculos, elevación, tipo de suelo, entre otros. El objetivo del mapa y de cada una de las características que presenta es acercar la simulación
a los parámetros deseados.

#### Modificadores del Entorno

En el entorno o mapa que se lleva a cabo la simuación como bien antes se mencionaba pueden estar presentes determinados modificadores que afecten la ejecución de la simulación. Estamos hablando de: estructuras, clima, tipo de suelo, elevación, obstáculos, implementados hasta el momento.

Cada uno de estos modificadores tienen como ojetivo cambiar las condiciones con la que el modo puede llevar a cabo la ejecución de la simulación. Estas brindan un conjunto de bonificaciones o penalizaciones a cada aspecto contemplado actualmente en la simulación dígase precisión, ataque, defensa, capacidad de movimiento, rango de visión, visibilidad y si es obstáculo que hasta el momento no hay nada que sea un obstñaculo para las unidades implicadas en la simulación.

La idea detrás de estos modificadores en el terreno es que el proyecto sea extensible a generar climas, terreno, estructuras, elevaciones, etc. Además de facilitar la posibilidad de tener acciones de las unidades que le permitan modificar el terreno para más conveniencia en la simulación ya sea construcción de estructuras como modificar la elevación del terreno incluso acomodarse y construir para no recibir las penalizaciones por clima.

## Lenguaje

Para controlar a las unidades, crear el campo de batalla, crear las armas y demás se utilizara un Domain Specific Language llamado `awar`. Cuenta con las principales funcionalidades de control de flujos como `if` y `while`.

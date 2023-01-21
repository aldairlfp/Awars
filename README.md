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

## DSL

Un lenguaje de dominio específico (DSL, por sus siglas en inglés) es un lenguaje de programación diseñado para resolver problemas específicos de un dominio particular. En el caso de un simulador de batallas, se puede crear un DSL para codificar las caracteristicas del campo de batalla. De esta forma, se puede conectar la simulación para evaluar las situaciones que se pueden presentar. Esto permite que sea optimizado y más facil de controlar el simulador en diferentes escenarios, por supuesto en lo referido a la simulación.

Para este caso en particular se utiliza el DSL para facilitarle al usuario la creación de los escenarios de batalla, de esta forma, el usuario no tiene que preocuparse por la sintaxis del lenguaje de programación que se utiliza para la simulación, sino que se puede concentrar en la creación de los escenarios. Evitando con esto la engorrosa tarea de definir los escenarios de batalla en el lenguaje de programación que se utiliza para la simulación.

### Sintaxis

La sintaxis esta formada principalmente de dos tipos de statements: los statements usuales de los lenguajes de propósito general y los statements que tienen que ver con la simulación. Todos los statements estan separados por un cambio de línea.

El Lenguaje para garantizar un mínimo de correcto uso realiza un chequeo de sintaxis, es decir, si el usuario escribe algo que no es un statement válido, el lenguaje no lo va a aceptar y va a mostrar un error. Los errores saltan en tiempo de compilación, es decir, cuando el usuario ejecuta el programa y se está compilando el mismo.

El concepto de 'tipo' para el DSL está simplificado, por supuesto para lograr una interacción más sencilla con el usuario del mismo, solamente existen `number` y `string`. Los `number` pueden ser cualquier número racional. Ambos son considerados como expresiones. Los `string` se escriben entre comillas dobles, por ejemplo:

```c#
"Hola mundo!"
```

Para la declaración de variables es necesario utilizar reservada `var` seguido del nombre de la variable, el operador de asignación `=` y el valor que se le desea asignar, nevamente este valor debe ser una expresión válida del DSL y por supuesto las variables también son expresiones, por ejemplo:

```c#
var variable1 = <expresion>
var variable2 = "Hola mundo!"
```

Las variables, al ser expresiones del lenguaje pueden ser reasignables las variables, es decir, lo que está almacenado en la variable puede ser cambiado cuantas veces se desee en el código, mientras se tenga acceso a la variable en el entorno en el cual se le llama, y al funcionar de manera dinámica, aunque una variable sea declarada como `number` luego se puede reasignar como un `string`, por ejemplo:

```c#
var a = 100
a = "hola"
```

Para facilitar el manejo visual de las expresiones y garantizar un mejor control del usuario existe una función built-in la cual es `print`, que recibe como argumento una expresión y la imprime, por ejemplo:

```c#
print(<expresion>)
```

Dado que el lenguaje es Turing completo, es decir en el se pueden programar todos los algoritmos que sean Turing computables y se obtendrá una solución, cuenta con controladores de flujo. Primero está el `if` el cual funciona de la siguiente manera:

```c#
if(<condition>){
	<statement>
} else {
	<statement>
}
```

Cabe destacar que entre `}` y el `else` no puede haber un cambio de línea, dado el caso, el `else` no será reconocido como parte de la expresión `if`, de dónde se obtiene un error de compilación.

También cuenta con ciclos como `while` y `for` los cuales se definen de la siguiente manera:

```c#
while(<condition>){
	<statement>
}
```

```c#
for(<declaration>; <condition>; <increment>)
```

Los ciclos pueden tener un `break` para detener su ejecución, o `continue` para saltar a la siguiente iteración

Claramente el lenguaje permite declarar funciones para encapsular determinados procedimientos, para esto la sintaxis es la siguiente:

```c#
func <nombre_de_la_funcion>(<params>){
	<statement>
}
```

Las funciones pueden devolver valores con `return <expresion>`. Las expresiones retornadas por una función pueden ser también vacías, en este caso no puede existir el statment `return`, es decir ninguna función de lenguaje puede tener un `return` sin una expresión válida, en otro caso se obtiene un syntax error.

La simulación se define de la siguiente manera:

```c#
simulator(<mode>, <max_turns>)
```

`max_turns` es un `number` e indica el máximo de turnos que se ejecutarán en la simulación. Los `mode` determinan la dificultad del mundo, los cuales son: `normal_mode` y `hard_mode`. Un ejemplo de como inicializar la simulacion es:

```c#
simulator(hard_mode, 1000)
```

Las unidades se crean de la siguiente manera:

`<unit>(<number>, <team>, <strategy>, <strategy_to_use>) -> simulator`.

Las `unit` son las siguientes: `normal` `archer_b`, `archer_c`, `swordman` y `spearman`. `number` es la cantidad de unidades que se sumarán de ese tipo, `team` es un `string` con el nombre del equipo, `strategy` es un `string` indicando como se llamará la estrategia a utilizar y `strategy_to_use` es esta estrategia que se utilizará. Las estrategias a usar son: `random_strategy`, `greedy_strategy`, `runner_strategy`, `attacker_strategy`, `normal_strategy`, `advanced_strategy`, `hard_optimal_strategy` y `hard_fuzzy_strategy`.

El campo de batalla se define como: `field(<width>,<height>) -> simulator`. Donde `width` y `height` son `number`.

Para ubicar a las unidades existe un `statement` llamado `random_allocate` el cual ubica todas las unidades en `simulator` aleatoriamente en el campo de batalla

Y por ultimo para ejecutar la simulacion se realiza simplemente escribiendo `simulator`. Si no hay unidades definidas, ni campo de batalla ni estan ubicadas las unidades, la simulacion no puede comenzar, esto lanza un error de compilacion. Al igual si no se ha definido la simulacion, no se pueden definir unidades, ni campo de batalla, ni ubicar unidades, esto tambien lanza un error de compilacion

### Arquitectura del compilador

Este lenguaje está desarrollado en `Python`, con una gramática LALR. Para el desarrollo del compilador se usó `ply`, que es una implementación de `Python` pura del constructor de compilación lex/yacc. Incluye soporte al parser LALR(1) así como herramientas para el análisis léxico de validación de entrada y para el reporte de errores. El análisis sintáctico se divide en 2 fases: en una se realiza el análisis léxico, con la construcción de un lexer, y en la otra se realiza el proceso de parsing, definiendo la gramática e implementando un parser para la construcción del Árbol de Sintaxis Abstracta (AST por sus siglas en inglés).

El programa fuente se procesa de izquierda a derecha y se agrupan en componentes
léxicos (tokens) que son secuencias de caracteres que tienen un significado. Todos los espacios
en blanco, comentarios y demás información innecesaria se elimina del programa fuente. El
lexer, por lo tanto, convierte una secuencia de caracteres (strings) en una secuencia de tokens.

El parser también se implementó mediante `ply`, especificando la gramática y las acciones para
cada producción. Para cada regla gramatical hay una función cuyo nombre empieza con p_. El
docstring de la función contiene la forma de la producción, escrita en EBNF. `ply` usa los dos puntos (:) para separar la parte izquierda y la derecha de la producción gramatical. El símbolo del lado izquierdo de la primera función es considerado el símbolo inicial. El cuerpo de esa función contiene código que realiza la acción de esa producción.
En cada producción se construye un nodo del árbol de sintaxis abstracta el cual esta definido desde 0.

El procesador de parser de `ply` procesa la gramática y genera un parser que usa el algoritmo de
shift-reduce LALR(1), que es uno de los más usados en la actualidad. Aunque LALR(1) no puede
manejar todas las gramáticas libres de contexto, la gramática usada fue refactorizada
para ser procesada por LALR(1) sin errores.

Para realizar los recorridos en el árbol de derivación se hace uso del patrón visitor. Este patrón nos permite abstraer el concepto de procesamiento de un nodo. Cada elemento del nodo se procesa y se envia a la simulación para ejecutarla. Usando este patron se definio un arbol de chequeo semantico, y un arbol evaluador.

Por ultimo tenemos los scopes, los cuales se utilizan con los recorridos del AST para verifica que las variables y funciones se puedan utilizar en el scope que le corresponde.
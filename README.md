# Awars

## Título

Proyecto Final de Compilación, Simulación e Inteligencia Artificial.

Carrera: Ciencias de la Computación.

Tercer año.

## Integrantes

- Jesús Aldair Alfonso Pérez C-312
- Mauro Bolado Vizoso C-311

## Resumen

Awar es un simulador de modos de batalla, donde las unidades (agentes) involucradas se enfrentan para salir victoriosos sobre el enemigo con las condiciones que presente el enfrentamiento. La idea general es llevar a cabo una simulación por agentes no determinista con el objetivo de poder verificar durante la ejecución el comportamiento de los agentes en la misma. Parte del trabajo consiste en hacer agentes inteligentes para poder verificar su comportamiento durante la simulación y poder acercar la ejecución de la misma lo más posible a la realidad. Para ello es necesario una genración de mapas de acorde a que se quiera tener en cuenta en durante la sumilación, dado que las condiciones del mapa claramente pueden influir directamente en el resultado de la batalla es necesario una implementación correcta de un generador de mapas para el modo de simulación deseado. el modo de simulación hace neta referencia a la pregunta ¿Qué deseamos simular?. Teniendo en cuneta esto las características de las unidades (agentes), la simulación brindará datos estadísticos de como se resuelve el estado inicial en múltiples ocaciones.

## Simulación

Para llevar a cabo la simulación es necesario haber definido previamente el modo de simulación, las unidades y con el modo una forma correcta de generar el mapa que sea consecuente con el mismo. Esto deja la posibilidad de simular cualquier entorno que se desarrolle con agentes inteligentes en un mapa determinado, nuevamente cabe destacar que es necesario que todo sea acorde a lo que se quiere simular para obtener resultados lo más realistas posibles de lo que se desea simular.

La simulación se llevó a cabo con el concepto de agentes inteligentes. Los agentes de la simulación son enteramente reactivos a la situación, es decir ellos no tienen uso de una memoria de lo que han ¨vivido¨, sino que su accionar está determinado enteramente por el contexto en el que se encuentran, tomando a su vez las deciones de acorde a la estrategia, forma de pensar del agente. Esta estrategia del agente está descrita por medio de un sistema de evaluación de las acciones que varía de acorde a la estrategia usada por el agente, la resolución de un Problema de Satisfacción de restricciones y un Minimax para lograr en el agente una idea básica de planificación.

El Simulador como bien antes se mencionaba deja espacio para poder simular cualquier entorno que tenga unidades (agentes) en un mapa donde interactúen entre sí siempre y cuando se defina a través del modo de simulación las especificaciones correctas a tener en cuenta a lo largo de la simulación, se definan las acciones posibles a realizar en la misma, y que el resultado pueda ser obtenido analizando el entorno y reaccionando al mismo sin interacción externa ajena al modo de simulación y al agente en sí mismo.

### Arquitectura

La arquitectura de la simulación está basada en un simulador que a su vez contiene un modo de simulación, un mapa donde se ejecuta la misma y las unidades que se quiere simular su comportamiento, el modo de simulación contiene el generador de mapas, este modifica el mapa de la simulación para establecer uno acorde a lo que se desea simular.   El modo interactúa directamente con la simulación durante su ejecución, a través del validardor de acciones, dado que las acciones sobre la simulación por parte de los agentes se ejecutan solo si el modo las valida y es el modo quien determina en parámetros reales el efecto de la acción en la simulación, teniendo en cuenta las condiciones establecidas en el mismo, de ahí la importancia de una correcta implementación para obtener resultados de acorde a los deseados en el proceso de simulación. El mapa que es generado por el modo está diseñado para contemplar determinadas características que influencian la simulación como bien antes mencionado a través del modo. Las unidades interactúan con la simulación turno a turno, en un turno todas las unidades en la simulación le dicen al simulador que acciones ellos quieren realizar en orden de acuerdo a su evaluación, esto es lo que recibe el modo para decidir cual ejecuta, cabe mencionar que siempre se ejecuta la primera acción válida que devuelva el agente a la simulación luego de evaluar todas las posibles acciones a realizar. Para la ubicación de las unidades en el mapa el simulador requiere de la implementación de un ¨ubicador de unidades¨, este ubicador de unidades necesita saber que función se desea seguir para ubicar los agentes en el mapa y las unidades que se quieren ubicar dado que esta es una de las formas posibles de asignarle unidades a la simulación.

A groso modo el proceso de simulación es una constante interacciones entre ¨simulador¨-¨agente¨-¨simulador¨-¨modo de simulación¨-¨mapa¨-¨agentes¨. ¿Cómo así? El ¨simulador¨ le pide al ¨agente¨ que relaice una acción, este le devuelve todas las acciones que puede realizar, el ¨simulador¨ toma la primera en la lista devuelta y le pide al ¨modo de simulación¨ que la valide, el ¨modo de simulación¨ valida la acción, en caso de no ser válida el ¨simulador¨ le envía
la siguiente y así hasta encontrar una válida, una vez que la acción sea válida el ¨modo de simulación¨ la ejecuta sobre el mapa y determina según la acción que efectos trae como consecuencia sobre el que ejecuta la acción y el resto de los agentes en la simulación.

### Modo de Simulación

El modo de simulación determina bajo que condiciones se lleva a cabo la simulación, la idea es tener un controlador de la simulación, es decir algo que tenga las reglas con las que se comportará la simulación, de manera que no le permita a los agentes implicados en la misma realizar nada fuera de los parámetros esperados. Este modo para su implementación requiere de un generador de mapas, con el objetivo de asegurar que el mapa generado tenga las condiciones que el modo requiere, es necesario en su implementación una forma de validar la acción a realizar en la simulación para así llevar un control de lo que se puedo o no hacer durante el proceso de simulación, evitando tener problemas de acciones inválidas o que algun agente haga ¨trampa¨ en la simulación dado que esto claramente influye en el resultado que se obtendrá en la simulación. El objetivo del modo es condicionar la simulación completamente a los parámetros deseados, en términos claros es como el ¨juez¨ que juzga que está correcto o mal, que usa a la hora de realizar las acciones penalizaciones y bonificaciones, tanto las que brinde el mapa como cualquier otra que se desee implementar en el mismo.

#### Modo Normal

El modo normal de simulación es producto de la primera implementación de pruebas para el proyecto, en este modo no se contemplan ninguno de los modificadores del mapa, el mapa es completamente un suelo de ¨hierba¨, con clima ¨soleado¨, sin ¨estructuras¨ ni ¨elevaciones¨, donde las bonificaciones de movimiento, precisión, ataque y defensa son todas el básico establecido en la creación de los agentes.

Como bien se puede notar este ¨modo¨ tuvo como objetivo las primeras pruebas de este proyecto, además de dejar espacio a una simulación más sencilla en cuanto a creación y a ejecución.

#### Modo Difícil

Este ¨modo de simulación¨ es la versión más detallada del entorno de simulación donde si se prueban las características del mapa, dígase ¨estructuras¨, ¨clima¨, ¨terreno¨ y ¨elevaciones¨. Cabe mencionar que se explica más adelante que son cada una de estas características del mapa básico más adelante.

El ¨modo difícil¨ tiene como objetivo evaluar el comportamiento de la simulación dependiendo de todas las características en la misma, más allá de ser ajeno a que los agentes, que en sus versiones de estrategia más desarrolladas siempre tienen en cuenta las características del terreno para determinar su forma de actuar, es estrictamente el modo el que decide cuanto influye esto en el resultado de la acción. Por eso, este modo, es la prueba de que funcionasen cada uno de los aspectos de la simulación de forma correcta.

#### Modo Ajedrez

El ajedrez es un juego de tablero para dos jugadores (equipos), que disponen al inicio de 16 piezas móviles que se colocan sobre un tablero, el jugador de las piezas ¨blancas¨ y el jugador de las piezas ¨negras¨. Se juega sobre un tablero cuadriculado de 8×8 casillas. Las piezas de cada jugador estan conformadas por un rey, una dama, dos alfiles, dos caballos, dos torres y ocho peones. Se trata de un juego de estrategia en el que el objetivo es derrocar al rey del oponente. Esto se hace amenazando la casilla que ocupa el rey con alguna de las piezas propias sin que el otro jugador pueda proteger a su rey interponiendo una pieza entre su rey y la pieza que lo amenaza, mover su rey a un escaque libre o capturar a la pieza que lo está amenazando, lo que trae como resultado el jaque mate y el fin de la partida.

Para este modo se diseñó un tipo especial de agente no inteligente que consiste en cada una de las piezas que tiene cada jugador ¨Rey (King)¨, ¨Reina (Queen)¨, ¨Alfil (Bishop)¨, ¨Caballo (Knight)¨, ¨Torre (Rook)¨ y ¨Peón (Pawn)¨. El tablero no tiene bonificaciones ni penalizaciones, aunque se deja la posibilidad de una implementación de un modo especial dónde esto se tenga en cuenta.

La validación de las jugadas del ajedrez se realiza teniendo en cuenta las reglas cláscicas y la ubicación de las piezas es determinada por una función especial que coloca las piezas en el orden correcto paa el inicio de la partida. Nuevamente en caso del usuario desear algo distinto se deja en sus manos la implementación de cualquier forma especial de realizar estas operaciones.

### Generador de mapas

Los generadores de mapas están contemplados en los ¨modos de simulación¨ como bien antes se menciona, con el objetivo de que sea a través de este que se llegue a la creación de un mapa ¨correcto¨ para la simulación. Las funciones de generación de mapas establecen las condiciones iniciales del terreno y todo lo que esto conlleva, ya sea asiganción deestructuras, suelos, clima, y elevaciones, características que a su vez tendrán su influencia en el transcurso de la simulación y que pueden determinar el resultado de la misma, acercándola a algo que pueda ser ¨justo¨ o desbalanceando el entorno completamente en favor de cualquiera de los participantes.

#### Generador de mapas básico

El generador de mapas básico genera una dispoción de terreno sin alturas, es decir terreno llano, con clima completamente soleado, y el terreno es enteramente de hierba. El objetivo de la creación de este tipo de terreno se remite a algo similar al ¨modo de simulación normal¨ siendo enteramente el modo de prueba de que la simulación funcionase correctamente. Más allá del motivo de la implementación de este generador, este está presente con el objetivo de hacer un mapa ¨parejo¨ para todos los implicados en el proceso de simulación, al no brindar ni penalizaciones ni bonificaciones a ninguno de los participantes. Aún con la simplicidad del mismo se pudn obtener escenarios de simulación que sean de agrado para el usuario del proyecto.

#### Generador de mapas de Ajedrez

El mapa de Ajedrez es un mapa especial, donde cada casilla no presenta ninguna de las características especiales ya antes mencionada, de dónde siempre será un tablero de 8x8 casillas con casillas vacías o casillas ocupadas por las piezas pertenecientes a cualquiera de los dos implicados en la partida de ajedrez.

Este generador simplemete incializa un mapa de tamaño 8x8 casillas con todas las casillas vacías para luego sea trabajo del ¨ubicador¨ disponer del posicionamiento correcto de las piezas en el tablero. Cabe mencionar que para el ajedrez lo que se ubica en el tablero (mapa) no son los agentes inteligentes que llevaran a cabo la simulación sino las piezas que serán controladas por los mismos.

### Unidad

Las unidades (agentes) son las que llevan a cabo cada acción en la simulación a través de una toma de decisiones simple. Esta toma de decisiones de las unidades es determinada por su estrategia, la cual puede variar en función de la creación de la unidad a la hora de inicializar el proceso de simulación. Las unidades son por su implementación agentes puramente reactivos y semi-inteligentes. Concesptos que se explican a continuación.

#### Agente

Un agente es un sistema computacional situado dentro de un medio-ambiente, dentro del cual es capaz de realizar acciones autónomas encaminadas a lograr sus objetivos. (Libro: Temas de Simulación pág 46. Concepto de Agente)

#### Agente Inteligente

Un agente inteligente es quel que es capaz de realizar acciones autonomas flexibles para lograr sus objetivos, en donde flexible significa tres cosas:

· Reactivo: Un agente inteligente debe ser capaz de percibir su ambiente y responder de un modo oportuno a los cambios que ocurren para lograr sus objetivos.

· Pro-Activo: Un agente debe ser capaz de mostrar un comportamiento goal-directed tomando la iniciativa para lograr sus objetivos

· Sociable: Un agente inteligente debe ser capaz de interactuar con otros agentes (posiblemente también con humanos), para lograr sus objetivos.

(Libro: Temas de Simulación pág 46. Concepto de Agente)

#### Agente puramente Reactivo

Ciertos tipos de agentes deciden que hacer sin hacer referencia a su historia. Ellos basan su decisión enteramente en el presente, sin referencia a todo lo pasado. Aeste tipo de agentes los llamaremos agentes puramente reactivos, debido a que simplemente responden directamente al ambiente. Formalmente, el comportamiento de estos agentes puede ser representado con una función ¨Ag: E* -> Ac¨.

#### Percepción

La primero para la hora de la construcción del agente es dividir la función de decisión en percepción y acción.

La idea es que la función ¨see¨ capta la habilidad de observar su ambiente, mientras que la función ¨action¨ respresenta el proceso de toma de decisón del agente.

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

##### Problema de Satisfacción de Restricciones

El CSP (por sus siglas en inglés) no es más que una forma de Inteligencia Artificial para como su nombre indica atacar problemas de satisfacción de restricciones. Para ducumentación al respecto de este algoritmo ver el Artificial Intelligence A Modern Approach, Global Edition Pearson, pág 164. En el proyecto esto es usado para que los agentes a la hora de tomar las decisiones estas tengan en cuenta todas las restricciones que vienen implicitas en el ambiente, para así obtener una evaluación más acertada y acciones válidas de acorde a cada instante.

##### Minimax

La otra forma implicada en la toma de decisiones de los agentes fue por la idea de modelar el problema a uno de búsqueda adversarial de suma cero y usar minimax para obtener las acciones positivas de acorde a un futuro cercano. Es importante mencionar que para poder usar esta técnica de Inteligencia Artificial fue necesario constuir evaluadores que modelaran el problema de la simulación deseada a un problema de suma cero, en otro ámbito no se debía aplicar este algoritmo. Para más información acerca de los requisitos y el concepto del algoritmo de Minimax véase Artificial Intelligence A Modern Approach, Global Edition Pearson, pág 192.

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
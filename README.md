# Awars

## Integrantes

- Jesús Aldair Alfonso Pérez C-312
- Mauro Bolado Vizoso C-311
- Raúl Beltrán Gómez C-312

## Resumen

Awars es un simulador de batallas donde varias unidades pelean entre sí para salir vencedoras ya sea por equipos o individualmente. 
Tiene como objetivo determinar el resultado de la batalla mediante una simulacion por agentes de cada individuo implicado en la batalla.
Se utilizarán algoritmos de IA y un componente aleatorio para determinar el accionar de cada sujeto, ya sea su interacción con el entorno,
su modo de combate o la estrategia en equipo si la simulación específica lo permite. 

## Campo de batalla

El campo de batalla tiene varios obstáculos que dependiendo de varias características, impedirán que las unidades puedan atacarse, disminuya la posibilidad de infligir daño, o que puedan saltar por encima de ellos. El tamaño se define antes de empezar la batalla y no podrá cambiarse luego de haber empezado la misma.

## Unidad

Las unidades cuentan con una vida, una eficiencia por heridas y una aleatoriedad dada por el carácter y su habilidad para enfrentar situaciones de presión. las mismas pueden estar equipadas o no con armas y mecanismos de defensa para acercar bastante a cada agente a la realidad.

## Arma

Las armas tienen un rango de ataque, la cantidad de daño que pueden infligir a las unidades. Las armas tienen un requerimiento de habilidad y cuando el portador no cuente con ello afecta su efectividad y acierto.

## Inteligencia artificial

Objetivamente la IA del proyecto está pensada para poder llevar a cabo el moviemiento, el combate y la estrategia, en conjunto con los conceptos de simulación dado la fuerte componente aleatoria del problema y la complejidad que presenta el mismo, además de la realidad que presenta una ineficiencia por parte de algoritmos deterministas en hallar solución al problema, se explora en estos campos para obtener resultados más acordes a lo que ocurre en la realidad y poder representar la situación.

## Lenguaje

Para controlar a las unidades, crear el campo de batalla, crear las armas y demás se utilizara un Domain Specific Language llamado `awar`. Cuenta con las principales funcionalidades de control de flujos como `if` y `while`.

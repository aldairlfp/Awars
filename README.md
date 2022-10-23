# Battle-Simulation

## Integrantes

- Jesús Aldair Alfonso Pérez C-312
- Mauro Bolado Vizoso C-313
- Raúl Beltrán Gómez C-312

## Resumen

Battle Simulation es un simulador de batallas donde varias unidades pelean entre si para salir vencedoras ya sea por equipos o individualmente. 

## Campo de batalla

El campo de batalla tiene varios obstáculos que dependiendo de varias características, impedirán que las unidades puedan atacarse, disminuya la posibilidad de infligir daño, o que puedan saltar por encima de ellos. El tamaño se define antes de empezar la batalla y no podrá cambiarse luego de haber empezado la misma.

## Unidad

Las unidades cuentan con un nivel de vida, cuando este nivel llega a 0, la unidad es eliminada, también cuentan con armas con las que pueden atacar a otras unidades y restarle salud.

## Arma

Las armas tienen un rango de ataque, la cantidad de daño que pueden infligir a las unidades y el porciento de acierto.

## Inteligencia artificial

Se podrán crear unidades controladas por inteligencia artificial, usando algoritmos óptimos y eficientes para las estrategias en combate.

## Lenguaje

Para controlar a las unidades, crear el campo de batalla, crear las armas y demás se utilizara un Domain Specific Language llamado `awars`. Cuenta con las principales funcionalidades de control de flujos como `if` y `while`.
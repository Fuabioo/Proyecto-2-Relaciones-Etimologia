Decisiones de diseño
===

Procesamiento de datos 
---

El procesamiento de datos es una parte vital del proyecto 2.
Para llevar a cabo el proyecto se nos suministró un archivo de 298MB **(etymwn.tsv)** que contiene una enorme cantidad de relaciones entre distintos términos en diversos lenguajes.
Cargar dicho archivo es relativamente costoso para un programa de Python, pero manejable. Sin embargo los datos no pueden ser utilizados así como están por pyDatalog. Es necesario hacer un preprocesamiento de los datos, que tiene un costo importante en tiempo.
Los cambios que se deben realizar a los datos son:

- Eliminar `-` al final de palabras (Eliminar signo que indica sufijo).
- Transcribir todas las palabras a minúscula debido a cómo pyDatalog interpreta los términos dentro de las cláusulas.
- Eliminar los cambios de línea.
- Partir las líneas de texto para poder utilizar cada palabra por separado.
- Formar cláusulas con la forma `regla("palabra1", "palabra2")`.
- Definir que las palabras pertenecen a su respectivo lenguaje.
- Agregar un `+ ` antes de cada cláusula para poder realizar consultas.

Para atacar algunos de estos inconvenientes se tomó la decisión de:
- Cambiar el caracter `"` que traían varias de las palabras por `'` para poder rodear cada palabra con  `"` y así eliminar el problema con los `-` al inicio o final de las palabras.

Teniendo en mente que la eficiencia es esencial en este proyecto debido al tamaño de la *Knowledge Base* KB, el equipo de trabajo decidió:

- Realizar un preprocesamiento del archivo `.tsv` de manera que los cambios sólo hubiese que hacerlos 1 vez, lo que reduce el tiempo de ejecución/carga considerablemente.
- Crear un archivo nuevo que contiene todos los cambios previamente mencionados, llamado `cl.cl`

Ejemplo de la versión 1 de la transcripción desde archivo `.tsv` a archivo `.cl`:

En el `.tsv`
```py
afr: aanvaller	rel:etymologically_related afr:aanvallend
```
En el `.cl` versión 1
```py
+ hasWord(afr," aanvaller")
+ hasWord(afr," aanvallend")
+ etymologically_related(" aanvaller"," aanvallend")
```
De esta manera nos ahorramos tener que preprocesar todos los datos con cada corrida del proyecto. Sin embargo esto nos planteó otro problema de diseño: El archivo que hay que cargar con `pyDatalog.load()` es 3 veces más grande que el original archivo `.tsv`.
Una de las ideas planteadas para solucionar este inconveniente fue condensar las cláusulas por cada relación en una sola. De manera que `afr: aanvaller rel:etymologically_related afr:aanvallend` pasara a ser `etymologically_related(" aanvaller", afr ," aanvallend", afr)` y así ahorrar 2 líneas en el archivo `.cl` por cada relación.
De esta manera sería más manejable la carga inicial de la KB pero habría que hacer las consultas más complejas.

En la siguiente tabla se muestran los tiempos de ejecución promedio de 20 corridas para 60.000 relaciones (180.000 líneas en el `.cl` / 60.000 lineas en el `.tsv`):

| | Desde el .tsv | Desde el .cl v1 |
| - | - | - |
| **Total** | 62.00s | 20.19s |
| **Parsing** | 41.70s | ---- |
| **Loading** | 20.15s | 20.19s |
| **Total Estimado para 6.031.431** | 6200s | 2020s |

El total para 6.031.431 se estima por la naturaleza lineal de los algoritmos implementados (6000 relaciones tardan 6s/2s respectivamente).



# Proyecto-2-Relaciones-Etimología

Manual de usuario
===

Instalación
---

Para instalar este proyecto simplemente se abre una consola en la carpeta raíz del proyecto y se ejecuta el siguiente comando:

```batch
python setup.py install
```

Para llamar al módulo instalado, hay un ejemplo en la carpeta *test* de este repositorio, esta contiene un archivo para ejecutar el proyecto con interfaz gráfica y una carpeta con los archivos de datos, simulando el comportamiento en la vida real luego de instalar el paquete.
La carpeta *database* es total y absolutamente necesaria para la ejecución del proyecto ya que los módulos buscan la carpeta en el directorio desde donde se ejecuta el código.
El archivo *gui_testing.py* contiene las siguientes lineas, que básicamente se explican por si solas:

```python
from tec.ic.ia.p2.g08_controller import Controller

def main():
    """Creates and runs the gui"""
    controller = Controller()  # debug=True)
    controller.run()

if __name__ == '__main__':
    main()
```

básicamente se carga el controlador de la librería y se corre. O, también existe la alternativa:

```python
from tec.ic.ia.p2.g08_gui_testing import main

if __name__ == '__main__':
    main()
```

Uso
---

El sistema de relaciones de etimología posee una interfaz gráfica ideada para hacer las consultas con la menor cantidad de acciones posibles, esto con la finalidad de acelerar el proceso de uso.
![Interfaz](https://github.com/Fuabioo/Proyecto-2-Relaciones-Etimologia/blob/master/addons/Manual_1.PNG "Interfaz")
- A la izquierda se encuentra la **consola**. En ella se muestran los datos relevantes a las consultas realizadas, y mensajes de error al ejecutar consultas.
- Bajo **"Select Relations"** se encuentran todas las relaciones presentes en la base de datos con las cuales se puede hacer consultas. Debe seleccionar una o varias para poder realizar una consulta. Si una de las relaciones no existe en la base de datos para el contexto específico que se solicita (si no existe esa relación para los idiomas seleccionados), en la consola se mostrará el mensaje de error.
- El botón de **"Search"** (Color verde) se encarga de realizar la consulta con los datos suministrados por el usuario. Sobre este botón se encuentra un texto que indica cuál tipo de consulta se tiene seleccionada. 
- El botón **"Clear Console"** (Color amarillo) borra el contenido de la consola.
- El botón **"Clear Form"** (Color rojo) borra el contenido de las casillas de idiomas y palabras; así como los resultados mostrados bajo dichas casillas.
- Bajo **"Select Query Form"** se encuentran los tipos de consulta disponibles. Word-Word para hacer consultas entre 2 palabras específicas; Idiom-Word para hacer consultas entre un idioma y una palabra específica e Idiom-Idiom para hacer consultas entre 2 idiomas específicos (o 1 solo idioma). Al hacer click en cualquiera de estos botones, en la parte derecha se despliega los campos para llenar los idiomas y las palabras.

Al seleccionar Word-Word se despliega el siguiente contenido:

![Word-Word](https://github.com/Fuabioo/Proyecto-2-Relaciones-Etimologia/blob/master/addons/Manual_WW.PNG "Word-Word")  

- **Idiom#1**, **Word#1**, **Idiom#2**, **Word#2** reciben el idioma#1, palabra#1, idioma#2 y palabra#2 respectivamente.

Una vez rellenados los campos solicitados, puede hacer click sobre uno o varios de los siguientes botones para realizar las consultas deseadas:

- **Brothers?** Si la palabra#1 del idioma#1 es hermana de la palabra#2 del idioma#2. Muestra "True" o "False" en el campo anexo.
- **Child?** Si la palabra#1 del idioma#1 es hija de la palabra#2 del idioma#2. Muestra "True" o "False" en el campo anexo.
- **Uncle?** Si la palabra#1 del idioma#1 es tía de la palabra#2 del idioma#2. Muestra "True" o "False" en el campo anexo.
- **Cousins?** Si la palabra#1 del idioma#1 y la palabra#2 del idioma#2 son primas (de primer grado). Muestra "True" o "False" en el campo anexo.
- **Cousin_Level** Si la palabra#1 del idioma#1 y la palabra#2 del idioma#2 son primas (de cualquier grado). Muestra "True" o "False" en el campo anexo. Muestra el grado en la consola con el formato `{(grado,)}`

Al seleccionar Idiom-Word se despliega el siguiente contenido:

![Idiom-Word](https://github.com/Fuabioo/Proyecto-2-Relaciones-Etimologia/blob/master/addons/Manual_IW.PNG "Idiom-Word")  

- **Idiom**, **Word's Idiom**, **Word** reciben el idioma a comparar, el idioma de la palabra a comparar y la palabra a comparar respectivamente.

Una vez rellenados los campos solicitados, puede hacer click sobre uno o varios de los siguientes botones para realizar las consultas deseadas:

- **Related?** Si la palabra "Word" del idioma "Word's Idiom" es hija o padre de alguna palabra del idioma "Idiom". Muestra "True" o "False" en el campo anexo. Muestra las palabras relacionadas en la consola (No todas, dada la naturaleza de la búsqueda, solo muestra los padres en caso de tenerlos).
- **Originated** Las palabras del idioma "Idiom" que son hijas de la palabra "Word" del idioma "Word's Idiom"". Muestra "True" o "False" en el campo anexo. Muestra las palabras originadas en la consola.
- **List related** Los idiomas que tienen padres o hijos de la palabra "Word" del idioma "Words's Idiom". Muestra "True" o "False" en el campo anexo. Muestra los idiomas de las palabras relacionadas en la consola.

Al seleccionar Idiom-Idiom se despliega el siguiente contenido:

![Idiom-Idiom](https://github.com/Fuabioo/Proyecto-2-Relaciones-Etimologia/blob/master/addons/Manual_II.PNG "Idiom-Idiom")  

- **Idiom#1** e **Idiom#2** reciben el idioma#1 y el idioma#2 respectivamente.

Una vez rellenados los campos solicitados, puede hacer click sobre uno o varios de los siguientes botones para realizar las consultas deseadas:

- **Common amount** La cantidad de palabras en común que tienen ambos idiomas. Muestra el resultado en la consola con la forma `{(cantidad_en_común,)}`
- **Common** Todas las palabras en común que tienen ambos idiomas. Muestra el resultado en la consola con la forma `{(palabra1,), (palabra2,), (palabra3,), ...}`
- **Contributed most** El idioma que más contribuyó (Padre->Hijo) al idioma#1. Muestra el resultado en la consola con la forma  `Idiom: idioma', Percentage: porcentaje`
- **Idiom list** Todos los idiomas que contribuyeron (Padre->Hijo) al idioma#1. Muestra el resultado en la consola con la forma  
	```
		idioma1:porcentaje1
		idioma2:porcentaje2
		idioma3:porcentaje3
		...
	```


Decisiones de diseño
===

Patrones
---
Con el objetivo de tener una división clara entre los componentes del proyecto, se origino el siguiente modelo, basado en la implementación clásica de MVC:

![Diagrama 1](https://github.com/Fuabioo/Proyecto-2-Relaciones-Etimologia/blob/master/addons/Diagram_1.png "Diagrama 1")  

**Model**: Contiene toda la lógica (Modelos) correspondiente a los datos y su almacenamiento, es la coneccion con la base de datos etimológica. Ya que con la implementación hilos (Threads), se separan las lógicas, entonces se modelo multiplicidad para este aspecto de la implementación con el fin de que cada hilo maneje una pequeña parte de la base de datos, y así, convertir un modelo que tendría complejidad algoritmica de <a href="https://www.codecogs.com/eqnedit.php?latex=$2^n$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$2^n$" title="$2^n$" /></a>, a <a href="https://www.codecogs.com/eqnedit.php?latex=$\sum&space;k_i^2$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$\sum&space;k_i^2$" title="$\sum k_i^2$" /></a> con <a href="https://www.codecogs.com/eqnedit.php?latex=$\sum&space;k_i&space;=&space;n$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$\sum&space;k_i&space;=&space;n$" title="$\sum k_i = n$" /></a>, lo cual en el caso de que se necesite cargar todas las relaciones de todos lo idiomas termina siendo igual a   <a href="https://www.codecogs.com/eqnedit.php?latex=$2^n$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$2^n$" title="$2^n$" /></a>, y es mejor en  cualquier otro caso. 

**View**: Encapsula todo lo relacionado con la interfaz gráfica, cuenta con todas las funciones para obtener inputs y mostrar outputs en la parte gráfica. Esto incluye:
 - Elección de relaciones a utilizar.
 - La consola en la que se imprimen los procesos internos en ejecución.
 - La selección de consultas a ejecutar.
 - Las entradas de las consultas.  

De esta manera, en caso de que el programa se caiga en alguna parte, las otras no se ven afectadas, ya que esta "capa", se encuentra lo más separada posible de la o las implementaciones.  

**Controller**: Es quien controla la interfaz gráfica, crea y sincroniza los hilos, y selecciona mediante uso de un strategy basado en las entradas la el tipo algoritmo a ejecutar.  

**Query**: este módulo se encarga de manejar casos en los que deben preparar para ejecución múltiples "comandos". Cada uno de estos *comandos* ejecuta una consulta, permitiendo al usuario ejecutar varias en una. Esto se logra mediante una implementación de un *command stack*, que se carga con comandos a ejecutar y en combinación con un *strategy* como el descrito anteriormente, decide en runtime cual consulta se ejecutará. Esto por cada comando.  

 > Al final la implementación difiere (manteniendo la idea principal de un modelo MVC tradicional) un poco con respecto al modelo debido a situaciones que se fueron desarrollando a lo largo del proyecto.
 > Gracias al modelo, se previnieron errores relacionados de todo tipo, haciendo la aplicación más robusta, mantenible y escalable.

Procesamiento de datos 
---

El procesamiento de datos es una parte vital del proyecto 2.
Para llevar a cabo el proyecto se nos suministró un archivo de 298MB **(etymwn.tsv)** que contiene una enorme cantidad de relaciones de diferente tipo entre distintos términos en diversos lenguajes.
Cargar dicho archivo es relativamente costoso para un programa de Python, pero manejable. Sin embargo los datos no pueden ser utilizados así como están por pyDatalog, ya que la complejidad algoritmica de un modelo logico es de <a href="https://www.codecogs.com/eqnedit.php?latex=$2^n$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$2^n$" title="$2^n$" /></a>, y como este modelo tiene más de 6 millones de relaciones esto es casi imposible de procesar para relaciones completas. Por lo anterior es necesario hacer un preprocesamiento de los datos, que tiene un costo importante en tiempo, pero solo se ejecuta una vez, ya que este se encuentra en un programa aislado, el cual crea una "base de datos" administrada de tal manera que el programa solo toma la fracción de la base que necesita.
Los cambios que se deben realizar a los datos son:

- Eliminar `-` al final de palabras (Eliminar signo que indica sufijo).
- Eliminar `-` al inicio de palabras (Eliminar signo que indica prefijo).
- Transcribir todas las palabras a minúscula debido a cómo pyDatalog interpreta los términos dentro de las cláusulas.
- Eliminar los cambios de línea.
- Partir las líneas de texto para poder utilizar cada palabra por separado.
- Definir que las palabras pertenecen a su respectivo lenguaje.
 - Formar cláusulas con la forma `regla("palabra1", "idioma1", "palabra2", "idioma2")`.
- Agregar un `+ ` antes de cada cláusula para poder realizar consultas.

Se encontraron caracteres que no eran reconocidos adecuadamente por python (aun con codificación UTF-8), los cuales "botaban" la aplicación al momento de su lectura, para atacar algunos de estos inconvenientes se tomó la decisión de:
- Cambiar el carácter `"` que traían varias de las palabras por `'` para poder rodear cada palabra con  `"` y así eliminar el problema con los `-` al inicio o final de las palabras.

Teniendo en mente que la eficiencia es esencial en este proyecto debido al tamaño de la *Knowledge Base* KB, el equipo de trabajo decidió:

- Realizar un preprocesamiento del archivo `.tsv` de manera que los cambios sólo hubiese que hacerlos 1 vez, lo que reduce el tiempo de ejecución/carga considerablemente.
- Crear una serie de  archivos nuevo que contiene todos los cambios previamente mencionados, llamados de la manera `idioma1_relacion_idioma2.cl`

Ejemplo de la versión 1 de la transcripción desde archivo `.tsv` a archivo `.cl`:

En el `.tsv`
```py
afr: aanvaller	rel:etymológically_related afr:aanvallend
```
En el `.cl` versión 1
```py
+ hasWord(afr," aanvaller")
+ hasWord(afr," aanvallend")
+ etymológically_related(" aanvaller"," aanvallend")
```
De esta manera nos ahorramos tener que preprocesar todos los datos con cada corrida del proyecto. Sin embargo esto nos planteó otro problema de diseño: El archivo que hay que cargar con `pyDatalog.load()` es 3 veces más grande que el original archivo `.tsv`. **(.cl v1)**, ya que por cada linea de el archivo `.tsv` generable 2 lineas adicionales. 
Una de las ideas planteadas para solucionar este inconveniente fue condensar las cláusulas por cada relación en una sola. De manera que `afr: aanvaller rel:etymológically_related afr:aanvallend` pasara a ser `etymológically_related(" aanvaller", afr ," aanvallend", afr)` y así ahorrar 2 líneas en el archivo `.cl` por cada relación. **(.cl v2)**. De esta manera se mantuvieron de 1 a 1 las relaciones a la hora de la transformación.

De esta manera sería más manejable la carga inicial de la KB pero habría que hacer las consultas más complejas.

En la siguiente tabla se muestran los tiempos de ejecución promedio de 20 corridas para 60.000 relaciones (180.000 líneas en el `.cl` / 60.000 líneas en el `.tsv`):

| Procesamiento de datos | Desde el .tsv | Desde el .cl v1 | Desde el .cl v2 |
| - | - | - | - |
| **Parsing** | 41.70s | ---- | ---- |
| **Loading** | 20.15s | 20.19s | 7.94s |
| **Total** | 62.00s | 20.19s | 7.94s |
| **Total Estimado para 6.031.431** | ~6200s | ~2020s |~794s |

El total para 6.031.431 se estima por la naturaleza lineal de los algoritmos implementados (6000 relaciones tardan 6s/2s respectivamente.

El tamaño de la Knowledge Base
---

Para el problema al que nos enfrentamos en la realización del proyecto, la *Knowledge Base* tiene un tamaño masivo de más de 6 Millones de relaciones lógicas que incluyen dos palabras, sus idiomas correspondientes y la relación en sí.
Cada entrada de la *Knowledge Base* tiene la forma
`relación(palabra1, idioma1, palabra2, idioma2)`

Al hacer consultas lógicas sobre un pequeño porcentaje de la *Knowledge Base* nos dimos cuenta de lo costoso que es computacionalmente realizar este tipo de consultas. Previendo los tiempos de ejecución excesivos para la realización de consultas complejas (e incluso que requieren evaluar idiomas completos) el equipo de trabajo tomó la decisión de separar la *Knowledge Base* en pedazos más pequeños y manejables dinámicamente, esto como se mencionó previamente, y por medio de un parser, se cambio la complejidad algoritmica de  <a href="https://www.codecogs.com/eqnedit.php?latex=$2^n$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$2^n$" title="$2^n$" /></a>, a <a href="https://www.codecogs.com/eqnedit.php?latex=$\sum&space;k_i^2$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$\sum&space;k_i^2$" title="$\sum k_i^2$" /></a> con <a href="https://www.codecogs.com/eqnedit.php?latex=$\sum&space;k_i&space;=&space;n$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$\sum&space;k_i&space;=&space;n$" title="$\sum k_i = n$" /></a>, lo cual en el caso de que se necesite cargar todas las relaciones de todos lo idiomas termina siendo igual a   <a href="https://www.codecogs.com/eqnedit.php?latex=$2^n$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$2^n$" title="$2^n$" /></a>, y es mejor en  cualquier otro caso, pero también habrá un tiempo de carga por cada consulta, mientras se crea carga la porción del database requerida a la aplicación.

De esta forma se clasifican las relaciones en archivos más pequeños con nombres descriptivos de la forma `idioma_relacion_idioma.cl`. Por ejemplo: **afr_etymológically_eng.cl**

-  Idioma se toma como las 3 siglas utilizadas como estándar por la base de datos original
- El segundo idioma puede ser reemplazado por un `*` en caso de necesitar cargar la relación específica entre el primer idioma y todos los demás idiomas

La **generación** de todos estos archivos pequeños clasificados nos arrojó los siguientes datos:

| Relación | Cantidad total | **Tiempo de ejecución**: 795.48s |
| - | - | - |
| derived | 2 | - |
| etymológical_origin_of| 473433|- | 
| etymológically| 1 | -| 
| etymológically_related| 538558 | -| 
| etymology| 473433|- | 
| has_derived_form| 2264744|- | 
| is_derived_from| 2264744|- | 
| variant:orthography|16516| -|

Como se puede observar, `has_derived_form` e `is_derived_from` tienen la misma cantidad de relacionesm; al igual que `etymológical_origin_of` e `etymology` , lo que indica que pueden tener las mismas relaciones pero a la inversa. Para comprobarlo se desarrolló un script que se aseguraba de que cada relación estuviera representada en su contraparte pero a la inversa. El script produjo un resultado positivo, por lo cual se tomó la decisión de eliminar tanto `is_derived_from` como `etymology` para simplificar las búsquedas.

El archivo más pesado después de la generación  es "*lat_has_derived_form_lat.cl*" con un tamaño de 32,1 MB y 607.989 relaciones, por lo que el "peor escenario" es cuando el sistema tiene que buscar una relación *has_derived_form* de *lat* a *lat*, entre otras.

Con respecto al **tiempo de carga** con esta tercera iteración de la base de datos **(.cl v3)**, debido a su naturaleza dinámica; el tiempo de carga se redujo inmensamente. 

| Procesamiento de datos | Desde el .tsv (60mil) | Desde el .cl v1 (60mil)| Desde el .cl v2 (60mil) | Desde los .cl v3|
| - | - | - | - | - |
| **Parsing** | 41.70s | ---- | ---- | 795s (total, solo 1 vez) |
| **Loading** | 20.15s | 20.19s | 7.94s | 79.65s (peor escenario) |
| **Total** | 62.00s | 20.19s | 7.94s | ---- |
| **Total (Estimado) para 6.031.431** | ~6200s | ~2020s |~794s |  |

Cabe destacar que una vez se realiza la carga para un tipo de relación usando el método **v3**, esta permanece en memoria, por lo que no es necesario cargar de nuevo, pero se debe volver a crear knowledge base (automáticamente).

Las consultas propiamente se ejecutan en un espacio reducido de la KB, que contiene únicamente lo necesario para satisfacer dichas consultas.

PyDatalog nos brinda la función `pyDatalog.Logic()`, mediante la cual se puede manipular la *Knowledge Base* de diferentes maneras. 
- Es posible crear un nuevo set de cláusulas vacías utilizando `pyDatalog.Logic()`
- Es posible guardar el set de cláusulas actual utlilizando `kb1 = pyDatalog.Logic(True)`
- Es posible cargar un set de cláusulas existente utilizando `pyDatalog.Logic(kb1)`

De este modo podemos hacer manejo de las partes de la *Knowledge Base* dinámicamente por medio de hilos, ya que el uso de la función *pyDatalog.Logic* es exclusivo para cada hilo. De esta manera realizar consultas se esta utilizando únicamente los recursos de búsqueda necesarios.

| Realizar consultas (1 tipo de relación) | Set único (60.000) | Set separado | - |
| - | - | - | - |
| **Promedio brothers** | 0.001s |  | |
| **Promedio uncle** | 0.014s |  | |
| **Promedio cousin** | 6.112s |  | |
| **Promedio total estimado para 6.031.431** | ~611s | ~s | |

Los datos de "set separado" varían dependiendo del tamaño de la KB.

Interpretación de las relaciones
-

Todas las relaciones presentes el la base de datos junto con las interpretaciones que se les da en el proyecto se listan a continuación:

| Relación | Interpretación |
|- |- |
|derived | Padre -> hijo |
|etymológically | Padre -> hijo|
|etymológical_origin_of | Padre -> hijo|
|has_derived_form | Padre -> hijo|
|etymológically_related | Hijo -> padre|
|variant:ortography | Hijo -> padre|

Para la formulación de consultas, se maneja internamente de manera que se estandariza la naturaleza padre-hijo/hijo-padre para realizar consultas consistentes.

![Diagrama 2](https://github.com/Fuabioo/Proyecto-2-Relaciones-Etimologia/blob/master/addons/Diagram_2.png "Diagrama 2")  

En este diagrama se detallan las definiciones de relaciones familiares que se utilizaron el proyecto. Por lo tanto todo lo programado en este, está basado en estas.

Adicionalmente, para hacer búsquedas en la base de datos es necesario formular consultas de acuerdo con las solicitadas para el proyecto:

| Relación | Interpretación | Significado |
|- |- | - |
| **Palabra-Palabra** | - | - |
|brother(X,Xi,Y,Yi) | hermano <-> hermano | ¿X es hermano de Y? |
|child(X,Xi,Y,Yi)| hijo -> padre | ¿X es hijo de de Y? |
|uncle(X,Xi,Y,Yi)| Tío -> Sobrino| ¿X es tío de de Y? |
|cousin(X,Xi,Y,Yi)|Primo <-> Primo| ¿X es primo de de Y? |
|cousin_level(X,Xi,Y,Yi,G)|Primo <-> Primo| ¿X es primo de de Y? (Adiciona el grado), se toman como primos 2 a los hijos de los primos, como primos 3 a los hijos de los primos 2, y asi sucesivamente|
| **Idioma-Palabra** | - | - |
|related(Xi,Y,Yi)|Padre <-> hijo| ¿Existe una palabra del idioma Xi relacionada padre->hijo o hijo->padre con Y? |
|originated(Xi,Y,Yi)|Padre -> hijo| Todas las palabras de las que Y es padre en el idioma Xi|
|listing(X, Xi)|Hijo <-> padre| Todos los idiomas que tienen palabras hijos o padres de X|
| **Idioma-Idioma** | - | - |
|igualesEntreIdiomas(I1,I2,X)|Idioma1, Idioma2, Resultado|Todas las palabras que se encuentra en el idioma 1 y a su vez en el idioma 2| 
|Y==len( igualesEntreIdiomas(I1,I2,X))|Idioma1, Idioma2, Resultado|La cuenta de todas las palabras que se encuentra en el idioma 1 y a su vez en el idioma 2|
|aporte(I1,I2,X)|Idioma1, Idioma2, Resultado|Todas las palabras de Idioma 1 cuyo padre se encuentra en idioma 2|

Resultados interesantes
===
Heman@s 
-
Se considera que atacar, del idioma español y taqueria, tambien en español, son hermanos bajo la regla has derived form, ya que tienen un padre comun que es taco

Prim@s
-
Se considera que tacones, del idioma español y ataca, tambien en español, son primos bajo la regla has derived form, ya que tienen un abuelo comun que es taco

Hij@s
-
Se considera que atacar, tacos, tacon, taqueria y taquito del idioma español son hijos de taco, tambien en español, bajo la regla has derived form

Ti@
-
Se considera que tacon del idioma español es tio de ataca, tambien en español, bajo la regla has derived form

Prim@s
-
Se considera que tacones del idioma español es primo de atacada, tambien en español, bajo la regla has derived form, pero en este caso es primo en grado 1,2,3,4 a la ves, ya que hay muchos caminos que determinan que son primos.

Distribución del Trabajo
===
| Tarea| Fabio| Sergio| Gabriel| 
| - | - | - | - |
| **lógica** | Si | Si | Si |
| **Desarrollo de interfaz** | Si | No | No |
| **Carga de archivos** | Si | Si | Si |
| **Generación de archivos** | No | Si | Si |
| **Investigación** | Si | Si | Si |
| **Documentacion** | Si | Si | Si |
| **Nota** | 100 | 100 | 100 |

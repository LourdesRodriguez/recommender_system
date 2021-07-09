# recommender_system
## Recomendador de Juegos de Mesa

El mercado de los juegos de mesa está en crecimiento en los últimos años. Aunque en España es desconocido, en el norte de Europa está muy consolidado. 
Con el fin de acercar a los usuarios este tipo de juegos, he basado mi TFM en crear un Recomendador de Juegos de Mesa. Así cada usuario puede conocer los juegos que mejor se adaptan a sus preferencias/gustos.


## Estructura del proyecto
Este proyecto se compone de 3 notebooks y una única carpeta.

- Data : Almacena todos los datos originales y generados durante la ejecución de los notebooks. Estos datos se encuentran en formato csv. Dentro de esta carpeta también encontramos los modelos generados, la imagen insertada en el visualizador y los dataset finales para la implementación del recomendador.

## Orden de ejecución
En este punto se explica la secuencia de lectura de los cuadernos para ver todo el proceso llevado a cabo.
Para ejecutar el proyecto correctamente se deberán **DESCARGAR** los datos de drive (**link dentro del notebook 1_Prepair_the_environment**) para una correcta ejecución.
Como se ha comentado en el apartado anterior dentro del repositorio existe una carpeta de datos (DATA) pero debido a lo pesados que son algunos dataset se ha omitido parte del contenido de los mismos en la subida a GitHub.
Tras descargar los datos, se deberán guardar en la misma ruta en la que aparecen dentro del repositorio.

El orden de lectura es el siguiente:

- 1_Prepair_the_Environment.ipynb en este notebook se muestran las librerías necesarias y la metodología a seguir, tanto al inicio como para la visualización del Recomendador.

- 2_Data_understanding.ipynb en este notebook se muestra el proceso realizado para el tratamiento de los datos, así como un análisis visual de los mismos para poder entender cada una de las variables.

- 3_Recommender_Systen.ipynb en este cuaderno se desarrollan los algoritmos de recomendación y todos los pasos necesarios para su posterior implementación en Streamlit.

## Streamlit 
La implementación y visualización de resultados se realiza con streamlit. Para una correcta ejecución será necesario instalar la librería.
Para ejecutar la aplicación con streamlit.

*streamlit run 20210704_streamlit.py*

Al ejecutar la sentencia se abre la aplicación.
Para comenzar debemos seleccionar el algoritmo deseado para la recomendación (Popularity, Content Based, Collaborative Filtering). 
Tras seleccionar el algoritmo, indicamos cual es nuestro juego de mesa preferido.
Y por último hacemos clik en el botón de recomendación.
Si todo funciona correctamente, deberiamos obtener como resultado una recomendación de 10 juegos de mesa.






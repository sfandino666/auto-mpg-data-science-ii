# Análisis de eficiencia de combustible - Auto MPG

## Proyecto

Proyecto correspondiente a la asignatura **Programación para Ciencia de Datos II** de la Fundación Universitaria Compensar.

El proyecto analiza el conjunto de datos **Auto MPG**, con el objetivo de estudiar la relación entre las características de los vehículos y su eficiencia de combustible.

## Problema de análisis

La pregunta inicial del proyecto fue:

> ¿Los vehículos más pesados presentan una menor eficiencia de consumo de combustible?

La variable objetivo utilizada fue `mpg`, mientras que una de las principales variables explicativas fue `weight`.

## Datos

El conjunto de datos contiene información sobre vehículos y las siguientes variables principales:

- `mpg`: eficiencia de combustible.
- `cylinders`: número de cilindros.
- `displacement`: desplazamiento del motor.
- `horsepower`: potencia.
- `weight`: peso del vehículo.
- `acceleration`: aceleración.
- `model-year`: año del modelo.

El conjunto contiene 398 registros.

## Modelamiento

Durante el proyecto se evaluaron diferentes estrategias:

1. Regresión lineal simple utilizando `weight`.
2. Regresión lineal múltiple utilizando `weight`, `horsepower` y `displacement`.
3. Tratamiento de valores faltantes mediante imputación por la mediana.
4. Experimentación con regularización Ridge y diferentes valores de `alpha`.
5. Creación de la característica `power_to_weight`.
6. Evaluación del posible sobreajuste mediante comparación entre entrenamiento y prueba.

## Resultado del modelo mejorado

La incorporación de la característica `power_to_weight`, calculada como:

`horsepower / weight`

permitió mejorar el rendimiento del modelo.

Resultados obtenidos:

- **MSE:** 15.1068
- **MAE:** 3.1717
- **R²:** 0.7368

El modelo explica aproximadamente el 73.68 % de la variabilidad de `mpg` en el conjunto de prueba utilizado.

## Dashboard

El proyecto incluye un dashboard interactivo desarrollado con **Dash y Plotly**.

El dashboard contiene:

- Indicador de MPG promedio.
- Indicador de peso promedio.
- Indicador R² del modelo.
- Indicador MAE del modelo.
- Gráfica de peso vs. MPG.
- Gráfica de MPG según número de cilindros.
- Gráfica de `power_to_weight` vs. MPG.
- Filtro interactivo por número de cilindros.
- Sección de interpretación de resultados.

## Instalación

Para instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```

## Ejecución

El dashboard puede ejecutarse mediante:

```bash
python app.py
```

## Archivos principales

- `app.py`: aplicación del dashboard.
- `auto-mpg.csv`: conjunto de datos utilizado.
- `requirements.txt`: dependencias necesarias.
- `README.md`: documentación del proyecto.

## Autor

Juan Sebastián Fandiño Castañeda

Fundación Universitaria Compensar
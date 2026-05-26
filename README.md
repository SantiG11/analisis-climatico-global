# Análisis de Datos Climáticos Globales

## Objetivo del proyecto

Analizar datos climáticos globales mediante Python, aplicando un flujo de trabajo organizado con Jira, Git, GitHub y Google Colab.

El proyecto busca calcular indicadores estadísticos básicos, generar resultados reproducibles y documentar el proceso de trabajo mediante una simulación de célula de desarrollo.

## Roles simulados

- P1 - Hugo: líder y organizador del proyecto.
- P2 - Paco: desarrollador técnico del análisis.
- P3 - Luis: revisor y responsable de calidad.

## Dataset utilizado

Se utilizó el dataset Global Temperature.

El dataset contiene registros históricos de anomalías de temperatura global. Las columnas principales utilizadas son:

- `Source`: fuente de los datos.
- `Year`: año del registro.
- `Mean`: anomalía media de temperatura global.

Debido a que el dataset seleccionado no incluye precipitaciones, el análisis se centra en indicadores estadísticos asociados a la evolución de la temperatura global.


## Estructura del repositorio

- `/datos`: contiene el dataset utilizado en el análisis.
- `/scripts`: contiene el script principal del proyecto.
- `/resultados`: contiene los archivos generados por el análisis.
- `README.md`: documenta el objetivo, estructura y ejecución del proyecto.
- `.gitignore`: evita subir archivos temporales o innecesarios al repositorio.

## Script principal

El análisis se ejecuta desde el archivo:

```bash
scripts/analisis_climatico.py
```

Para reproducir el análisis, desde la raíz del repositorio ejecutar:

```bash
python scripts/analisis_climatico.py
```

## Resultados generados

El script genera los siguientes archivos dentro de la carpeta `/resultados`:

- `resumen_general.csv`: contiene indicadores generales del dataset, como promedio, valor máximo, valor mínimo, año con mayor anomalía, año con menor anomalía y cantidad de registros.
- `resumen_por_fuente.csv`: contiene estadísticas agrupadas por fuente de datos.
- `grafico_anomalia_temperatura.png`: muestra la evolución de la anomalía de temperatura global a lo largo del tiempo.

## Herramientas utilizadas

| Herramienta | Uso en el proyecto | Justificación |
|---|---|---|
| Jira | Organización de tareas e issues. | Permite ordenar el trabajo y seguir el avance. |
| Git | Control de versiones local. | Permite registrar los cambios realizados. |
| GitHub | Repositorio remoto y Pull Request. | Permite guardar, compartir y revisar el proyecto. |
| Google Colab | Entorno de trabajo para ejecutar Git y Python. | Permite trabajar sin instalación local. |
| Python | Desarrollo del script de análisis. | Es adecuado para procesar datos de forma simple. |
| Pandas | Lectura y análisis del CSV. | Facilita el trabajo con datos tabulares. |
| Matplotlib | Creación del gráfico final. | Permite representar visualmente los resultados. |

## Buenas prácticas aplicadas

- Organización del repositorio en carpetas separadas para datos, scripts y resultados.
- Uso de ramas para separar el desarrollo de la rama principal.
- Commits vinculados a issues de Jira mediante el identificador correspondiente.
- Revisión del trabajo mediante Pull Request.
- Uso de `.gitignore` para evitar archivos temporales o innecesarios.
- Evitación de credenciales, tokens o información sensible dentro del repositorio.
- Uso de rutas relativas para favorecer la reproducibilidad del proyecto.

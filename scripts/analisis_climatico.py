from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Se utilizan rutas relativas para que el proyecto pueda ejecutarse
# correctamente desde Google Colab o desde cualquier entorno clonado.
ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT_DIR / "datos" / "global_temp_anual.csv"
RESULTS_DIR = ROOT_DIR / "resultados"

# El script asume que la estructura de carpetas fue creada previamente
# por el rol P1 - Hugo durante la inicialización del repositorio.
if not DATA_PATH.exists():
    raise FileNotFoundError("No se encontró el archivo de datos en /datos.")

if not RESULTS_DIR.exists():
    raise FileNotFoundError("No se encontró la carpeta /resultados.")

# Carga del dataset climático global.
df = pd.read_csv(DATA_PATH)

# Limpieza básica: se eliminan registros incompletos en las columnas necesarias
# para evitar errores en los cálculos estadísticos.
df = df.dropna(subset=["Source", "Year", "Mean"])

# Conversión de columnas numéricas para asegurar que los cálculos sean correctos.
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["Mean"] = pd.to_numeric(df["Mean"], errors="coerce")
df = df.dropna(subset=["Year", "Mean"])

# Cálculo de indicadores estadísticos generales.
resumen_general = {
    "promedio_anomalia": df["Mean"].mean(),
    "maxima_anomalia": df["Mean"].max(),
    "minima_anomalia": df["Mean"].min(),
    "año_maxima_anomalia": int(df.loc[df["Mean"].idxmax(), "Year"]),
    "año_minima_anomalia": int(df.loc[df["Mean"].idxmin(), "Year"]),
    "cantidad_registros": len(df)
}

# Cálculo de indicadores agrupados por fuente de datos.
resumen_por_fuente = df.groupby("Source")["Mean"].agg(
    promedio="mean",
    maxima="max",
    minima="min",
    cantidad_registros="count"
).reset_index()

# Exportación de resultados para dejar evidencia reproducible del análisis.
pd.DataFrame([resumen_general]).to_csv(
    RESULTS_DIR / "resumen_general.csv",
    index=False
)

resumen_por_fuente.to_csv(
    RESULTS_DIR / "resumen_por_fuente.csv",
    index=False
)

# Generación del gráfico de evolución temporal de la anomalía de temperatura.
plt.figure(figsize=(10, 6))

for source in df["Source"].unique():
    datos_fuente = df[df["Source"] == source]
    plt.plot(datos_fuente["Year"], datos_fuente["Mean"], label=source)

plt.title("Evolución de la anomalía de temperatura global")
plt.xlabel("Año")
plt.ylabel("Anomalía de temperatura media global (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(RESULTS_DIR / "grafico_anomalia_temperatura.png")
plt.close()

print("Análisis climático finalizado correctamente.")
print("Resumen general:")

for clave, valor in resumen_general.items():
    print(f"{clave}: {valor}")

print("\nArchivos generados en la carpeta /resultados:")
print("- resumen_general.csv")
print("- resumen_por_fuente.csv")
print("- grafico_anomalia_temperatura.png")

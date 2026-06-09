# %% [markdown]
# # 📊 Análisis Exploratorio de Datos (EDA)
# 
# El objetivo de este proyecto es analizar un dataset de usuarios de Netflix para identificar los patrones de comportamiento que influyen en la suscripción de la plataforma.

# %% [markdown]
# 1. CARGA DE LIBRERÍAS

# %%
import numpy as np
import pandas as pd
import openpyxl as xc
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

# %% [markdown]
# 2. CARGA DE DATOS

# %% [markdown]
# ## 📥 Carga de datos
# 
# Se cargan los distintos archivos disponibles, incluyendo el dataset principal en formato CSV y una tabla adicional en formato Excel.

# %%
# CSV principal
netflix_01 = pd.read_csv(r"C:\Users\vanes\OneDrive\Escritorio\Proyecto final\netflix_user_behavior_dataset.csv")
# Excel adicional
netflix_02 = pd.read_excel(r"C:\Users\vanes\OneDrive\Escritorio\Proyecto final\netflix_content_dataset.xlsx")

# %% [markdown]
# 3. EXPLORACIÓN INICIAL DEL DATASET PRINCIPAL

# %% [markdown]
# ## 🔍 Exploración inicial
# 
# Se realiza un análisis preliminar de los datos para entender su estructura, tipos de variables, presencia de valores nulos y posibles duplicados.

# %%
netflix_01.head()

# %%
netflix_01.shape

# %%
netflix_01.info()

# %%
netflix_01.describe()

# %%
netflix_02.head()

# %%
netflix_02.shape

# %%
netflix_02.info()

# %%
netflix_02.describe().round(2)

# %% [markdown]
# 4. LIMPIEZA BÁSICA DEL CSV

# %% [markdown]
# ## 🧹 Limpieza superficial de datos
# 
# En esta fase se procede a:
# 
# - tratar valores nulos
# - comprobar la existencia de valores duplicados

# %%
netflix_01.isnull().sum()

# %%
netflix_01.duplicated().sum()

# %%
netflix_02.isnull().sum()

# %%
netflix_02.duplicated().sum()

# %% [markdown]
# 5. UNIÓN DE DATASETS (MERGE)

# %% [markdown]
# ## 🔗 Integración de datos
# 
# Se genera una tabla de interacciones simuladas entre usuarios y contenido para integrar ambos datasets mediante user_id y content_id.

# %%
interactions = pd.DataFrame({
    "user_id": np.random.choice(netflix_01["user_id"], 50000),
    "content_id": np.random.choice(netflix_02["content_id"], 50000)
})

# %%
netflix = (
    interactions
    .merge(netflix_01, on="user_id")
    .merge(netflix_02, on="content_id")
)

# %% [markdown]
# 6. LIMPIEZA FINAL

# %% [markdown]
# ## 🧹 Limpieza y preparación de datos
# 
# En esta fase se procede a:
# 
# - eliminar columnas irrelevantes
# - transformar variables
# 
# El objetivo es obtener un dataset limpio y consistente para el análisis.

# %%
netflix = netflix.drop(columns=["subgenre"])

# %%
netflix["release_year"] = netflix["release_year"].astype("category")

# %% [markdown]
# 8. VERIFICACIÓN FINAL DEL DATASET

# %% [markdown]
# Comprobación final de los datos previo al análisis

# %%
netflix.head()

# %%
netflix.shape

# %%
netflix.info()

# %%
netflix.describe().round(2)

# %%
netflix.isnull().sum()

# %% [markdown]
# El dataset presenta un bajo porcentaje de valores nulos, principalmente en variables relacionadas con el contenido.

# %%
netflix.duplicated().sum()

# %% [markdown]
# Se detectan duplicados esperados debido a la simulación de interacciones entre usuarios y contenido.

# %% [markdown]
# 9. ANÁLISIS UNIVARIADO

# %% [markdown]
# ## 📊 Análisis univariado
# 
# Se analiza cada variable de forma individual para comprender su distribución, detectar valores atípicos y evaluar su comportamiento.

# %% [markdown]
# 9.1. SEPARAR VARIABLES

# %%
numericas = netflix.select_dtypes(include="number")
numericas.head()

# %%
categoricas = netflix.select_dtypes(include=["object", "category"])
categoricas.head()

# %% [markdown]
# 9.2. VARIABLES NUMÉRICAS

# %%
netflix["age_group"] = pd.cut(
    netflix["age"],
    bins=[18, 25, 35, 45, 60, 80],
    labels=["18-25", "26-35", "36-45", "46-60", "60+"]
)

# %% [markdown]
# Se procede a agrupar las edades de los suscriptores para facilitar la lectura de los gráficos y evitar que se saturen.

# %%
sns.countplot(x="age_group", data=netflix)
plt.title("Distribución por grupo de edad")
plt.show()

# %% [markdown]
# En este gráfico se puede observar cómo los grupos de edad centrales son los que cuentan con mayor número de suscriptores, siendo el grupo de (46-60) el que ocupa el primer lugar, mientras que entre 26 y 45 están bastante equiparados. También se observa que el grupo de (+60) es el que cuenta con menor número de suscriptores.

# %%
netflix["watch_time_group"] = pd.cut(
    netflix["avg_watch_time_minutes"],
    bins=[0, 30, 60, 120, 180, 300],
    labels=["<30", "30-60", "60-120", "120-180", "180+"]
)

# %% [markdown]
# Al igual que con las edades, se agrupan las medias de los minutos visualizados para facilitar la lectura de los gráficos posteriores.

# %%
sns.countplot(x="watch_time_group", data=netflix)
plt.title("Grupos de minutos vistos")
plt.show()

# %% [markdown]
# Se observa en la gráfica que hay una gran diferencia entre los usuarios que cuentan con más de 180 min visualizados de media y el grupo anterior (120-180). Esto refleja un gran consumo de minutos visualizados en la plataforma por la gran mayoría de los usuarios.

# %%
netflix["completion_group"] = pd.cut(
    netflix["completion_rate"],
    bins=[0, 50, 75, 90, 100],
    labels=["Bajo", "Medio", "Alto", "Muy alto"]
)

# %% [markdown]
# En el ratio de sesiones completadas en la plataforma también se sustituyen los valores numéricos por categorías (Bajo, Medio, Alto y Muy alto) para evitar la saturación del gráfico.

# %%
sns.countplot(x="completion_group", data=netflix)
plt.title("Nivel de finalización")
plt.show()

# %% [markdown]
# A pesar de que la media de minutos vistos por la gran mayoría de usuarios sea mayor a 180 minutos, el ratio de sesiones completadas tiene su mayor número de usuarios entre "Bajo" y "Medio". Lo cual puede significar que consumen muchos minutos en la plataforma, pero no terminan de ver los episodios o películas completas.

# %%
netflix["sessions_group"] = pd.cut(
    netflix["watch_sessions_per_week"],
    bins=[0, 2, 5, 10, 20],
    labels=["Bajo", "Medio", "Alto", "Muy alto"]
)

# %% [markdown]
# En esta categoría también repetimos el proceso de sustituir valores númericos por categorías (Bajo, Medio, Alto y Muy alto) para facilitar la legibilidad de los gráficos.

# %%
sns.countplot(x="sessions_group", data=netflix)
plt.title("Nivel de sesiones por semana")
plt.show()

# %% [markdown]
# En este gráfico se puede observar que en el número de sesiones por semana predomina de manera bastante notable el grupo de "Muy alto". Comparada con la gráfica anterior, se observa que el número de sesiones por semana es muy alto aunque el ratio de las mismas finalizadas sea bastante más bajo.

# %% [markdown]
# 9.3. VARIABLES CATEGÓRICAS

# %%
sns.countplot(
    y="subscription_type",
    data=netflix,
    order=netflix["subscription_type"].value_counts().index
)
plt.title("Distribución de tipos de suscripción")
plt.show()

# %% [markdown]
# En esta gráfica se ve que la suscriprción Standard es la más elegida por los usuarios, aunque la Basic es la más económica es la que cuenta con menor número de suscriptores. El motivo puede ser la relación entre el precio y el contenido de publicidad durante las visualizaciones. La suscripción Basic es más barata pero contiene anuncios y la Standard es un poco más cara, pero elimina los anuncios.

# %%
sns.countplot(
    y="primary_device",
    data=netflix,
    order=netflix["primary_device"].value_counts().index
)
plt.title("Distribución de dispositivos")
plt.show()

# %% [markdown]
# En esta gráfica se puede observar que no hay una preferencia clara de dispositivo a la hora de consumir contenido en la plataforma.

# %%
top_countries = netflix["country"].value_counts().head(10)

sns.barplot(
    x=top_countries.values,
    y=top_countries.index
)
plt.title("Top 10 países")
plt.show()

# %% [markdown]
# En este gráfico vemos cómo los tres primeros países están entre Asia y América y los tres últimos son países europeos. Además también se observa cómo predominan los países de habla inglesa (India, USA, Canada, Australia y UK)

# %%
sns.countplot(x="churned", data=netflix)
plt.title("Distribución de abandono de usuarios")
plt.show()

# %% [markdown]
# En este gráfico se observa con mucha claridad que la inmesa mayoría de los usuarios está satisfecho con la plataforma, por lo que la tasa de abandono es bastante baja.

# %% [markdown]
# 10. ANÁLISIS BIVARIADO

# %% [markdown]
# ## 🔗 Análisis bivariado
# 
# 

# %%
netflix["churn_label"] = netflix["churned"].map({
    "No": "Activo",
    "Yes": "Inactivo"
})

# %%
sns.boxplot(
    x="churn_label",
    y="avg_watch_time_minutes",
    data=netflix
)

plt.title("Minutos vistos vs abandono")
plt.show()

# %% [markdown]
# En este gráfico no se observan diferencias significativas en el tiempo promedio de visualización entre usuarios activos e inactivos. Ambos grupos presentan distribuciones y medianas muy similares, lo que sugiere que el tiempo de visualización, por sí solo, no parece ser un factor determinante en el abandono de la plataforma.

# %%
sns.countplot(
    x="subscription_type",
    hue="churn_label",
    data=netflix
)

plt.title("Abandono por tipo de suscripción")
plt.show()

# %% [markdown]
# Al contrario que en la gráfica anterior, aquí sí se aprecia una diferencia bastante evidente dentro de los tipos de suscripción en relación a la tasa de abandono. La cantidad de usuarios activos es mucho mayor que la de usuarios inactivos en las tres suscripciones disponibles en la plataforma. Además, también se relaciona con el tipo de suscripción más popular entre los usuarios, donde predomina la Standard con mayor número de suscriptores activos. Quedan equiparados los usuarios Premium y Basic.

# %%
sns.boxplot(
    x="churn_label",
    y="recommendation_click_rate",
    data=netflix
)

plt.title("Interacción con recomendaciones vs abandono")
plt.show()

# %% [markdown]
# No se observan diferencias significativas entre usuarios activos e inactivos en la tasa de interacción con recomendaciones. Ambos grupos presentan distribuciones muy similares, lo que sugiere que esta variable no parece tener una relación fuerte con el abandono de la plataforma.

# %%
sns.countplot(
    x="age_group",
    hue="subscription_type",
    data=netflix
)

plt.title("Suscripción por grupo de edad")
plt.show()

# %% [markdown]
# De nuevo en esta gráfica se reafirma la preferencia de la suscripción Standard, esta vez reflejado en los grupos de edad de los usuarios. Esta suscripción predomina en el grupo de (46-60), al igual que la Premium y la Basic.

# %%
netflix.groupby("favorite_genre")["avg_watch_time_minutes"]\
.mean()\
.sort_values()\
.plot(kind="barh")

plt.title("Consumo medio por género")
plt.show()

# %% [markdown]
# En esta gráfica se ve como las preferencias en cuanto al género del contenido visualizado es bastante equitativa entre todas las categorías.

# %%
netflix.groupby("favorite_genre")["monthly_fee"]\
.sum()\
.sort_values()\
.plot(kind="barh")

plt.title("Ingresos por género favorito")
plt.show()

# %% [markdown]
# Como complement de la gráfica anterior, podemos observar que, aunque el género de Comedia sea el más visualizado no es el género que más ingresa, cayendo relegado al tercer puesto. En este caso, Romance sube del segundo puesto al primero en cuanto a ingresos y como algo a destacar, el género de Sci-Fi escala bastante en el ránking. En preferencias de usuarios era el 7 y en ingresos ocupa el 8 lugar.

# %%
sns.boxplot(
    x="primary_device",
    y="watch_sessions_per_week",
    data=netflix
)

plt.title("Sesiones por dispositivo")
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# La frecuencia de sesiones semanales se mantiene relativamente estable entre los distintos dispositivos analizados. No se observan diferencias relevantes en las medianas ni en la dispersión, lo que indica que el dispositivo principal utilizado no parece influir significativamente en la frecuencia de consumo de contenido.

# %%
country_language = pd.crosstab(
    netflix["country"],
    netflix["language"]
)

sns.heatmap(country_language, cmap="Blues")
plt.title("País vs idioma")
plt.show()

# %% [markdown]
# De este gráfico es curioso poder observar cómo en ninguno de los países de la lista el lenguaje preferido para ver contenido en la plataforma no se corresponde con el idioma nativo de los mismos. A destacar la preferencia del francés en Brasil y Estados Unidos, del coreano en la India y del español en Australia.

# %%
netflix.to_csv("netflix_final.csv", index=False)



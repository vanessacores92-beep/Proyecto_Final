🎬 Netflix User Behavior Analysis & Business Intelligence Dashboard
📌 Descripción del proyecto
Este proyecto tiene como objetivo analizar el comportamiento de los usuarios de una plataforma de streaming inspirada en Netflix mediante técnicas de análisis de datos y Business Intelligence.
A través de un proceso completo de preparación, exploración y visualización de datos, se estudian patrones de consumo, preferencias de contenido, comportamiento de los usuarios y factores relacionados con la retención y el abandono del servicio (Churn).
El proyecto combina análisis exploratorio realizado en Python con la construcción de un Dashboard interactivo en Power BI para facilitar la toma de decisiones basada en datos.

🎯 Objetivos
Los principales objetivos del proyecto son:
Analizar hábitos de consumo de los usuarios.
Identificar patrones de comportamiento y segmentación.
Estudiar factores asociados al abandono de clientes (Churn).
Evaluar la relación entre engagement y retención.
Visualizar indicadores clave mediante herramientas de Business Intelligence.
Transformar datos en información útil para la toma de decisiones empresariales.

🗂️ Estructura del proyecto
Netflix-User-Behavior-Analysis/

│
├── data/
│   ├── netflix_user_behavior_dataset.csv
│   ├── netflix_content_dataset.xlsx

│   └── netflix_final.csv
│
├── EDA/
│   └── Proyecto_Final_Netflix.py
│
├── dashboard/
│   └── Proyecto_Final_Dashboard.pbix
│
├── reports/
│   ├── Informe_EDA.ipynb
│   └── Informe_Dashboard.docx
│
└── README.md


🛠️ Herramientas utilizadas
Análisis de datos
Python
Jupyter Notebook
Pandas
NumPy
Visualización
Matplotlib
Seaborn
Business Intelligence
Power BI Desktop
Power Query
DAX
Control de versiones
Git
GitHub

📊 Metodología
El proyecto se desarrolló siguiendo las siguientes fases:
1. Comprensión de los datos
Se realizó una exploración inicial de los datasets para identificar:
Variables disponibles
Tipos de datos
Valores nulos
Registros duplicados
2. Limpieza y transformación
Las tareas incluyeron:
Eliminación de variables redundantes
Revisión de inconsistencias
Creación de categorías de análisis
Preparación de variables para visualización
3. Integración de datos
Los datasets fueron combinados mediante:
user_id
content_id
permitiendo relacionar usuarios, contenidos e interacciones en una única tabla analítica.
4. Análisis Exploratorio de Datos (EDA)
Se realizaron análisis:
Univariados
Bivariados
para identificar patrones relevantes y relaciones entre variables.
5. Desarrollo del Dashboard
Finalmente se diseñó un dashboard interactivo en Power BI para visualizar los principales indicadores del negocio.

📈 Principales análisis realizados
Análisis univariado
Distribución por grupos de edad.
Tiempo de visualización.
Nivel de finalización de contenido.
Frecuencia de uso.
Tipo de suscripción.
Dispositivos utilizados.
Distribución geográfica.
Churn.
Análisis bivariado
Minutos visualizados vs Churn.
Tipo de suscripción vs Churn.
Interacción con recomendaciones vs Churn.
Edad vs Tipo de suscripción.
Consumo por género favorito.
Ingresos por género.
Sesiones por dispositivo.
Relación País-Idioma.

📊 Dashboard de Power BI
El dashboard permite analizar la información mediante filtros interactivos y visualizaciones dinámicas.
KPIs principales
Total de usuarios.
Minutos visualizados.
Total de visualizaciones.
Ingresos generados.
Visualizaciones incluidas
Usuarios por tipo de suscripción.
Churn por tipo de suscripción.
Suscripciones por grupo de edad.
Dispositivos por grupo de edad.
Distribución geográfica.
Género favorito y volumen de visualizaciones.
Filtros
País.
Tipo de suscripción.

🔍 Principales hallazgos
Los resultados obtenidos sugieren que:
El nivel de consumo está estrechamente relacionado con la retención de usuarios.
Los usuarios con menor interacción presentan una mayor probabilidad de abandono.
Existen diferencias significativas entre grupos de edad respecto a hábitos de consumo.
Determinados géneros de contenido generan mayores niveles de engagement.
La personalización y los sistemas de recomendación pueden contribuir a reducir el churn.

🚀 Posibles mejoras futuras
Algunas líneas de desarrollo futuras podrían incluir:
Modelos predictivos de Churn.
Sistemas de recomendación basados en Machine Learning.
Segmentación avanzada mediante clustering.
Análisis temporal de comportamiento.
Automatización de la actualización del dashboard.

📚 Aprendizajes obtenidos
Durante el desarrollo del proyecto se aplicaron conocimientos relacionados con:
Limpieza y transformación de datos.
Integración de múltiples fuentes de información.
Análisis exploratorio de datos.
Visualización efectiva.
Business Intelligence.
Comunicación de resultados mediante dashboards interactivos.


📂 Fuentes de datos

Los datos utilizados proceden de las siguientes fuentes:

- Dataset de usuarios: 

https://www.kaggle.com/datasets/rhythmghai/netflix-user-watching-behavior-dataset

- Dataset de contenidos:

https://www.kaggle.com/datasets/falco1992/netflix-users-dataset

Transformaciones realizadas

Para los fines de este proyecto se realizaron procesos de:

- Limpieza de datos.
- Integración de datasets.
- Generación de variables derivadas.
- Creación de tablas de interacción simuladas para enriquecer el análisis.

Por tanto, los datos finales empleados en el análisis no coinciden exactamente con los datasets originales. 


👤 Autor
Vanesa Cores
Proyecto desarrollado como parte de la formación en Análisis de Datos.


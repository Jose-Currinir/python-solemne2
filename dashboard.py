import altair as alt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dashboard Solemne B", layout="wide")


def _normalizar_columnas(columnas: pd.Index) -> pd.Index:
    return columnas.str.strip().str.lower().str.replace(" ", "_")


@st.cache_data
def cargar_datos(ruta: str) -> tuple[pd.DataFrame, list[str]]:
    try:
        df = pd.read_csv(ruta)
    except UnicodeDecodeError:
        df = pd.read_csv(ruta, encoding="latin1")

    df.columns = _normalizar_columnas(df.columns)
    df["code"] = df["code"].fillna("Desconocido")

    mapa_columnas = {
        "country": "pais",
        "code": "codigo",
        "year": "año",
        "meningitis": "meningitis",
        "alzheimer's_diesease": "enfermedad_de_alzheimer",
        "parkinson's_disease": "enfermedad_de_parkinson",
        "nutritional_deficiency": "deficiencia_nutricional",
        "malaria": "malaria",
        "drowning": "ahogamiento",
        "interpersonal_violence": "violencia_interpersonal",
        "maternal_disorders": "trastornos_maternos",
        "hiv/aids": "vih_sida",
        "drug_use_disorders": "trastornos_por_uso_de_drogas",
        "tuberculosis": "tuberculosis",
        "cardiovascular_diseases": "enfermedades_cardiovasculares",
        "lower_respiratory_infections": "infecciones_respiratorias_bajas",
        "neonatal_disorders": "trastornos_neonatales",
        "alcohol_use_disorders": "trastornos_por_uso_de_alcohol",
        "self_harm": "autolesiones",
        "exposure_to_forces_of_nature": "exposicion_a_fuerzas_de_la_naturaleza",
        "diarrheal_diseases": "enfermedades_diarreicas",
        "environmental_heat_and_cold_exposure": "exposicion_a_calor_y_frio_ambiental",
        "neoplasms": "neoplasias",
        "conflict_and_terrorism": "conflicto_y_terrorismo",
        "diabetes_mellitus": "diabetes_mellitus",
        "chronic_kidney_disease": "enfermedad_renal_cronica",
        "poisonings": "intoxicaciones",
        "protein_energy_malnutrition": "desnutricion_proteico_energetica",
        "terrorism": "terrorismo",
        "road_injuries": "lesiones_por_transito",
        "chronic_respiratory_diseases": "enfermedades_respiratorias_cronicas",
        "chronic_liver_diseases": "enfermedades_hepaticas_cronicas",
        "digestive_diseases": "enfermedades_digestivas",
        "fire_heat_hot_substance": "fuego_calor_sustancias_calientes",
        "acute_hepatitis": "hepatitis_aguda",
    }

    df = df.rename(columns=mapa_columnas)

    id_cols = ["pais", "codigo", "año"]
    causa_cols = [c for c in df.columns if c not in id_cols]

    df[causa_cols] = df[causa_cols].apply(pd.to_numeric, errors="coerce").fillna(0)
    df["año"] = pd.to_numeric(df["año"], errors="coerce").fillna(0).astype(int)
    df["total_muertes"] = df[causa_cols].sum(axis=1)

    causa_cols = [c for c in df.columns if c not in id_cols + ["total_muertes"]]

    return df, causa_cols


df, causa_cols = cargar_datos("material-prueba/Forma_B.csv")

st.title("Prueba Solemne N°2 - Dashboard Forma B")
st.write(
    "Visualizaciones interactivas sobre mortalidad por causas. "
    "Usa los filtros para explorar el dataset."
)

min_year = int(df["año"].min())
max_year = int(df["año"].max())

col_filtros_1, col_filtros_2 = st.columns([2, 3])

with col_filtros_1:
    rango_anios = st.slider(
        "Rango de años",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year),
    )

with col_filtros_2:
    causa_seleccionada = st.selectbox(
        "Causa para tendencia anual",
        options=causa_cols,
        index=0,
    )

filtro = (df["año"] >= rango_anios[0]) & (df["año"] <= rango_anios[1])
df_filtrado = df.loc[filtro]

mortalidad_anual = (
    df_filtrado.groupby("año")["total_muertes"].mean().reset_index()
)

chart_total = (
    alt.Chart(mortalidad_anual)
    .mark_line(point=True)
    .encode(
        x=alt.X("año:Q", title="Año", axis=alt.Axis(format="d")),
        y=alt.Y("total_muertes:Q", title="Total de muertes promedio"),
        tooltip=["año:Q", "total_muertes:Q"],
    )
    .properties(title="Tendencia anual del total de muertes")
)

causa_anual = df_filtrado.groupby("año")[causa_seleccionada].sum().reset_index()
chart_causa = (
    alt.Chart(causa_anual)
    .mark_line(point=True)
    .encode(
        x=alt.X("año:Q", title="Año", axis=alt.Axis(format="d")),
        y=alt.Y(f"{causa_seleccionada}:Q", title="Muertes acumuladas"),
        tooltip=["año:Q", alt.Tooltip(f"{causa_seleccionada}:Q", title="Muertes")],
    )
    .properties(title=f"Tendencia de {causa_seleccionada}")
)

ranking_paises = (
    df_filtrado.groupby("pais")["total_muertes"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

chart_paises = (
    alt.Chart(ranking_paises)
    .mark_bar()
    .encode(
        x=alt.X("total_muertes:Q", title="Total de muertes"),
        y=alt.Y("pais:N", sort="-x", title="País"),
        tooltip=["pais:N", "total_muertes:Q"],
    )
    .properties(title="Top 5 países con más muertes acumuladas")
)

col1, col2 = st.columns(2)

with col1:
    st.altair_chart(chart_total, use_container_width=True)

with col2:
    st.altair_chart(chart_paises, use_container_width=True)

st.altair_chart(chart_causa, use_container_width=True)

st.caption(
    "Dashboard basado en el análisis de Forma_B.csv con filtros por año y causa."
)

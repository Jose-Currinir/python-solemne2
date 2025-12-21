import io
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Análisis de Mortalidad por Causas", layout="wide")

COLOR_PRIMARY = "#E53935"
COLOR_ACCENT = "#FF6B6B"
COLOR_BAR = "#C62828"


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


@st.cache_data
def cargar_archivo_bytes(ruta: str) -> bytes:
    return Path(ruta).read_bytes()


@st.cache_data
def exportar_excel(df: pd.DataFrame) -> bytes:
    buffer = io.BytesIO()
    df.to_excel(buffer, index=False)
    return buffer.getvalue()


df, causa_cols = cargar_datos("material-complementario/Forma_B.csv")

st.title("Análisis de Mortalidad por Causas")
st.write(
    "Visualizaciones interactivas sobre mortalidad por causas. "
    "Usa los filtros para explorar el dataset."
)
st.caption("Pasa el mouse sobre los gráficos para ver detalles.")

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

hover_total = alt.selection_point(
    fields=["año"], nearest=True, on="mouseover", empty=False
)
base_total = alt.Chart(mortalidad_anual).encode(
    x=alt.X("año:Q", title="Año", axis=alt.Axis(format="d")),
    y=alt.Y("total_muertes:Q", title="Total de muertes promedio"),
    tooltip=[
        alt.Tooltip("año:Q", title="Año", format="d"),
        alt.Tooltip("total_muertes:Q", title="Total muertes promedio", format=",.0f"),
    ],
)
line_total = base_total.mark_line(color=COLOR_PRIMARY)
points_total = base_total.mark_circle(size=60, color=COLOR_PRIMARY, opacity=0.7)
hover_points_total = base_total.mark_circle(size=130, color=COLOR_PRIMARY).encode(
    opacity=alt.condition(hover_total, alt.value(1), alt.value(0))
)
rule_total = (
    alt.Chart(mortalidad_anual)
    .mark_rule(color="#6B7280")
    .encode(x="año:Q")
    .transform_filter(hover_total)
)
chart_total = (
    (line_total + points_total + hover_points_total + rule_total)
    .add_params(hover_total)
    .properties(title="Tendencia anual del total de muertes")
)

causa_anual = df_filtrado.groupby("año")[causa_seleccionada].sum().reset_index()
hover_causa = alt.selection_point(
    fields=["año"], nearest=True, on="mouseover", empty=False
)
base_causa = alt.Chart(causa_anual).encode(
    x=alt.X("año:Q", title="Año", axis=alt.Axis(format="d")),
    y=alt.Y(f"{causa_seleccionada}:Q", title="Muertes acumuladas"),
    tooltip=[
        alt.Tooltip("año:Q", title="Año", format="d"),
        alt.Tooltip(f"{causa_seleccionada}:Q", title="Muertes acumuladas", format=",.0f"),
    ],
)
line_causa = base_causa.mark_line(color=COLOR_ACCENT)
points_causa = base_causa.mark_circle(size=60, color=COLOR_ACCENT, opacity=0.7)
hover_points_causa = base_causa.mark_circle(size=130, color=COLOR_ACCENT).encode(
    opacity=alt.condition(hover_causa, alt.value(1), alt.value(0))
)
rule_causa = (
    alt.Chart(causa_anual)
    .mark_rule(color="#6B7280")
    .encode(x="año:Q")
    .transform_filter(hover_causa)
)
chart_causa = (
    (line_causa + points_causa + hover_points_causa + rule_causa)
    .add_params(hover_causa)
    .properties(title=f"Tendencia de {causa_seleccionada}")
)

ranking_paises = (
    df_filtrado.groupby("pais")["total_muertes"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

hover_paises = alt.selection_point(fields=["pais"], on="mouseover", empty="none")
chart_paises = (
    alt.Chart(ranking_paises)
    .mark_bar()
    .encode(
        x=alt.X("total_muertes:Q", title="Total de muertes"),
        y=alt.Y("pais:N", sort="-x", title="País"),
        color=alt.condition(
            hover_paises, alt.value(COLOR_ACCENT), alt.value(COLOR_BAR)
        ),
        tooltip=[
            alt.Tooltip("pais:N", title="País"),
            alt.Tooltip("total_muertes:Q", title="Total muertes", format=",.0f"),
        ],
    )
    .add_params(hover_paises)
    .properties(title="Top 5 países con más muertes acumuladas")
)

col1, col2 = st.columns(2)

with col1:
    st.altair_chart(chart_total, use_container_width=True)

with col2:
    st.altair_chart(chart_paises, use_container_width=True)

st.altair_chart(chart_causa, use_container_width=True)

st.subheader("Descargas")
st.caption("Descarga la presentación, los datos filtrados o visita el repositorio.")

col_descarga_1, col_descarga_2, col_descarga_3 = st.columns([2, 2, 1])

with col_descarga_1:
    pptx_path = Path("material-complementario/Presentacion_Solemne_B.pptx")
    pdf_path = Path("material-complementario/Presentacion_Solemne_B.pdf")
    if pptx_path.exists():
        st.download_button(
            "Descargar presentación (PPTX)",
            data=cargar_archivo_bytes(str(pptx_path)),
            file_name=pptx_path.name,
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        )
    elif pdf_path.exists():
        st.download_button(
            "Descargar presentación (PDF)",
            data=cargar_archivo_bytes(str(pdf_path)),
            file_name=pdf_path.name,
            mime="application/pdf",
        )
    else:
        st.info("No se encontró el archivo de presentación en el repositorio.")

with col_descarga_2:
    excel_bytes = exportar_excel(df_filtrado)
    st.download_button(
        "Descargar datos filtrados (Excel)",
        data=excel_bytes,
        file_name="Forma_B_filtrado.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

with col_descarga_3:
    st.link_button(
        "Repo en GitHub",
        "https://github.com/Jose-Currinir/python-solemne2.git",
    )

st.caption(
    "Dashboard basado en el análisis de Forma_B.csv con filtros por año y causa."
)

# Streamlit deploy

Requisitos:
- Python 3.x
- `requirements.txt` en la raiz
- `material-complementario/Forma_B.csv` en el repo

Deploy en Streamlit Community Cloud:
1) Subir el repo a GitHub (incluye `material-complementario/Forma_B.csv`).
2) Create app -> elegir repo y branch.
3) Main file path: `dashboard.py`.
4) Deploy y revisar logs si falla.

Local (opcional):
```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

## Explicacion linea por linea del dashboard (`dashboard.py`)
Formato: `L<n>` corresponde a la linea n del archivo.

- L1: `import io` - Importa el modulo `io` para usar `BytesIO` al exportar a Excel.
- L2: `from pathlib import Path` - Importa `Path` para manejar rutas de archivos.
- L3: (linea en blanco) - Separa bloques de importacion.
- L4: `import altair as alt` - Importa Altair para graficos.
- L5: `import pandas as pd` - Importa pandas para manejo de datos.
- L6: `import streamlit as st` - Importa Streamlit para la app.
- L7: (linea en blanco) - Separa importaciones de configuracion.
- L8: `st.set_page_config(page_title="Análisis de Mortalidad por Causas", layout="wide")` - Configura el titulo y layout de la pagina.
- L9: (linea en blanco) - Separa configuracion de constantes.
- L10: `COLOR_PRIMARY = "#E53935"` - Define color principal.
- L11: `COLOR_ACCENT = "#FF6B6B"` - Define color de acento.
- L12: `COLOR_BAR = "#C62828"` - Define color base para barras.
- L13: (linea en blanco) - Separa constantes de funciones.
- L14: (linea en blanco) - Espacio antes de definir la funcion helper.
- L15: `def _normalizar_columnas(columnas: pd.Index) -> pd.Index:` - Declara funcion para normalizar nombres de columnas.
- L16: `return columnas.str.strip().str.lower().str.replace(" ", "_")` - Limpia espacios, pasa a minusculas y reemplaza espacios por guiones bajos.
- L17: (linea en blanco) - Separa funciones.
- L18: (linea en blanco) - Espacio antes del decorador.
- L19: `@st.cache_data` - Habilita cache para la carga de datos.
- L20: `def cargar_datos(ruta: str) -> tuple[pd.DataFrame, list[str]]:` - Declara funcion de carga y limpieza.
- L21: `try:` - Inicia manejo de excepciones al leer CSV.
- L22: `df = pd.read_csv(ruta)` - Lee el CSV con encoding por defecto.
- L23: `except UnicodeDecodeError:` - Captura errores de encoding.
- L24: `df = pd.read_csv(ruta, encoding="latin1")` - Reintenta lectura con latin1.
- L25: (linea en blanco) - Separa lectura de limpieza.
- L26: `df.columns = _normalizar_columnas(df.columns)` - Normaliza nombres de columnas.
- L27: `df["code"] = df["code"].fillna("Desconocido")` - Rellena codigos faltantes.
- L28: (linea en blanco) - Separa limpieza de mapeo.
- L29: `mapa_columnas = {` - Inicia diccionario de renombrado.
- L30: `"country": "pais",` - Mapea `country` a `pais`.
- L31: `"code": "codigo",` - Mapea `code` a `codigo`.
- L32: `"year": "año",` - Mapea `year` a `año`.
- L33: `"meningitis": "meningitis",` - Mantiene el nombre de la columna de meningitis.
- L34: `"alzheimer's_diesease": "enfermedad_de_alzheimer",` - Renombra la columna de Alzheimer.
- L35: `"parkinson's_disease": "enfermedad_de_parkinson",` - Renombra la columna de Parkinson.
- L36: `"nutritional_deficiency": "deficiencia_nutricional",` - Renombra deficiencia nutricional.
- L37: `"malaria": "malaria",` - Mantiene malaria.
- L38: `"drowning": "ahogamiento",` - Renombra ahogamiento.
- L39: `"interpersonal_violence": "violencia_interpersonal",` - Renombra violencia interpersonal.
- L40: `"maternal_disorders": "trastornos_maternos",` - Renombra trastornos maternos.
- L41: `"hiv/aids": "vih_sida",` - Renombra VIH/SIDA.
- L42: `"drug_use_disorders": "trastornos_por_uso_de_drogas",` - Renombra trastornos por drogas.
- L43: `"tuberculosis": "tuberculosis",` - Mantiene tuberculosis.
- L44: `"cardiovascular_diseases": "enfermedades_cardiovasculares",` - Renombra enfermedades cardiovasculares.
- L45: `"lower_respiratory_infections": "infecciones_respiratorias_bajas",` - Renombra infecciones respiratorias bajas.
- L46: `"neonatal_disorders": "trastornos_neonatales",` - Renombra trastornos neonatales.
- L47: `"alcohol_use_disorders": "trastornos_por_uso_de_alcohol",` - Renombra trastornos por alcohol.
- L48: `"self_harm": "autolesiones",` - Renombra autolesiones.
- L49: `"exposure_to_forces_of_nature": "exposicion_a_fuerzas_de_la_naturaleza",` - Renombra exposicion a fuerzas de la naturaleza.
- L50: `"diarrheal_diseases": "enfermedades_diarreicas",` - Renombra enfermedades diarreicas.
- L51: `"environmental_heat_and_cold_exposure": "exposicion_a_calor_y_frio_ambiental",` - Renombra exposicion a calor y frio ambiental.
- L52: `"neoplasms": "neoplasias",` - Renombra neoplasias.
- L53: `"conflict_and_terrorism": "conflicto_y_terrorismo",` - Renombra conflicto y terrorismo.
- L54: `"diabetes_mellitus": "diabetes_mellitus",` - Mantiene diabetes mellitus.
- L55: `"chronic_kidney_disease": "enfermedad_renal_cronica",` - Renombra enfermedad renal cronica.
- L56: `"poisonings": "intoxicaciones",` - Renombra intoxicaciones.
- L57: `"protein_energy_malnutrition": "desnutricion_proteico_energetica",` - Renombra desnutricion proteico-energetica.
- L58: `"terrorism": "terrorismo",` - Renombra terrorismo.
- L59: `"road_injuries": "lesiones_por_transito",` - Renombra lesiones por transito.
- L60: `"chronic_respiratory_diseases": "enfermedades_respiratorias_cronicas",` - Renombra enfermedades respiratorias cronicas.
- L61: `"chronic_liver_diseases": "enfermedades_hepaticas_cronicas",` - Renombra enfermedades hepaticas cronicas.
- L62: `"digestive_diseases": "enfermedades_digestivas",` - Renombra enfermedades digestivas.
- L63: `"fire_heat_hot_substance": "fuego_calor_sustancias_calientes",` - Renombra fuego/calor/sustancias calientes.
- L64: `"acute_hepatitis": "hepatitis_aguda",` - Renombra hepatitis aguda.
- L65: `}` - Cierra el diccionario de renombrado.
- L66: (linea en blanco) - Separa el diccionario del renombrado.
- L67: `df = df.rename(columns=mapa_columnas)` - Aplica el renombrado.
- L68: (linea en blanco) - Separa renombrado de columnas ID.
- L69: `id_cols = ["pais", "codigo", "año"]` - Define columnas identificadoras.
- L70: `causa_cols = [c for c in df.columns if c not in id_cols]` - Detecta columnas de causas.
- L71: (linea en blanco) - Separa definiciones de conversion de tipos.
- L72: `df[causa_cols] = df[causa_cols].apply(pd.to_numeric, errors="coerce").fillna(0)` - Convierte causas a numerico e imputa 0.
- L73: `df["año"] = pd.to_numeric(df["año"], errors="coerce").fillna(0).astype(int)` - Convierte `año` a entero.
- L74: `df["total_muertes"] = df[causa_cols].sum(axis=1)` - Calcula el total de muertes por fila.
- L75: (linea en blanco) - Separa recalculo de columnas.
- L76: `causa_cols = [c for c in df.columns if c not in id_cols + ["total_muertes"]]` - Recalcula columnas de causas sin el total.
- L77: (linea en blanco) - Separa retorno de funcion.
- L78: `return df, causa_cols` - Devuelve dataframe y lista de causas.
- L79: (linea en blanco) - Separa funciones.
- L80: (linea en blanco) - Espacio antes del siguiente decorador.
- L81: `@st.cache_data` - Cachea lectura de archivos binarios.
- L82: `def cargar_archivo_bytes(ruta: str) -> bytes:` - Define funcion para leer archivos como bytes.
- L83: `return Path(ruta).read_bytes()` - Lee el archivo y retorna sus bytes.
- L84: (linea en blanco) - Separa funciones.
- L85: (linea en blanco) - Espacio antes del siguiente decorador.
- L86: `@st.cache_data` - Cachea la exportacion a Excel.
- L87: `def exportar_excel(df: pd.DataFrame) -> bytes:` - Define funcion para exportar un dataframe a Excel en memoria.
- L88: `buffer = io.BytesIO()` - Crea un buffer en memoria.
- L89: `df.to_excel(buffer, index=False)` - Escribe el Excel sin indice.
- L90: `return buffer.getvalue()` - Devuelve los bytes del buffer.
- L91: (linea en blanco) - Separa funciones del flujo principal.
- L92: (linea en blanco) - Espacio antes de cargar datos.
- L93: `df, causa_cols = cargar_datos("material-complementario/Forma_B.csv")` - Carga el dataset y la lista de causas.
- L94: (linea en blanco) - Separa carga de la interfaz.
- L95: `st.title("Análisis de Mortalidad por Causas")` - Muestra el titulo principal.
- L96: `st.write(` - Inicia el texto descriptivo.
- L97: `"Visualizaciones interactivas sobre mortalidad por causas. "` - Primera frase del texto.
- L98: `"Usa los filtros para explorar el dataset."` - Segunda frase del texto.
- L99: `)` - Cierra `st.write`.
- L100: `st.caption("Pasa el mouse sobre los gráficos para ver detalles.")` - Agrega una nota al usuario.
- L101: (linea en blanco) - Separa texto de calculo de rango.
- L102: `min_year = int(df["año"].min())` - Obtiene el anio minimo.
- L103: `max_year = int(df["año"].max())` - Obtiene el anio maximo.
- L104: (linea en blanco) - Separa calculo de layout.
- L105: `col_filtros_1, col_filtros_2 = st.columns([2, 3])` - Crea dos columnas para filtros.
- L106: (linea en blanco) - Separa layout del primer filtro.
- L107: `with col_filtros_1:` - Abre la columna del slider.
- L108: `rango_anios = st.slider(` - Inicia el slider de rango de anios.
- L109: `"Rango de años",` - Etiqueta del slider.
- L110: `min_value=min_year,` - Valor minimo del slider.
- L111: `max_value=max_year,` - Valor maximo del slider.
- L112: `value=(min_year, max_year),` - Rango inicial completo.
- L113: `)` - Cierra el slider.
- L114: (linea en blanco) - Separa filtros.
- L115: `with col_filtros_2:` - Abre la columna del selector.
- L116: `causa_seleccionada = st.selectbox(` - Inicia el selectbox de causa.
- L117: `"Causa para tendencia anual",` - Etiqueta del selector.
- L118: `options=causa_cols,` - Lista de opciones.
- L119: `index=0,` - Seleccion por defecto.
- L120: `)` - Cierra el selectbox.
- L121: (linea en blanco) - Separa filtros del filtrado.
- L122: `filtro = (df["año"] >= rango_anios[0]) & (df["año"] <= rango_anios[1])` - Define la mascara de filtrado por anio.
- L123: `df_filtrado = df.loc[filtro]` - Aplica la mascara al dataframe.
- L124: (linea en blanco) - Separa filtrado de agregacion.
- L125: `mortalidad_anual = (` - Inicia el calculo de mortalidad anual.
- L126: `df_filtrado.groupby("año")["total_muertes"].mean().reset_index()` - Calcula el promedio anual.
- L127: `)` - Cierra la asignacion.
- L128: (linea en blanco) - Separa datos del grafico.
- L129: `hover_total = alt.selection_point(` - Crea seleccion de hover para el grafico total.
- L130: `fields=["año"], nearest=True, on="mouseover", empty=False` - Configura la seleccion por anio.
- L131: `)` - Cierra la seleccion.
- L132: `base_total = alt.Chart(mortalidad_anual).encode(` - Define el grafico base del total.
- L133: `x=alt.X("año:Q", title="Año", axis=alt.Axis(format="d")),` - Configura el eje X.
- L134: `y=alt.Y("total_muertes:Q", title="Total de muertes promedio"),` - Configura el eje Y.
- L135: `tooltip=[` - Inicia tooltips.
- L136: `alt.Tooltip("año:Q", title="Año", format="d"),` - Tooltip para el anio.
- L137: `alt.Tooltip("total_muertes:Q", title="Total muertes promedio", format=",.0f"),` - Tooltip para total.
- L138: `],` - Cierra tooltips.
- L139: `)` - Cierra `encode`.
- L140: `line_total = base_total.mark_line(color=COLOR_PRIMARY)` - Traza la linea principal.
- L141: `points_total = base_total.mark_circle(size=60, color=COLOR_PRIMARY, opacity=0.7)` - Agrega puntos sobre la linea.
- L142: `hover_points_total = base_total.mark_circle(size=130, color=COLOR_PRIMARY).encode(` - Define puntos grandes para hover.
- L143: `opacity=alt.condition(hover_total, alt.value(1), alt.value(0))` - Controla la opacidad en hover.
- L144: `)` - Cierra configuracion de hover.
- L145: `rule_total = (` - Inicia la regla vertical de hover.
- L146: `alt.Chart(mortalidad_anual)` - Usa los datos de mortalidad anual.
- L147: `.mark_rule(color="#6B7280")` - Dibuja una regla gris.
- L148: `.encode(x="año:Q")` - Ubica la regla en el eje X.
- L149: `.transform_filter(hover_total)` - Muestra la regla solo con hover.
- L150: `)` - Cierra la regla.
- L151: `chart_total = (` - Inicia la composicion del grafico total.
- L152: `(line_total + points_total + hover_points_total + rule_total)` - Combina capas del grafico.
- L153: `.add_params(hover_total)` - Agrega la interaccion de hover.
- L154: `.properties(title="Tendencia anual del total de muertes")` - Agrega titulo al grafico.
- L155: `)` - Cierra el grafico total.
- L156: (linea en blanco) - Separa el grafico de causa.
- L157: `causa_anual = df_filtrado.groupby("año")[causa_seleccionada].sum().reset_index()` - Suma anual de la causa seleccionada.
- L158: `hover_causa = alt.selection_point(` - Crea seleccion de hover para la causa.
- L159: `fields=["año"], nearest=True, on="mouseover", empty=False` - Configura la seleccion por anio.
- L160: `)` - Cierra la seleccion.
- L161: `base_causa = alt.Chart(causa_anual).encode(` - Define el grafico base de causa.
- L162: `x=alt.X("año:Q", title="Año", axis=alt.Axis(format="d")),` - Configura el eje X.
- L163: `y=alt.Y(f"{causa_seleccionada}:Q", title="Muertes acumuladas"),` - Configura el eje Y.
- L164: `tooltip=[` - Inicia tooltips.
- L165: `alt.Tooltip("año:Q", title="Año", format="d"),` - Tooltip de anio.
- L166: `alt.Tooltip(f"{causa_seleccionada}:Q", title="Muertes acumuladas", format=",.0f"),` - Tooltip de la causa.
- L167: `],` - Cierra tooltips.
- L168: `)` - Cierra `encode`.
- L169: `line_causa = base_causa.mark_line(color=COLOR_ACCENT)` - Traza la linea de la causa.
- L170: `points_causa = base_causa.mark_circle(size=60, color=COLOR_ACCENT, opacity=0.7)` - Agrega puntos a la linea.
- L171: `hover_points_causa = base_causa.mark_circle(size=130, color=COLOR_ACCENT).encode(` - Define puntos de hover para la causa.
- L172: `opacity=alt.condition(hover_causa, alt.value(1), alt.value(0))` - Controla opacidad por hover.
- L173: `)` - Cierra configuracion de hover.
- L174: `rule_causa = (` - Inicia la regla vertical de la causa.
- L175: `alt.Chart(causa_anual)` - Usa datos de causa anual.
- L176: `.mark_rule(color="#6B7280")` - Dibuja la regla.
- L177: `.encode(x="año:Q")` - Coloca la regla en X.
- L178: `.transform_filter(hover_causa)` - Muestra la regla solo en hover.
- L179: `)` - Cierra la regla.
- L180: `chart_causa = (` - Inicia la composicion del grafico de causa.
- L181: `(line_causa + points_causa + hover_points_causa + rule_causa)` - Combina capas de causa.
- L182: `.add_params(hover_causa)` - Agrega interaccion de hover.
- L183: `.properties(title=f"Tendencia de {causa_seleccionada}")` - Asigna titulo dinamico.
- L184: `)` - Cierra el grafico de causa.
- L185: (linea en blanco) - Separa del ranking por pais.
- L186: `ranking_paises = (` - Inicia calculo de ranking de paises.
- L187: `df_filtrado.groupby("pais")["total_muertes"]` - Agrupa por pais.
- L188: `.sum()` - Suma muertes por pais.
- L189: `.sort_values(ascending=False)` - Ordena descendentemente.
- L190: `.head(5)` - Toma los 5 primeros.
- L191: `.reset_index()` - Restablece el indice como columna.
- L192: `)` - Cierra el ranking.
- L193: (linea en blanco) - Separa ranking del grafico.
- L194: `hover_paises = alt.selection_point(fields=["pais"], on="mouseover", empty="none")` - Seleccion por pais al pasar el mouse.
- L195: `chart_paises = (` - Inicia grafico de barras.
- L196: `alt.Chart(ranking_paises)` - Usa el dataset del ranking.
- L197: `.mark_bar()` - Define barras.
- L198: `.encode(` - Inicia codificacion.
- L199: `x=alt.X("total_muertes:Q", title="Total de muertes"),` - Define eje X.
- L200: `y=alt.Y("pais:N", sort="-x", title="País"),` - Define eje Y ordenado.
- L201: `color=alt.condition(` - Aplica color condicional.
- L202: `hover_paises, alt.value(COLOR_ACCENT), alt.value(COLOR_BAR)` - Elige color segun hover.
- L203: `),` - Cierra condicion de color.
- L204: `tooltip=[` - Inicia tooltips.
- L205: `alt.Tooltip("pais:N", title="País"),` - Tooltip de pais.
- L206: `alt.Tooltip("total_muertes:Q", title="Total muertes", format=",.0f"),` - Tooltip de total.
- L207: `],` - Cierra tooltips.
- L208: `),` - Cierra `encode`.
- L209: `.add_params(hover_paises)` - Agrega hover al grafico.
- L210: `.properties(title="Top 5 países con más muertes acumuladas")` - Define el titulo.
- L211: `)` - Cierra el grafico.
- L212: (linea en blanco) - Separa graficos del layout.
- L213: `col1, col2 = st.columns(2)` - Crea columnas para graficos.
- L214: (linea en blanco) - Separa columnas.
- L215: `with col1:` - Abre la primera columna.
- L216: `st.altair_chart(chart_total, use_container_width=True)` - Renderiza el grafico total.
- L217: (linea en blanco) - Separa columnas.
- L218: `with col2:` - Abre la segunda columna.
- L219: `st.altair_chart(chart_paises, use_container_width=True)` - Renderiza el grafico de paises.
- L220: (linea en blanco) - Separa graficos.
- L221: `st.altair_chart(chart_causa, use_container_width=True)` - Renderiza el grafico de causa.
- L222: (linea en blanco) - Separa graficos de descargas.
- L223: `st.subheader("Descargas")` - Agrega subtitulo de descargas.
- L224: `st.caption("Descarga la presentación, los datos filtrados o visita el repositorio.")` - Muestra una descripcion de descargas.
- L225: (linea en blanco) - Separa texto de columnas.
- L226: `col_descarga_1, col_descarga_2, col_descarga_3 = st.columns([2, 2, 1])` - Crea columnas para botones de descarga.
- L227: (linea en blanco) - Separa columnas.
- L228: `with col_descarga_1:` - Abre columna para la presentacion.
- L229: `pptx_path = Path("material-complementario/Presentacion_Solemne_B.pptx")` - Define ruta del PPTX.
- L230: `pdf_path = Path("material-complementario/Presentacion_Solemne_B.pdf")` - Define ruta del PDF.
- L231: `if pptx_path.exists():` - Si existe el PPTX.
- L232: `st.download_button(` - Inicia boton de descarga de PPTX.
- L233: `"Descargar presentación (PPTX)",` - Texto del boton.
- L234: `data=cargar_archivo_bytes(str(pptx_path)),` - Carga bytes del PPTX.
- L235: `file_name=pptx_path.name,` - Asigna nombre de archivo.
- L236: `mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",` - MIME del PPTX.
- L237: `)` - Cierra el boton PPTX.
- L238: `elif pdf_path.exists():` - Si no hay PPTX pero si PDF.
- L239: `st.download_button(` - Inicia boton de descarga de PDF.
- L240: `"Descargar presentación (PDF)",` - Texto del boton PDF.
- L241: `data=cargar_archivo_bytes(str(pdf_path)),` - Carga bytes del PDF.
- L242: `file_name=pdf_path.name,` - Nombre del archivo PDF.
- L243: `mime="application/pdf",` - MIME del PDF.
- L244: `)` - Cierra el boton PDF.
- L245: `else:` - Caso sin archivos de presentacion.
- L246: `st.info("No se encontró el archivo de presentación en el repositorio.")` - Muestra mensaje informativo.
- L247: (linea en blanco) - Separa columnas de descarga.
- L248: `with col_descarga_2:` - Abre columna para Excel.
- L249: `excel_bytes = exportar_excel(df_filtrado)` - Genera el Excel filtrado.
- L250: `st.download_button(` - Inicia boton de descarga de Excel.
- L251: `"Descargar datos filtrados (Excel)",` - Texto del boton Excel.
- L252: `data=excel_bytes,` - Bytes del Excel.
- L253: `file_name="Forma_B_filtrado.xlsx",` - Nombre del archivo Excel.
- L254: `mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",` - MIME del Excel.
- L255: `)` - Cierra el boton Excel.
- L256: (linea en blanco) - Separa columnas.
- L257: `with col_descarga_3:` - Abre columna para el enlace.
- L258: `st.link_button(` - Inicia boton con link.
- L259: `"Repo en GitHub",` - Texto del boton.
- L260: `"https://github.com/Jose-Currinir/python-solemne2.git",` - URL del repo.
- L261: `)` - Cierra el boton.
- L262: (linea en blanco) - Separa del pie de pagina.
- L263: `st.caption(` - Inicia caption final.
- L264: `"Dashboard basado en el análisis de Forma_B.csv con filtros por año y causa."` - Texto final.
- L265: `)` - Cierra la caption final.

## Explicacion linea por linea del notebook (`Solemne_B.ipynb`)
Nota: se explican solo las celdas de codigo; las celdas Markdown son titulos y texto descriptivo.

### Celda 3 (codigo)
- L1: `# Importa librerias y configura el estilo de graficos` - Comentario que describe la celda.
- L2: `import pandas as pd` - Importa pandas.
- L3: `import numpy as np` - Importa numpy.
- L4: `import matplotlib.pyplot as plt` - Importa matplotlib para graficos.
- L5: `import seaborn as sns` - Importa seaborn.
- L6: `from IPython.display import display` - Importa `display` para mostrar objetos.
- L7: (linea en blanco) - Separa importaciones del estilo.
- L8: `sns.set_theme(style='whitegrid')` - Configura el estilo visual.

### Celda 4 (codigo)
- L1: `# Carga el CSV con fallback de encoding y muestra las primeras filas` - Comentario descriptivo.
- L2: `ruta = 'material-complementario/Forma_B.csv'` - Define la ruta del CSV.
- L3: `try:` - Inicia intento de lectura.
- L4: `df_raw = pd.read_csv(ruta)` - Lee el CSV con encoding por defecto.
- L5: `except UnicodeDecodeError:` - Captura error de encoding.
- L6: `df_raw = pd.read_csv(ruta, encoding='latin1')` - Reintenta con latin1.
- L7: (linea en blanco) - Separa lectura de salida.
- L8: `df_raw.head()` - Muestra las primeras filas.

### Celda 5 (codigo)
- L1: `# Muestra estructura, tipos y nulos del dataset` - Comentario descriptivo.
- L2: `df_raw.info()` - Imprime info general del dataframe.

### Celda 6 (codigo)
- L1: `# Genera resumen estadistico de columnas numericas` - Comentario descriptivo.
- L2: `df_raw.describe()` - Muestra estadisticas descriptivas.

### Celda 8 (codigo)
- L1: `# Copia el dataset, normaliza columnas e imputa valores faltantes` - Comentario descriptivo.
- L2: `df = df_raw.copy()` - Crea una copia del dataframe.
- L3: `df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')` - Normaliza nombres de columnas.
- L4: (linea en blanco) - Separa normalizacion de imputacion.
- L5: `df['code'] = df['code'].fillna('Desconocido')` - Rellena codigos faltantes.
- L6: `# Se imputan valores faltantes en columnas de causas (numéricas)` - Comentario sobre imputacion.
- L7: `causa_cols = [c for c in df.columns if c not in ['country', 'code', 'year']]` - Identifica columnas de causas.
- L8: `df[causa_cols] = df[causa_cols].apply(pd.to_numeric, errors='coerce').fillna(0)` - Convierte causas a numerico y rellena con 0.
- L9: (linea en blanco) - Separa transformacion de salida.
- L10: `df.isna().sum().head(10)` - Muestra conteo de nulos.

### Celda 10 (codigo)
- L1: `# Renombra columnas al espanol para trabajar mas comodo` - Comentario descriptivo.
- L2: `mapa_columnas = {` - Inicia diccionario de renombrado.
- L3: `'country': 'pais',` - Mapea `country` a `pais`.
- L4: `'code': 'codigo',` - Mapea `code` a `codigo`.
- L5: `'year': 'año',` - Mapea `year` a `año`.
- L6: `'meningitis': 'meningitis',` - Mantiene meningitis.
- L7: `"alzheimer's_diesease": 'enfermedad_de_alzheimer',` - Renombra Alzheimer.
- L8: `"parkinson's_disease": 'enfermedad_de_parkinson',` - Renombra Parkinson.
- L9: `'nutritional_deficiency': 'deficiencia_nutricional',` - Renombra deficiencia nutricional.
- L10: `'malaria': 'malaria',` - Mantiene malaria.
- L11: `'drowning': 'ahogamiento',` - Renombra ahogamiento.
- L12: `'interpersonal_violence': 'violencia_interpersonal',` - Renombra violencia interpersonal.
- L13: `'maternal_disorders': 'trastornos_maternos',` - Renombra trastornos maternos.
- L14: `'hiv/aids': 'vih_sida',` - Renombra VIH/SIDA.
- L15: `'drug_use_disorders': 'trastornos_por_uso_de_drogas',` - Renombra trastornos por drogas.
- L16: `'tuberculosis': 'tuberculosis',` - Mantiene tuberculosis.
- L17: `'cardiovascular_diseases': 'enfermedades_cardiovasculares',` - Renombra enfermedades cardiovasculares.
- L18: `'lower_respiratory_infections': 'infecciones_respiratorias_bajas',` - Renombra infecciones respiratorias bajas.
- L19: `'neonatal_disorders': 'trastornos_neonatales',` - Renombra trastornos neonatales.
- L20: `'alcohol_use_disorders': 'trastornos_por_uso_de_alcohol',` - Renombra trastornos por alcohol.
- L21: `'self_harm': 'autolesiones',` - Renombra autolesiones.
- L22: `'exposure_to_forces_of_nature': 'exposicion_a_fuerzas_de_la_naturaleza',` - Renombra exposicion a fuerzas de la naturaleza.
- L23: `'diarrheal_diseases': 'enfermedades_diarreicas',` - Renombra enfermedades diarreicas.
- L24: `'environmental_heat_and_cold_exposure': 'exposicion_a_calor_y_frio_ambiental',` - Renombra exposicion a calor y frio ambiental.
- L25: `'neoplasms': 'neoplasias',` - Renombra neoplasias.
- L26: `'conflict_and_terrorism': 'conflicto_y_terrorismo',` - Renombra conflicto y terrorismo.
- L27: `'diabetes_mellitus': 'diabetes_mellitus',` - Mantiene diabetes mellitus.
- L28: `'chronic_kidney_disease': 'enfermedad_renal_cronica',` - Renombra enfermedad renal cronica.
- L29: `'poisonings': 'intoxicaciones',` - Renombra intoxicaciones.
- L30: `'protein_energy_malnutrition': 'desnutricion_proteico_energetica',` - Renombra desnutricion proteico-energetica.
- L31: `'terrorism': 'terrorismo',` - Renombra terrorismo.
- L32: `'road_injuries': 'lesiones_por_transito',` - Renombra lesiones por transito.
- L33: `'chronic_respiratory_diseases': 'enfermedades_respiratorias_cronicas',` - Renombra enfermedades respiratorias cronicas.
- L34: `'chronic_liver_diseases': 'enfermedades_hepaticas_cronicas',` - Renombra enfermedades hepaticas cronicas.
- L35: `'digestive_diseases': 'enfermedades_digestivas',` - Renombra enfermedades digestivas.
- L36: `'fire_heat_hot_substance': 'fuego_calor_sustancias_calientes',` - Renombra fuego/calor/sustancias calientes.
- L37: `'acute_hepatitis': 'hepatitis_aguda',` - Renombra hepatitis aguda.
- L38: `}` - Cierra el diccionario.
- L39: (linea en blanco) - Separa el diccionario del renombrado.
- L40: `df = df.rename(columns=mapa_columnas)` - Aplica el renombrado.
- L41: `df.columns` - Muestra las columnas resultantes.

### Celda 11 (codigo)
- L1: `# Revisa las primeras filas del dataset limpio` - Comentario descriptivo.
- L2: `df.head()` - Muestra las primeras filas del dataset limpio.

### Celda 14 (codigo)
- L1: `# Define columnas id y asegura tipos numericos (incluye anio)` - Comentario descriptivo.
- L2: `id_cols = ['pais', 'codigo', 'año']` - Define columnas identificadoras.
- L3: `causa_cols = [c for c in df.columns if c not in id_cols]` - Identifica columnas de causas.
- L4: (linea en blanco) - Separa definiciones de conversion.
- L5: `df[causa_cols] = df[causa_cols].apply(pd.to_numeric, errors='coerce').fillna(0)` - Convierte causas a numerico.
- L6: `df['año'] = pd.to_numeric(df['año'], errors='coerce').fillna(0).astype(int)` - Convierte `año` a entero.
- L7: (linea en blanco) - Separa conversion de salida.
- L8: `df.dtypes.head(10)` - Muestra tipos de datos.

### Celda 17 (codigo)
- L1: `# Calcula total de muertes y estadisticas basicas` - Comentario descriptivo.
- L2: `df['total_muertes'] = df[causa_cols].sum(axis=1)` - Suma causas por fila.
- L3: (linea en blanco) - Separa suma de estadisticas.
- L4: `estadisticas_total = df['total_muertes'].agg(['mean', 'median', 'std']).to_frame(name='valor')` - Calcula media, mediana y desviacion.
- L5: `estadisticas_total` - Muestra el dataframe de estadisticas.

### Celda 19 (codigo)
- L1: `# Calcula percentil 75 y lista paises destacados` - Comentario descriptivo.
- L2: `p75 = df['total_muertes'].quantile(0.75)` - Calcula el percentil 75.
- L3: `paises_destacados = df.loc[df['total_muertes'] >= p75, 'pais'].unique()` - Extrae paises con total alto.
- L4: (linea en blanco) - Separa calculo de salida.
- L5: `len(paises_destacados), paises_destacados[:10]` - Muestra cantidad y ejemplo.

### Celda 21 (codigo)
- L1: `# Calcula agregados y ranking de causas y paises principales` - Comentario descriptivo.
- L2: `mortalidad_anual = df.groupby('año')['total_muertes'].mean().reset_index()` - Calcula promedio anual.
- L3: (linea en blanco) - Separa agregados.
- L4: `causa_cols_sin_total = [c for c in df.columns if c not in id_cols + ['total_muertes']]` - Excluye total de causas.
- L5: `top_causas = df[causa_cols_sin_total].sum().sort_values(ascending=False).head(5)` - Obtiene top 5 causas.
- L6: (linea en blanco) - Separa ranking de paises.
- L7: `top_paises = (` - Inicia calculo de top paises.
- L8: `df.groupby('pais')['total_muertes']` - Agrupa por pais.
- L9: `.sum()` - Suma muertes.
- L10: `.sort_values(ascending=False)` - Ordena de mayor a menor.
- L11: `.head(5)` - Toma top 5.
- L12: `)` - Cierra el bloque.
- L13: (linea en blanco) - Separa calculos de impresion.
- L14: `print("Top 5 causas")` - Imprime etiqueta para causas.
- L15: `display(top_causas)` - Muestra el ranking de causas.
- L16: `print("Top 5 países")` - Imprime etiqueta para paises.
- L17: `display(top_paises)` - Muestra el ranking de paises.

### Celda 23 (codigo)
- L1: `# Grafica la distribucion de total_muertes (KDE)` - Comentario descriptivo.
- L2: `# KDE de total_muertes` - Comentario del grafico.
- L3: `plt.figure(figsize=(8, 5))` - Define el tamano de la figura.
- L4: `sns.kdeplot(df['total_muertes'], fill=True)` - Grafica la densidad KDE.
- L5: `plt.title('Distribución (KDE) de Total de Muertes')` - Titulo del grafico.
- L6: `plt.xlabel('Total de muertes')` - Etiqueta del eje X.
- L7: `plt.ylabel('Densidad')` - Etiqueta del eje Y.
- L8: `plt.tight_layout()` - Ajusta el layout.
- L9: `plt.show()` - Muestra el grafico.

### Celda 24 (codigo)
- L1: `# Grafica la participacion de las 5 causas principales` - Comentario descriptivo.
- L2: `# Gráfico de torta: top 5 causas` - Comentario del grafico.
- L3: `plt.figure(figsize=(7, 7))` - Define el tamano de la figura.
- L4: `plt.pie(top_causas.values, labels=top_causas.index, autopct='%1.1f%%', startangle=140)` - Dibuja el grafico de torta.
- L5: `plt.title('Distribución de las 5 causas más comunes')` - Titulo del grafico.
- L6: `plt.tight_layout()` - Ajusta el layout.
- L7: `plt.show()` - Muestra el grafico.

### Celda 25 (codigo)
- L1: `# Grafica los 5 paises con mas muertes` - Comentario descriptivo.
- L2: `# Barras: top 5 países con más muertes` - Comentario del grafico.
- L3: `plt.figure(figsize=(8, 5))` - Define el tamano de la figura.
- L4: `sns.barplot(x=top_paises.values, y=top_paises.index, orient='h')` - Dibuja barras horizontales.
- L5: `plt.title('Top 5 países con más muertes acumuladas')` - Titulo del grafico.
- L6: `plt.xlabel('Total de muertes')` - Etiqueta del eje X.
- L7: `plt.ylabel('País')` - Etiqueta del eje Y.
- L8: `plt.tight_layout()` - Ajusta el layout.
- L9: `plt.show()` - Muestra el grafico.

### Celda 26 (codigo)
- L1: `# Grafica tendencia anual del total de muertes promedio` - Comentario descriptivo.
- L2: `# Línea de tendencia de total_muertes por año (promedio)` - Comentario del grafico.
- L3: `plt.figure(figsize=(9, 5))` - Define el tamano de la figura.
- L4: `sns.lineplot(data=mortalidad_anual, x='año', y='total_muertes', marker='o')` - Grafica la tendencia anual.
- L5: `plt.title('Tendencia anual del total de muertes (promedio)')` - Titulo del grafico.
- L6: `plt.xlabel('Año')` - Etiqueta del eje X.
- L7: `plt.ylabel('Total de muertes promedio')` - Etiqueta del eje Y.
- L8: `plt.tight_layout()` - Ajusta el layout.
- L9: `plt.show()` - Muestra el grafico.

### Celda 27 (codigo)
- L1: `# Compara en el tiempo las 2 causas principales` - Comentario descriptivo.
- L2: `# Comparación de las 2 causas principales a lo largo del tiempo` - Comentario del grafico.
- L3: `top2_causas = list(top_causas.index[:2])` - Selecciona las 2 causas principales.
- L4: `top2_por_anio = df.groupby('año')[top2_causas].sum().reset_index()` - Suma por anio para esas causas.
- L5: (linea en blanco) - Separa calculo del grafico.
- L6: `plt.figure(figsize=(9, 5))` - Define el tamano de la figura.
- L7: `for causa in top2_causas:` - Itera sobre las causas.
- L8: `sns.lineplot(data=top2_por_anio, x='año', y=causa, marker='o', label=causa)` - Traza cada causa.
- L9: `plt.title('Comparación de las 2 causas principales en el tiempo')` - Titulo del grafico.
- L10: `plt.xlabel('Año')` - Etiqueta del eje X.
- L11: `plt.ylabel('Muertes acumuladas')` - Etiqueta del eje Y.
- L12: `plt.legend(title='Causa')` - Agrega leyenda.
- L13: `plt.tight_layout()` - Ajusta el layout.
- L14: `plt.show()` - Muestra el grafico.

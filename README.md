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

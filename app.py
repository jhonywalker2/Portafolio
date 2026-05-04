import streamlit as st

st.set_page_config(
    page_title="Portafolio · Streamlit Apps",
    page_icon="🗂",
    layout="wide",
)

# ── Datos de las apps ──────────────────────────────────────────────────────────
APPS = [
    {"name": "Portafolio",        "desc": "Vista central de todas las aplicaciones del proyecto.",          "url": "https://portafolio-2h88sdo96v98q2otdws68v.streamlit.app/",   "cat": "Visualización",  "icon": "🗂"},
    {"name": "Traductor",         "desc": "Traducción automática de texto entre idiomas.",                  "url": "https://traductor-gzjvew38gjgc6vu4ndicht.streamlit.app/",      "cat": "NLP",            "icon": "🌐"},
    {"name": "Tutorial NLP",      "desc": "Tutorial interactivo de procesamiento de lenguaje natural.",    "url": "https://tutorial2-jhonnywalkers2.streamlit.app/",               "cat": "NLP",            "icon": "📖"},
    {"name": "Vision App",        "desc": "Análisis de imágenes con visión por computadora.",              "url": "https://visionapp-toyyhwhjaznqttubkaygds.streamlit.app/",       "cat": "IA · Visión",    "icon": "👁️"},
    {"name": "Word Cloud",        "desc": "Generación de nubes de palabras desde texto personalizado.",    "url": "https://wordcloud-nubecitadepalabras.streamlit.app/",           "cat": "Visualización",  "icon": "☁️"},
    {"name": "YOLOv5 Detector",   "desc": "Detección de objetos en imágenes con YOLOv5.",                 "url": "https://yolov5-detectordeimagenes.streamlit.app/",             "cat": "IA · Visión",    "icon": "🎯"},
    {"name": "Draw Recognition",  "desc": "Reconocimiento de dibujos hechos a mano libre.",               "url": "https://drawrecog-1234.streamlit.app/",                        "cat": "IA · Visión",    "icon": "✏️"},
    {"name": "Escritura a mano",  "desc": "Reconocimiento de texto escrito a mano (OCR).",                "url": "https://escrituraamano.streamlit.app/",                        "cat": "IA · Visión",    "icon": "🖊️"},
    {"name": "Historia",          "desc": "Aplicación narrativa / storytelling interactivo.",              "url": "https://historia-3vsvcieow5wqjudxobnrnk.streamlit.app/",       "cat": "Creativo",       "icon": "📜"},
    {"name": "Domra Teacher",     "desc": "Herramienta educativa para práctica y enseñanza.",              "url": "https://domraroteacher.streamlit.app/",                        "cat": "Documentos",     "icon": "🎓"},
    {"name": "LSTM NLP",          "desc": "Modelo LSTM para clasificación o generación de texto.",         "url": "https://lstmnlp-63n4vrojjedvdgflfqzrdj.streamlit.app/",        "cat": "NLP",            "icon": "🧠"},
    {"name": "Presentación",      "desc": "Presentación interactiva de proyectos.",                        "url": "https://jhonypres.streamlit.app/",                             "cat": "Visualización",  "icon": "📊"},
    {"name": "Parque Berrío 4pm", "desc": "Proyecto creativo / documental urbano.",                        "url": "https://parqueberrioalas4delatarde.streamlit.app/",            "cat": "Creativo",       "icon": "🌆"},
    {"name": "La Casa",           "desc": "Experiencia narrativa interactiva.",                             "url": "https://lacasationooo.streamlit.app/",                         "cat": "Creativo",       "icon": "🏠"},
    {"name": "Análisis Sentimental","desc": "Detección de emociones positivas, negativas y neutras.",     "url": "https://sentimental-tristefelizyno.streamlit.app/",            "cat": "NLP",            "icon": "💬"},
    {"name": "TF-IDF Español",    "desc": "Vectorización TF-IDF para textos en español.",                  "url": "https://tdfesp-espanol.streamlit.app/",                        "cat": "NLP",            "icon": "📝"},
    {"name": "Texto y Documento", "desc": "Procesamiento y análisis de documentos de texto.",              "url": "https://textoydocumento.streamlit.app/",                       "cat": "Documentos",     "icon": "📄"},
    {"name": "TF-IDF Inglés",     "desc": "TF-IDF aplicado a párrafos en inglés.",                        "url": "https://tfidfingles-parrafos.streamlit.app/",                  "cat": "NLP",            "icon": "🔤"},
    {"name": "Canvas",            "desc": "Lienzo interactivo para dibujo o anotaciones.",                "url": "https://canvas-oqc9eulljuzce4cysgknns.streamlit.app/",          "cat": "Visualización",  "icon": "🎨"},
    {"name": "Chat PDF",          "desc": "Chat conversacional sobre el contenido de un PDF.",             "url": "https://chatpdf-mjqnpmcgwgjq9gxuxnu8ht.streamlit.app/",        "cat": "IA · Visión",    "icon": "💡"},
    {"name": "Ctrl Voice",        "desc": "Control de aplicaciones o texto mediante voz.",                 "url": "https://ctrlvoice-egwqzvm47jqvzsnpecrvar.streamlit.app/",      "cat": "Audio",          "icon": "🎙️"},
]

CATEGORY_COLORS = {
    "NLP":          {"bg": "#dbeafe", "text": "#1e40af"},
    "IA · Visión":  {"bg": "#d1fae5", "text": "#065f46"},
    "Visualización":{"bg": "#ede9fe", "text": "#4c1d95"},
    "Documentos":   {"bg": "#fef3c7", "text": "#92400e"},
    "Audio":        {"bg": "#fee2e2", "text": "#991b1b"},
    "Creativo":     {"bg": "#fce7f3", "text": "#9d174d"},
}

CATEGORIES = ["Todas"] + sorted(CATEGORY_COLORS.keys())

# ── CSS personalizado ─────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.pf-header-label {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #888;
    margin-bottom: 4px;
}

.pf-title {
    font-size: 2rem;
    font-weight: 600;
    margin-bottom: 0.2rem;
}

.pf-subtitle {
    font-size: 0.85rem;
    color: #888;
    margin-bottom: 1.5rem;
}

.app-card {
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 1rem;
    height: 100%;
    transition: box-shadow 0.2s ease;
    background: white;
}

.app-card:hover {
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
}

.card-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
}

.card-icon {
    font-size: 1.5rem;
    width: 40px;
    height: 40px;
    border-radius: 10px;
    background: #f3f4f6;
    display: flex;
    align-items: center;
    justify-content: center;
}

.card-badge {
    font-family: 'Space Mono', monospace;
    font-size: 9px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 999px;
    letter-spacing: 0.04em;
}

.card-name {
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 4px;
}

.card-desc {
    font-size: 0.75rem;
    color: #6b7280;
    line-height: 1.5;
    margin-bottom: 10px;
}

.card-url {
    font-family: 'Space Mono', monospace;
    font-size: 9px;
    color: #9ca3af;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    border-top: 1px solid #f3f4f6;
    padding-top: 8px;
}

.pf-count {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: #9ca3af;
    margin-bottom: 1rem;
}

a.card-link {
    text-decoration: none;
    color: inherit;
    display: block;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<p class="pf-header-label">Streamlit Apps · Portafolio</p>', unsafe_allow_html=True)
st.markdown('<h1 class="pf-title">Mis aplicaciones</h1>', unsafe_allow_html=True)
st.markdown('<p class="pf-subtitle">21 apps en producción — NLP, visión, IA generativa y más</p>', unsafe_allow_html=True)

# ── Filtro de categorías ──────────────────────────────────────────────────────
selected_cat = st.selectbox("Filtrar por categoría", CATEGORIES, label_visibility="collapsed")

filtered = APPS if selected_cat == "Todas" else [a for a in APPS if a["cat"] == selected_cat]

st.markdown(f'<p class="pf-count">{len(filtered)} / {len(APPS)} apps</p>', unsafe_allow_html=True)

# ── Grid de tarjetas ──────────────────────────────────────────────────────────
COLS = 3
rows = [filtered[i:i+COLS] for i in range(0, len(filtered), COLS)]

for row in rows:
    cols = st.columns(COLS)
    for col, app in zip(cols, row):
        colors = CATEGORY_COLORS.get(app["cat"], {"bg": "#f3f4f6", "text": "#374151"})
        with col:
            st.markdown(f"""
            <a class="card-link" href="{app['url']}" target="_blank">
                <div class="app-card">
                    <div class="card-top">
                        <div class="card-icon">{app['icon']}</div>
                        <span class="card-badge" style="background:{colors['bg']};color:{colors['text']};">{app['cat']}</span>
                    </div>
                    <div class="card-name">{app['name']}</div>
                    <div class="card-desc">{app['desc']}</div>
                    <div class="card-url">{app['url'].replace('https://', '')}</div>
                </div>
            </a>
            """, unsafe_allow_html=True)
    # Rellenar columnas vacías si la última fila tiene menos de COLS apps
    for empty_col in cols[len(row):]:
        with empty_col:
            st.empty()

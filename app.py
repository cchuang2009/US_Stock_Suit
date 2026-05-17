import streamlit as st

st.set_page_config(page_title="My App Launcher", layout="wide")

apps = [
    {
        "name": "Quantum Computing Prediction",
        "url": "https://stock-qc.streamlit.app/",
        "tag": "Quantum",
        "icon": "⚛️",
        "desc": "Stock forecasting with quantum-inspired algorithms.",
    },
    {
        "name": "Pre-Market Analysis",
        "url": "https://stockpremarket.streamlit.app/",
        "tag": "Pre-Market",
        "icon": "📊",
        "desc": "ATR targets, sentiment scoring, bull/bear gauges.",
    },
    {
        "name": "Scan Market News",
        "url": "https://scanstock.streamlit.app/",
        "tag": "Scanner",
        "icon": "📡",
        "desc": "Live news aggregator to catch signals early.",
    },
    {
        "name": "Swing Momentum & Breakout Scan",
        "url": "https://swingstock.streamlit.app/",
        "tag": "Swing, Breakout Scanner",
        "icon": "📡",
        "desc": "Scanner the Swing/Breakout Tickers",
    },
    {
        "name": "Learning Date Report",
        "url": "https://ustock-infos.streamlit.app/",
        "tag": "Report",
        "icon": "📋",
        "desc": "Daily reports for stock learning progress.",
    },
    {
        "name": "Cerebras Analysis, since 2026-05-14",
        "url": "https://cerebras-app.streamlit.app/",
        "tag": "Report",
        "icon": "📋",
        "desc": "Cerebras tracking",
    },
]

cols = st.columns(2)
for i, app in enumerate(apps):
    with cols[i % 2]:
        st.link_button(f"{app['icon']} {app['name']}", app["url"], use_container_width=True)
        st.caption(app["desc"])

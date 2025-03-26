import streamlit as st
from common import HTML_Template, MainCSS


st.set_page_config(layout="wide")
st.html(HTML_Template.base_style.substitute(css=MainCSS.initial_page_styles))
# Define the navigation menu for ML OptiSlang Alternative
nav_menu = {
    "Main": [
        st.Page(
            title="Home",
            page="pages/home.py",
            icon=":material/home:",
        )
    ],
    "Data Processing": [
        st.Page(
            title="Load Data",
            page="pages/load_data.py",
            icon=":material/upload:",
        ),
        st.Page(
            title="Preprocessing",
            page="pages/preprocessing.py",
            icon=":material/tune:",
        ),
    ],
    "Feature Engineering": [
        st.Page(
            title="Feature & Target Selection",
            page="pages/feature_selection.py",
            icon=":material/select_all:",
        ),
    ],
    "Modeling": [
        st.Page(
            title="Train Model",
            page="pages/train.py",
            icon=":material/auto_awesome:",
        ),
        st.Page(
            title="Optimize Model",
            page="pages/optimize.py",
            icon=":material/track_changes:",
        ),
    ],
    "Evaluation": [
        st.Page(
            title="Model Evaluation",
            page="pages/evaluate.py",
            icon=":material/insights:",
        ),
    ],
    "Deployment": [
        st.Page(
            title="Save Model & Scaler",
            page="pages/save_model.py",
            icon=":material/save:",
        ),
        st.Page(
            title="Deploy Model",
            page="pages/deploy.py",
            icon=":material/cloud_upload:",
        ),
    ],
}

# Add sidebar navigation
nav = st.navigation(nav_menu, position="sidebar")
nav.run()

import streamlit as st
from streamlit_app2 import rendered_html
import stripe

st.image("10.png")

config = pdfkit.configuration(wkhtmltopdf="wkhtmltopdf.exe")
pdf = pdfkit.from_string(rendered_html, configuration=config)

st.success("Your pdf was generated!")

st.download_button(
    "⬇️ Download PDF",
    data=pdf,
    file_name=f"Digital_{aaa}.pdf",
    mime="application/octet-stream",
)

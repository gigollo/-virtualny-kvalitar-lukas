import streamlit as st
import os
from openai import OpenAI

# Inicializácia klienta
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit UI
st.set_page_config(page_title="Virtuálny kvalitár Lukas", layout="centered")
st.title("🤖 Virtuálny kvalitár Lukas")
st.write("AI asistent pre kvalitu – IATF, 8D, FMEA, e-maily")

tab1, tab2, tab3 = st.tabs(["📋 8D report", "📨 Email zákazníkovi", "💬 Kvalita Q&A Chat"])
lang = st.selectbox("Vyber jazyk výstupu:", ["Slovenčina", "Angličtina", "Nemčina"])

with tab1:
    st.subheader("Generátor 8D reportu")
    problem = st.text_area("Popíš problém (napr. typ reklamácie, chyba...)")
    if st.button("Vygeneruj 8D report"):
        if problem:
            with st.spinner("GPT-3.5 generuje 8D report..."):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": f"Si expert na kvalitu, pomáhaj s 8D reportmi. Odpovedaj v jazyku: {lang}"},
                        {"role": "user", "content": f"Vygeneruj 8D report na tému: {problem}"}
                    ]
                )
                st.markdown(response.choices[0].message.content)
        else:
            st.warning("Zadaj popis problému.")

with tab2:
    st.subheader("Generátor e-mailu zákazníkovi")
    email_topic = st.text_input("Zhrni situáciu (napr. reklamácia č. 1234 – poškodený diel)")
    if st.button("Vytvoriť e-mail"):
        if email_topic:
            with st.spinner("GPT-3.5 tvorí e-mail..."):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": f"Si kvalitár, píšeš oficiálne e-maily. Jazyk: {lang}"},
                        {"role": "user", "content": f"Vytvor e-mail zákazníkovi na tému: {email_topic}"}
                    ]
                )
                st.info(response.choices[0].message.content)
        else:
            st.warning("Zadaj tému e-mailu.")

with tab3:
    st.subheader("Chat: Opýtaj sa na čokoľvek z oblasti kvality")
    question = st.text_input("Tvoja otázka (napr. Čo je bod 10.2 v IATF?)")
    if st.button("Získať odpoveď"):
        if question:
            with st.spinner("GPT-3.5 odpovedá..."):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": f"Si AI expert na kvalitu. Jazyk: {lang}"},
                        {"role": "user", "content": question}
                    ]
                )
                st.success(response.choices[0].message.content)
        else:
            st.warning("Zadaj otázku.")

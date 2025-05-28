import streamlit as st

st.set_page_config(page_title="Virtuálny kvalitár Lukas", layout="centered")
st.title("🤖 Virtuálny kvalitár Lukas")
st.write("AI asistent pre kvalitu – IATF, 8D, FMEA, e-maily")

tab1, tab2, tab3 = st.tabs(["📋 8D report", "📨 Email zákazníkovi", "💬 Kvalita Q&A Chat"])
lang = st.selectbox("Vyber jazyk výstupu:", ["Slovenčina", "Angličtina", "Nemčina"])

with tab1:
    st.subheader("Generátor 8D reportu")
    problem = st.text_area("Popíš problém (napr. typ reklamácie, chyba...)")
    if st.button("Vygeneruj 8D report"):
        st.success(f"""### 8D report ({lang})
**D1 – Tím:** Zostavený tím pre riešenie problému  
**D2 – Popis problému:** {problem}  
**D3 – Dočasné opatrenie:** Identifikácia a izolácia chybných dielov  
**D4 – Koreňová príčina:** Príčina bude určená ďalšou analýzou  
**D5 – Trvalé riešenie:** Implementácia dodatočnej kontroly  
**D6 – Opatrenia na opakovanie:** Aktualizácia FMEA a kontrolného plánu  
**D7 – Uzavretie:** Schválené manažmentom  
**D8 – Gratulácia tímu:** Ďakujeme za efektívne vyriešenie problému""")

with tab2:
    st.subheader("Generátor e-mailu zákazníkovi")
    email_topic = st.text_input("Zhrni situáciu (napr. reklamácia č. 1234 – poškodený diel)")
    if st.button("Vytvoriť e-mail"):
        st.info(f"""### E-mail ({lang})
Vážený zákazník,  
ďakujeme za informovanie o situácii: **{email_topic}**.  
Vaša reklamácia bola zaevidovaná a momentálne prebieha analýza.  
Budeme vás čoskoro kontaktovať s výsledkami vyšetrovania a návrhom opatrení.  
S pozdravom,  
Tím kvality""")

with tab3:
    st.subheader("Chat: Opýtaj sa na čokoľvek z oblasti kvality")
    question = st.text_input("Tvoja otázka (napr. Čo je bod 10.2 v IATF?)")
    if st.button("Získať odpoveď"):
        st.write(f"""**Odpoveď ({lang}):**  
Fiktívna odpoveď AI: V bode 10.2 normy IATF 16949 sa hovorí o riadení nezhôd a prijatí nápravných opatrení...  
(Tu bude odpoveď od skutočného AI modelu, ak sa pripojí OpenAI alebo vlastný backend.)""")

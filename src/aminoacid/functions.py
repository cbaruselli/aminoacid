import streamlit as st

st.title("🎯 Learn the amino acid")

if "page" not in st.session_state:
    st.session_state.page = "menu"

def show_menu():
    st.markdown("## What do you want to do ?")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🧪 Quizz"):
            st.session_state.page = "quizz"

    with col2:
        if st.button("📘 Learn the amino acid"):
            st.session_state.page = "learn"

def show_quizz():
    st.markdown("## 🎮 Quizz")
    st.write("Ici, tu pourrais mettre des questions, des boutons de réponses, etc.")
    if st.button("🔙 back"):
        st.session_state.page = "menu"

def show_learn():
    st.markdown("## 📚 Learn the amino acid")
    st.write("Ici tu pourrais afficher des fiches, images, infos utiles.")
    if st.button("🔙 back"):
        st.session_state.page = "menu"

if st.session_state.page == "menu":
    show_menu()
elif st.session_state.page == "quizz":
    show_quizz()
elif st.session_state.page == "learn":
    show_learn()

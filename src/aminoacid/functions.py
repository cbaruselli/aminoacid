import streamlit as st
from rdkit import Chem #nao
from rdkit.Chem  import Draw #nao

st.title("🎯 aminoacid")

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
    st.caption("What is the structure of a amino acid?") #NAOMI
    st.write("An amino acid  contains both amino and  carboxylic acid functional groupe, a carbon alpha and a side chain which is variable.")
    img= "aastruct.jpeg"
    st.image(img, caption="Amino acid structure", use_container_width=True)
    st.write("Select an amino acid to view its molecular structure:") 

    amino_acids = {
        "Glycine (Gly, G)": "C(C(=O)O)N",
        "Alanine (Ala, A)": "CC(C(=O)O)N",
        "Valine (Val, V)": "CC(C)C(C(=O)O)N",
        "Leucine (Leu, L)": "CC(C)CC(C(=O)O)N",
        "Isoleucine (Ile, I)": "CC(C)C(C(=O)O)N",
        "Serine (Ser, S)": "C(C(C(=O)O)N)O",
        "Threonine (Thr, T)": "CC(C(C(=O)O)N)O",
        "Cysteine (Cys, C)": "C(C(C(=O)O)N)S",
        "Methionine (Met, M)": "CSCC(C(=O)O)N",
        "Phenylalanine (Phe, F)": "C1=CC=CC=C1CC(C(=O)O)N",
        "Tyrosine (Tyr, Y)": "C1=CC=C(C=C1)CC(C(=O)O)N",
        "Tryptophan (Trp, W)": "C1=CC=C2C(=C1)C=CN2CC(C(=O)O)N",
        "Asparagine (Asn, N)": "C(CC(=O)N)(C(=O)O)N",
        "Glutamine (Gln, Q)": "C(CCC(=O)N)(C(=O)O)N",
        "Aspartic acid (Asp, D)": "C(CC(=O)O)(C(=O)O)N",
        "Glutamic acid (Glu, E)": "C(CCC(=O)O)(C(=O)O)N",
        "Lysine (Lys, K)": "C(CCCN)CC(C(=O)O)N",
        "Arginine (Arg, R)": "C(CCCN=C(N)N)CC(C(=O)O)N",
        "Histidine (His, H)": "C1=CNC=N1CC(C(=O)O)N",
        "Proline (Pro, P)": "C1CC(NC1)C(=O)O"
    }

    selected_name = st.selectbox("Choose an amino acid:", list(amino_acids.keys()))

    smiles = amino_acids[selected_name]
    mol = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(mol, size=(400, 400))
    st.image(img, caption=selected_name, use_container_width=False)

    if st.button("🔙 back"):
        st.session_state.page = "menu"

if st.session_state.page == "menu":
    show_menu()
elif st.session_state.page == "quizz":
    show_quizz()
elif st.session_state.page == "learn":
    show_learn()






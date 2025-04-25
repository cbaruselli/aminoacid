import streamlit as st
from streamlit_ketcher import st_ketcher #moni
from rdkit import Chem #nao
from rdkit.Chem import Draw #nao
from rdkit.Chem import rdMolDescriptors #moni
import random #moni

st.title("🎯 aminoacid")

if "page" not in st.session_state:
    st.session_state.page = "menu"

def show_menu():
    st.markdown("## What do you want to do ?")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🧪 Quizz"):
            st.session_state.page = "quizz"
            st.rerun()

    with col2:
        if st.button("📘 Learn the amino acid"):
            st.session_state.page = "learn"
            st.rerun()

def show_quizz():
    st.markdown("## 🎮 Quizz")
    st.write("Let's test your knowledge!")
    st.markdown("---")

    # Step 1: Define your amino acids
    amino_acids = {
        "Alanine": "CC(C(=O)O)N",
        "Arginine": "NC(CCCNC(=N)N)C(=O)O",
        "Asparagine": "C(CC(=O)N)(C(=O)O)N",
        "Aspartic Acid": "NC(C(=O)O)CC(=O)O",
        "Cysteine": "C(C(C(=O)O)N)S",
        "Glutamic Acid": "C(CCC(=O)O)(C(=O)O)N",
        "Glutamine": "C(CCC(=O)N)(C(=O)O)N",
        "Glycine": "NCC(=O)O",
        "Histidine": "NC(C(=O)O)Cc1c[nH]cn1",
        "Isoleucine": "CCC(C)C(C(=O)O)N",
        "Leucine": "CC(C)CC(C(=O)O)N",
        "Lysine": "NC(CCCCN)C(=O)O",
        "Methionine": "CSCCC(C(=O)O)N",
        "Phenylalanine": "NC(Cc1ccccc1)C(=O)O",
        "Proline": "O=C(O)C1CCCN1",
        "Serine": "C(C(C(=O)O)N)O",
        "Threonine": "CC(C(C(=O)O)N)O",
        "Tryptophan": "NC(Cc1c[nH]c2ccccc12)C(=O)O",
        "Tyrosine": "NC(Cc1ccc(O)cc1)C(=O)O",
        "Valine": "CC(C)C(C(=O)O)N"
    }

    # Step 2: Initialize session state 
    if "round_order" not in st.session_state:
        st.session_state.round_order = random.sample(list(amino_acids.keys()), len(amino_acids))  # shuffle once
    if "ketcher_key" not in st.session_state:
        st.session_state.ketcher_key = 0
    if "current_index" not in st.session_state:
        st.session_state.current_index = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "answered" not in st.session_state:
        st.session_state.answered = False

    # Step 3: Set current target
    current_target = st.session_state.round_order[st.session_state.current_index]
    target_smiles = amino_acids[current_target]

    # Step 4: Display game info
    st.markdown(f"Draw this amino acid in the box below: **{current_target}**")
    st.markdown("Once you are done, click **Apply** to see if it's correct!")
    st.markdown("And move on to the next question with **Next**.")
    progress = (st.session_state.current_index + 1) / len(amino_acids)
    st.progress(progress, text= f"Progress : {st.session_state.current_index + 1} / {len(amino_acids)}")

    # Step 5: User draws molecule
    ketcher_smiles = st_ketcher(height=600, key=f"ketcher_{st.session_state.ketcher_key}")

    # Step 6: Normalize and compare molecules
    def are_equivalent(smiles1, smiles2):
        mol1 = Chem.MolFromSmiles(smiles1)
        mol2 = Chem.MolFromSmiles(smiles2)
        if mol1 is None or mol2 is None:
            return False
        return Chem.MolToInchi(mol1) == Chem.MolToInchi(mol2)

    # Step 7: Feedback
    if ketcher_smiles:
        if are_equivalent(ketcher_smiles, target_smiles):
            st.success("✅ Correct!")
            st.markdown("---")
            if "answered" not in st.session_state or not st.session_state.answered:
                st.session_state.score += 1
                st.session_state.answered = True
        else:
            st.error("❌ Not quite right. Keep on training!")
            st.markdown(f"The answer is : " )
            mol = Chem.MolFromSmiles(target_smiles)
            if mol:
                img = Draw.MolToImage(mol, size=(300, 300))
                st.image(img, caption=f"Structure of {current_target}", use_container_width=False)
            else:
                st.warning("Impossible to generate the molecule from SMILES.")
            st.markdown("---")

    # Step 8: Go to next
    if st.session_state.current_index < len(amino_acids) - 1:
        if st.button("Next"):
            st.session_state.current_index += 1
            st.session_state.ketcher_key += 1  # Trigger Ketcher reset
            st.session_state.answered = False
            st.rerun()  # refresh app state
    elif st.session_state.current_index == len(amino_acids) - 1:
        if st.button("Show score"):
            st.header("🏁 Round Complete!")
            percent_score = (st.session_state.score / len(amino_acids)) * 100
            st.success(f"Your final score is : {st.session_state.score} / {len(amino_acids)}")
            if percent_score == 100:
                st.balloons()
                st.markdown("🎉 You're an amino acid expert !")
            elif percent_score >= 75:
                st.markdown("Great job 👏 : You know your stuff !")
            elif percent_score >= 50:
                st.markdown("🧪 Keep practicing and you'll get there.")
            else:
                st.markdown("📚 It's time to hit the books, don't give up !")
            st.markdown("---")
        if st.button("Restart"):
            keys_to_clear = ["current_index", "ketcher_key", "score", "answered", "round_order"]
            for key in keys_to_clear:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()


    if st.button("🔙 back to menu"):
        st.session_state.page = "menu"
        st.rerun()

def show_learn():
    st.markdown("## 📚 Learn the amino acid")
    st.caption("What is the structure of a amino acid?") #NAOMI
    st.write("An amino acid  contains both amino and  carboxylic acid functional groupe, a carbon alpha and a side chain which is variable.")
    img= "aastruct.jpeg"
    st.image(img, caption="Amino acid structure", use_container_width=True)
    st.write("Select an amino acid to view its molecular structure:") 

    amino_acids = {
        "Glycine (Gly, G)": "C(C(=O)O)N",
        "Alanine (Ala, A)": "C[C@@H](C(=O)O)N",
        "Valine (Val, V)": "CC(C)[C@H](N)C(O)=O",
        "Leucine (Leu, L)": "CC(C)C[C@@H](C(=O)O)N",
        "Isoleucine (Ile, I)": "N[C@@H](C(C)CC)C(=O)O",
        "Serine (Ser, S)": "N[C@@H](CO)C(=O)O",
        "Threonine (Thr, T)": "C[C@H]([C@@H](C(=O)O)N)O",
        "Cysteine (Cys, C)": "N[C@@H](CS)C(=O)O",
        "Methionine (Met, M)": "N[C@@H](CCSC)C(=O)O",
        "Phenylalanine (Phe, F)": "N[C@@H](CC1=CC=CC=C1)C(=O)O",
        "Tyrosine (Tyr, Y)": "N[C@@H](CC1=CC=C(O)C=C1)C(=O)O",
        "Tryptophan (Trp, W)": "N[C@@H](CC1=CNC2=CC=CC=C12)C(=O)O",
        "Asparagine (Asn, N)": "N[C@@H](CC(=O)N)C(=O)O",
        "Glutamine (Gln, Q)": "N[C@@H](CCC(=O)N)C(=O)O",
        "Aspartic acid (Asp, D)": "N[C@@H](CC(=O)O)C(=O)O",
        "Glutamic acid (Glu, E)": "N[C@@H](CCC(=O)O)C(=O)O",
        "Lysine (Lys, K)": "N[C@@H](CCCCN)C(=O)O",
        "Arginine (Arg, R)": "N[C@@H](CCCNC(=N)N)C(=O)O",
        "Histidine (His, H)": "N[C@@H](CC1=CN=CN1)C(=O)O",
        "Proline (Pro, P)": "C1C[C@H](NC1)C(=O)O"
        }

    selected_name = st.selectbox("Choose an amino acid:", list(amino_acids.keys()))

    smiles = amino_acids[selected_name]
    mol = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(mol, size=(400, 400))
    st.image(img, caption=selected_name, use_container_width=False)

    if st.button("🔙 back to menu"):
        st.session_state.page = "menu"
        st.rerun()

if st.session_state.page == "menu":
    show_menu()
elif st.session_state.page == "quizz":
    show_quizz()
elif st.session_state.page == "learn":
    show_learn()
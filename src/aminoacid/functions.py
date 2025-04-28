import streamlit as st
from streamlit_ketcher import st_ketcher #moni
from rdkit import Chem #nao
from rdkit.Chem import Draw #nao
from rdkit.Chem import rdMolDescriptors #moni
import random #moni
import base64

st.title("🎯 Aminoacid")

def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    image = get_base64(png_file)
    background = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(background, unsafe_allow_html=True)
set_background("aminoacid.png")

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

def draw_quizz():
    st.markdown("## 🎮 Quizz : Draw amino acids")
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

    # Step 4: Display game info and progress bar
    st.markdown(f"Draw this amino acid in the box below: **{current_target}**")
    st.markdown("Once you are done, click **Apply** to see if it's correct!")
    st.markdown("And move on to the next question with **Next**.")
    progress = (st.session_state.current_index + 1) / len(amino_acids)
    st.progress(progress, text= f"Progress : {st.session_state.current_index + 1} / {len(amino_acids)}")

    # Step 5: User draws molecule
    if not st.session_state.answered:
        ketcher_smiles = st_ketcher(height=600, key=f"ketcher_{st.session_state.ketcher_key}")
    else:
        st.info("You already answered! Click **Next** to continue.")
        ketcher_smiles = None
    

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
            st.session_state.answered = True
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


    if st.button("🔙 Back to menu"):
        st.session_state.page = "menu"
        st.rerun()

def reset_quizz(quizz_variables=[]):
    '''
    To reset the sessions after finishing it.
    
    Input: list with object by default. 
    '''
    quizz_variables = quizz_variables or [
        'name_quizz_order',
        'wrong_answers',
        'reset_input_flag',
        'name_quizz_score',
        'name_quizz_index',
        'user_guess_input',
        'name_quizz_answered'
        ]
    
    for variable in quizz_variables:
        if hasattr(st.session_state, variable):
            del st.session_state[variable]


def name_quizz():
    '''
    Function used to write the name of the amino acid from its structure.
    '''

    st.markdown("## ✏️ Quizz : Name amino acids")
    st.write("Guess the name of the amino acid based on their structure.")

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
    #Creation of session state
    if "name_quizz_order" not in st.session_state:
        st.session_state.name_quizz_order = random.sample(list(amino_acids.items()), len(amino_acids))
        st.session_state.name_quizz_index = 0
        st.session_state.wrong_answers = [] #list to keep the wrong answers
    if "name_quizz_score" not in st.session_state:
        st.session_state.name_quizz_score = 0
    if "user_guess_input" not in st.session_state:
        st.session_state.user_guess_input = ""
    if "reset_input_flag" not in st.session_state: 
        st.session_state.reset_input_flag = False
    if "name_quizz_answered" not in st.session_state:
        st.session_state.name_quizz_answered = False
    

    #Get the current aminoacid
    if st.session_state.name_quizz_index < len(st.session_state.name_quizz_order):
        correct_name, smiles = st.session_state.name_quizz_order[st.session_state.name_quizz_index]
        mol = Chem.MolFromSmiles(smiles)

        #Progress bar
        progress = st.session_state.name_quizz_index + 1
        total = len(st.session_state.name_quizz_order)
        st.progress(progress / total)
        st.write(f"Question {progress} of {total}")

        if mol:
            st.image(Draw.MolToImage(mol, size=(300, 300)), caption="Guess this amino acid")

        #To remove the name after the click on "Next molecule"
        default_value = "" if st.session_state.reset_input_flag else st.session_state.get("user_guess_input", "")
        user_guess = st.text_input("Enter the name of this amino acid:", value=default_value, key="user_guess_input").strip()

        if st.session_state.reset_input_flag:  
            st.session_state.reset_input_flag = False
        
        if st.session_state.name_quizz_answered:
            st.info("You already answered! Click **Next molecule** to continue.")

    #Check answer
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Check answer") and not st.session_state.name_quizz_answered:
                if user_guess.lower() == correct_name.lower():
                    st.success("✅ Correct!")
                    st.session_state.name_quizz_score += 1
                else:
                    st.error(f"❌ Nope! The correct answer was: **{correct_name}**")
                    st.session_state.wrong_answers.append(correct_name) #save which aminoacids is wrong
                st.session_state.name_quizz_answered = True

        with col2:
            if st.button("Next molecule"):
                if not st.session_state.name_quizz_answered: 
                    st.session_state.wrong_answers.append(correct_name)  #Append the answer as wrong in case the user didn't check the answer/ wrote an answer and directly click on "Next molecule"
                st.session_state.name_quizz_index += 1
                st.session_state.reset_input_flag = True 
                st.session_state.name_quizz_answered = False 
                st.rerun()

    #Feedback
    else:
        st.success("🏁 You've completed all the amino acids!")
        retry_mode = st.session_state.get("retry_mode", False) #To see if retry_mode is active or not

        tot_questions= len(st.session_state.name_quizz_order) if retry_mode else len(amino_acids) #Adapt the nb of total questions depending on the mode
        percent_score = (st.session_state.name_quizz_score / tot_questions) * 100

        if percent_score == 100:
            st.balloons()
            st.success(f"Your final score is : {st.session_state.name_quizz_score} / {tot_questions}")
            if retry_mode:
                st.markdown("🎯 Perfect corrections !")
            else:
                st.markdown("🎉 You're an expert !")
        elif percent_score >= 75:
            st.success(f"Your final score is : {st.session_state.name_quizz_score} / {tot_questions}")
            if retry_mode:
                st.markdown("🎊 Almost right !")
            else:
                st.markdown("Great job 👏 : A little more practice and it will be perfect !")
        elif percent_score >= 50:
            st.success(f"Your final score is : {st.session_state.name_quizz_score} / {tot_questions}")
            if retry_mode:
                st.markdown("📗 Continue like that !")
            else:
                st.markdown("🧪 Keep practicing and you'll get there.")
        else:
            st.warning(f"Your final score is : {st.session_state.name_quizz_score} / {tot_questions}")
            if retry_mode:
                st.markdown("📚 Don't give up, study more if needed !")
            else:
                st.markdown("📚 It's time to hit the books, don't give up !")
        st.markdown("---")

        #Practice the wrong aminoacids
        if st.session_state.wrong_answers:
            st.warning(f"You missed {len(st.session_state.wrong_answers)} amino acids !")

            col3, col4 = st.columns(2)
            with col3:
                if st.button("🔄 Retry incorrect answers "):
                    st.session_state.name_quizz_order = [(aa, amino_acids[aa]) for aa in st.session_state.wrong_answers]
                    st.session_state.name_quizz_index = 0
                    st.session_state.name_quizz_score = 0
                    st.session_state.wrong_answers = []
                    st.session_state.reset_input_flag = False
                    st.session_state.name_quizz_answered = False
                    st.session_state.retry_mode = True 
                    st.rerun()

            with col4:
                if st.button("Restart"):
                    reset_quizz(["name_quizz_order", "name_quizz_index", "name_quizz_score", "user_guess_input"])
                    st.rerun()
        else:
            if st.button("Restart"):
                reset_quizz()
                st.rerun()

    if st.button("🔙 Back to menu"):
            st.session_state.page = "menu"
            st.rerun()

def show_quizz():
    '''
    Allows you to choose which game mode you want between 'Draw amino acids' and 'Name amino acids'.
    '''
    st.markdown(
    """
    <style>
    .stApp {
        background-image: none;
        background-color: #D4E6F1;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    mode = st.radio("Select a game mode :", ["📗 Draw amino acids", "🖌 Name amino acids"])
    if mode == "📗 Draw amino acids":
        draw_quizz()
    elif mode == "🖌 Name amino acids":
        name_quizz()
 

def show_learn():
    st.markdown("## 📚 Learn the amino acid")
    st.caption("What is the structure of a amino acid?") 
    st.write("An amino acid contains both amino and carboxylic acid functional groupe, a carbon alpha and a side chain which is variable."
             " In nature you can only find the L-configuration of amino acids, therefore they will be drawn in this configuration."
             )
    st.markdown(
    """
    <style>
    .stApp {
        background-image: none;
        background-color: #D4E6F1;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    img= "../../assets/aastruct.jpeg"
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
# Dropdown menu where you can select the amino acids to be drawn.
    selected_name = st.selectbox("Choose an amino acid:", list(amino_acids.keys()))

    smiles = amino_acids[selected_name]
    mol = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(mol, size=(400, 400))
    st.image(img, caption=selected_name, use_container_width=False)

    if st.button("🔙 Back to menu"):
        st.session_state.page = "menu"
        st.rerun()

if st.session_state.page == "menu":
    show_menu()
elif st.session_state.page == "quizz":
    show_quizz()
elif st.session_state.page == "learn":
    show_learn()
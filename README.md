<div align="center"> 
  <img src="assets/aminoacid.png" width="800">
</div>

![Coverage Status](assets/coverage-badge.svg)

<h1 align="center">
Aminoacid
</h1>

<br>


Aminoacid is an interactive game divided in two parts. The first one allows you to learn the structure of the 20 amino acids and then test your knowledge with the game with two functionalities. One allows you to draw amino acids from their name and the other is for naming amino acids according to their structure.


## 👩‍💻 Installation

Create a new environment, you may also give the environment a different name. 

```
conda create -n aminoacid python=3.10 
```

```
conda activate aminoacid
```

The package can be clone on your local machine using the following command lines:

```
git clone https://github.com/cbaruselli/aminoacid.git
```

Then, to install the package, you can run:

```
pip install -e .
```

## 🛠️ Requirements

The package requires other dependencies to run. The file "requirements.txt" lists all dependencies at the specific version we used. The package installation (previous section) should install the requirements properly. In case it failed or you want to install them separatly, use the following command:

```
pip install -r requirements.txt
```
In order to open the streamlit interface, run the following commands in "aminoacid" environment:

```
streamlit run aa_app.py
```

## Run tests and coverage

```
pip install tox
tox
```
If there is an error because of some dependencies issues, write the following commands:

```
pip install "pyproject-api<1.9"
pip install "packaging<25"
```

## 📖 Autors 

Chloé Baruselli: https://github.com/cbaruselli 

Monica Minazzo: https://github.com/mminazzo 

Naomi Pantillon: https://github.com/NaomiPant 

Cléa Pernet: https://github.com/clea04 

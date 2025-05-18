<div align="center"> 
  <img src="assets/aminoacid.png" width="800">
</div>

![Coverage Status](assets/coverage-badge.svg)

<h1 align="center">
Aminoacid
</h1>

<br>


Aminoacid is an interactive game divided in two parts. The first one allows you to learn the structure of the 20 aminoacids and then test your knowledge with the game with two functionalities. One allows you to draw amino acids from their name and the other for naming amino acids according to their structure.

## 🔥 Usage

```python
from mypackage import main_func

# One line to rule them all
result = main_func(data)
```

This usage example shows how to quickly leverage the package's main functionality with just one line of code (or a few lines of code). 
After importing the `main_func` (to be renamed by you), you simply pass in your `data` and get the `result` (this is just an example, your package might have other inputs and outputs). 
Short and sweet, but the real power lies in the detailed documentation.

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
In order to open the streamlit interface, run the following commands in "projet" environment:

```
streamlit run aa_app.py
```

### Run tests and coverage

```
pip install tox
tox
```

## 📖 Autors 

Chloé Baruselli: https://github.com/cbaruselli 

Monica Minazzo: https://github.com/mminazzo 

Naomi Pantillon: https://github.com/NaomiPant 

Cléa Pernet: https://github.com/clea04 

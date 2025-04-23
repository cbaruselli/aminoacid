![Project Logo](assets/aminoacid.png)

![Coverage Status](assets/coverage-badge.svg)

<h1 align="center">
Aminoacid
</h1>

<br>


Aminoacid is an interactive game to learn and test your knowledge of the different amino acids.

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

The package runs with different other packages to function properly. The file "requirements.txt" has been used to prevent compatibility issues. 

To install the packages in "requirements.txt", use the following commands:


```
pip install -r requirements.txt
```


### Run tests and coverage

```
pip install tox
tox
```

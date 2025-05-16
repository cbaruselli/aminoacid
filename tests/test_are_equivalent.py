from aminoacid.aa_app import are_equivalent
 
def test_are_equivalent(): 
    assert are_equivalent("CC(C(=O)O)N", "CC(C(=O)O)N") == True 

def test_are_not_equivalent():
    assert are_equivalent("CC(C(=O)O)N", "NC(CCCNC(=N)N)C(=O)O") == False

def test_1invalid_smiles():
    assert are_equivalent("not a smile", "CC(C(=O)O)N") == False

def test_onlyinvalid_smiles(): 
    assert are_equivalent("not a smile", "also wrong") == False 
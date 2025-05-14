import sys
import base64
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from aminoacid.aa_app import get_base64


def test_get_base64():
    """
    Test that the fonction get_base64 returns a string that is encoded in base64.
    """
    path = "../../assets/aminoacid2.png"
    encoded = get_base64(path)

    assert isinstance(encoded, str) #check if it return a str
    assert len(encoded) > 0 
import sys
import base64
import os
path = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "aminoacid2.png")
from aminoacid.aa_app import get_base64


def test_get_base64():
    """
    Test that the fonction get_base64 returns a string that is encoded in base64.
    """
    current_dir = os.path.dirname(__file__)
    path = os.path.join(current_dir, "..", "assets", "aminoacid2.png")
    encoded = get_base64(path)

    assert isinstance(encoded, str) #check if it return a str
    assert len(encoded) > 0 
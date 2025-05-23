from aminoacid.aa_app import get_base64

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
AMINOACID2_PATH = PROJECT_ROOT / "assets" / "aminoacid2.png"


def test_get_base64():
    """
    Test that the fonction get_base64 returns a string that is encoded in base64.
    """
    encoded = get_base64(AMINOACID2_PATH)

    assert isinstance(encoded, str) #check if it return a str
    assert len(encoded) > 0

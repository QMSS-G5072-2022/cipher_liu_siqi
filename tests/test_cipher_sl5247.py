from cipher_sl5247 import cipher_sl5247

def test_cipher():
    assert cipher_sl5247.cipher("text", 2, False) == "rcvr"

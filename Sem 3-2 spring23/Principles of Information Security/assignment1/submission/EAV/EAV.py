from ..PRG.PRG import PRG

# ---------------------- Utility Functions ----------------------
def int_to_bits(x: int):
    return str(bin(x))[2:]

def bits_to_int(x: str):
    return int(x, 2)

def pad(x: str, length: int) -> str:
    res = x
    while len(res) < length:
        res = "0" + res
    return res

def string_xor(a: str, b: str) -> str:
    if len(a) < len(b):
        pad(a, len(b))
    else:
        pad(b, len(a))
    
    res = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            res += "0"
        else:
            res += "1"
    return res

class Eavesdrop:

    prg = 0
    key = 0

    def __init__(self, security_parameter: int, key: int, expansion_factor: int,
                generator: int, prime_field: int):
        """
        Initialize values here
        :param security_parameter: 1ⁿ
        :type security_parameter: int
        :param key: k, uniformly sampled key
        :type key: int
        :param expansion_factor: l(n)
        :type expansion_factor: int
        :param generator: g
        :type generator: int
        :param prime_field: p
        :type prime_field: int
        """

        self.prg = PRG(security_parameter, generator, prime_field, expansion_factor)
        self.key = key

        pass

    def enc(self, message: str) -> str:
        """
        Encrypt Message against Eavesdropper Adversary
        :param message: message encoded as bit-string
        :type message: str
        """
        
        random_str = self.prg.generate(self.key)
        # random_int = bits_to_int(random_str)
        # message_int = bits_to_int(message)
        # ciphertext = message_int ^ random_int
        # return int_to_bits(ciphertext)

        return string_xor(message, random_str)

    def dec(self, cipher: str) -> str:
        """
        Decipher ciphertext
        :param cipher: ciphertext encoded as bit-string
        :type cipher: str
        """

        random_str = self.prg.generate(self.key)
        random_int = bits_to_int(random_str)
        cipher_int = bits_to_int(cipher)
        message = cipher_int ^ random_int
        return int_to_bits(message)
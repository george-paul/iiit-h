from ..PRF.PRF import PRF
from ..utility.utility import *

# ---------------------- Utility Functions ----------------------




class CPA:

    prf = 0
    key = 0
    security_parameter = 0
    mode = "CTR"    

    def __init__(self, security_parameter: int, prime_field: int,
                generator: int, key: int, mode="CTR"):
        """
        Initialize the values here
        :param security_parameter: 1ⁿ
        :type security_parameter: int
        :param prime_field: q
        :type prime_field: int
        :param generator: g
        :type generator: int
        :param key: k
        :type key: int
        :param mode: Block-Cipher mode of operation
            - CTR
            - OFB
            - CBC
        :type mode: str
        """

        self.prf = PRF(security_parameter, generator, prime_field, key)
        self.key = key
        self.security_parameter = security_parameter
        self.mode = mode
        pass

    def enc_unit(self, random_seed: int) -> str:
        prfgen = self.prf.evaluate(random_seed)
        return int_to_bits(prfgen)

    def enc(self, message: str, random_seed: int) -> str:
        """
        Encrypt message against Chosen Plaintext Attack using randomized ctr mode
        :param message: m
        :type message: int
        :param random_seed: ctr
        :type random_seed: int
        """

        r = random_seed
        r += 1
        ciphertext = ""

        for i in range(self.security_parameter, len(message) + 1 , self.security_parameter):
            encgen = self.enc_unit(r)
            ciphertext += string_xor(message[i-self.security_parameter:i], encgen)
            r += 1
        
        #do padding
        random_seed_string = int_to_bits(random_seed)
        random_seed_string = pad(random_seed_string, self.security_parameter)
        
        return random_seed_string + ciphertext

    def dec(self, cipher: str) -> str:
        """
        Decrypt ciphertext to obtain plaintext message
        :param cipher: ciphertext c
        :type cipher: str
        """

        r = bits_to_int(cipher[0:self.security_parameter])
        r += 1
        c = cipher[self.security_parameter:]

        m = ""

        for i in range(self.security_parameter, len(c) + 1 , self.security_parameter):
            encgen = self.enc_unit(r)
            m += string_xor(c[i-self.security_parameter:i], encgen)
            r += 1

        return m
from ..PRG.PRG import PRG
from ..utility.utility import *

class PRF:

    prg = 0
    k = 0

    def __init__(self, security_parameter: int, generator: int, prime_field: int,  key: int):
        """
        Initialize values here
        :param security_parameter: 1ⁿ
        :type security_parameter: int
        :param generator: g
        :type generator: int
        :param prime_field: p
        :type prime_field: int
        :param key: k, uniformly sampled key
        :type key: int
        """
        self.prg = PRG(security_parameter, generator, prime_field, 2)
        self.k = key
        pass



    def evaluate(self, x: int) -> int:
        """
        Evaluate the pseudo-random function at `x`
        :param x: input for Fₖ
        :type x: int
        """
        
        input_str = int_to_bits(x)
        input_str = pad(input_str, self.prg.security_parameter)
        
        self.prg.expansion_factor = 2 * len(input_str)        
        s = int_to_bits(self.k)

        for i in range(len(input_str)):
            prg_output = self.prg.generate(bits_to_int(s))
            if input_str[i] == '0':
                s = prg_output[0:len(prg_output)//2]
            else:
                s = prg_output[len(prg_output)//2:]
        return bits_to_int(s)
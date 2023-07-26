from ..utility.utility import *

class PRG:

    security_parameter = 0
    generator = 0
    prime_field = 0
    expansion_factor = 0

    def __init__(self, security_parameter: int, generator: int,
                prime_field: int, expansion_factor: int):
        """
        Initialize values here
        :param security_parameter: n (from 1ⁿ)
        :type security_parameter: int
        :param generator: g
        :type generator: int
        :param prime_field: p
        :type prime_field: int
        :param expansion_factor: l(n)
        :type expansion_factor: int
        """
        self.security_parameter = security_parameter
        self.generator = generator
        self.prime_field = prime_field
        self.expansion_factor = expansion_factor

        pass

    def generate(self, seed: int) -> str:
        """
        Generate the pseudo-random bit-string from `seed`
        :param seed: uniformly sampled seed
        :type seed: int
        """
        output = ""
        s = seed
        msb = 0

        for i in range(0, self.expansion_factor):
            if s < ((self.prime_field - 1)/2):
                msb = 0
            else:
                msb = 1
            s = (self.generator ** s) % self.prime_field
            output += str(msb)

        return output


# prg = PRG(7, 13, 41, 10)
# print(prg.generate(17))
# prg = PRG(9, 4, 11, 12)
# print(prg.generate(35))
# prg = PRG(7, 7, 17, 11)
# print(prg.generate(125))
# prg = PRG(9, 35, 97, 20)
# print(prg.generate(263))
# prg = PRG(8, 191, 36, 16)
# print(prg.generate(150))
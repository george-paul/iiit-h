from ..PRF.PRF import PRF
from ..utility.utility import *

class MAC:

    prf = 0
    security_parameter = 0

    def __init__(self, security_parameter: int, prime_field: int,
                generator: int, seed: int):
        """
        Initialize the values here
        :param security_parameter: 1ⁿ
        :type security_parameter: int
        :param prime_field: q
        :type prime_field: int
        :param generator: g
        :type generator: int
        :param seed: k
        :type seed: int
        """

        self.prf = PRF(security_parameter, generator, prime_field, seed)
        self.security_parameter = security_parameter
        pass

    def mac(self, message: str, random_identifier: int) -> str:
        """
        Generate tag t
        :param random_identifier: r
        :type random_identifier: int
        :param message: message encoded as bit-string
        :type message: str
        """
        pass

    def vrfy(self, message: str, tag: str) -> bool:
        """
        Verify whether the tag commits to the message
        :param message: m
        :type message: str
        :param tag: t
        :type tag: str
        """
        pass
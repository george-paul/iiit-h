from submission.PRF.PRF import PRF
from submission.EAV.EAV import Eavesdrop
from submission.CPA.CPA import CPA

# prf = PRF(8, 36, 191, 150)
# print(prf.evaluate(190))
# prf = PRF(8, 45, 137, 129)
# print(prf.evaluate(201))
# prf = PRF(10, 71, 179, 568)
# print(prf.evaluate(890))
# prf = PRF(11, 44, 107, 1056)
# print(prf.evaluate(1300))
# prf = PRF(12, 14, 79, 1389)
# print(prf.evaluate(1780))

# e = Eavesdrop(7, 16, 7, 21, 59)
# print(e.enc("1000101"))
# print(e.dec("1100101"))

# e = Eavesdrop(8, 19, 8, 28, 163)
# print(e.enc("10101001"))
# print(e.dec("11000000"))

# e = Eavesdrop(8, 156, 8, 71, 599)
# print(e.enc("10101001"))
# print(e.dec("11111011"))

# e = Eavesdrop(10, 312, 10, 213, 719)
# print(e.enc("1010110010"))
# print(e.dec("1110110011"))

# e = Eavesdrop(10, 112, 10, 259, 881)
# print(e.enc("1010110010"))
# print(e.dec("1010100101"))

# cpa = CPA(4,307,112,58)
# print(cpa.dec(cpa.enc("1010100011100111",4)))
# cpa = CPA(5,599,189,145)
# print(cpa.dec(cpa.enc("11100011011110010111",7)))
# cpa = CPA(6,881,217,113)
# print(cpa.dec(cpa.enc("101011011101",5)))
# cpa = CPA(6,59,14,10)
# print(cpa.dec(cpa.enc("111000101010",37)))
# cpa = CPA(8,11,3,15)
# print(cpa.dec(cpa.enc("1010100110110111",8)))

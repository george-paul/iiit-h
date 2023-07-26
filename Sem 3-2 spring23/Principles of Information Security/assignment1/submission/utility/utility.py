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
        fa = a
        fb = b
        if len(a) < len(b):
            fa = pad(a, len(b))
        else:
            fb = pad(b, len(a))
        
        res = ""
        for i in range(len(fa)):
            if fa[i] == fb[i]:
                res += "0"
            else:
                res += "1"
        return res
def leftrotate(value: int, shift: int) -> int:
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF


def sha1(message: bytes) -> bytes:
    h = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]
    ml = len(message) * 8
    pm = message + b"\x80"
    while (len(pm) * 8) % 512 != 448:
        pm += b"\x00"
    pm += ml.to_bytes(8, "big")
    chunks = [pm[i : i + 64] for i in range(0, len(pm), 64)]
    for c in chunks:
        w = {i:int.from_bytes(c[p : p + 4], "big") for i, p in enumerate(range(0, len(c), 4))}
        for i in range(16, 80):
            w[i] = leftrotate(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16], 1)
        a, b, c, d, e = h
        for i in range(80):
            if 0 <= i < 20:
                f = (b & c) | (~b & d)
                k = 0x5A827999
            elif 20 <= i < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            temp = (leftrotate(a, 5) + f + e + k + w[i]) & 0xFFFFFFFF
            a, b, c, d, e = temp, a, leftrotate(b, 30), c, d
        h = [(h[i] + x) & 0xFFFFFFFF for i, x in enumerate([a, b, c, d, e])]
    return b''.join(x.to_bytes(4, 'big') for x in h)

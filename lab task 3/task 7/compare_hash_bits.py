def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str)*4)

h1 = "1a758a0b08d57415cdf418c15ebaf779bfb27379c13fdfbc01109bea792f9a2b"
h2 = "cafa591a5e28742392824db53e38014f3ad4ab117aaf31f8f0cceb71823d1a0d"

b1 = hex_to_bin(h1)
b2 = hex_to_bin(h2)

same_bits = sum(c1 == c2 for c1, c2 in zip(b1, b2))
print(f"Total same bits: {same_bits} / {len(b1)}")

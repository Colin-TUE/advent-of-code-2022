from algo import compute

gps, gps10 = compute("example.csv")

assert gps == 3, f"expected 3 got {gps}"
assert gps10 == 1623178306, f"expected 1623178306 got {gps10}"

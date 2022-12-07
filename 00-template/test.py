from algo import compute

ass1, ass2 = compute("example.csv")

assert ass1 == 42, f"expected 42 got {ass1}"
assert ass2 == 252, f"expected 252 got {ass2}"

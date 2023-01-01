from algo import compute

path, ass2 = compute("example.csv")

assert path == 31, f"expected 31 got {path}"
assert ass2 == 252, f"expected 252 got {ass2}"

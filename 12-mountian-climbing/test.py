from algo import compute

path, pathToA = compute("example.csv")

assert path == 31, f"expected 31 got {path}"
assert pathToA == 29, f"expected 29 got {pathToA}"

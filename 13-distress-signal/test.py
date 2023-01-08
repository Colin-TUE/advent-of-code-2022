from algo import compute

sumIndices, ass2 = compute("example.csv")

assert sumIndices == 13, f"expected 13 got {sumIndices}"
# assert ass2 == 252, f"expected 252 got {ass2}"

sumIndices, ass2 = compute("test.csv")

assert sumIndices == 43, f"expected 43 got {sumIndices}"
# assert ass2 == 252, f"expected 252 got {ass2}"

from algo import compute

nrOfSections, ass2 = compute("example.csv")

assert nrOfSections == 2, f"expected 2 got {nrOfSections}"
assert ass2 == 252, f"expected 252 got {ass2}"

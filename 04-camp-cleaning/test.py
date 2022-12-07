from algo import compute

nrOfSections, overlappingPairs = compute("example.csv")

assert nrOfSections == 2, f"expected 2 got {nrOfSections}"
assert overlappingPairs == 4, f"expected 4 got {overlappingPairs}"

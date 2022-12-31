from algo import compute

nrVisibleTrees, scenicScore = compute("example.csv")

assert nrVisibleTrees == 21, f"expected 21 got {nrVisibleTrees}"
assert scenicScore == 8, f"expected 8 got {scenicScore}"

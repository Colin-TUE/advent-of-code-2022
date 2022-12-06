from algo import compute

highestValue, sumThreeHighest = compute("example.csv")

assert highestValue == 24000, f"expected 24000 got {highestValue}"
assert sumThreeHighest == 45000, f"expected 45000 got {sumThreeHighest}"

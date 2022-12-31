from algo import compute

visitedPositions, visitedPositionsRope = compute("example.csv")

assert visitedPositions == 13, f"expected 13 got {visitedPositions}"
assert visitedPositionsRope == 1, f"expected 1 got {visitedPositionsRope}"

visitedPositions, visitedPositionsRope = compute("example2.csv")
assert visitedPositionsRope == 36, f"expected 36 got {visitedPositionsRope}"

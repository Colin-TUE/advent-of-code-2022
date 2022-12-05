from algo import compute

score,newScore = compute("example.csv")
assert score == 15, f"expected 15 got {score}"
assert newScore == 12, f"expected 12 got {newScore}"

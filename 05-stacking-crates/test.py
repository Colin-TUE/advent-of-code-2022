from algo import compute

outputOne, outputMany = compute("example.csv")

assert outputOne == 'CMZ', f"expected CMZ got {outputOne}"
assert outputMany == 'CMZ', f"expected CMZ got {outputMany}"

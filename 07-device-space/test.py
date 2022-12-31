from algo import compute

totalSize, minSpaceRemoved = compute("example.csv")

assert totalSize == 95437, f"expected 95437 got {totalSize}"
assert minSpaceRemoved == 24933642, f"expected 24933642 got {minSpaceRemoved}"

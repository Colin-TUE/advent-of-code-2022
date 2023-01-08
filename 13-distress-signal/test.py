from algo import compute

sumIndices, decoderKey = compute("example.csv")

assert sumIndices == 13, f"expected 13 got {sumIndices}"
assert decoderKey == 140, f"expected 140 got {decoderKey}"

sumIndices, decoderKey = compute("test.csv")

assert sumIndices == 43, f"expected 43 got {sumIndices}"
assert decoderKey == 396, f"expected 396 got {decoderKey}"

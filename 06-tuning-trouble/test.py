import array
from algo import compute

startMarkerChars, startMessageChars = compute("example.csv")

assert startMarkerChars.tolist() == [7, 5, 6, 10, 11], f"expected [7, 5, 6, 10, 11] got {startMarkerChars}"
assert startMessageChars.tolist() == [19, 23, 23, 29, 26], f"expected [19, 23, 23, 29, 26] got {startMessageChars}"

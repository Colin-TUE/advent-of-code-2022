from algo import compute

signalStrengths, ass2 = compute("example.csv")

assert signalStrengths == ([420, 1140, 1800, 2940, 2880, 3960], 
                           13140), f"expected ([420, 1140, 1800, 2940, 2880, 3960], 13140) got {signalStrengths}"
assert ass2 == 252, f"expected 252 got {ass2}"

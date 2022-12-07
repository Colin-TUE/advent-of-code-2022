from algo import compute

prios, badgePrios = compute("example.csv")

assert prios == 157, f"expected 157 got {prios}"
assert badgePrios == 70, f"expected 252 got {badgePrios}"

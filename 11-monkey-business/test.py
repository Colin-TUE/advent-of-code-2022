from algo import compute

monkeyBusiness, monkeyBusinessUnmanageable = compute("example.csv")

assert monkeyBusiness == 10605, f"expected 10605 got {monkeyBusiness}"
assert monkeyBusinessUnmanageable == 2713310158, f"expected 2713310158 got {monkeyBusinessUnmanageable}"

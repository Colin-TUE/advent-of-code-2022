from algo import compute

path, pathToA = compute("input.csv")

print(f"Shortest Path has length: {path}")
print(f"Shortest Path to any A has length: {pathToA}")

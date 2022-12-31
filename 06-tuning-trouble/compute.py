from algo import compute

startMarkerPosition, startMessagePosition = compute("input.csv")

print(f"Position of the marker is: {startMarkerPosition[0]}")
print(f"Position of the message is: {startMessagePosition[0]}")

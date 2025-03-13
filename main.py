density = 0.998773 

def mass_to_volume(mass):
    return mass / density

def calculate_mean(values):
    total = sum(values)
    count = len(values)
    return total / count

def calculate_standard_deviation(values, mean):
    squared_diffs = [(x - mean) ** 2 for x in values]
    variance = sum(squared_diffs) / (len(values) - 1)
    return variance ** 0.5

masses = [float(input(f"Enter mass {i+1} (g): ")) for i in range(5)]

volumes = [mass_to_volume(m) for m in masses]

mean_volume = calculate_mean(volumes)
std_dev_volume = calculate_standard_deviation(volumes, mean_volume)

for i, (mass, volume) in enumerate(zip(masses, volumes), 1):
    print(f"Mass {i}: {mass:.3f} g -> Volume: {volume:.3f} mL")

print(f"\nMean Volume: {mean_volume:.3f} mL")
print(f"Standard Deviation: {std_dev_volume:} mL")
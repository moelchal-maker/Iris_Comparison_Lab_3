import pandas as pd
import os




# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

sepal_df = pd.read_csv(os.path.join(script_dir, "Sepal_Data.csv"))
petal_df = pd.read_csv(os.path.join(script_dir, "Petal_Data.csv"))



# Combine Datasets


iris_df = pd.merge(sepal_df, petal_df, on=["sample_id", "species"])


print("\nCombined DataFrame:")
print(iris_df.head())


# Correlation Between Variables


# Select only numeric measurement columns
measurements = iris_df[
    ["petal_length", "petal_width",
     "sepal_length", "sepal_width"]
]

correlation_matrix = measurements.corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

# 6 unique comparisons:
# petal_length vs petal_width
# petal_length vs sepal_length
# petal_length vs sepal_width
# petal_width vs sepal_length
# petal_width vs sepal_width
# sepal_length vs sepal_width


# Average of Each Variable (All Species Combined)

means = measurements.mean()

print("\nMean of Each Variable:")
print(means)

# Median of Each Variable


medians = measurements.median()

print("\nMedian of Each Variable:")
print(medians)

# Standard Deviation of Each Variable

std_devs = measurements.std()#That's a crazy abbreviation 

print("\nStandard Deviation of Each Variable:")
print(std_devs)


# Species Comparison (Similarity)

species_means = iris_df.groupby("species").mean(numeric_only=True)

print("\nMean Measurements by Species:")
print(species_means)

# To compare similarity, calculate difference between species means
species_difference = species_means.diff().abs()

print("\nAbsolute Differences Between Species Means:")
print(species_difference)


# Which species are most/least similar?

print("\n" + "="*70)
print("SPECIES SIMILARITY ANALYSIS")
print("="*70)

measurement_columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
species_list = iris_df["species"].unique()
distances = {}

# Calculate distance between each species pair
for i, s1 in enumerate(species_list):
    for s2 in species_list[i+1:]:
        mean1 = iris_df[iris_df["species"] == s1][measurement_columns].mean()
        mean2 = iris_df[iris_df["species"] == s2][measurement_columns].mean()
        distance = ((mean1 - mean2) ** 2).sum() ** 0.5
        distances[f"{s1} vs {s2}"] = distance

sorted_dist = sorted(distances.items(), key=lambda x: x[1])

print(f"\nMost Similar:   {sorted_dist[0][0]} (Distance: {sorted_dist[0][1]:.3f})")
print(f"Least Similar:  {sorted_dist[-1][0]} (Distance: {sorted_dist[-1][1]:.3f})")

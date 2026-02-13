# Iris_Comparison_Lab_3
To analyze data about Irises

Purpose
This project uses pandas to analyze the Iris dataset and compare three species based on their physical measurements. The goal is to understand how the measurements relate to one another and determine which species are most similar and least similar using statistical evidence.

Implementation
The program loads two CSV files containing sepal and petal measurements and merges them into one DataFrame using sample_id and species. It then calculates correlation, mean, median, and standard deviation for petal length, petal width, sepal length, and sepal width. The data is also grouped by species to compare average measurements.

Results
The analysis shows that Versicolor and Virginica are the most similar species because their average measurements are close in value. Setosa is the least similar because its petal measurements are significantly smaller than the others.

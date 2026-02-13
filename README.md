# Iris_Comparison_Lab_3
To analyze data about Irises

This project analyzes a Iris dataset using pandas to combine sepal and petal measurements into a single DataFrame and analyze the information. The program loads two CSV files, merges them using sample_id and species, and calculates correlation, mean, median, and standard deviation for petal length, petal width, sepal length, and sepal width. Grouped averages by species are used to compare similarity. Results show that Versicolor and Virginica are the most similar species based on close mean measurements, while Setosa is the least similar due to significantly smaller petal dimensions. The implementation uses pandas DataFrames, OS and built-in methods such as read_csv, merge, corr, mean, median, std, and groupby. 

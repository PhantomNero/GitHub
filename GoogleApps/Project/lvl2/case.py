import csv
import matplotlib.pyplot as plt

# Read in the data from the CSV file
with open('countries of the world.csv') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row

    # Create lists to store the data
    countries = []
    populations = []

    # Loop through the rows and extract the data
    for row in reader:
        countries.append(row[0])
        populations.append(int(row[1]))

# Create the horizontal bar graph
plt.barh(countries, populations)

# Set the chart title
plt.title("Population of Countries")

# Show the chart
plt.show()

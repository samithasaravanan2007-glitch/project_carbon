import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data/emissions.csv")

# Print basic info
print("Total Emissions:", data["Emissions (Million Tons CO2)"].sum())

# Plot emissions by sector
plt.figure()
plt.bar(data["Sector"], data["Emissions (Million Tons CO2)"])
plt.xlabel("Sector")
plt.ylabel("Emissions (Million Tons CO2)")
plt.title("Carbon Emissions by Sector - Chennai")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("emissions_chart.png")
plt.show()

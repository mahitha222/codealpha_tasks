# =========================================================
# TASK 2: Unemployment Analysis in India
# =========================================================

# 1️⃣ Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt

# 2️⃣ Load Dataset
df = pd.read_csv("Unemployment in India.csv")

# 3️⃣ Data Cleaning

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Sort data by date
df = df.sort_values('Date')

# Drop missing values
df = df.dropna()

print("Dataset Cleaned Successfully!\n")

# 4️⃣ Overall Monthly Average Unemployment
monthly_avg = df.groupby('Date')['Estimated Unemployment Rate (%)'].mean()

# 5️⃣ Plot Overall Unemployment Trend
plt.figure()
plt.plot(monthly_avg.index, monthly_avg.values)
plt.axvline(pd.to_datetime("2020-03-01"), linestyle='--')
plt.title("Overall Unemployment Rate Trend in India")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6️⃣ Covid Impact Analysis

pre_covid = monthly_avg[monthly_avg.index < "2020-03-01"].mean()
during_covid = monthly_avg[
    (monthly_avg.index >= "2020-03-01") &
    (monthly_avg.index <= "2020-12-31")
].mean()

print("Pre-Covid Average Unemployment Rate: {:.2f}%".format(pre_covid))
print("During-Covid Average Unemployment Rate: {:.2f}%".format(during_covid))

# 7️⃣ Seasonal Analysis

df['Month'] = df['Date'].dt.month
seasonal_avg = df.groupby('Month')['Estimated Unemployment Rate (%)'].mean()

plt.figure()
plt.bar(seasonal_avg.index, seasonal_avg.values)
plt.title("Seasonal Pattern of Unemployment Rate")
plt.xlabel("Month")
plt.ylabel("Average Unemployment Rate (%)")
plt.tight_layout()
plt.show()

# 8️⃣ Additional Analysis: Rural vs Urban

area_avg = df.groupby('Area')['Estimated Unemployment Rate (%)'].mean()

plt.figure()
plt.bar(area_avg.index, area_avg.values)
plt.title("Average Unemployment Rate: Rural vs Urban")
plt.xlabel("Area")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()

print("\nAverage Unemployment by Area:")
print(area_avg)

# =========================================================
# END OF PROJECT
# =========================================================
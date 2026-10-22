import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

df2019 = pd.read_csv("/Users/am25aet/OneDrive - University of Hertfordshire/Small Project/2019data8.csv")
df2022 = pd.read_csv("/Users/am25aet/OneDrive - University of Hertfordshire/Small Project/2022data8.csv")


df2019["Date"] = pd.to_datetime(df2019["Date"])
df2022["Date and time"] = pd.to_datetime(df2022["Date and time"])

df2019["Total"] = (
    df2019["Bus pax number peak"] + df2019["Bus pax number offpeak"] +
    df2019["Tram pax number peak"] + df2019["Tram pax number offpeak"] +
    df2019["Metro pax number peak"] + df2019["Metro pax number offpeak"]
)

df2019["norm"] = df2019["Total"] / df2019["Total"].max()
df2019["day"] = range(1, len(df2019)+1)

df2022["date_only"] = df2022["Date and time"].dt.date
daily22 = df2022.groupby("date_only").size().reset_index(name="Total")
daily22["norm"] = daily22["Total"] / daily22["Total"].max()
daily22["day"] = range(1, len(daily22)+1)

def smooth(y, terms=8):
    Y = np.fft.rfft(y)
    Y[terms+1:] = 0
    return np.fft.irfft(Y, n=len(y))

smooth19 = smooth(df2019["norm"].values)
smooth22 = smooth(daily22["norm"].values)

df2022["month"] = df2022["Date and time"].dt.month
spring = df2022[df2022["month"].isin([3,4,5])]
summer = df2022[df2022["month"].isin([6,7,8])]
autumn = df2022[df2022["month"].isin([9,10,11])]
total_2022 = len(df2022)

X = 100 * len(spring) / total_2022
Y = 100 * len(summer) / total_2022
Z = 100 * len(autumn) / total_2022

print("\nSeasonal Journey Fractions (2022):")
print("X (Spring %):", round(X,2))
print("Y (Summer %):", round(Y,2))
print("Z (Autumn %):", round(Z,2))

bus19 = df2019["Bus pax number peak"].sum() + df2019["Bus pax number offpeak"].sum()
tram19 = df2019["Tram pax number peak"].sum() + df2019["Tram pax number offpeak"].sum()
metro19 = df2019["Metro pax number peak"].sum() + df2019["Metro pax number offpeak"].sum()
total19 = bus19 + tram19 + metro19

bus22 = len(df2022[df2022["Mode"]=="Bus"])
tram22 = len(df2022[df2022["Mode"]=="Tram"])
metro22 = len(df2022[df2022["Mode"]=="Metro"])
total22 = bus22 + tram22 + metro22

print("\nTransport Mode Percentages:")
print("2019 Bus:", round(100*bus19/total19,2), "%")
print("2019 Tram:", round(100*tram19/total19,2), "%")
print("2019 Metro:", round(100*metro19/total19,2), "%")
print("2022 Bus:", round(100*bus22/total22,2), "%")
print("2022 Tram:", round(100*tram22/total22,2), "%")
print("2022 Metro:", round(100*metro22/total22,2), "%")

metro = df2022[df2022["Mode"] == "Metro"]
xv = metro["Distance"]
yv = metro["Price"]

slope, intercept, r, p, err = linregress(xv, yv)
line = slope * xv + intercept

print("\nRegression Results (Metro Price vs Distance):")
print("Slope:", round(slope,4))
print("Intercept:", round(intercept,4))
print("R-squared:", round(r**2,4))

plt.figure(figsize=(12,6))
plt.scatter(df2019["day"], df2019["norm"], s=20, color="steelblue", alpha=0.7)
plt.scatter(daily22["day"], daily22["norm"], s=20, color="darkorange", alpha=0.7)
plt.plot(df2019["day"], smooth19, linewidth=3, color="indigo")
plt.plot(daily22["day"], smooth22, linewidth=3, color="orangered")
plt.grid(True, linestyle="--", alpha=0.4)
plt.title("Figure 1: Daily Public Transport Usage (2019 vs 2022) with Fourier Smoothing\nStudent ID: 24112386", fontsize=15, fontweight="bold")
plt.xlabel("Day of Year")
plt.ylabel("Passenger Count")
plt.legend(["2019 Smoothed","2022 Smoothed","2019 Normalised","2022 Normalised"])
plt.tight_layout()
plt.savefig("Figure1_24112386.png", dpi=300)
plt.show()

df2019["weekday"] = df2019["Date"].dt.weekday
df2022["weekday"] = df2022["Date and time"].dt.weekday

w19 = df2019.groupby("weekday")["norm"].mean()
w22 = df2022.groupby("weekday").size() / df2022.groupby("weekday").size().max()

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
x = np.arange(7)

plt.figure(figsize=(12,6))
plt.bar(x - 0.2, w19.values, width=0.4, color="steelblue")
plt.bar(x + 0.2, w22.values, width=0.4, color="darkorange")
plt.grid(True, linestyle="--", alpha=0.4)
plt.title("Figure 2: Average Passenger Numbers by Weekday (2019 vs 2022)\nStudent ID: 24112386", fontsize=15, fontweight="bold")
plt.xticks(x, days)
plt.ylabel("Average Passengers")
plt.legend(["2019 (Normalised)", "2022 (Normalised)"])

plt.text(0.03, 0.92,
         f"X = {X:.2f}%   Y = {Y:.2f}%   Z = {Z:.2f}%",
         transform=plt.gca().transAxes,
         fontsize=14, fontweight="bold", color="black",
         bbox=dict(facecolor="white", edgecolor="black", boxstyle="round,pad=0.3"))

plt.tight_layout()
plt.savefig("Figure2_24112386.png", dpi=300)
plt.show()

plt.figure(figsize=(10,6))
plt.scatter(xv, yv, color="indigo", s=40)
plt.plot(xv, line, color="orangered", linewidth=3)
plt.grid(True, linestyle="--", alpha=0.4)
plt.title("Figure 3: Metro Price vs Distance with Linear Regression Fit\nStudent ID: 24112386", fontsize=15, fontweight="bold")
plt.xlabel("Distance (km)")
plt.ylabel("Price (€)")
plt.legend(["Regression Fit", "Metro Trips"])

plt.text(0.05, 0.90,
         f"Price = {slope:.3f}x + {intercept:.3f}",
         transform=plt.gca().transAxes,
         fontsize=14, fontweight="bold", color="orangered",
         bbox=dict(facecolor="white", edgecolor="orangered", boxstyle="round,pad=0.3"))

plt.tight_layout()
plt.savefig("Figure3_24112386.png", dpi=300)
plt.show()

vals19 = [100*bus19/total19, 100*tram19/total19, 100*metro19/total19]
vals22 = [100*bus22/total22, 100*tram22/total22, 100*metro22/total22]

modes = ["Bus","Tram","Metro"]
x = np.arange(3)

plt.figure(figsize=(12,6))
plt.bar(x - 0.2, vals19, width=0.4, color="steelblue")
plt.bar(x + 0.2, vals22, width=0.4, color="darkorange")
plt.grid(True, linestyle="--", alpha=0.4)
plt.title("Figure 4: Percentage Share of Journeys by Transport Mode (2019 vs 2022)\nStudent ID: 24112386", fontsize=15, fontweight="bold")
plt.xlabel("Mode")
plt.ylabel("Percentage (%)")
plt.xticks(x, modes)
plt.legend(["2019","2022"])
plt.tight_layout()
plt.savefig("Figure4_24112386.png", dpi=300)
plt.show()

# Public Transport Analysis: 2019 vs 2022

## Project Overview

This project uses Python to explore public transport data from 2019 and 2022. It examines passenger counts, journey patterns, transport-mode shares, seasonal journey fractions, and the relationship between metro journey distance and price.

The analysis combines data preparation, descriptive calculations, visualisation and linear regression to explore patterns in the supplied datasets.

## Research Objectives

- Explore daily public transport passenger counts in 2019.
- Examine journey records from 2022.
- Compare bus, tram and metro usage using the available data.
- Investigate journey patterns across weekdays and seasons.
- Explore the relationship between metro journey distance and price using linear regression.
- Produce visualisations to communicate the results.

## Datasets

### 2019 dataset — `2019data8.csv`

Contains 358 daily records and 13 columns, including:

- Date
- Bus passenger counts during peak and off-peak periods
- Bus peak and off-peak prices
- Tram passenger counts during peak and off-peak periods
- Tram peak and off-peak prices
- Metro passenger counts during peak and off-peak periods
- Metro peak and off-peak prices

### 2022 dataset — `2022data8.csv`

Contains 30,000 journey records and five columns:

| Column | Description |
|---|---|
| `Date and time` | Date and time of the journey |
| `Mode` | Transport mode, such as bus, tram or metro |
| `Distance` | Journey distance |
| `Duration` | Recorded journey duration |
| `Price` | Journey price |

The units and precise definitions should be confirmed from the original dataset documentation.

## Tools and Libraries

- Python
- pandas — data manipulation
- NumPy — numerical operations and Fourier smoothing
- Matplotlib — chart creation
- SciPy — linear regression

## Methodology

### 1. Data loading and preparation

The script loads both CSV files, converts date fields to datetime format and derives additional variables for analysis.

For 2019, passenger counts across bus, tram and metro peak/off-peak categories are combined into a total. For 2022, journey records are grouped by date to calculate daily record counts.

### 2. Trend visualisation

The first figure compares normalised daily values for 2019 and 2022 and applies Fourier-based smoothing to highlight broad patterns.

### 3. Weekday and seasonal analysis

The second figure compares weekday-related measures. The script also calculates the proportions of 2022 records falling in spring (March–May), summer (June–August) and autumn (September–November).

### 4. Metro price and distance

The third figure uses linear regression to examine the relationship between metro journey distance and price. The script reports the slope, intercept and R-squared value.

### 5. Transport-mode comparison

The fourth figure compares the calculated percentage shares of bus, tram and metro activity for the two datasets.

## Visualisations

The script generates four PNG figures:

| Figure | Description |
|---|---|
| `Figure1_24112386.png` | Daily public transport usage with Fourier smoothing |
| `Figure2_24112386.png` | Weekday comparison and seasonal journey fractions |
| `Figure3_24112386.png` | Metro price versus distance with linear regression |
| `Figure4_24112386.png` | Percentage share by transport mode |

## Repository Structure

```text
public-transport-analysis-2019-2022/
├── README.md
├── 24112386.py
├── 2019data8.csv
├── 2022data8.csv
└── figures/
    ├── Figure1_24112386.png
    ├── Figure2_24112386.png
    ├── Figure3_24112386.png
    └── Figure4_24112386.png
```

The `figures/` directory is the suggested location for the generated PNG files. Create it and place the exported figures there if you want to use this structure.

## How to Run

### Install dependencies

```bash
pip install pandas numpy matplotlib scipy
```

### Run the analysis

Place the Python script and both CSV files in the same directory. Update the file paths in the script to relative paths:

```python
df2019 = pd.read_csv("2019data8.csv")
df2022 = pd.read_csv("2022data8.csv")
```

Then run:

```bash
python 24112386.py
```

The script generates the visualisations and prints the calculated statistics.

## Limitations

- The datasets have different structures: 2019 contains daily aggregated passenger counts, while 2022 contains individual journey records.
- Some comparisons use different underlying measures and should not be interpreted as direct, like-for-like comparisons without further aggregation and validation.
- The current weekday comparison uses different calculations for 2019 and 2022, so its results require careful interpretation.
- The script uses normalised values for some plots; these do not represent raw passenger counts.
- The seasonal calculations cover spring, summer and autumn only.
- Linear regression describes an association between metro distance and price; it does not establish causation.
- The dataset source, geographic coverage, units and licensing terms should be documented using the original data provider's information.

## Conclusion

This project demonstrates a Python workflow for analysing public transport data across two years. It combines trend visualisation, weekday and seasonal calculations, transport-mode comparisons and linear regression to explore the available information.

Further improvements could standardise the measures across datasets, validate the aggregation methods, document the source data and strengthen the statistical interpretation.

## Academic Context

This repository contains the code, supporting datasets and visual outputs for an academic data analysis project.

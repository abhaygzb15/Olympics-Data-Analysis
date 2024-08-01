# Olympics-Data-Analysis

The given dataset can be accessed from here: [Kaggle Olympics Dataset](https://www.kaggle.com/datasets/krishd123/olympics-legacy-1896-2020).

## Introduction
This project involves a comprehensive Exploratory Data Analysis (EDA) on the modern Olympic Games dataset, spanning from Athens 1896 to Rio 2020. The dataset, collected from Kaggle, allows for an in-depth analysis of how the Olympics have evolved over time, focusing on various aspects such as the participation and performance of different nations, genders, sports, and events.

## About the Dataset
The project utilizes three primary datasets:

1. **all_athlete_games.csv**: Contains 286,237 rows and 12 columns, where each row corresponds to an individual athlete competing in an Olympic event.
2. **all_regions.csv**: Contains 235 rows and 2 columns, providing a mapping of National Olympic Committee (NOC) codes to regions.
3. **host_country.csv**: Contains information about the host countries of the Olympic Games. Has 2 columns - Year and Host Country

## Project Structure
1. **Importing the Required Python Libraries**
   The analysis makes use of various Python libraries including Pandas, Numpy, Matplotlib, Seaborn, Scipy, Plotly, and Scikit-Learn.

2. **Importing the Datasets**
   Data is loaded from CSV files and initial inspections such as checking shapes and data types are performed to ensure proper data import.

3. **Data Cleaning**
   The data cleaning process includes:
   - Filtering for Summer Olympics data.
   - Merging datasets to include region information.
   - Handling missing values and duplicates.
   - Restructuring the medal data for better analysis.

4. **Exploratory Data Analysis (EDA)**
   The EDA covers:
   - Historical trends in Olympic Games, such as the years and cities in which the games were organized.
   - Country-wise participation and medal tallies.
   - Analysis of athlete performance and demographics.
   - Gender participation trends over the years.

5. **Data Visualization**
   Data visualization techniques are employed to present insights on:
   - Top countries with the highest medals and participants.
   - Age distribution of athletes.
   - Gender distribution across the years.
   - Year-wise medal counts.

6. **Predictive Modeling**
   Predictive models including Linear Regression, Random Forest, and Support Vector Machine (SVR) are used to forecast medal counts based on historical data. The models are evaluated using metrics such as R-squared and Mean Squared Error (MSE).

7. **Web Application**
   An interactive web app is developed using Streamlit to provide users with a platform to explore the data through:
   - Overall analysis of the Olympics.
   - Country-wise performance metrics.
   - Detailed athlete statistics.
   - Medal tally visualizations.

## How to Run

To run this project locally on your machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Olympics-Data-Analysis.git
   cd Olympics-Data-Analysis
   streamlit run app.py

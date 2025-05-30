# Bikeshare Data Analysis

## Project Overview

This repository contains a Jupyter Notebook that performs exploratory data analysis on bike share data for three major U.S. cities: New York City (NYC), Chicago, and Washington, D.C. The analysis leverages Python and Pandas to uncover usage patterns and user demographics.

## Data Description

The analysis assumes a CSV file with the following key columns:

* `city`: City where the trip took place (NYC, Chicago, Washington)
* `Start Time`: Timestamp when the trip began
* `End Time`: Timestamp when the trip ended
* `Trip Duration` (or `travel_time`): Duration of the trip in seconds
* `Start Station`: Name of the starting station
* `End Station`: Name of the ending station
* `User Type`: Subscriber or Customer
* `Gender`: Male, Female (available for NYC & Chicago)
* `Birth Year`: Year of birth of the user (available for NYC & Chicago)

> **Note:** Washington data does not include `Gender` or `Birth Year` columns.

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/bikeshare-analysis.git
   cd bikeshare-analysis
   ```
2. **Create a virtual environment (optional but recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Place your bikeshare CSV file** in the project directory. Name it `bikeshare.csv` or update the notebook path accordingly.
2. **Launch the Jupyter Notebook**

   ```bash
   jupyter notebook
   ```
3. **Run all cells** to reproduce data loading, cleaning, and analysis. The notebook computes:

   * Most common month, day of week, and start hour per city
   * Most popular start station, end station, and trip combination per city
   * Total and average trip duration per city
   * Counts of each user type (Subscriber vs. Customer)
   * Gender counts (NYC & Chicago)
   * Birth year statistics: earliest, most recent, and most common year (NYC & Chicago)

## Results Summary

* **Time Statistics**: Identify peak usage by month, day, and hour.
* **Station Statistics**: Reveal top stations and the most frequent trip routes.
* **Trip Duration**: Provide total and average travel times, with optional conversion to minutes or H\:M\:S format.
* **User Demographics**:

  * User types across all cities
  * Gender distribution and birth year insights for NYC and Chicago

Refer to the notebook for detailed outputs and visualizations.

## File Structure

```
├── bikeshare.csv             # Raw data file (CSV)
├── bikeshare_analysis.ipynb  # Jupyter Notebook with code and analysis
├── README.md                 # Project overview and instructions
└── requirements.txt          # Python dependencies
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Author

Your Name — [GitHub Profile](https://github.com/your-username)

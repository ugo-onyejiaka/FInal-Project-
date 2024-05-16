---

# School Performance Analysis

This Python script analyzes school performance data, specifically focusing on average scores in Critical Reading, Mathematics, and Writing. It uses `pandas` for data manipulation and `matplotlib` for visualization, providing insights into how different schools perform across these subjects.

## Features

- **Data Cleaning**: Removes incomplete entries to ensure data quality.
- **Type Conversion**: Converts score data to numeric type for analysis.
- **Data Analysis**: Calculates mean scores across all schools for specified subjects.
- **Visualization**: Plots the mean scores using a bar chart for easy comparison.

## Prerequisites

Before you run this script, you need to install the following Python packages:
- pandas
- matplotlib

You can install these packages using pip:

```bash
pip install pandas matplotlib
```

## Usage

1. Ensure you have Python installed on your machine.
2. Clone this repository or download the script to your local machine.
3. Place your dataset in the same directory as the script or update the script with the path to your dataset. The dataset should be in CSV format and named `dataset.csv`.
4. Run the script using Python:

```bash
python school_performance_analysis.py
```

## Dataset

Your dataset should be a CSV file with the following columns:
- DBN
- School Name
- Number of Test Takers
- Critical Reading Mean
- Mathematics Mean
- Writing Mean

Make sure there are no missing values in the `Critical Reading Mean`, `Mathematics Mean`, and `Writing Mean` columns as the script will remove these entries.

## Output

The script will display a bar chart showing the average scores for Critical Reading, Mathematics, and Writing. This visualization helps identify which subjects might need more focus and resources based on the average scores.

## License

This project is licensed under the MIT License - see the LICENSE.md file for  details.

---

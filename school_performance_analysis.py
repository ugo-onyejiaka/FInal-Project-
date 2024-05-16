import pandas as pd
import matplotlib.pyplot as plt

# Reading data using pandas
dataset = pd.read_csv('dataset.csv')

# There are some empty entries in the the data so we'll remove those rows
dataset = dataset.replace(r'^\s*$', pd.NA, regex=True)
dataset.dropna(subset=['Critical Reading Mean', 'Mathematics Mean', 'Writing Mean'], inplace=True)

# after reading we'll convert the columns into numeric form
dataset['Critical Reading Mean'] = pd.to_numeric(dataset['Critical Reading Mean'])
dataset['Mathematics Mean'] = pd.to_numeric(dataset['Mathematics Mean'])
dataset['Writing Mean'] = pd.to_numeric(dataset['Writing Mean'])

# calculating mean scores
mean_scores = dataset[['Critical Reading Mean', 'Mathematics Mean', 'Writing Mean']].mean()

# Used Matplotlib here, to plot graphs of all the means calculated
plt.figure(figsize=(8, 5))
mean_scores.plot(kind='bar', color=['blue', 'green', 'red'])
plt.title('Average Scores for Critical Reading, Mathematics, and Writing')
plt.ylabel('Mean Scores')
plt.xlabel('Subjects')
plt.xticks(rotation=0)
plt.grid(True)
plt.show()

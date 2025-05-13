import pandas as pd
import matplotlib.pyplot as plt

# Optional: Style for plots
plt.style.use('seaborn')

f = pd.read_csv('sales-data.csv')

df.head()

df.info()

df.describe()

df.isnull().sum()

df.dtypes

if 'Category' in df.columns:
    print(df['Category'].value_counts())

if 'Price' in df.columns:
    print("Average price:", df['Price'].mean())

# Histogram
df['Price'].hist(bins=20)
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Bar chart
if 'Category' in df.columns:
    df['Category'].value_counts().plot(kind='bar')
    plt.title('Category Counts')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.show()

# Scatter plot
if 'Price' in df.columns and 'Sales' in df.columns:
    plt.scatter(df['Price'], df['Sales'])
    plt.title('Price vs Sales')
    plt.xlabel('Price')
    plt.ylabel('Sales')
    plt.show()


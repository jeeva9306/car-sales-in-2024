
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel("C:\\Users\\ELCOT\\Downloads\\Car Sales in India - 2024.xlsx")
print(df.head())

print("Rows before removing duplicates:", len(df))

df = df.drop_duplicates()

print("Rows after removing duplicates:", len(df))


numeric_columns = df.select_dtypes(include=np.number).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].mean())

text_columns = df.select_dtypes(include=['object', 'string']).columns

for col in text_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print("Data cleaned successfully")

# ----------------------------
# CHART 1 - Top Car Brands
# ----------------------------

brand_sales = df.groupby('Make')['Sales'].sum().head(10)

plt.figure(figsize=(10, 5))

sns.barplot(
    x=brand_sales.index,
    y=brand_sales.values,
    hue=brand_sales.index,
    palette='Blues_d',
    legend=False
)

plt.title("Top Car Brand Sales")
plt.xlabel("Brand")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.show()

# ----------------------------
# CHART 2 - Monthly Sales
# ----------------------------

monthly_sales = df.groupby('Months')['Sales'].sum()

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker='o',
    color='green'
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.show()

# ----------------------------
# CHART 3 - Segment Count
# ----------------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x='Segment',
    hue='Segment',
    palette='Set2',
    legend=False
)

plt.title("Car Segment Count")
plt.xlabel("Segment")
plt.ylabel("Count")

plt.show()

# ----------------------------
# CHART 4 - Body Type Count
# ----------------------------

plt.figure(figsize=(10, 5))

sns.countplot(
    data=df,
    x='Body Type',
    hue='Body Type',
    palette='pastel',
    legend=False
)

plt.title("Body Type Count")
plt.xlabel("Body Type")
plt.ylabel("Count")
plt.xticks(rotation=45)

plt.show()

# ----------------------------
# CHART 5 - Platform Sales
# ----------------------------


top_make_sales = df.groupby('Make')['Sales'].sum().head(5)

plt.figure(figsize=(7, 7))

plt.pie(
    top_make_sales.values,
    labels=top_make_sales.index,
    autopct='%1.1f%%'
)

plt.title("Top 5 Car Makes Sales")

plt.show()
# ----------------------------
# CHART 5 - Platform Sales
# ----------------------------


make_sales = df.groupby('Make')['Sales'].sum().head(5)

plt.figure(figsize=(7,7))

plt.pie(
    make_sales.values,
    labels=make_sales.index,
    autopct='%1.1f%%',
    colors=['red', 'blue', 'green', 'orange', 'purple']
)

plt.title("Top 5 Car Brands by Sales Percentage")

plt.show()
# ----------------------------
# CHART 6 - Top Car Models
# ----------------------------

model_sales = df.groupby('Model')['Sales'].sum().head(10)

plt.figure(figsize=(10, 5))

sns.barplot(
    x=model_sales.index,
    y=model_sales.values,
    hue=model_sales.index,
    palette='rocket',
    legend=False
)

plt.title("Top Car Models")
plt.xlabel("Model")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.show()

print("Program completed successfully")

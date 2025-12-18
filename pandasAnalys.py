import pandas as pd
import matplotlib.pyplot as plt

sheet_id = "1gr9TVZeVxkF0WIYPT1apJwS7hskAuko9W_91YjA-Lkk"
sheet_name = "feedback" 

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df = pd.read_csv(url)
print(df.head())

coubts_of_sentiments = df['sentiment'].value_counts()

percentage_of_sentiment =   df['sentiment'].value_counts(normalize=True) * 100
average_raing = df['rating'].mean()
top_ratings = df['rating'].max()
min_ratings = df['rating'].min()


fig, axes = plt.subplots(1, 2, figsize=(10, 4))  
df['sentiment'].value_counts().plot(
    kind='bar',
    ax=axes[0],
    title='Sentiment Distribution'
)

df['rating'].value_counts().sort_index().plot(
    kind='bar',
    ax=axes[1],
    title='Ratings Distribution'
)

plt.tight_layout()     

plt.savefig("feedback_charts.pdf")   # ← هنا السطر المهم
plt.show()
std_rating = df['rating'].std()
print(std_rating)
positive_rate = (df['sentiment'] == 'Positive').mean() * 100

if positive_rate > 80:
    print("Excellent feedback! Most customers are happy.")
elif positive_rate > 50:
    print(" Good feedback overall.")
else:
    print(" Needs improvement: Many negative reviews detected.")


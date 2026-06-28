import sqlite3
import matplotlib.pyplot as plt
import pandas as pd


# Load the dataset
df = pd.read_csv('Train_data.csv')

# First look at the data
print(df.head())        # first 5 rows
print(df.shape)         # (rows, columns)
print(df.info())        # column names + data types
print(df.columns.tolist())
print(df['class'].value_counts())
print(df['class'].value_counts(normalize=True) * 100)
df['class'].value_counts().plot(kind='bar', color=['green', 'red'])
plt.title('Network Traffic: Normal vs Anomaly')
plt.xlabel('Class')
plt.ylabel('Count')
plt.savefig('class_distribution.png')
plt.show()
# Protocol-wise attack breakdown
protocol_class = df.groupby('protocol_type')['class'].value_counts()
print(protocol_class)
# Protocol-wise stacked bar chart
pd.crosstab(df['protocol_type'], df['class']).plot(kind='bar', stacked=True, color=['red', 'green'])
plt.title('Attacks by Protocol Type')
plt.xlabel('Protocol')
plt.ylabel('Count')
plt.savefig('protocol_attacks.png')
plt.show()
# Service-wise attack analysis - top 10 most attacked services
service_class = df.groupby('service')['class'].value_counts().unstack()
service_class['total'] = service_class.sum(axis=1)
service_class['attack_rate'] = (service_class['anomaly'] / service_class['total'] * 100).round(1)
top_services = service_class.sort_values('total', ascending=False).head(10)
print(top_services)
# Top 10 services attack rate chart
top_services['attack_rate'].sort_values().plot(kind='barh', color='darkred')
plt.title('Attack Rate % by Service (Top 10 by Traffic)')
plt.xlabel('Attack Rate (%)')
plt.ylabel('Service')
plt.tight_layout()
plt.savefig('service_attack_rate.png')
plt.show()
conn = sqlite3.connect('network_data.db')
df.to_sql('traffic', conn, if_exists='replace', index=False)

# Same insight via SQL query
query = """
SELECT protocol_type, class, COUNT(*) as count
FROM traffic
GROUP BY protocol_type, class
ORDER BY protocol_type
"""
result = pd.read_sql(query, conn)
print(result)

conn.close()
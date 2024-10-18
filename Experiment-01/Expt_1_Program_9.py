import pandas as pd
from sklearn.model_selection import train_test_split
# Sample DataFrame creation
data = {
 'mileage': [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000,  100000],
 'price': [20000, 18000, 16000, 14000, 12000, 10000, 8000, 6000, 4000, 2000] }
df = pd.DataFrame(data)
# Shuffle the data
df = df.sample(frac=1, random_state=42).reset_index(drop=True) # Split the data into training and test sets
X = df[['mileage']] # Features
y = df['price'] # Target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,  random_state=42)
print('Mohammed Shaikh 211P017')
print("Training set:")
print(pd.concat([X_train, y_train], axis=1))
print("\nTest set:")
print(pd.concat([X_test, y_test], axis=1))
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from data_loader import load_data

data = load_data("src\\data\\CarPrice_Assignment.csv")

# print(data.head(10))
# print(data.shape)
# print(data.info())

# # لو فيه أعمدة نصية كتير، شيلها مؤقتًا
# numeric_df = data.select_dtypes(include=['int64', 'float64'])

# # # احسب معامل الارتباط
# correlation = numeric_df.corr()

# # ارسم خريطة الارتباط
# plt.figure(figsize=(12,8))
# sns.heatmap(correlation, annot=True, cmap='coolwarm')
# plt.title('Correlation Matrix')
# plt.tight_layout()
# plt.show()

data.drop(columns=["car_ID","symboling","stroke","enginelocation","CarName"],inplace=True)

word_to_num = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12
}

data["cylindernumber"] = data["cylindernumber"].str.lower().map(word_to_num)


data["doornumber"] = data["doornumber"].str.lower().map(word_to_num)

data["fueltype"] = data["fueltype"].astype("category").cat.codes
data["aspiration"] = data["aspiration"].astype("category").cat.codes
data["carbody"] = data["carbody"].astype("category").cat.codes
data["drivewheel"] = data["drivewheel"].astype("category").cat.codes
data["enginetype"] = data["enginetype"].astype("category").cat.codes
data["fuelsystem"] = data["fuelsystem"].astype("category").cat.codes

for col in data.columns:
    data[col] = (data[col] - data[col].min()) / (data[col].max() - data[col].min())

print(data.head(10))

data.to_csv('src\\data\\CarPriceAfterEditing.csv', index=False)

# print(data.head(20))
# print(data.describe())
# print(data.info())
# print(data.shape)


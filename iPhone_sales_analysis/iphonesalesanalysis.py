# For the iPhone sales analysis task, I have collected a dataset that contains data about the sales of iPhone in India on Flipkart.

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("apple_products.csv")
# print(data.head())
# print(data.isnull().sum())
# print(data.describe())
highest_rating = data.sort_values(by=["Star Rating"], ascending=False)
highest_rating = highest_rating.head(10)
'''# print(highest_rating["Product Name"])
iphone = highest_rating["Product Name"].value_counts()
label = iphone.index
counts = highest_rating['Number Of Ratings']
figure = px.bar(highest_rating, x=label, y=counts, title="Numbers of rating of highest rated iPhone")
figure.show()'''

figure = px.scatter(data_frame=data, x="Number Of Ratings", y="Sale Price", size="Discount Percentage",
                    title="Relationship between sale price & number of iPhones")
figure.show()
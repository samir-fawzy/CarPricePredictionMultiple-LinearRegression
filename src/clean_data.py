
from data_loader import load_data
from preprocessing import *

df = load_data("src\\data\\CarPrice_Assignment.csv")

map = map_nums()

map_str_num(df,["doornumber","cylindernumber"],map)

drop_columns(df,["car_ID","CarName","enginelocation"])

convert_string_to_nums(df,["fueltype","aspiration","carbody","drivewheel","enginetype","fuelsystem"])

scailing_data(df)
cols = df.shape[1]
x_df = df.iloc[:,:cols - 1]
y_df = df.iloc[:,cols - 1]



x_np = x_df.to_numpy()
y_np = y_df.to_numpy()

y_np = y_np.reshape(-1,1)

split_index = int(len(y_np) * 0.9)

x_training = x_np[:split_index]
y_training = y_np[:split_index]

x_testing = x_np[split_index:]
y_testing = y_np[split_index:]









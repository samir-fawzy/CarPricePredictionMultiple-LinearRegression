import pandas as pd

def drop_columns(df,columns_to_drop): 
    df.drop(columns= columns_to_drop,inplace=True)

def map_nums():
    return {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12
    }

def map_str_num(df,list_column_name,map):
    if df is not None:
        for col in list_column_name:
            df[col] = df[col].str.lower().map(map)
    else:
        print("data frame is none")
def convert_string_to_nums(df,list_columns_name):
    if df is not None:
        for col in list_columns_name:
            df[col] = df[col].astype("category").cat.codes
    else:
        print("data frame is none")

def scailing_data(df):
    if df is not None:
        for col in df.columns :
            min_val = df[col].min()
            max_val = df[col].max()
            if max_val != min_val:
                df[col] = (df[col] - min_val) / (max_val - min_val)
            else:
                df[col] = 0  # أو خليه NaN مثلاً          
    else:
        print("data frame is none")


def save_data_csv(df,file_path):
    df.to_csv(file_path, index=False)

def data_information(df):
    print(df.head(20))
    print(df.describe())
    df.info()
    print(df.shape)

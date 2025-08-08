def load_data(file_path):
    import pandas as pd
    data = pd.read_csv(file_path)
    return data
from pathlib import Path
import pandas as pd
from dataset_handler import clean_data

data_path = Path("data/city_temperature.csv")

def get_csv() -> pd.DataFrame:
    df = pd.read_csv(data_path,dtype={"State": "string", "City": "string"})
    return df

#TODO: get_csv(), perform calculation for means, averages, and other standards
def main() -> None:
    df = get_csv()
    cleaned_df = clean_data(df)

    print(cleaned_df.head())

if __name__ == "__main__":
    main()
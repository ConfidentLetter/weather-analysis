import pandas as pd
import kagglehub

def download_data() -> None:
    path = kagglehub.dataset_download("sudalairajkumar/daily-temperature-of-major-cities")

    print("Path to dataset files:", path)

def clean_data(df : pd.DataFrame) -> pd.DataFrame:
    df["State"] = df["State"].fillna("N/A")
    cleaned_csv = df.dropna()
    return cleaned_csv

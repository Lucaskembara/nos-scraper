from datetime import datetime
import pandas as pd


def create_date_range(min: str, max: str) -> object:
    start_date = datetime.strptime(min, "%Y-%m-%d")
    end_date = datetime.strptime(max, "%Y-%m-%d")
    D = "D"

    return pd.date_range(start_date, end_date, freq=D).strftime("%Y-%m-%d")


def txt_to_list(path: str) -> list:
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines

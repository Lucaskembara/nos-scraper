from utils import create_date_range
from scraper import scrape_loop
import pandas as pd

DATE_RANGE_MIN = "2023-05-03"
DATE_RANGE_MAX = "2023-05-03"
DATE_RANGE = create_date_range(DATE_RANGE_MIN, DATE_RANGE_MAX)

data = scrape_loop(DATE_RANGE=DATE_RANGE)

data.to_csv(
    f"output_{DATE_RANGE_MIN}_{DATE_RANGE_MAX}.csv",
    index=False,
)

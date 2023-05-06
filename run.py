from utils import create_date_range
from scraper import scrape_loop

""" NOS Scraper

This scraper scrapes all articles of the NOS website with a given date range.

Outputs a csv with the columns:
    - Date
    - Title
    - Text
    - Category

"""

DATE_RANGE_MIN = "2023-05-03"
DATE_RANGE_MAX = "2023-05-03"
DATE_RANGE = create_date_range(DATE_RANGE_MIN, DATE_RANGE_MAX)
OUTPUT_DIR = "outputs"

data = scrape_loop(DATE_RANGE=DATE_RANGE)

data.to_csv(
    f"{OUTPUT_DIR}/output_{DATE_RANGE_MIN}_{DATE_RANGE_MAX}.csv",
    index=False,
)

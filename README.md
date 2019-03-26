# Texas party chairs scraper

Two Python scripts:
- [`download_pages.py`](https://github.com/cjwinchester/texas-party-chairs/blob/master/download_pages.py), which downloads pages with data tables for [Texas county and precinct chairs](https://webservices.sos.state.tx.us/cpc-filing/cpc-report.aspx) to the local files `county.html` and `precinct.html`
- [`scrape_data.py`](https://github.com/cjwinchester/texas-party-chairs/blob/master/scrape_data.py), which scrapes data from the downloaded pages into CSVs

### Running this script
Assumes you have Python 3 and [`pipenv`](https://pipenv.readthedocs.io) installed.

1. Clone or download this repo
2. In your command-line interface, `cd` into the directory
3. `pipenv install`
4. `pipenv shell`
5. `python download_pages.py`
6. `python scrape_data.py`
7. `exit`
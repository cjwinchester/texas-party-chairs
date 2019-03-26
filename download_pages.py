import requests
import bs4
import time


# the base URL for all requests
url = 'https://webservices.sos.state.tx.us/cpc-filing/cpc-report.aspx'

# fetch the page
r = requests.get(url)

# turn it into soup
soup = bs4.BeautifulSoup(r.text, 'html.parser')

# find the hidden viewstate input value
viewstate = soup.find('input', {'id': '__VIEWSTATE'})['value']

# find the hidden event validation value
eventvalidation = soup.find('input', {'id': '__EVENTVALIDATION'})['value']

# some headers to add to the session
headers = {
    'Referer': 'https://webservices.sos.state.tx.us/cpc-filing/cpc-report.aspx', # noqa
    'Origin': 'https://webservices.sos.state.tx.us',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36' # noqa
}

# create a session object
s = requests.Session()

# update it with headers
s.headers.update(headers)

# the two keys to send along with the form data
dtypes = ['btnCC', 'btnPC']

# for each one
for dt in dtypes:

    # build the data dictionary to send with the form
    data = {
        'rblParty': 0,
        dt: '+',
        '__EVENTVALIDATION': eventvalidation,
        '__VIEWSTATE': viewstate
    }

    # post the data to the URL
    r = s.post(url, data=data)

    # decide what to call the downloaded file
    # based on the type of table we're returning
    if dt == 'btnPC':
        filename = 'precinct.html'
    else:
        filename = 'county.html'

    # open an HTML file for this type of precinct chair
    # and write to a local file
    with open(filename, 'w') as outfile:
        outfile.write(r.text)

    # let us know what's up
    print('Downloaded', filename)

    # pause for a second
    time.sleep(1)

import csv

import bs4


# open the local county HTML file
with open('county.html', 'r') as county_page:

    # read the contents
    county_html = county_page.read()

    # turn the HTML into soup
    county_soup = bs4.BeautifulSoup(county_html, 'html.parser')

# open the local precinct HTML file
with open('precinct.html', 'r') as precinct_page:

    # read the contents
    precinct_html = precinct_page.read()

    # turn the HTML into soup
    precinct_soup = bs4.BeautifulSoup(precinct_html, 'html.parser')


# find the tables
county_table = county_soup.find('table', {'id': 'grdCC'})
precinct_table = precinct_soup.find('table', {'id': 'grdPC'})

# scrape the county table and write to a csv
# first, open a csv file to write to
with open('county_chairs.csv', 'w', newline='') as county_file:

    # create a writer object
    county_writer = csv.writer(county_file)

    # list of headers
    county_headers = ['county', 'party', 'name']

    # write out list of headers
    county_writer.writerow(county_headers)

    # get list of rows, minus header row
    county_rows = county_table.find_all('tr')[1:]

    # loop over the rows in the table, skipping header row
    for row in county_rows:

        # find the td tags
        columns = row.find_all('td')

        # county is in position 0
        county = columns[0].text

        # party is in position 1
        party = columns[1].text

        # name is in position 2
        name = columns[2].text

        # drop it into a list
        county_data = [county, party, name]

        # and write to file
        county_writer.writerow(county_data)


# scrape the precinct table and write to a csv
# open a csv file to write to
with open('precinct_chairs.csv', 'w', newline='') as precinct_file:

    # create a writer object
    precinct_writer = csv.writer(precinct_file)

    # list of headers
    precinct_headers = ['county', 'party', 'precinct', 'name']

    # write out list for headers
    precinct_writer.writerow(precinct_headers)

    # get list of rows, minus header row
    precinct_rows = precinct_table.find_all('tr')[1:]

    # loop over the rows in the table, skipping header row
    for row in precinct_rows:

        # find the td tags
        columns = row.find_all('td')

        # county is in position 0
        county = columns[0].text

        # party is in position 1
        party = columns[1].text

        # precinct number is in position 2
        precinct_number = columns[2].text

        # name is in position 3
        name = columns[3].text

        # make a list of data to write out
        precinct_data = [county, party, precinct_number, name]

        precinct_writer.writerow(precinct_data)

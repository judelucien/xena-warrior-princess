#!/usr/bin/env python3

# Simple program to convert the Master Fan Fic List from .csv to Markdown
# Improvement welcome, please open an Issue or Pull Request

import csv

with open('Master-Fanfic-List.md', 'w') as f:
    header = "| Title/Link | Author | Category | Icon | Who | What |\n"
    header2 = "|-------|-------|--------|-------|-------|-------|\n"
    f.write(header)
    f.write(header2)

    with open('Xena-Master-Fan-Fic-List.csv', newline='') as csvfile:
        fieldnames = ['Title', 'Author', 'Who', 'What', 'Link', 'Icon', 'Category']

        spamreader = csv.DictReader(csvfile, fieldnames=fieldnames)
        icon = ''
        for row in spamreader:
            if 'X' == row['Category']:
                icon = ':flushed:'
            elif '#' == row['Category']:
                icon = ':disappointed:'
            elif 'PostFIN' == row['Category']:
                icon = ':sob:'
            elif 'Alt' == row['Category']:
                icon = ':two_women_holding_hands:'
            elif 'U/O' == row['Category']:
                icon = ':busts_in_silhouette:'
            elif 'Conqueror' == row['Category']:
                icon = ':prince:'
            elif 'PWP' == row['Category']:
                icon = ':sweat_smile:'
            else:
                icon = row['Category']

            title = "[" + row['Title'] + "](" + row['Link'] + ")"

            line = " | " + title + " | " + row['Author'] + " | " + row['Category'] + \
                " | " + icon + " | " + row['Who'] + " | " + row['What'] + " |\n"

            f.write(line)

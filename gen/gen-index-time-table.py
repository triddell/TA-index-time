#!/usr/bin/env python3

import csv, fileinput, re

esc_bs = lambda x: x.translate(str.maketrans({"|":  r"\|"}))

table = ""

with open('gen/index-time-props.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    
    table += "| Sourcetype | Example | Time Prefix | Time Format | Line Breaker |\n"
    table += "| :--------- | :------ | :---------: | :---------- | :----------- |\n"

    for row in reader:

        table += "| %s | %s | %s | %s | %s |\n" % (esc_bs(row['SOURCETYPE']), esc_bs(row['EXAMPLE']), esc_bs(row['TIME_PREFIX']), '`'+esc_bs(row['TIME_FORMAT'])+'`', '`'+esc_bs(row['LINE_BREAKER'])+'`')

with fileinput.FileInput('README.md', inplace=True) as file:
    for line in file:
        if line.startswith('| Sourcetype '):
            print(table, end='')
        elif line.startswith('| :--------- ') or line.startswith('| it:'):
            print("", end='')
        else:
            print(line, end='')

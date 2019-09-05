#!/usr/bin/env python3

import configparser, csv

config = configparser.RawConfigParser(allow_no_value=True)
config.optionxform = str


with open('lookups/index-time-props.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    cfgfile = open('default/props.conf', 'w')
    
    for row in reader:
        config.add_section(row['SOURCETYPE'])
        config.set(row['SOURCETYPE'],'# Example: ' + row['EXAMPLE'])
        config.set(row['SOURCETYPE'],'TIME_PREFIX', row['TIME_PREFIX'])
        config.set(row['SOURCETYPE'],'TIME_FORMAT', row['TIME_FORMAT'])
        config.set(row['SOURCETYPE'],'LINE_BREAKER', row['LINE_BREAKER'])
        if row['MAX_TIMESTAMP_LOOKAHEAD'] == "":
            config.set(row['SOURCETYPE'],'MAX_TIMESTAMP_LOOKAHEAD', len(row['EXAMPLE']) + 5 )
        else:
            config.set(row['SOURCETYPE'],'MAX_TIMESTAMP_LOOKAHEAD', row['MAX_TIMESTAMP_LOOKAHEAD'])
        config.set(row['SOURCETYPE'],'SHOULD_LINEMERGE', 'false')
        config.set(row['SOURCETYPE'],'TRUNCATE', '99999')
        config.set(row['SOURCETYPE'],'TRANSFORMS-00000-it-replace-sourcetype', 'it-replace-sourcetype, it-clear-from-meta')

    config.write(cfgfile)
    cfgfile.close()
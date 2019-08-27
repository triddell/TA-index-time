#!/usr/bin/env python3

import configparser, csv, os

config = configparser.RawConfigParser(allow_no_value=True)
config.optionxform = str

if not os.path.exists('gen/test'):
    os.mkdir('gen/test')

with open('gen/index-time-props.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    cfgfile = open('gen/test/inputs.conf', 'w')

    config.add_section('default')
    config.set('default', 'index', 'index_time')

    for row in reader:
        log_filename = row['SOURCETYPE'].replace(":", "_") + ".log"

        section = 'monitor://$SPLUNK_HOME/etc/apps/TA-index-time/gen/test/' + log_filename
        config.add_section(section)
        config.set(section, 'sourcetype', row['SOURCETYPE'])
        config.set(section, '_meta', 'it:sourcetype::' + row['SOURCETYPE'] + "_mod")

         
        with open('gen/test/' + log_filename, 'w') as logfile:
            logfile.write(row['EXAMPLE'] + " Line 1\nLine2\n")
            logfile.write(row['EXAMPLE'] + " Line 3\nLine4\n")

    config.write(cfgfile)
    cfgfile.close()

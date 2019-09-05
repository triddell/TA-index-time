#!/usr/bin/env python3

import configparser, csv, os

config = configparser.RawConfigParser(allow_no_value=True)
config.optionxform = str

if not os.path.exists('logs'):
    os.mkdir('logs')

if not os.path.exists('local'):
    os.mkdir('local')

cfgfile = open('local/inputs.conf', 'w')

with open('lookups/index-time-props.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    
    config.add_section('default')
    config.set('default', 'index', 'index_time')

    for row in reader:
        log_filename = row['SOURCETYPE'].replace(":", "_") + ".log"

        section = 'monitor://$SPLUNK_HOME/etc/apps/TA-index-time/logs/' + log_filename
        config.add_section(section)
        config.set(section, 'sourcetype', row['SOURCETYPE'])
        config.set(section, '_meta', 'it:sourcetype::' + row['SOURCETYPE'] + "_mod")

         
        with open('logs/' + log_filename, 'w') as logfile:
            logfile.write(row['EXAMPLE'] + " Line 1\nLine2\n")
            logfile.write(row['EXAMPLE'] + " Line 3\nLine4\n")

with open('gen/index-time-test.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        log_filename = row['TARGET_SOURCETYPE'].replace(":", "_") + ".log"

        section = 'monitor://$SPLUNK_HOME/etc/apps/TA-index-time/logs/' + log_filename
        config.add_section(section)
        config.set(section, 'sourcetype', row['IT_SOURCETYPE'])
        config.set(section, '_meta', 'it:sourcetype::' + row['TARGET_SOURCETYPE'])

         
        with open('logs/' + log_filename, 'w') as logfile:
            logfile.write(row['TIMESTAMP'] + " Line 1\nLine2\n")
            logfile.write(row['TIMESTAMP'] + " Line 3\nLine4\n")

config.write(cfgfile)
cfgfile.close()

config = configparser.RawConfigParser(allow_no_value=True)
config.optionxform = str
config.add_section('default')
config.set('default', 'MAX_DAYS_AGO', '365')
config.set('default', 'MAX_DAYS_HENCE', '365')

cfgfile = open('local/props.conf', 'w')
config.write(cfgfile)
cfgfile.close()

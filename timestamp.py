#!/usr/bin/python3

import sys
import re
from datetime import datetime

def main():
    args = sys.argv[1:]

    if not len(args):
        # Use the current datetime
        dt = datetime.utcnow()
        ts = timestamp(dt)

    else:
        args = ' '.join(args)

        # If args is a single uninterrupted number, treat it as a timestamp
        if re.match(r'^-?\d+$', args):
            ts = int(args)
            dt = datetime.utcfromtimestamp(ts)
        else:
            # Assume UTC and all values are in descending order of magnitude
            dt = datetime(*map(int, re.split(r'\D', args)))
            ts = timestamp(dt)

    print("{} UTC".format(dt.strftime("%Y-%m-%d %H:%M:%S")))
    print(int(ts))

def timestamp(utc_dt):
    return (utc_dt - datetime(1970, 1, 1)).total_seconds()

if __name__ == "__main__":
    main()

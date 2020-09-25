#!/usr/bin/env python3
#
# (C) eda-abec
# 2020/09/25

import csv

logfile = file("hostapd-eaphammer.log")

gotHash = []
gotPlain = []

with open('gtc.log', 'w') as gtclog:
    with open('mschapv2.log', 'w') as mschapv2log:

        arr = logfile.read().split("\n\n\n")
        print("loaded: " + str(len(arr)))

        for i in arr:
            lines = i.splitlines()
            for line in lines:
                if "username" in line:
                    username = line

            if "GTC" in i and username not in gotPlain:
                gotPlain.append(username)
                gtclog.write(i + "\n")
            elif "mschapv2" in i and username not in gotHash:
                gotHash.append(username)
                mschapv2log.write(i + "\n\n")

print("unique plaintext: " + str(len(gotPlain)))
print("unique MSCHAPV2: " + str(len(gotHash)))

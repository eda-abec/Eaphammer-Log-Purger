# Eaphammer Log Purger
This is a little Python script for parsing output of [Eaphammer](https://github.com/s0lst1c3/eaphammer/).

What it does:
- removes duplicates
- splits entries into two files, one with plaintext (GTC) and the other with hashes (mschapv2)

# Usage
In the same directory as the "hostapd-eaphammer.log":
```
python purger.py
```
# TODOs
- handle other types of hashes
- normalize number of lines between entries (there is an inconsistence from Eaphammer)

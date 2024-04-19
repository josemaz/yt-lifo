
### Introduction

This application named _yt-lifo_ was developed to manage a LIFO of Youtube videos. This app use youtube video id (see links) to fill the content of links.

In order to focus on selected videos in Youtube, we implemented a Pandas LIFO to avoid distractions of search in Youtube and its history.

You don't need expending time on F\*ck1ng Youtube Channels an Searchs.

This app is based on minimalist philosophy.


### Parameters of CLI (Command Line Interface)

```python

python app.py push dUdaAm4x3Wg
python app.py pull
python app.py show -l 1
python app.py cat
python app.py save file.tsv

```


### TODO
- We wish to use an sqlite DB
- Create a DB from scratch
- We wish to modularazing whole source code
- We wish to avoid duplicated videos in database
- We wish adding colors in output
- We wish writing a better help
- We wish improving the output of show command
- We wish improving validation of *No valid command* with argparse
- We wish to use different LIFOs (DBs)




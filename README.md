
### Introduction

This application named _yt-lifo_ was developed to manage a LIFO of Youtube videos. This app use youtube video id (see links) to fill the content of them.

In order to focus on selected videos in Youtube, we implemented a Pandas LIFO to avoid distractions and perturbations of searching in Youtube and your historial.

You don't need expending more time on F\*ck1ng Youtube Channels and Searches.

Moreover, this app is based on a minimalist philosophy.


### Parameters of CLI (Command Line Interface)

```python

python yt-lifo.py push dUdaAm4x3Wg
python yt-lifo.py push "\-Hwlvkfp698"
python yt-lifo.py pull
python yt-lifo.py show -l 1
python yt-lifo.py cat
python yt-lifo.py save file.tsv

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
- Adding date of push video



import argparse
from pytube import YouTube
import shutil, sys
import pandas as pd


parser = argparse.ArgumentParser(prog='yt-fifo')

subparsers = parser.add_subparsers(dest='cmd', help='Commands to manage database')

#! Create parser to subcommands
parser_push = subparsers.add_parser('push', help='Push a video on a DB')
parser_push.add_argument('idVideo', type=str, \
        help='Video id from Youtube')

parser_pop = subparsers.add_parser('pop', \
        help='Pop a video and print standard output')

parser_show = subparsers.add_parser('show', \
        help='Print standard output')
parser_show.add_argument('-l', type=int, default=5,
        help='Number of lines to show')

parser_save = subparsers.add_parser('save', \
        help='Save database to file')
parser_save.add_argument('fout', type=str,
        nargs='?', default='db.tsv',
        help='Filename to save a DB')


#! Processing arguments
args = parser.parse_args()


#! Open connection to DB
colnames=['idVideo','author','title','retrived']
df = pd.read_csv('data-new.tsv', sep = '\t', names=colnames)


#! START MAIN
if args.cmd == 'push' :
    video_url = 'https://www.youtube.com/watch?v=' + args.idVideo
    yt = YouTube(video_url)
    title = yt.title
    author = yt.author
    df.loc[len(df)] = [args.idVideo,author,title,1]

    shutil.copy('data-new.tsv', 'data-old.tsv')
    df.to_csv('data-new.tsv', sep='\t', index=False, header = None)

elif args.cmd == 'pop' :
    row = df.loc[len(df)-1]
    df.drop(df.index[-1], inplace=True)
    liga = 'https://www.youtube.com/watch?v=' + row['idVideo']
    print(f"Link: {liga}")
    print(f"Author: {row['author']}")
    print(f"Title: {row['title']}")

    shutil.copy('data-new.tsv', 'data-old.tsv')
    df.to_csv('data-new.tsv', sep='\t', index=False, header = None)

elif args.cmd == 'show' :
    pd.set_option('display.max_columns', None)
    print(df.iloc[-args.l:])

elif args.cmd == 'save' :
    df.to_csv(args.fout, sep='\t', index=False, header = None)

else:
    print(f"No valid command")

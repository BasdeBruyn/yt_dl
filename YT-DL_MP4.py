from __future__ import unicode_literals

import os

import youtube_dl
import time


class MyLogger(object):
    def debug(self, msg):
        with open(debugFileName, 'a') as debugFile:
            debugFile.write(msg)

    def warning(self, msg):
        with open(debugFileName, 'a') as debugFile:
            debugFile.write(msg)
        print('\nWARNIG!\n')

    def error(self, msg):
        with open(debugFileName, 'a') as debugFile:
            debugFile.write(msg)
        print('\nERROR!\n')
        print(msg)


class Timer:
    def __init__(self):
        self.starttime = 0

    def settime(self):
        self.starttime = time.time()

    def gettime(self):
        return self.starttime

    def time(self):
        return time.time() - self.starttime


debugFileName = 'debug.txt'
conversionTimer = Timer()


def my_hook(d):
    if d['status'] == 'downloading':
        print('.', end='', flush=True)
    elif d['status'] == 'finished':
        print('\nDownload successfull')
        print('File: ' + d['filename'])
        print('Now converting ...')
        conversionTimer.settime()


def downlaod(yt_link):
    ydl_opts = {'noplaylist': True,
                'outtmpl': 'D:\OneDrive\Muziek\yt_dl\%(title)s.%(ext)s',
                'logger': MyLogger(),
                'progress_hooks': [my_hook]
                }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('Downloading', end='')
        ydl.download([yt_link])


if __name__ == '__main__':
    os.remove(debugFileName)
    link = input("Link: ")
    downlaod(link)
    print('File is ready')
    print('The conversion took: ' + "%.2f" % conversionTimer.time() + ' seconds')
    input('PRESS ANY KEY.........')

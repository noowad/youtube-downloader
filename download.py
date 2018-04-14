# coding:utf-8

from __future__ import print_function
import sys
import os
from search import youtube_search
from pytube import YouTube
from pytube.exceptions import RegexMatchError

DEVELOPER_KEY = "REPLACE-ME"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_download_by_keyword(keyword, max_results):
    videos, _, _ = youtube_search(keyword, max_results)
    print("Videos:\n", "\n".join(map(lambda x: x.split('\t')[0], videos)))
    for video in videos:
        ID = video.split('\t')[1]
        query = 'https://www.youtube.com/watch?v=' + ID
        youtube_download_by_url(query)


def youtube_download_by_url(url):
    try:
        yt = YouTube(url)
        print("Downloading...{}".format(yt.title.encode('utf-8')))
        yt.streams.filter(subtype='mp4').first().download(output_path="./videos")
    except RegexMatchError:
        print('Cannnot Download Removed Videos or Private Videos')
    except KeyError:
        print('Cannot Download This Video In Your Country')


if __name__ == "__main__":
    if not os.path.exists('videos'): os.mkdir('videos')
    print("Enter mode (1: by keyword, 2: by URL):")
    input = sys.stdin.readline
    mode = int(input())
    if mode == 1:
        print("Enter Keyword:")
        keyword = str(input()).strip()
        youtube_download_by_keyword(keyword=keyword, max_results=3)
    elif mode == 2:
        print("Enter URL:")
        url = str(input()).strip()
        youtube_download_by_url(url=url)

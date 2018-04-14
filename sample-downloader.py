# coding:utf-8

import requests
from bs4 import BeautifulSoup
from pytube import YouTube
from download import youtube_download_by_url
from search import youtube_search
import os
import sys


# 특정 업로더의 상위 25개의 동영상을 자동으로 다운로드
def by_registered_channel(url='https://www.youtube.com/channel/UCQe05cEJc3KJd4zPSfKXCog/videos'):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    videos = []
    for a in soup.find_all('a', {'dir': 'ltr'}):
        if a["href"][:6] == '/watch':
            if a['href'] + '\t' + a.text not in videos:
                videos.append(a['href'] + '\t' + a.text)
    for video in videos:
        ID = video.split('\t')[0]
        youtube_download_by_url('https://www.youtube.com' + ID)


# 특정 플레이리스트의 상위 100개의 동영상을 자동으로 다운로드
def by_playlist(ID='PLdaQsrKzi9Z_xRePSChEWQ4C8Z8udOgWe'):
    html = requests.get('https://www.youtube.com/playlist?list=' + ID)
    soup = BeautifulSoup(html.text, 'html.parser')
    videos = []
    for a in soup.find_all('a', {'dir': 'ltr'}):
        if a["href"][:6] == '/watch':
            if a['href'] + '\t' + a.text not in videos:
                videos.append(a['href'] + '\t' + a.text)
    for video in videos:
        ID = video.split('\t')[0]
        youtube_download_by_url('https://www.youtube.com' + ID)


if __name__ == "__main__":
    if not os.path.exists('videos'): os.mkdir('videos')
    print("Enter mode (1: by registered channel, 2: by playlist):")
    input = sys.stdin.readline
    mode = int(input())
    if mode == 1:
        print("Enter channel name:")
        keyword = str(input()).strip()
        if keyword == 'vinyl':
            by_registered_channel('https://www.youtube.com/channel/UCQe05cEJc3KJd4zPSfKXCog/videos')
        if keyword == 'andre':
            by_registered_channel('https://www.youtube.com/channel/UCw-l7-0zWYsSG5UnkdaO2pg/videos')
    elif mode == 2:
        print("Enter playlist ID:")
        ID = str(input()).strip()
        if ID == '':
            by_playlist()
        else:
            by_playlist(ID)

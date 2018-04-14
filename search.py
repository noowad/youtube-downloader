# coding:utf-8

from __future__ import print_function
import sys
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "REPLACE-ME"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(keyword, max_results=10):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(q=keyword, part="id,snippet", maxResults=max_results).execute()
    videos, channels, playlists = [], [], []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s\t%s" % (search_result["snippet"]["title"],
                                      search_result["id"]["videoId"]))
        elif search_result["id"]["kind"] == "youtube#channel":
            channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                         search_result["id"]["channelId"]))
        elif search_result["id"]["kind"] == "youtube#playlist":
            playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                          search_result["id"]["playlistId"]))

    return videos, channels, playlists


if __name__ == "__main__":
    # argparser.add_argument("--q", help="Search term", default="Google")
    # argparser.add_argument("--max-results", help="Max results", default=25)
    # args = argparser.parse_args()
    print("Enter Keyword")
    input = sys.stdin.readline
    keyword = str(input()).strip()
    try:
        youtube_search(keyword=keyword)
    except HttpError, e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))

import json
import unittest
from src.streaming import TwitterStreamer


class TestTwitterStreamer(unittest.TestCase):

    def test_stream_tweets(self):

        hash_tag_list = ['gamestop']
        fetched_tweets_filename = 'tweets.txt'

        streamer = TwitterStreamer()

        streamer.stream_tweets(
            output_filename=fetched_tweets_filename,
            hash_tag_list=hash_tag_list)

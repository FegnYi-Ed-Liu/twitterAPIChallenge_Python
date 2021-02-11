import json
import unittest
from src.streaming import TwitterStreamer


class TestTwitterStreamer(unittest.TestCase):

    def test_stream_tweets(self):

        hash_tag_list = ['stock', 'wallstreet', 'US stock', 'stock market']
        fetched_tweets_filename = '../tweets.txt'
        lang = ['en']

        streamer = TwitterStreamer()

        streamer.stream_tweets(
            output_filename=fetched_tweets_filename,
            hash_tag_list=hash_tag_list,
            lang=lang)

    def test_read_tweets_txt(self):

        with open('../tweets.txt') as file:
            for line in file:
                data = json.loads(line.strip())
                self.assertTrue(type(data) is dict)

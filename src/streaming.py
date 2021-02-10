from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from .credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


class TwitterStreamer:

    def stream_tweets(self, output_filename, hash_tag_list):

        listener = StdoutListener(output_filename=output_filename)

        auth = OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
        auth.set_access_token(key=ACCESS_TOKEN, secret=ACCESS_TOKEN_SECRET)

        stream = Stream(auth=auth, listener=listener)

        stream.filter(track=hash_tag_list)


class StdoutListener(StreamListener):

    def __init__(self, output_filename):
        super().__init__()
        self.output_filename = output_filename

    def on_data(self, data):

        try:
            d = data.strip()
            print(d)

            with open(self.output_filename, 'a') as writer:
                writer.write(d + '\n')

            return True

        except BaseException as e:
            print("Error on_data %s" % str(e))

        return True

    def on_error(self, status):
        print(status)

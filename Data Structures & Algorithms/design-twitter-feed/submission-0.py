import heapq
import collections
class Twitter(object):
    def __init__(self):
        self.timestamp = 0
        # userId -> list of (-timestamp, tweetId)
        self.user_tweets = collections.defaultdict(list)
        # followerId -> set of followeeIds
        self.user_follows = collections.defaultdict(set)
    
    def postTweet(self, userId, tweetId):

        self.timestamp += 1
        self.user_tweets[userId].append((-self.timestamp, tweetId))
    
    def getNewsFeed(self, userId):
        heap = []
        # include user owns tweets
        if userId in self.user_tweets:
            heap.extend(self.user_tweets[userId][-10:])
        # whoever he follows tweets
        for followeeId in self.user_follows[userId]:
            if followeeId in self.user_tweets:
                heap.extend(self.user_tweets[followeeId][-10:])
        heapq.heapify(heap)
        feed = []
        while heap and len(feed) < 10:
            feed.append(heapq.heappop(heap)[1])
        return feed
    
    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.user_follows[followerId].add(followeeId)
    
    def unfollow(self, followerId, followeeId):
        self.user_follows[followerId].discard(followeeId)
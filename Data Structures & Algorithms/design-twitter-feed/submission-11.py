class Twitter:

    def __init__(self):
        self.tweetMap = {}
        self.followerMap = {}
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = deque()
            self.followerMap[userId] = set()
            self.followerMap[userId].add(userId)

        self.tweetMap[userId].append((self.time, tweetId))
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].popleft()

        self.time += 1
            

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for f in self.followerMap[userId]:
            for tweet in self.tweetMap[f]:
                feed.append(tweet)
        feed.sort()
        feed.reverse()
        length = min(10, len(feed))
        res = []
        for i in range(length):
            res.append(feed[i][1])

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followerMap:
            self.followerMap[followerId] = set()
            self.followerMap[followerId].add(followerId)
            self.tweetMap[followerId] = deque()
        
        self.followerMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followerMap and followeeId != followerId: 
            if followeeId in self.followerMap[followerId]:
                self.followerMap[followerId].remove(followeeId)

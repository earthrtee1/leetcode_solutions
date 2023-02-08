class Twitter:

    def __init__ (self):
        self.userIdSet=set()
        self.tweetIdDict={}
        self.followDict={}
        self.followedDict={}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        match userId in self.userIdSet:
            case False:
                self.userIdSet.add(userId)
        match tweetId in self.tweetIdDict.keys():
            case False:
                tempDict = {}
                tempDict[tweetId]=userId
                tempDict.update(self.tweetIdDict)
                self.tweetIdDict = tempDict
        # print(self.tweetIdDict)
        

    def getNewsFeed(self, userId: int) -> list[int]:
        returnList = []
        followedSet = {userId}
        if userId in self.followDict.keys():
            for i in self.followDict[userId]:
                followedSet.add(i)
        print(followedSet)
        for i in self.tweetIdDict:
            if self.tweetIdDict[i] in followedSet:
                returnList.append(i)
            if len(returnList)==10:
                break
        return(returnList)    


    def follow(self, followerId: int, followeeId: int) -> None:
        if self.followedDict =={} or followeeId not in self.followedDict.keys():
            self.followedDict[followeeId] = set()
        self.followedDict[followeeId].add(followerId)
        if self.followDict =={} or followerId not in self.followDict.keys():
            self.followDict[followerId] = set()
        self.followDict[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followedDict.keys():
            self.followedDict[followeeId].remove(followerId)
        if followerId in self.followDict.keys():
            self.followDict[followerId].remove(followeeId)

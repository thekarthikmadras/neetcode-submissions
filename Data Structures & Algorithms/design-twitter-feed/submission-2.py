class Twitter:
    def __init__(self):
        # A counter used to track when each tweet was posted.
        # We decrease it each time so the most recent tweet has the smallest count.
        self.count = 0
        # Stores all tweets posted by each user.
        # Format: userId -> [[count, tweetId], ...]
        # Tweets are stored in the order they are posted.
        self.tweetMap = defaultdict(list)
        # Stores the users that each user follows.
        # Format: userId -> {followeeId1, followeeId2, ...}
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Save the tweet along with its posting order.
        # A smaller count means a more recent tweet.
        self.tweetMap[userId].append([self.count, tweetId])
        # Decrease the counter for the next tweet.
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Stores the final list of tweet IDs.
        res = []

        # A min-heap helps us find the most recent tweet quickly.
        # Each heap entry contains:
        # [count, tweetId, userId, indexOfPreviousTweet]
        minHeap = []

        # A user should always see their own tweets.
        # A set prevents adding the same user more than once.
        self.followMap[userId].add(userId)

        # Get the latest tweet from every user this person follows.
        for followeeId in self.followMap[userId]:

            # Skip users who have never posted a tweet.
            if followeeId in self.tweetMap:

                # Find the index of this user's most recent tweet.
                index = len(self.tweetMap[followeeId]) - 1

                # Get the most recent tweet.
                count, tweetId = self.tweetMap[followeeId][index]

                # Add this tweet to the heap.
                # index - 1 points to the next older tweet from this user.
                heapq.heappush(
                    minHeap,
                    [count, tweetId, followeeId, index - 1]
                )

        # Keep getting the newest tweet until we have 10 tweets
        # or there are no more tweets left in the heap.
        while minHeap and len(res) < 10:

            # Remove the most recent tweet among the available tweets.
            count, tweetId, followeeId, index = heapq.heappop(minHeap)

            # Add its tweet ID to the news feed.
            res.append(tweetId)

            # If this user has older tweets, add their next tweet.
            if index >= 0:

                # Get the next older tweet from the same user.
                count, tweetId = self.tweetMap[followeeId][index]

                # Add it to the heap so it can compete with tweets
                # from other users for the next position in the feed.
                heapq.heappush(
                    minHeap,
                    [count, tweetId, followeeId, index - 1]
                )

        # Return at most 10 tweets, newest first.
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add the followee to the follower's set.
        # Using a set avoids storing duplicate follow relationships.
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove the followee only if the follower currently follows them.
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
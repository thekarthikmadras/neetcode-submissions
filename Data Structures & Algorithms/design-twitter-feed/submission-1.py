import heapq
from collections import defaultdict, deque
from typing import List

class Twitter:
    def __init__(self):
        # Increasing timestamp: larger => newer
        self._timestamp = 0

        # userId -> deque of (timestamp, tweetId); keep at most 10 most recent per user
        self._tweets = defaultdict(lambda: deque(maxlen=10))

        # followerId -> set of followeeIds
        self._followees = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Post a new tweet for userId.
        We append (timestamp, tweetId) to the right; deque(maxlen=10) auto-evicts oldest.
        O(1) amortized.
        """
        self._tweets[userId].append((self._timestamp, tweetId))
        self._timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Return up to 10 most recent tweetIds from userId and people they follow.
        Uses a max-heap (implemented with heapq by pushing -timestamp) and a k-way merge:
        - push the latest tweet from each followee
        - pop the newest; then push the previous tweet from the same followee (if any)
        Repeat until we collected up to 10 tweets.

        Time: O(F log F + 10 log F) where F = number of followees (including self)
        """
        result = []
        heap = []

        # build set of followees and include the user themself (don't modify stored follow set)
        follow_set = set(self._followees[userId])
        follow_set.add(userId)

        # push each followee's latest tweet (if any)
        for fid in follow_set:
            user_deque = self._tweets.get(fid)
            if user_deque:
                idx = len(user_deque) - 1
                ts, tid = user_deque[idx]
                # Push tuple: (priority, tweetId, followeeId, index_in_that_followee_deque)
                # priority is -ts for max-heap semantics with Python's min-heap
                heapq.heappush(heap, (-ts, tid, fid, idx))

        # extract up to 10 tweets
        while heap and len(result) < 10:
            neg_ts, tid, fid, idx = heapq.heappop(heap)
            result.append(tid)

            # push the previous tweet from the same followee, if any
            prev_idx = idx - 1
            if prev_idx >= 0:
                prev_ts, prev_tid = self._tweets[fid][prev_idx]
                heapq.heappush(heap, (-prev_ts, prev_tid, fid, prev_idx))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        followerId starts following followeeId.
        Ignore no-op (self-follow) to keep follow graph simple.
        """
        if followerId == followeeId:
            return
        self._followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        followerId stops following followeeId.
        No-op if followeeId wasn't being followed.
        """
        if followeeId in self._followees[followerId]:
            self._followees[followerId].remove(followeeId)

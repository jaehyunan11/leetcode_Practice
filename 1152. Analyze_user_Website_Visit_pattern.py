from collections import defaultdict
from itertools import combinations


class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        # Sort the website info base on the timestamps
        webInfo = []
        for time, usr, web in zip(timestamp, username, website):
            webInfo.append((time, usr, web))
        webInfo.sort(key=lambda x: x[0])
        print(webInfo)

        # Find the websites visited by particular user
        websiteVisit = defaultdict(list)
        for _, usr, web in webInfo:
            websiteVisit[usr].append(web)

        print(websiteVisit)
        # Find the Routes in the form of tuples of length 3
        possibleTuples = defaultdict(int)
        for usr in websiteVisit:
            webRoutes = set(combinations(websiteVisit[usr], 3))
            for webRoute in webRoutes:
                possibleTuples[webRoute] += 1
        print(possibleTuples)

        # Find Max Value of users visited
        maxVal, routes = max(possibleTuples.values()), []
        for r, val in possibleTuples.items():
            if val == maxVal:
                routes.append(r)
        if len(routes) > 1:
            routes.sort()

        return routes[0]


S = Solution()
username = ["joe", "joe", "joe", "james", "james",
            "james", "james", "mary", "mary", "mary"]
timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
website = ["home", "about", "career", "home", "cart",
           "maps", "home", "home", "about", "career"]
S.mostVisitedPattern(username, timestamp, website)

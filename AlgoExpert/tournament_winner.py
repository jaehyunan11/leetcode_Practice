class Solution:

    def tournamentWinner(self, competitions, results):
        HOME_TEAM_WON = 1
        currentBestTeam = ""
        scores = {currentBestTeam: 0}

        for idx, competition in enumerate(competitions):
            result = results[idx]
            # first element, second element(decompose home and awayteam)
            homeTeam, awayTeam = competition
            print(f"HomeTeam:{homeTeam}")
            print(f"AwayTeam:{awayTeam}")
            winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

            self.updateScores(winningTeam, 3, scores)

            if scores[winningTeam] > scores[currentBestTeam]:
                currentBestTeam = winningTeam
        print(scores)
        return currentBestTeam

    def updateScores(self, team, points, scores):
        if team not in scores:
            scores[team] = 0
        scores[team] += points
        return ""


S = Solution()
competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]
results = [0, 0, 1]
print(S.tournamentWinner(competitions, results))

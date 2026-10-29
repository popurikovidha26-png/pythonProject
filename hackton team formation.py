# Hackathon Team Formation and Ranking

teams = {
    "Team A": [80, 90, 85],
    "Team B": [75, 85, 90],
    "Team C": [90, 95, 85]
}

min_size = 2
max_size = 4
ranking = []

for team, scores in teams.items():
    size = len(scores)

    if size < min_size or size > max_size:
        print(team, "- Invalid team size")
    else:
        total = sum(scores)
        ranking.append((team, total, max(scores)))
        print(team, "Total Score:", total)

# Rank by total score, then highest individual score
ranking.sort(key=lambda x: (x[1], x[2]), reverse=True)

print("\nFinal Rankings:")
for rank, (team, total, highest) in enumerate(ranking, 1):
    print(rank, team, "Score:", total)

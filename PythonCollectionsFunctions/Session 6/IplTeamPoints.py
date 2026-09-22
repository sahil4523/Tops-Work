teams=["RCB", "MI", "GT", "RR"]
points=[16, 12, 16, 10]

team_points=dict(zip(teams, points))

for team, point in team_points.items():
    if point > 10:
        print(team, point)
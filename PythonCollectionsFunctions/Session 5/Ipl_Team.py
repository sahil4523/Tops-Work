team = {
    "RCB": {
        "captain": "Rajat",
        "players": 18
    },
    "MI": {
        "captain": "Rohit",
        "players": 17
    }
}

team["GT"] = {
    "captain": "Shubhman",
    "players": 16
}

for name, data in team.items():
    print(name, data["captain"])
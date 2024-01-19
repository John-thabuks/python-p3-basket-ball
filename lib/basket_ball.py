def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }


def num_points_per_game(player_name):
    #return number_of_points
    players_object = game_dict()["home"]["players"] + game_dict()["away"]["players"]
    for player in players_object:
       if player["name"] == player_name:
          return player["points_per_game"]

# num_points_per_game("Darius Garland")

def player_age(player_name):
  #return player's age
   players_list = game_dict()["home"]["players"] + game_dict()["away"]["players"]
   for player in players_list:
      if player["name"] == player_name:
         return player["age"]
#    print(players_list)
   

# player_age("Kristaps Porzingis")   

def team_colors(team_name):
  #returns list of team's color
    for team in game_dict():
       if (game_dict()[team]["team_name"] == team_name):
          return game_dict()[team]["colors"]
    


# team_colors("Washington Wizards")

def team_names():
    teams = []
    for team in game_dict():
        teams.append(game_dict()[team]["team_name"])
    return teams

# team_names()

def player_numbers(team_name):
#   returns list of jersey numbers
    jersey_numbers = []
    for team in game_dict():
    #   print(game_dict()[team]["team_name"])
        if game_dict()[team]["team_name"] == team_name:
           players = game_dict()[team]["players"]
        #    print(players)
           for player in players:
              jersey_numbers.append(player["number"])
    return jersey_numbers

# player_numbers("Washington Wizards")

def player_stats(player_name):
  #returns dictionary of that player's stats
    #Get a list of all players
    #Loop through the list and find the player name
    #return player details
    players_object = game_dict()["home"]["players"] + game_dict()["away"]["players"]

    for player in players_object:

        if player["name"] == player_name:
            return player






    # all_players = {}
    # players_object = game_dict()["home"]["players"] + game_dict()["away"]["players"]
    # for player in players_object:
    # #    print(player)
    #     if player["name"] == player_name:
    #         print(player)
    #         all_players.update(
    #         {player['name'] : player
            #  {
            #     "name": player["name"],
            #     "number": player["number"],
            #     "position": player["position"],
            #     "points_per_game": player["points_per_game"],
            #     "rebounds_per_game": player["rebounds_per_game"],
            #     "assists_per_game": player["assists_per_game"],
            #     "steals_per_game": player["steals_per_game"],
            #     "blocks_per_game": player["blocks_per_game"],
            #     "career_points": player["career_points"],
            #     "age": player["age"],
            #     "height_inches": player["height_inches"],
            #     "shoe_brand": player["shoe_brand"]
            #     }
            # }
        # )
    # print(all_players)
    # print( all_players[player_name])

# print(player_stats("Darius Garland"))

def average_rebounds_by_shoe_brand():
    #[{"Nike":[5.0,6.7,8.1]}, {"Reebok":[8.2,3.4,5.6]}, {"Puma":[10.5,6.7,9.0]}]

    players_object = game_dict()["home"]["players"] + game_dict()["away"]["players"]
    shoe_brands = []
    for player in players_object:
        if player["shoe_brand"] not in shoe_brands:
            shoe_brands.append(player["shoe_brand"])
    # print(shoe_brands)

    for brand in shoe_brands:
        # print(brand)
        brand_dict = {brand: []}
        # print(brand_dict)
        result = [brand_dict[brand].append(player["rebounds_per_game"]) for player in 
                  players_object if player["shoe_brand"] == brand]
        # print(brand_dict)

        avarage = sum(brand_dict[brand])/len(brand_dict[brand])
        print(f"{brand}:  {avarage:.2f}")



average_rebounds_by_shoe_brand()


    # shoe_dict = {}
    # all_players = {}
    # for team in ["home", "away"]:
    #     for player in game_dict()[team]['players']:
    #        all_players.update(
    #     {player['name']: {
    #       "name": player["name"],
    #       "number": player["number"],
    #       "position": player["position"],
    #       "points_per_game": player["points_per_game"],
    #       "rebounds_per_game": player["rebounds_per_game"],
    #       "assists_per_game": player["assists_per_game"],
    #       "steals_per_game": player["steals_per_game"],
    #       "blocks_per_game": player["blocks_per_game"],
    #       "career_points": player["career_points"],
    #       "age": player["age"],
    #       "height_inches": player["height_inches"],
    #       "shoe_brand": player["shoe_brand"]
    #       }
    #     }
    #   )
    # players = all_players
    # for player in players:
    #     brand = players[player]["shoe_brand"]
    #     rebounds = players[player]["rebounds_per_game"]
    # if (brand in shoe_dict):
    #     shoe_dict[brand].append(rebounds)
    # else:
    #     shoe_dict[brand] = [rebounds]
    # for brand in shoe_dict:
    #     avg = sum(shoe_dict[brand]) / len(shoe_dict[brand])
    # print(f'{brand}: ', "{0:.2f}".format(avg))
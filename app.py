
  
import constants
import copy
import sys

number_of_player_per_team = len(constants.PLAYERS) / len(constants.TEAMS)



my_players = copy.deepcopy(constants.PLAYERS)

my_teams = copy.deepcopy(constants.TEAMS)

team2_players = number_of_player_per_team + number_of_player_per_team

def cleaning_data_from_PLAYERS_heights(players):
    for player in players:
        for key, value in player.items():
            if key == "height":
                new_value = value.split()
                new_value[0] = int(new_value[0])
                player["height"] = new_value
               
            
            
def cleaning_data_from_PLAYERS_experiences(players):
    for player in players:
        for key, value in player.items():
            if key == "experience":
                if value == "YES":
                    player["experience"] = True
                else:
                    player["experience"] = False
                    
                    
def cleaning_data_from_PLAYERS_guardians(players):
    for player in players:
        for key, value in player.items():
            if key == "guardians":
                new_value = value.split(" ")
                player["guardians"] = new_value

        
def a_team():
    return list()


def balance_teams(team1, team2, team3):
    index = 1
    exp_p = 1
    for player in my_players:
        for key, value in player.items():
            if (index <= number_of_player_per_team):
                if (value == True and (exp_p >= 0 and exp_p <= 3)):
                    team1.append(player)
                    index += 1
                    exp_p += 1
                else:
                    team1.append(player)
                    index += 1
            elif (index > number_of_player_per_team and index <= team2_players):
                if (value == True and (exp_p >= 3 and exp_p <= 6)):
                    team2.append(player)
                    index += 1
                    exp_p += 1
                else:
                    team2.append(player)
                    index += 1
            else:
                team3.append(player)
         
        
def intro():
    print("BASKETT BALL TEAM STAT TOOL 🏀 \n" )
    print(("-" * 12) + " MENU " + ("-" * 12) + "\n")
    
    
def help_promp():
       print("""
* answer \'1\' to select team stats
* answer \'2\' to quit 
             """)
        
    

def team_selection():
    print("""
1)  Panthers
2)  Bandits
3)  Warrios """)
    answer = input(">   ")
    if answer == "1":
        return team1
    elif answer == "2":
        return team2
    elif answer == "3":
        return team3
    else:
        print("please select a valid value EX. 1, 2 or 3")
        
        
    
def display_team(team):
    if team == team1:
        print(("-" * 10) + "Panthers Players" + ("-" * 10))
    elif team == team2:
        print(("-" * 10) + "Bandits Players" + ("-" * 10))
    else:
        print(("-" * 10) + "Warrius Players" + ("-" * 10))
    for players in team:
        for key, value in players.items():
            if key == "name":
                print("\033[1m" + key + ":" + "\033[0m")
                print(value)
            elif key == "guardians":
                # https://kite.com/python/answers/how-to-print-in-bold-in-          python#:~:text=Add%20the%20ANSI%20escape%20sequence,formatting%20for%20any%20following%20strings.&text=Further%20reading%3A%20Read%20more%20about,and%20other%20formatting%20options%20here.
                    print("\033[1m" + key + ":" + "\033[0m")
                    print(value)
            elif key == "experience":
                print("\033[1m" + key + ":" + "\033[0m")
                print(value)
            elif key == "height":
                print("\033[1m" + key + ":" + "\033[0m")
                print(value)
                print("\n")
            else:
                print("something when wrong, please try again")
    display_stats(team)

def display_stats(team):
    new_list = list()
    print(("-" * 10) + "Overview" + ("-" * 10))
    print("Total players:  " + "\033[1m" + str(len(team)) + "\033[0m")
    for tea in team:
        for key, value in tea.items():
            if key == "name":
                new_list.append(value)
    print(", ".join(new_list) + "\n")
    

if __name__ == "__main__":
    
    intro()
    
    while True:
        print("If unsure type \'INSTRUCT\' ")
        control = input(">  ")
        if control.upper() == "INSTRUCT":
            help_promp()
            continue
        elif control == "1":
            cleaning_data_from_PLAYERS_heights(my_players)
            cleaning_data_from_PLAYERS_experiences(my_players)
            team1 = a_team()
            team2 = a_team()
            team3 = a_team()
            balance_teams(team1,team2, team3)
            display_team(team_selection())
            continue
            
            #funcdysplay team stats
            break
        elif control == "2":
            sys.exit()
            

        
    
    

   


import constants
import copy
import sys

number_of_player_per_team = len(constants.PLAYERS) / len(constants.TEAMS)



my_players = copy.deepcopy(constants.PLAYERS)

my_teams = copy.deepcopy(constants.TEAMS)



def cleaning_data_from_PLAYERS_height(players):
    for player in players:
        for key, value in player.items():
            if key == "height":
                new_value = value.split()
                # https://www.geeksforgeeks.org/python-convert-numeric-string-to-integers-in-mixed-list/
                new_value_to_dic = [int(string) if string.isdigit() else string for string in new_value]
                return new_value_to_dic
            
            
def cleaning_data_from_PLAYERS_experience(players):
    for player in players:
        for key, value in player.items():
            if key == "experience":
                if value == "YES":
                    return True
                else:
                    return False
                
         
def new_data_for_dic_height(value):
    for player in my_players:
        player["height"] = value
        
        
def new_data_for_dic_experience(value):
    for player in my_players:
        player["experience"] = value

        
def a_team():
    return list()


def balance_teams(team1, team2, team3):
    index = 1
    for player in my_players:
        if index <= number_of_player_per_team:
                team1.append(player)
                index += 1
        elif (index > number_of_player_per_team) and (index <= (number_of_player_per_team + number_of_player_per_team)):
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
    print("Total players:  " + "\033[1m" + str(len(team)) + "\033[0m")
    

if __name__ == "__main__":
    
    intro()
    
    while True:
        print("If unsure type \'INSTRUCT\' ")
        control = input(">  ")
        if control.upper() == "INSTRUCT":
            help_promp()
            continue
        elif control == "1":
            new_data_for_dic_height(cleaning_data_from_PLAYERS_height(my_players))
            new_data_for_dic_experience(cleaning_data_from_PLAYERS_experience(my_players))
            team1 = a_team()
            team2 = a_team()
            team3 = a_team()
            balance_teams(team1,team2, team3)
            display_team(team_selection())
            
            #funcdysplay team stats
            break
        elif control == "2":
            sys.exit()
            

        
    
    

   
    
   
    

    


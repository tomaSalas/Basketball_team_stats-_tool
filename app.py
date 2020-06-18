
  
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
                new_new_value = new_value[0]
                player["height"] = new_new_value
               
            
            
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
                new_value = value.split(" and ")
                player["guardians"] = new_value

        
def a_team():
    return list()


def balance_teams(team1, team2, team3):
    team1_count = 1
    team2_count = 1
    team3_count = 1
    exp = 1
    non_exp = 1
    for player in my_players:
        if (team1_count <= number_of_player_per_team  and player["experience"] == True and exp <= 3):
            team1.append(player)
            team1_count += 1
            exp += 1
        elif (team1_count <= number_of_player_per_team and player["experience"] == False and non_exp <= 3):
            team1.append(player)
            team1_count += 1
            non_exp += 1
        elif (team2_count <= team2_players and player["experience"] == True and exp <= 6):
            team2.append(player)
            team2_count += 1
            exp += 1
        elif (team2_count <= team2_players and player["experience"] == False and non_exp <= 6):
            team2.append(player)
            team2_count += 1
            non_exp += 1
        else:
            team3.append(player)
            
def intro():
    print("BASKETT BALL TEAM STAT TOOL 🏀 \n" )
    print(("-" * 12) + " MENU " + ("-" * 12) + "\n")
    
    
def help_promp():
       print("""
* input \'1\' to select team stats
* input \'2\' to quit 
             """)
        
    
def team_selection():
    print("""
1)  Panthers
2)  Bandits
3)  Warrios """)
    while True:
        answer = input(">   ")
        if answer == "1":
            return team1
        elif answer == "2":
            return team2
        elif answer == "3":
            return team3
        else:
            print("please select a valid value (EX. 1, 2 or 3)")
            continue
        
        
    
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
    count = 0
    count_exp = 0
    count_non_exp = 0
    add_height = 0
    new_list = list()
    print(("-" * 10) + "Overview" + ("-" * 10))
    print("Total players:  " + "\033[1m" + str(len(team)) + "\033[0m")
    for tea in team:
        for key, value in tea.items():
            if key == "name":
                new_list.append(value)
            elif key == "experience" and value == True:
                count_exp += 1
            elif key == "experience" and value == False:
                count_non_exp += 1
            elif key == "height":
                add_height += value
                count += 1
    print(", ".join(new_list) + "\n")
    print("Total experienced: " + "\033[1m" + str(count_exp) + "\033[0m")
    print("Total inexperienced: "  + "\033[1m" + str(count_non_exp) + "\033[0m")
    print("Average height: " + "\033[1m" + " {:.2f} ".format(add_height/count) +"\033[0m")
    print("-" * 30)
    
    while True:
        asnwer = input("Would you like to see other teams stats? Y/N >  ")
        if asnwer.upper() == "Y":
            display_team(team_selection())
            break
        elif asnwer.upper() == "N":
            sys.exit()
        else:
            print("That is not a valid input! Please try again")
            continue

if __name__ == "__main__":
    
    intro()
    help_promp()
    while True:
        control = input(">  ")
        if control.upper() == "HELP":
            help_promp()
            continue
        elif control == "1":
            cleaning_data_from_PLAYERS_heights(my_players)
            cleaning_data_from_PLAYERS_experiences(my_players)
            cleaning_data_from_PLAYERS_guardians(my_players)
            team1 = a_team()
            team2 = a_team()
            team3 = a_team()
            balance_teams(team1,team2, team3)
            value = display_team(team_selection())
        elif control == "2":
            sys.exit()
        else:
            print("\n"+ "That is not a valid input! Please try again" + "\n" + "You can always type \'HELP\' if you do not remenber the commands")
            continue
            

        
    
    

   

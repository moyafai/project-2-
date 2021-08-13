import copy
import constants
import sys
teams = copy.deepcopy(constants.TEAMS)
teams_name = "A-pantthers\nB-Bandits\nC-warriors" 
players_list = copy.deepcopy(constants.PLAYERS)
panthers = []
bandits = []
warriors = []


def clean_data():
    
    for player in players_list:
        height = player["height"].split()
        height= int(height[0])
        if player["experience"] == "YES":
            player["experience"] = True
            players_with_exp.append(player)
        elif player["experience"] == "NO":
            player["experience"] = False
            players_no_exp.append(player)
        
players_with_exp = []
players_no_exp = []
clean_data()        

def balance_team():
    num_of_expteam = len(players_with_exp) / len(teams_name)
    no_expteam = len(players_no_exp) / len(teams_name)
    total_players_per_team = num_of_expteam + no_expteam
    
    for player in players_with_exp:
        
        if len(panthers) < 3:
            player_name = player['name']
            player_name = "".join(player_name)
            panthers.append(player_name)
        elif len(bandits) < 3:
            player_name = player['name']
            player_name = "".join(player_name)
            bandits.append(player_name)
        elif len(warriors) < 3:
            player_name = player['name']
            player_name = "".join(player_name)
            warriors.append(player_name)
            
    for player in players_no_exp:  
        
        if len(panthers) < 6:
            player_name = player['name']
            player_name = ''.join(player_name)
            panthers.append(player_name)
        elif len(bandits) < 6:
            player_name = player['name']
            player_name = ''.join(player_name)
            bandits.append(player_name)
        elif len(warriors) < 6:
            player_name = player['name']
            player_name = ''.join(player_name)
            warriors.append(player_name)
                
balance_team()    


def start_game():
    print("BASKETBALL TEAM STATS TOOL")
    print("\n")
    print("*********  MENU  *********")
    print("\n")
    print("Here are your choices:")



    try:
        while True:
        
            first_option = input("\nA- Display Team Stats\nB- Quit\n")
            print("\n")
            if first_option.lower() == "a":
                print(teams_name)
                break
        

            elif first_option.lower() == "b":
                print("Thank you, see you soon! ")
                sys.exit()
    except ValueError:
                    print("Pleas enter a valid data")

        
    

    print("\n")
    try:

        while True:
            second_option = input("Choose a team: ")    
            if second_option.lower()=="a":
                print("Team: Panthers stats:\n------------")
                print("Total players : 6")
    
                print(", ".join(panthers))
                break

            elif second_option.lower()=="b":
                print("Team: Panthers stats:\n------------")
                print("Total players : 6")
            
                print(", ".join(bandits))
                break
                
            elif second_option.lower()=="c":
                print("Team: Panthers stats:\n------------")
                print("Total players : 6")
            
                print(", ".join(warriors))
                break
        
            
    except ValueError:
        print("please enter a valid data ")

start_game()        
            
if __name__ == "__main__":
    start_game()
    clean_data()
    balance_team() 
    
    

#dodać usuwanie 

import random
import sys
import os
import json
import requests

#Random Joke
name_json_file = "favorities.json"
yes = ["yes","y"]
no = ["no","n"]


def main():
    if os.path.exists(f"{name_json_file}"):
        try:
            with open(f"{name_json_file}", "r") as j:
                loaded_data = json.load(j)
                
            if isinstance(loaded_data, list):
                json_data = loaded_data
            else:
                print("Warning: File data.json contains invalid data format. Initializing an empty task list.")
                
        except json.JSONDecodeError:
            print("Warning: File data.json contains invalid data format. Initializing an empty task list.")
    else:
        with open(f"{name_json_file}", "w") as j:
            json.dump([], j, indent=2)
    print(f"File 'task_list.json' not found, created new empty JSON file.")
    json_data = loaded_data
    menu(json_data)

    
def request_joke(json_data):
    url_joke_website = 'https://icanhazdadjoke.com/'
    headers = {
    "Accept": "application/json", 
    "User-Agent": "My Joke App (your_email@example.com)"
    }
    response = requests.get(url_joke_website,headers=headers)
    data_joke = response.json()
    show_joke(data_joke)
    ask_for_save_joke(data_joke, json_data)


def show_joke(data_joke):
    print("\nRandom joke is: \n\n", data_joke["joke"])
    

def ask_for_save_joke(data_joke, json_data):
    ask_for_save = input("\n\nDo you want yo save that joke? yes/no. Type:  ")
    while ask_for_save.lower() not in yes + no:
        print("Type correct answer!!!")
        ask_for_save = input(ask_for_save)
    else:
        if ask_for_save.lower() in ["yes","y"]:
            save_favourite(data_joke, json_data)
        else:
            ask_for_menu()

def save_favourite(data_joke,json_data):
    joke_list = {'ID':len(json_data)+1, 'Joke':data_joke["joke"]}
    
    json_data.append(joke_list)
    with open(f"{name_json_file}", "w") as j:
        json.dump(json_data, j, indent=2)
    print(f"Added {data_joke} to your favourite list!")
    ask_for_menu(json_data)
        
        

def menu(json_data):
    ask = "Type 1 to draw a joke, Type 2 to show favourites jokes or delete, Type 3 to go to menu or exit. Type:    "
    ask_what_to_go = input(ask)
    while ask_what_to_go in ["1",'2','3']:
        if ask_what_to_go == "1":
            request_joke(json_data)
            
            break
        elif ask_what_to_go == "2":
            show_favourities(json_data)
        else:
            ask_for_menu(json_data)
            break
    else:
        print("Type correctly 1, 2 or 3")
        ask_what_to_go = input(ask)
            

def ask_for_menu(json_data):
    ask_what_to_do = input("Do you want to go to menu or exit. menu/exit    ")
    while ask_what_to_do.lower() in ["menu",'exit']:
        if ask_what_to_do.lower() in ['menu']:
            menu(json_data)
        else:
            exit_program()

def show_favourities(json_data):
    if not json_data:
        print("No favourite jokes yet.")
    else:
        print("Favourite jokes:")
        for i in json_data:
            print(f"{i['ID']}: {i['Joke']}")
    
    ask_for_delete = input("Dou you want to delete jokes? yes/no Type:  ")
    while ask_for_delete.lower() in yes + no:
        if ask_for_delete.lower() in yes:
            delete_from_faveourities(json_data)
        else:
            ask_for_menu(json_data)
    ask_for_menu(json_data)
    
    
    
def delete_from_faveourities(json_data):
    for i in json_data:
        print(i)
    ask_which_delete = int(input("Which joke do you want to delete? Type ID:    "))
    ids = [z["ID"] for z in json_data]
    while ask_which_delete in i:
        json_data=[z for z in json_data if z["ID"] != ask_which_delete]
    for _, z in enumerate(json_data, start=1):
        z["ID"] = i
    for idx, z in enumerate(json_data, start=1):
        z["ID"] = idx
    with open ("task_list.json", "w") as delete:
        json.dump(json_data, delete , indent=2)
    print("Joke deleted successfully!")
    ask_for_menu(json_data)


def exit_program():
    print('Exiting program...')
    sys.exit()

main()
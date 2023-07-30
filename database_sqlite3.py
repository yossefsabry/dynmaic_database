# -----------------------------------------------
# making database skills => sqlite3 => database
# -----------------------------------------------


# start import 

import sqlite3


# creating database

db = sqlite3.connect("skills.db")

# making cursor for db

cr = db.cursor()

# create table skills

cr.execute("create table if not exists skills(name text, progress integer, user_id integer)")

# make change commit and close database

def close_commit_database():

    """ function for close and save commit change in the datebase  """
    db.commit()
    db.close()
    print("- the connection close between database -")

# fetch all

cr.execute("select * from skills")

# person ID

person_id = input("Write The User ID : ")

# input big massage

input_massage = """
- what do you want to do ?
- "s" => show all skills
- "a" => add skills
- "d" => delete skills
- "u" => update skills
- "q" => quit the app
- choose option:
- """

# user input

user_input = input(input_massage).strip().lower()

# commend list 

commend_list = ["s", "a", "d", "u", "q"]

# define the metheds

def show_skills():

    cr.execute(f"select * from skills where user_id = {person_id}")
    
    results = cr.fetchall()
    
    print(f" you have {len(results)} skills ".center(60,'-'))
    
    for rows in results:
    
        print(f"- Skill Name : {rows[0]} -")
    
        print(f"- Skill Progress : {rows[1]} -")
    
        print(f"- User ID : {rows[2]} -")
    
        print('-'*40)
    
    close_commit_database()

def add_skills():

    sk_name = input("- write skill name: ").strip().capitalize()

    cr.execute(f"select name from skills where name = '{sk_name}' and user_id = '{person_id}'")    
    
    results = cr.fetchone()

    if results == None:

        prog = input("- write skill progress:  ").strip()

        cr.execute(f"insert into skills(name , progress, user_id) values ( '{sk_name}', '{prog}', '{person_id}' )")

        print(f"- skill {sk_name} added successful -")

        close_commit_database()

    else:

        print("- you cannot add it, its already exists -")
    
        close_commit_database()

def delete_skills():
        
    sk_name = input("- write skill name: ").strip().capitalize()

    cr.execute(f"delete from skills where name = '{sk_name}' and user_id = '{person_id}'")

    print(f"- skill {sk_name} deleted successful -")

    close_commit_database()

def update_skills():

    sk_name = input("- write skill name: ").strip().capitalize()

    cr.execute(f"select name from skills where name = '{sk_name}' and user_id = '{person_id}'")    
    
    results = cr.fetchone()

    if results == None:

        print(f"- the {sk_name} is not exists -")

        close_commit_database()
    else:

        prog = input("- write skill progress: ").strip()

        cr.execute(f"update skills set progress = '{prog}' where name = '{sk_name}' and user_id = '{person_id}' ")

        print(f"- skill {sk_name} updated successful -")

        close_commit_database()

def quit_skills():
    
    print("- quit app -")
    close_commit_database()

# check if commend is there in comment list

if user_input in commend_list :

    print(f"- comment found {user_input} -")

    if user_input == "s":

        show_skills()
    
    elif user_input == "a":

        add_skills()

    
    elif user_input == "d":

        delete_skills()

    
    elif user_input == "u":

        update_skills()

    else:

        quit_skills()
    
else:

    print(f"- sorry this commend \"{user_input}\" is not found -")
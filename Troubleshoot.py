'''
/Applications/Python\ 3.10/Install\ Certificates.command

pip install all of the things
pip install PySimpleGUI

https://www.youtube.com/watch?v=q_3doIUZTFg


Basic input:
Run User.py
    -> Enter Username
        -> Wrong
            -> Try again
        -> Right
            -> Run pswd.py
                -> Enter Password
                    -> Wrong
                        -> Try again
                    -> Right
                        -> Run Main.py

def EnterData():
  with open("user_data.csv", "w") as f:
    fieldnames = [["usernames"],["passwords"]]
    writer = csv.writer(f)
    n = int(input("Number of Users: "))
    for i in range(n):
      usr = input("Enter the new username : ")
      psw = input("Enter the password : ")
      writer.writerow([usr,psw])
'''

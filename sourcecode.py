# Dhimaan and Manshul's Analytical Sorter & Compiler 4 User Simplicity

import PySimpleGUI as gui
import ButtonGUI as b
import wolframalpha
import csv

gui.theme("Topanga")
client = wolframalpha.Client("V5TE9K-LLRV86XKPQ")

layout = [ 
        [ gui.Text(b.username) ],
        [ gui.Input() ],
        [ gui.Text(b.password) ],
        [ gui.Input() ],
        [ gui.Button(b.login) ],
        [ gui.Button(b.register), gui.Button(b.cancel) ]
    ]
window = gui.Window("D.A.M.A.S.C.U.S.", layout)

while True:
    event, values = window.read()
    user = values[0]
    password = values[1]

    if event == b.cancel:
        break

    elif event == b.register:
        layout2 = [ 
                [ gui.Text(b.newusername) ],
                [ gui.Input() ],
                [ gui.Text(b.newpassword) ],
                [ gui.Input() ],
                [ gui.Button(b.go), gui.Button(b.cancel) ]
            ]

        window2 = gui.Window("D.A.M.A.S.C.U.S.", layout2)

        while True:
            event2, values2 = window2.read()
            user2 = values2[0]
            password2 = values2[1]

            if event2 == b.cancel:
                exit()

            else:
                with open("user_data.csv", "a") as f:
                    fieldnames = [ [ "usernames" ], [ "passwords" ] ]
                    writer = csv.writer(f)
                    writer.writerow( [ user2, password2 ] )
                exit()
                
    else:
        l = "notfound"
        with open("user_data.csv", "r") as f:
            reader = csv.reader(f)
            for line in reader:
                if user in line[0]:
                    if password in line[1]:
                        l = "found"      

                        layout3 = [ 
                                [ gui.Text("Ask me any Math, Science or GK questions") ],
                                [ gui.Input() ],
                                [ gui.Output(size = (42,15))],
                                [ gui.Button(b.search) ],
                                [ gui.Button(b.output), gui.Button(b.input) ],
                                [ gui.Button(b.shh), gui.Button(b.cancel2) ]
                            ]

                        window3 = gui.Window("D.A.M.A.S.C.U.S.", layout3)

                        def readout():
                            with open("Output Logs.txt", "r") as g:
                                    print(b.outputline)
                                    size_to_read = 1000
                                    g_contents = g.read(size_to_read)
                                    print(g_contents, end=' ')

                        def readin():
                            with open("Input Logs.txt", "r") as g:
                                    print(b.inputline)
                                    size_to_read = 1000
                                    g_contents = g.read(size_to_read)
                                    print(g_contents, end=' ')		

                        while True:
                            event3, values3 = window3.read()

                            if event3 == b.cancel2:
                                exit()

                            elif event3 == b.output:
                                readout()
                                print(b.line)

                            elif event3 == b.input:
                                readin()
                                print(b.line)

                            elif event3 == b.shh:
                                wolfram_res = next(client.query(values3[0]).results).text
                                print("[ Answer ]", wolfram_res, "\n")

                            else:
                                wolfram_res = next(client.query(values3[0]).results).text

                                print("[ Answer ]", wolfram_res, "\n")
                                with open("Output Logs.txt", "a") as f:
                                    f.write(wolfram_res)
                                    f.write("\n")
                                    f.write("\n")

                                with open("Input Logs.txt", "a") as g:
                                    g.write(values3[0])
                                    g.write("\n")
                                    g.write("\n")
                 
        if l != "found":
            print("Incorrect Username or Password")

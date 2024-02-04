from tkinter import *

# building a window for the game
root = Tk()
root.geometry("300x350")
root.title("Tic Tac Toe")

# for game name
frame1 = Frame(root)
frame1.pack()

titleLabel = Label(frame1, text="Tic Tac Toe", font=("Arial", 15))
titleLabel.pack()

# for nine buttons
frame2 = Frame(root)
frame2.pack()

# global variables
turn = "X"
winningLabelExists = False
drawLabelExists = False
end = False
buttonsList = []

# board 
board = { 1:" ", 2:" ", 3:" ",
          4:" ", 5:" ", 6:" ",
          7:" ", 8:" ", 9:" "}

# checking for win
def checkWin(player):
    if (board[1] == board [2] and board[2] == board[3] and board[3]== player) or (board[4] == board [5] and board[5] == board[6] and board[6]== player) or (board[7] == board [8] and board[8] == board[9] and board[9]== player) or (board[1] == board [5] and board[5] == board[9] and board[9]== player) or (board[3] == board [5] and board[5] == board[7] and board[7]== player)or (board[1] == board [4] and board[4] == board[7] and board[7]== player) or (board[2] == board [5] and board[5] == board[8] and board[8]== player) or (board[3] == board [6] and board[6] == board[9] and board[9]== player):
        return True
    else:
        return False

# checking for draw
def checkDraw():
    for i in board.keys():
        if board[i] == " ":
            return False
    return True

# labels
def labelForWin(player):

    global winningLabel
    global winningLabelExists

    winningLabel = Label(frame2, text=f'{player} wins this game', font = ("Araial",15), bg ="lightgray")
    winningLabel.grid(row=0, column= 0 , rowspan = 3,columnspan = 3)
    winningLabelExists = True
    
def labelForDraw():

    global drawLabel
    global drawLabelExists

    drawLabel = Label(frame2, text="Game Draw.", font = ("Araial",15), bg ="lightgray")
    drawLabel.grid(row=0, column= 0 , rowspan = 3, columnspan = 3)
    drawLabelExists = True

# bringing to default
def emptyButtons():
    for buttons in buttonsList:
        buttons["text"] = " "

def emptyBoard():
    for i in board.keys():
        board[i] = " "

# restart game
def restartGame(event):

    global turn
    global end
    global winningLabelExists
    global drawLabelExists

    turn = "X"
    end = False

    emptyButtons()
    emptyBoard()

    if winningLabelExists : 
        winningLabel.destroy()
        winningLabelExists = False
    if drawLabelExists: 
        drawLabel.destroy()
        drawLabelExists = False

# gameloop
def play(event):
   
    # can't access the global variables in a function
    global turn
    global end

    if end:
        return 
    
    button = event.widget
    
    clicked = str(button)[-1]
    if clicked == 'n':
        clicked = 1
    else:
        clicked = int(clicked)


    if button["text"] == " ":
        if  turn == "X":

            button["text"] = "X"
            board[clicked] = turn
            if checkWin(turn):
               
               labelForWin(turn)
               end = True
               
            turn = "O"

        elif turn == "O":

            button["text"] = "O"
            board[clicked] = turn
            if checkWin(turn):

                labelForWin(turn)
                end = True
                
            turn = "X"
    
    if checkDraw() and not end:
        labelForDraw()

# <Button-1> means mouse-left button
# GUI stuff
button1 = Button(frame2, text = " ", width = 6 , height =3 ,font =("Arail", 15))
button1.grid(row= 0, column= 0)
button1.bind("<Button-1>", play)
buttonsList.append(button1)

button2 = Button(frame2, text = " ", width = 6 , height =3,font =("Arail", 15))
button2.grid(row= 0, column= 1)
button2.bind("<Button-1>", play)
buttonsList.append(button2)

button3 = Button(frame2, text = " ", width = 6 , height =3,font =("Arail", 15))
button3.grid(row= 0, column= 2)
button3.bind("<Button-1>", play)
buttonsList.append(button3)

button4 = Button(frame2, text = " ", width = 6 , height =3,font =("Arail", 15))
button4.grid(row= 1, column= 0)
button4.bind("<Button-1>", play)
buttonsList.append(button4)

button5 = Button(frame2, text = " ", width = 6 , height =3,font =("Arail", 15))
button5.grid(row= 1, column= 1)
button5.bind("<Button-1>", play)
buttonsList.append(button5)

button6 = Button(frame2, text = " ", width = 6 , height =3,font =("Arail", 15))
button6.grid(row= 1, column= 2)
button6.bind("<Button-1>", play)
buttonsList.append(button6)

button7 = Button(frame2, text = " ", width = 6 , height =3,font =("Arail", 15))
button7.grid(row= 2, column= 0)
button7.bind("<Button-1>", play)
buttonsList.append(button7)

button8 = Button(frame2, text = " ", width = 6 , height =3,font =("Arail", 15))
button8.grid(row= 2, column= 1)
button8.bind("<Button-1>", play)
buttonsList.append(button8)

button9 = Button(frame2, text = " ", width = 6 , height =3,font =("Arail", 15))
button9.grid(row= 2, column= 2)
button9.bind("<Button-1>", play)
buttonsList.append(button9)

restartButton = Button(frame2, text= "Restart Game", width = 12, height = 1, font = ("Araial",15))
restartButton.grid(row = 3, column = 0, columnspan = 3)
restartButton.bind("<Button-1>", restartGame)

root.mainloop()


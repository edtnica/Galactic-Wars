from tkinter import Tk, Canvas, PhotoImage, Button, Entry
from random import randint as rand
from time import sleep

# RESOLUTION 1280x720


#									            ***	GALACTIC WARS ***
#										             -the game-		


# tkinter and canvas settings
window = Tk()
window.title("GALACTIC WARS")
window.resizable(width=False, height=False)
canvas = Canvas(window, width=1280, height=720, highlightthickness=0)
canvas.pack()
canvas.config(bg="black")
																					

# --> FUNCTIONS

# Creating the background
def background():
	
	stars = []
	colours = ["#F7F9F9", "#F4F6F7", "#F2F3F4"]

	for i in range(500):
		xStar = rand(1, 1279)
		yStar = rand(1, 719)

		size = rand(2, 5)
		colour = rand(0, 2)

		xyStar = (xStar, yStar, xStar+size, yStar+size)

		tmp_star = canvas.create_oval(xyStar, fill=colours[colour])

		stars.append(tmp_star)


# Move the spaceship to the left 
def moveLeft(event):
	
	global isPaused
	global isPaused2

	posShip = canvas.coords(spaceShip)

	if (posShip[0] > 51 and isPaused == False and isPaused2 == False):
		x = -10
		y = 0
		canvas.move(spaceShip, x, y)


# Move the spaceship to the right
def moveRight(event):
	
	global isPaused
	global isPaused2

	posShip = canvas.coords(spaceShip)

	if (posShip[0] < 1229 and isPaused == False and isPaused2 == False):
		x = 10
		y = 0
		canvas.move(spaceShip, x, y)


# Move the spaceship up
def moveUp(event):
	
	global isPaused
	global isPaused2

	posShip = canvas.coords(spaceShip)

	if (posShip[1] > 51 and isPaused == False and isPaused2 == False):
		x = 0
		y = -10
		canvas.move(spaceShip, x, y)


# Move the spaceship down
def moveDown(event):
	
	global isPaused
	global isPaused2

	posShip = canvas.coords(spaceShip)

	if (posShip[1] < 669 and isPaused == False and isPaused2 == False):
		x = 0
		y = 10
		canvas.move(spaceShip, x, y)


# Pauses the game 
def pause(event):
	
	global isPaused
	global pauseText
	global btnPauseWindow
	global btnQtWindow

	if (isPaused):
		isPaused = False
		if (pauseText in canvas.find_all()):
			canvas.delete(pauseText)
			canvas.delete(btnPauseWindow)
			canvas.delete(btnQtWindow)
	else:
		if (isPaused2 == False and ok2 == 0):
			isPaused = True
			pauseText = canvas.create_text(640, 360, fill="white", font="Arial 50 bold", text="PAUSED")

			# Save button
			btnPause = Button(canvas, text="SAVE", command=lambda:save(event), background="darkgrey", font="Arial 20 bold")
			btnPause.configure(activebackground = "grey", highlightthickness=0)
			btnPauseWindow = canvas.create_window(1210, 630, window=btnPause)

			btnQt = Button(canvas, text="QUIT", command=lambda:quit(), background="darkgrey", font="Arial 20 bold")
			btnQt.configure(activebackground = "grey", highlightthickness=0)
			btnQtWindow = canvas.create_window(1210, 680, window=btnQt)


# 'Boss Key'
def bossKey(event):
	
	global isPaused2
	global bossKeyImg
	global bossKeyCreate


	if (isPaused2):
		isPaused2 = False
		if (bossKeyCreate in canvas.find_all()):
			canvas.delete(bossKeyCreate)
	else:
		if (isPaused == False):
			isPaused2 = True
			bossKeyImg = PhotoImage(file="bosskey.png")
			bossKeyCreate = canvas.create_image(0, 0, anchor="nw", image=bossKeyImg)


# Gives you one more life		
def cheatCode(event):
	
	global livesNum

	if (livesNum < 3):
		livesNum += 1
		canvas.itemconfig(lives, text="LIVES: " + str(livesNum))


bulletStart = 0

# Creates the bullet
def shoot(event):
	
	global bulletStart
	global bullet
	global isPaused
	global isPaused2

	if (bulletStart == 0 and isPaused == False and isPaused2 == False):
		posShip = canvas.coords(spaceShip)
		bullet = canvas.create_oval(posShip[0]-3, posShip[1]-65, posShip[0]+3, posShip[1]-40, fill="red")
		bulletStart = 1
		window.after(10, shoot_after)


# Moves the bullet after the spaceship shoots
def shoot_after():
	
	global bulletStart
	global isPaused
	global isPaused2

	posBullet = canvas.coords(bullet)
	
	if (bullet in canvas.find_all()):
		if (bulletStart == 1 and posBullet[1] < 1):
			canvas.delete(bullet)
			bulletStart = 0
			return 0

	if (isPaused == False and isPaused2 == False):
		canvas.move(bullet, 0, -2)
		#window.update()
	window.after(10, shoot_after)


# Asks for the username
def askUsername():
	
	global askUser
	global askUserWindow
	global btnGetWindow
	global askUserText

	canvas.delete(gameTitle)
	canvas.delete(btnNewGameWindow)
	canvas.delete(btnLoadWindow)
	canvas.delete(btnLeaderboardWindow)
	canvas.delete(btnHTPWindow)
	canvas.delete(btnControlsWindow)
	canvas.delete(btnQuit1Window)

	askUserText = canvas.create_text(640, 280, fill="white", font="Arial 30 bold", text="CHOOSE YOUR USERNAME")

	askUser = Entry(canvas, font="Arial 20")
	askUserWindow = canvas.create_window(640, 360, window=askUser)

	btnGet = Button(canvas, text="OK", command=lambda:getUsername(), background="darkgrey", font="Arial 20")
	btnGet.configure(activebackground = "grey", highlightthickness=0)
	btnGetWindow = canvas.create_window(640, 430, window=btnGet) 


# Puts username in a variable
def getUsername():
	
	global username
	global newOrLoad

	username = askUser.get()

	canvas.delete(askUserText)
	canvas.delete(askUserWindow)
	canvas.delete(btnGetWindow)

	newOrLoad = 0

	main()


# Goes back to menu
def backToMenuGeneral():
	
	canvas.delete("all")

	playGame()


# Goes back to main menu when button is pressed
def backToMenu():
	
	global bulletStart
	global callShoot

	canvas.delete(backgroundCreate)
	canvas.delete(endMessage)
	canvas.delete(btnMenuWindow)
	canvas.delete(btnWindowQuit)

	if (bulletStart == 1):
		canvas.delete(bullet)
		bulletStart = 0

	playGame()


# Saves the game after pressing key
def save(event):
	
	with open("savefile.txt", "w") as saveFile:
		saveFile.write(str(scoreNum) + "\n" + str(lvlNum) + "\n" + str(livesNum) + "\n" + str(galaxyNum) + "\n" + username)


# Loads the game
def load():
	
	global newOrLoad
	global newScoreNum
	global newLvlNum
	global newLivesNum
	global newGalaxyNum
	global sameUsername

	with open("savefile.txt") as loadVar:
		loadVarList = loadVar.read().split()

		newScoreNum = loadVarList[0]
		newLvlNum = loadVarList[1]
		newLivesNum = loadVarList[2]
		newGalaxyNum = loadVarList[3]
		sameUsername = loadVarList[4]

	newOrLoad = 1

	main()


# Creates the leaderboard
def leaderboard():

	canvas.delete(gameTitle)
	canvas.delete(btnNewGameWindow)
	canvas.delete(btnLoadWindow)
	canvas.delete(btnLeaderboardWindow)
	canvas.delete(btnHTPWindow)
	canvas.delete(btnControlsWindow)
	canvas.delete(btnQuit1Window)

	leaderboardTitle = canvas.create_text(640, 100, fill="darkblue", font="Arial 40 bold", text="LEADERBOARD")

	if (len(scoreList) == 0):
		pass
	elif (len(scoreList) == 1):
		player1 = canvas.create_text(640, 200, fill="white", font="Arial 30 bold", text=nameList[0] + " - " + scoreList[0])
	elif (len(scoreList) == 2):
		player1 = canvas.create_text(640, 200, fill="white", font="Arial 30 bold", text=nameList[0] + " - " + scoreList[0])
		player2 = canvas.create_text(640, 250, fill="white", font="Arial 30 bold", text=nameList[1] + " - " + scoreList[1])
	elif (len(scoreList) == 3):
		player1 = canvas.create_text(640, 200, fill="white", font="Arial 30 bold", text=nameList[0] + " - " + scoreList[0])
		player2 = canvas.create_text(640, 250, fill="white", font="Arial 30 bold", text=nameList[1] + " - " + scoreList[1])
		player3 = canvas.create_text(640, 300, fill="white", font="Arial 30 bold", text=nameList[2] + " - " + scoreList[2])
	elif (len(scoreList) == 4):
		player1 = canvas.create_text(640, 200, fill="white", font="Arial 30 bold", text=nameList[0] + " - " + scoreList[0])
		player2 = canvas.create_text(640, 250, fill="white", font="Arial 30 bold", text=nameList[1] + " - " + scoreList[1])
		player3 = canvas.create_text(640, 300, fill="white", font="Arial 30 bold", text=nameList[2] + " - " + scoreList[2])
		player4 = canvas.create_text(640, 350, fill="white", font="Arial 30 bold", text=nameList[3] + " - " + scoreList[3])
	else:
		player1 = canvas.create_text(640, 200, fill="white", font="Arial 30 bold", text=nameList[0] + " - " + scoreList[0])
		player2 = canvas.create_text(640, 250, fill="white", font="Arial 30 bold", text=nameList[1] + " - " + scoreList[1])
		player3 = canvas.create_text(640, 300, fill="white", font="Arial 30 bold", text=nameList[2] + " - " + scoreList[2])
		player4 = canvas.create_text(640, 350, fill="white", font="Arial 30 bold", text=nameList[3] + " - " + scoreList[3])
		player5 = canvas.create_text(640, 400, fill="white", font="Arial 30 bold", text=nameList[4] + " - " + scoreList[4])

	# Back to menu button
	btnBack = Button(canvas, text="BACK TO MENU", command=lambda:backToMenuGeneral(), background="darkgrey", font="Arial 20")
	btnBack.configure(activebackground = "grey", highlightthickness=0)
	btnBackWindow = canvas.create_window(640, 500, window=btnBack)


# Gives intructions to play
def howToPlay():

	canvas.delete(gameTitle)
	canvas.delete(btnNewGameWindow)
	canvas.delete(btnLoadWindow)
	canvas.delete(btnLeaderboardWindow)
	canvas.delete(btnHTPWindow)
	canvas.delete(btnControlsWindow)
	canvas.delete(btnQuit1Window)

	instruction1 = canvas.create_text(640, 120, fill="white", font="Arial 22 bold", text="YOU ARE THE LAST PILOT ALIVE")
	instruction2 = canvas.create_text(640, 180, fill="white", font="Arial 22 bold", text="MAKE YOUR WAY THROUGH THE ASTEROIDS WITHOUT CRASHING YOUR SPACESHIP")
	instruction3 = canvas.create_text(640, 240, fill="white", font="Arial 22 bold", text="THE SPACESHIP CAN BE HIT BY TWO ASTEROIDS BEFORE IT IS DESTROYED")
	instruction4 = canvas.create_text(640, 300, fill="white", font="Arial 22 bold", text="DESTROY AS MANY ASTEROIDS AS YOU CAN USING YOUR FIRE WEAPON")
	instruction5 = canvas.create_text(640, 360, fill="white", font="Arial 22 bold", text="REACH THE LAST GALAXY ALIVE AND SAFE")
	instruction6 = canvas.create_text(640, 420, fill="white", font="Arial 22 bold", text="BE BRAVE SOLDIER!")


	btnBack = Button(canvas, text="BACK TO MENU", command=lambda:backToMenuGeneral(), background="darkgrey", font="Arial 20")
	btnBack.configure(activebackground = "grey", highlightthickness=0)
	btnBackWindow = canvas.create_window(640, 600, window=btnBack)


# Show controls
def controls():
	
	canvas.delete(gameTitle)
	canvas.delete(btnNewGameWindow)
	canvas.delete(btnLoadWindow)
	canvas.delete(btnLeaderboardWindow)
	canvas.delete(btnHTPWindow)
	canvas.delete(btnControlsWindow)
	canvas.delete(btnQuit1Window)

	key1 = canvas.create_text(500, 100, fill="white", font="Arial 22 bold", anchor="nw", text="MOVE UP: UP KEY")
	key2 = canvas.create_text(500, 150, fill="white", font="Arial 22 bold", anchor="nw", text="MOVE DOWN: DOWN KEY")
	key3 = canvas.create_text(500, 200, fill="white", font="Arial 22 bold", anchor="nw", text="MOVE LEFT: LEFT KEY")
	key4 = canvas.create_text(500, 250, fill="white", font="Arial 22 bold", anchor="nw", text="MOVE RIGHT: RIGHT KEY")
	key5 = canvas.create_text(500, 300, fill="white", font="Arial 22 bold", anchor="nw", text="SHOOT: SPACE")
	key6 = canvas.create_text(500, 350, fill="white", font="Arial 22 bold", anchor="nw", text="SAVE: S")
	key7 = canvas.create_text(500, 400, fill="white", font="Arial 22 bold", anchor="nw", text="PAUSE: P")
	key8 = canvas.create_text(500, 450, fill="white", font="Arial 22 bold", anchor="nw", text="'BOSS KEY': B")
	key9 = canvas.create_text(500, 500, fill="white", font="Arial 22 bold", anchor="nw", text="CHEAT CODE: CONTROL+SHIFT+C")



	btnBack = Button(canvas, text="BACK TO MENU", command=lambda:backToMenuGeneral(), background="darkgrey", font="Arial 20")
	btnBack.configure(activebackground = "grey", highlightthickness=0)
	btnBackWindow = canvas.create_window(640, 600, window=btnBack)


# Window which appear after you reach lvl 10 and you finish the game
def win():

	canvas.unbind("<Left>")
	canvas.unbind("<Right>")
	canvas.unbind("<Up>")
	canvas.unbind("<Down>")
	canvas.unbind("<space>")

	canvas.delete("all")

	background()

	winText = canvas.create_text(640, 260, fill="darkblue", font="Arial 50 bold", text="YOU FINISHED YOUR JOURNEY")

	btnMenuWin = Button(canvas, text="MAIN MENU", command=lambda:backToMenuGeneral(), background="darkgrey", font="Arial 30")
	btnMenuWin.configure(activebackground = "grey", highlightthickness=0)
	btnMenuWinWindow = canvas.create_window(640, 420, window=btnMenuWin)

	btnQuitWin = Button(canvas, text="QUIT", command=lambda:quit(), background="darkgrey", font="Arial 30")
	btnQuitWin.configure(activebackground = "grey", highlightthickness=0)
	btnWindowQuitWin = canvas.create_window(640, 500, window=btnQuitWin)


# Quit the game
def quit():

	window.quit()


# Generates a number of asteroids depending of the current level and checks the other actions
def asteroidRain():

	global asteroids
	global endMessage
	global btnMenuWindow
	global btnWindowQuit
	global backgroundImg
	global backgroundCreate
	global bulletStart
	global scoreNum
	global lvlNum
	global okok
	global ok
	global ok2
	global lvlNum2
	global nr
	global lvlNumRaise
	global galaxyNum
	global livesNum
	global scoreList
	global nameList


	if not isPaused and not isPaused2:
		nr = 0

		if (okok == 0):
			lvlNum2 = lvlNum
			for i in range(lvlNum):
				xObs = rand(1, 1255)
				yObs = 0
				xy = (xObs, yObs, xObs+25, yObs+25)

				asteroids.append(canvas.create_rectangle(xy, fill="grey"))

			if (okok == 0):
				okok = 1

		ok = 0
		ok2 = 0
		
		for i in range(lvlNum):

			if (asteroids[i] not in canvas.find_all()):
				continue

			pos = canvas.coords(asteroids[i])
			posShipp = canvas.coords(spaceShip)

			if (bulletStart == 1):
				posBullet = canvas.coords(bullet)

				if (pos[3] > posBullet[1] and posBullet[0] + 3 > pos[0] and posBullet[0] + 3 < pos[0] + 25):
					canvas.delete(bullet)
					bulletStart = 0
					canvas.delete(asteroids[i])
					scoreNum = scoreNum + 10
					canvas.itemconfig(score, text="SCORE: " + str(scoreNum))
					if (scoreNum % 100 == 0):
						lvlNumRaise = True
						nr += 1
						galaxyNum += 1
						canvas.itemconfig(level, text="LEVEL: " + str(lvlNum + nr))
						canvas.itemconfig(galaxy, text=str(galaxyList[galaxyNum]))

					lvlNum2 -= 1
					if (lvlNum2 == 0):
						ok = 1
					continue
			
			if (pos[3] >= posShipp[1] - 50 and pos[3] <= posShipp[1] - 25 and pos[2] > posShipp[0] - 12 and pos[2] - 25 < posShipp[0] + 12):	
				canvas.delete(asteroids[i])
				livesNum -= 1
				canvas.itemconfig(lives, text="LIVES: " + str(livesNum))
				lvlNum2 -= 1
				if (lvlNum2 == 0):
					ok = 1
				continue

			if (pos[3] >= posShipp[1] - 20 and pos[3] <= posShipp[1] + 15 and pos[2] > posShipp[0] - 35 and pos[2] - 25 < posShipp[0] + 35):	
				canvas.delete(asteroids[i])
				livesNum -= 1
				canvas.itemconfig(lives, text="LIVES: " + str(livesNum))
				lvlNum2 -= 1
				if (lvlNum2 == 0):
					ok = 1
				continue

			if (pos[3] >= posShipp[1] + 15 and pos[3] <= posShipp[1] + 50 and pos[2] > posShipp[0] - 50 and pos[2] - 25 < posShipp[0] + 53):	
				canvas.delete(asteroids[i])
				livesNum -= 1
				canvas.itemconfig(lives, text="LIVES: " + str(livesNum))
				lvlNum2 -= 1
				if (lvlNum2 == 0):
					ok = 1
				continue

			if (pos[3] > 720):
				canvas.delete(asteroids[i])
				ok = 1

			if (livesNum <= 0):
				ok = 1
				ok2 = 1

			canvas.move(asteroids[i], 0, 2)
		
		if (scoreNum >= 990):
			win()


		if (ok == 1):
			asteroids.clear()

			if (lvlNumRaise == True):
				lvlNum += 1
				lvlNumRaise = False

			lvlNum2 = lvlNum
			for i in range(lvlNum):
				xObs = rand(1, 1255)
				yObs = 0
				xy = (xObs, yObs, xObs+25, yObs+25)

				asteroids.append(canvas.create_rectangle(xy, fill="grey"))

		if (ok2 == 1):

			canvas.unbind("<Left>")
			canvas.unbind("<Right>")
			canvas.unbind("<Up>")
			canvas.unbind("<Down>")
			canvas.unbind("<space>")

			scoreList.append(scoreNum)
			nameList.append(username)

			for item in range(len(scoreList)-1):
				for item2 in range(len(scoreList) - 1 - item):
					if (int(scoreList[item2]) < int(scoreList[item2+1])):
						scoreList[item], scoreList[item2] = scoreList[item2], scoreList[item]
						nameList[item], nameList[item2] = nameList[item2], nameList[item]

			with open("leaderboardscore.txt", "w") as scoreFile:
				for i in range(len(scoreList)):
					scoreFile.write(str(scoreList[i]) + "\n")

			with open("leaderboardnames.txt", "w") as nameFile:
				for j in range(len(nameList)):
					nameFile.write(str(nameList[j]) + "\n")

			canvas.delete("all")
			
			backgroundImg = PhotoImage(file="smokebackground.png")

			backgroundCreate = canvas.create_image(0, 0, anchor="nw", image=backgroundImg)

			endMessage = canvas.create_text(640, 260, fill="darkred", font="Arial 70 bold", text="YOU DIED")

			btnMenu = Button(canvas, text="MAIN MENU", command=lambda:backToMenu(), background="darkgrey", font="Arial 30")
			btnMenu.configure(activebackground = "grey", highlightthickness=0)
			btnMenuWindow = canvas.create_window(640, 400, window=btnMenu)

			btnQuit = Button(canvas, text="QUIT", command=lambda:quit(), background="darkgrey", font="Arial 30")
			btnQuit.configure(activebackground = "grey", highlightthickness=0)
			btnWindowQuit = canvas.create_window(640, 500, window=btnQuit)

		else:
			if (scoreNum < 990):
				window.after(10, asteroidRain)

	else:
		window.after(10, asteroidRain)


# Main function
def main():

	canvas.delete(gameTitle)
	canvas.delete(btnNewGameWindow)
	canvas.delete(btnLoadWindow)
	canvas.delete(btnLeaderboardWindow)
	canvas.delete(btnHTPWindow)
	canvas.delete(btnControlsWindow)
	canvas.delete(btnQuit1Window)

	global scoreNum
	global score
	global lvlNum
	global level
	global galaxy
	global okok
	global ok
	global asteroids
	global shipImg
	global spaceShip
	global lvlNumRaise
	global galaxyList
	global galaxyNum
	global isPaused
	global isPaused2
	global livesNum
	global lives
	global username

	isPaused = False
	isPaused2 = False

	# Names of the galaxies
	galaxyList = ["OUTLAND", "ASGARD", "NEVERLAND", "HOGSMEADE", "RIVENDELL", "PANDORA", "PEGASUS", "SKRULL", "XANDAR", "GOLYAT'S NEST"]
	asteroids = []

	# Creating the space ship which will be controled by the player
	shipImg = PhotoImage(file="finalspaceship.png")
	spaceShip = canvas.create_image(640, 600, image=shipImg)

	if (newOrLoad == 0):
		scoreNum = 0
		lvlNum = 1
		livesNum = 3
		galaxyNum = 0
		galaxy = canvas.create_text(640, 45, fill="darkblue", font="Arial 30 bold", text="OUTLAND")

	elif (newOrLoad == 1):
		scoreNum = int(newScoreNum)
		lvlNum = int(newLvlNum)
		livesNum = int(newLivesNum)
		galaxyNum = int(newGalaxyNum)
		username = sameUsername
		galaxy = canvas.create_text(640, 45, fill="darkblue", font="Arial 30 bold", text=galaxyList[galaxyNum])


	# Text on the screen
	score = canvas.create_text(30, 20, fill="darkblue", font="Arial 22 bold", anchor="nw", text="SCORE: " + str(scoreNum))

	level = canvas.create_text(1200, 35, fill="darkblue", font="Arial 22 bold", text="LEVEL " + str(lvlNum))

	lives = canvas.create_text(1200, 65, fill="darkblue", font="Arial 22 bold", text="LIVES: " + str(livesNum))

	# Control keys
	canvas.bind("<Left>", moveLeft)
	canvas.bind("<Right>", moveRight)
	canvas.bind("<Up>", moveUp)
	canvas.bind("<Down>", moveDown)
	canvas.bind("<space>", shoot)
	canvas.bind("<p>", pause)
	canvas.bind("<b>", bossKey)
	canvas.bind("<Control-Shift-C>", cheatCode)
	canvas.bind("<s>", save)

	canvas.focus_set()

	okok = 0
	ok = 0
	lvlNumRaise = False

	asteroidRain()


# Displays the main menu
def playGame():

	global gameTitle
	global btnNewGameWindow
	global btnLoadWindow
	global btnLeaderboardWindow
	global btnHTPWindow
	global btnControlsWindow
	global btnQuit1Window
	global scoreList
	global nameList

	with open("leaderboardscore.txt") as ldrbFile:
		scoreList = ldrbFile.read().split()

	with open("leaderboardnames.txt") as ldrbFile2:
		nameList = ldrbFile2.read().split()

	background()

	gameTitle = canvas.create_text(640, 200, fill="darkblue", font="Arial 50 bold", text="GALACTIC WARS")

	# New game button
	btnNewGame = Button(canvas, text="NEW GAME", command=lambda:askUsername(), background="darkgrey", font="Arial 20")
	btnNewGame.configure(activebackground="grey", highlightthickness=0)
	btnNewGameWindow = canvas.create_window(640, 350, window=btnNewGame)

	# Load button
	btnLoad = Button(canvas, text="LOAD", command=lambda:load(), background="darkgrey", font="Arial 20")
	btnLoad.configure(activebackground="grey", highlightthickness=0)
	btnLoadWindow = canvas.create_window(640, 400, window=btnLoad)

	# Leaderboard button
	btnLeaderboard = Button(canvas, text="LEADERBOARD", command=lambda:leaderboard(), background="darkgrey", font="Arial 20")
	btnLeaderboard.configure(activebackground="grey", highlightthickness=0)
	btnLeaderboardWindow = canvas.create_window(640, 450, window=btnLeaderboard)

	# How to play button
	btnHTP = Button(canvas, text="HOW TO PLAY", command=lambda:howToPlay(), background="darkgrey", font="Arial 20")
	btnHTP.configure(activebackground="grey", highlightthickness=0)
	btnHTPWindow = canvas.create_window(640, 500, window=btnHTP)

	# Controls button
	btnControls = Button(canvas, text="CONTROLS", command=lambda:controls(), background="darkgrey", font="Arial 20")
	btnControls.configure(activebackground="grey", highlightthickness=0)
	btnControlsWindow = canvas.create_window(640, 550, window=btnControls)

	# Quit button
	btnQuit1 = Button(canvas, text="QUIT GAME", command=lambda:quit(), background="darkgrey", font="Arial 20")
	btnQuit1.configure(activebackground="grey", highlightthickness=0)
	btnQuit1Window = canvas.create_window(640, 600, window=btnQuit1)


# --> PROGRAM START

playGame()

window.mainloop()


#                                                       --- END ---
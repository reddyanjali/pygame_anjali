# Game - REAL FIGHTERS
# AUTHOR - ANJALI DEEPAK REDDY
# LANG - PYTHON 3.7(PyGame)

# import the modules
import pygame,random,sys
from pygame.locals import *

# set the window size
WINDOWWIDTH = 1400
WINDOWHEIGHT =800

# set the colors
text_color = (255, 255, 255)
bg_color = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
yellow = (255,255,0)
green = (0, 128,0)

# set the constant variables
FPS = 30
VIRUSMINSPEED = 1
VIRUSMAXSPEED = 4
ADDNEWVIRUSRATE = 10
ADDNEWVIRUSRATE1 = 20
ADDSUPERVIRUSRATE = 40
PLAYERMOVERATE = 5
VIRUSSIZE = 50
MEDICINESPEED = 7
NOSUPERMEDICINE = 5
POWERUPRATE = 1000
POWERUPSIZE = 50
POWERUPSPEED = 4
ADDNEWLIFERATE = 3000
LIFESIZE = 50
PAUSE = False

def terminate():
	pygame.quit()
	sys.exit()
	
def waitForPlayerToPressKey():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					terminate()
				return

# function to draw text on the screen
def drawText(text,font,surface, x, y):
	textobj= font.render(text, 1, text_color)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)

# set up pygame, the window and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('REAL FIGHTERS')
pygame.mouse.set_visible(False)

# set up fonts
font = pygame.font.SysFont(None,48)

#  End Music when you lose
gameOverSound = pygame.mixer.Sound('endmusic.wav')
# Game music
pygame.mixer.music.load('startingmusic.mp3')

doctor1 = pygame.image.load('doctor.png')
doctor = pygame.transform.scale(doctor1, (60,60))
playerRect = doctor.get_rect()
virusImage = pygame.image.load('virus1.png')
virusImage1 = pygame.image.load('virus3.png')
killerVirusImage = pygame.image.load('virus.png')
stayHomeImage = pygame.image.load('stayHome.png')
sanitizerImage = pygame.image.load('sanitizer.png')
superMedicineImage = pygame.image.load('superMedicine.png')

# background image
background = pygame.image.load("bg.jpg")
backgroundImage = pygame.transform.scale(background,(WINDOWWIDTH,WINDOWHEIGHT))
backgroundRect = backgroundImage.get_rect()

# Front screen
drawText('Real Fighters',font, windowSurface, (WINDOWWIDTH / 3)+100, (WINDOWHEIGHT / 3))
drawText('Let us Start!!!', font, windowSurface, (WINDOWWIDTH / 3) +90, (WINDOWHEIGHT / 3) + 50)
drawText('Press any keyyyyy!', font, windowSurface, (WINDOWWIDTH / 3) + 60, (WINDOWHEIGHT / 3) + 100)
pygame.display.update()
waitForPlayerToPressKey()


highScore = 0
while True:
	# set up the start of the game
	virus=[]
	virus1=[]
	killerVirus = []
	DocsMedicines = []
	superMedicines = []
	virusMedicines = []
	superPower = []
	lifes = []
	score = 0
	levelUpScore = 1000
	level = 0
	LIFES = 3
	playerRect.topleft = (WINDOWWIDTH/2, WINDOWHEIGHT - 50)
	moveLeft = moveRight = moveUp = moveDown = False
	virusAddCounter = 0
	virusAddCounter1 = 0
	superVirusAddCounter = 0
	superMedicineCounter = 0
	newLifeCounter = 0
	pygame.mixer.music.play(-1,0.0)
	
	windowSurface.blit(backgroundImage, backgroundRect)
	pygame.display.update()
	
	while True:
		
		# to pause the game 
		while PAUSE == True: 
			for event in pygame.event.get():
				if event.type == KEYUP:
					if event.key == ord('p'):
						PAUSE = False
		
		# to quit the game 
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
				
			if event.type == KEYDOWN:
				if event.key == K_LEFT or event.key == ord('a'):
					moveRight = False
					moveLeft = True
				if event.key == K_RIGHT or event.key == ord('d'):
					moveLeft = False
					moveRight = True
				if event.key == K_UP or event.key == ord('w'):
					moveDown = False
					moveUp = True
				if event.key == K_DOWN or event.key == ord('s'):
					moveUp = False
					moveDown = True
				if event.key == K_SPACE:
					# create new medicines if space is pressed
					newDoctorMedicine = pygame.Rect(playerRect.centerx-20, playerRect.centery+5, 3, 6)
					DocsMedicines.append(newDoctorMedicine)
					newDoctorMedicine2 = pygame.Rect(playerRect.centerx+15, playerRect.centery+5, 3, 6)
					DocsMedicines.append(newDoctorMedicine2)
				if event.key == K_LSHIFT and NOSUPERMEDICINE > 0:
					# use the super medicine when left shift is pressed
					newSuperMedicine = {'rect': pygame.Rect(playerRect.centerx-12, playerRect.centery-50, 20, 50), 'surface':pygame.transform.scale(superMedicineImage, (20,50))}
					superMedicines.append(newSuperMedicine)
					NOSUPERMEDICINE -= 1
			
			if event.type == KEYUP:
				if event.key == K_ESCAPE: 
					terminate()
				if event.key == ord('p'): 
					PAUSE = True
					
				if event.key == K_LEFT or event.key == ord('a'):
					moveLeft = False
				if event.key == K_RIGHT or event.key == ord('d'):
					moveRight = False
				if event.key == K_UP or event.key == ord('w'):
					moveUp = False
				if event.key == K_DOWN or event.key == ord('s'):
					moveDown = False
					
			# move doctor as mouse moves
			if event.type == MOUSEMOTION:
				playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)
		
		# add virus count at the top of the screen
		virusAddCounter += 1
		if virusAddCounter == ADDNEWVIRUSRATE:
			virusAddCounter = 0
			newVirus = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - VIRUSSIZE),0 - VIRUSSIZE, VIRUSSIZE, VIRUSSIZE), 'speed': random.randint(VIRUSMINSPEED,VIRUSMAXSPEED),'surface': pygame.transform.scale(virusImage, (VIRUSSIZE, VIRUSSIZE))}
			virus.append(newVirus)
		
		# add different type virus 
		virusAddCounter1 += 1
		if virusAddCounter1 == ADDNEWVIRUSRATE1:
			virusAddCounter1 = 0
			newVirus1 = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - VIRUSSIZE), 0 - VIRUSSIZE, VIRUSSIZE, VIRUSSIZE), 'speed': random.randint(VIRUSMINSPEED, VIRUSMAXSPEED), 'surface': pygame.transform.scale(virusImage1,(VIRUSSIZE, VIRUSSIZE))}
			virus1.append(newVirus1)
		
		# add super virus 
		superVirusAddCounter += 1
		if superVirusAddCounter == ADDSUPERVIRUSRATE:
			superVirusAddCounter = 0
			newSuperDoctor = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - VIRUSSIZE), 0 - VIRUSSIZE, VIRUSSIZE, VIRUSSIZE), 'speed': random.randint(VIRUSMINSPEED, VIRUSMAXSPEED), 'surface': pygame.transform.scale(killerVirusImage, (VIRUSSIZE, VIRUSSIZE)), 'hit': 3}
			killerVirus.append(newSuperDoctor)
		
		# add powerups to increase no of super medicines
		superMedicineCounter += 1
		if superMedicineCounter == POWERUPRATE:
			superMedicineCounter = 0
			newPower = {'rect': pygame.Rect(random.randint(0,WINDOWWIDTH - POWERUPSIZE), 0 - POWERUPSIZE, POWERUPSIZE, POWERUPSIZE), 'surface': pygame.transform.scale(sanitizerImage, (POWERUPSIZE, POWERUPSIZE))}
			superPower.append(newPower)
		
		# add new powerup to increase the no of lifes
		newLifeCounter += 1
		if newLifeCounter == ADDNEWLIFERATE:
			newLifeCounter = 0
			newLife = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - LIFESIZE), 0 - LIFESIZE, LIFESIZE, LIFESIZE), 'surface': pygame.transform.scale(stayHomeImage, (LIFESIZE, LIFESIZE))}
			lifes.append(newLife)
		
		# move the doctor around
		if moveLeft and playerRect.left > 0:
			playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
		if moveRight and playerRect.right < WINDOWWIDTH:
			playerRect.move_ip(PLAYERMOVERATE, 0)
		if moveUp and playerRect.top > 0:
			playerRect.move_ip(0, -1 * PLAYERMOVERATE)
		if moveDown and playerRect.bottom < WINDOWHEIGHT:
			playerRect.move_ip(0, PLAYERMOVERATE)
		
		# move the mouse cursor to match the player
		pygame.mouse.set_pos(playerRect.centerx,playerRect.centery)
		
		# move the virus down
		for a in virus:
			a['rect'].move_ip(0,a['speed'])
		
		for a1 in virus1:
			a1['rect'].move_ip(0, a1['speed'])
		
		for kv in killerVirus:
			kv['rect'].move_ip(0, kv['speed'])
		
		# move the powerups down
		for p in superPower[:]:
			p['rect'].move_ip(0, POWERUPSPEED)
		
		for l in lifes[:]:
			l['rect'].move_ip(0, POWERUPSPEED)
		
		# move the medicines up
		for b in DocsMedicines:
			b.move_ip(0,-MEDICINESPEED)
		
		for s in superMedicines:
			s['rect'].move_ip(0,-MEDICINESPEED)
		
		# delete medicines that have moved past the top
		for b in DocsMedicines[:]:
			if b.top < 0:
				DocsMedicines.remove(b)
		
		for s in superMedicines[:]:
			if s['rect'].top <0:
				superMedicines.remove(s)
		
		# delete virus that have fallen past the bottom
		for a in virus[:]:
			if a['rect'].top > WINDOWHEIGHT:
				virus.remove(a)
		
		for a1 in virus1[:]:
			if a1['rect'].top > WINDOWHEIGHT:
				virus1.remove(a1)
		
		for kv in killerVirus[:]:
			if kv['rect'].top > WINDOWHEIGHT:
				killerVirus.remove(kv)
		
		# delete powerups that have fallen past the bottom 
		for l in lifes[:]:
			if l['rect'].top > WINDOWHEIGHT:
				lifes.remove(l)
		
		for p in superPower[:]:
			if p['rect'].top > WINDOWHEIGHT:
				superPower.remove(p)
		
		# draw the game world on the window
		windowSurface.blit(backgroundImage, backgroundRect)
		pygame.display.update()

		
		# draw the score, high score, Lifes and super medicines
		drawText('LivesSaved: %s' %(score), font, windowSurface, 10, 0)
		drawText('MaxLivesSaved: %s' %(highScore),font, windowSurface, 10,30)
		drawText('Divine Medicine: %s' %(NOSUPERMEDICINE),font, windowSurface, WINDOWWIDTH - 300, 30)
		drawText('DocLives: %s' %(LIFES), font, windowSurface, WINDOWWIDTH - 260, 0)
		
		# draw the doctor
		windowSurface.blit(doctor, playerRect)
		pygame.display.update()
		
		# draw the virus
		for a in virus:
			windowSurface.blit(a['surface'], a['rect'])
		
		for a1 in virus1:
			windowSurface.blit(a1['surface'],a1['rect'])
		
		for kv in killerVirus:
			windowSurface.blit(kv['surface'],kv['rect'])
		
		# draw the powerups
		for l in lifes:
			windowSurface.blit(l['surface'],l['rect'])
		
		# draw the medicines being injected by the doctor
        
		for b in DocsMedicines:
			pygame.draw.rect(windowSurface, blue, b, 0)
		for s in superMedicines:
			windowSurface.blit(s['surface'], s['rect'])
		
		# draw the powerups
		for p in superPower:
			windowSurface.blit(p['surface'], p['rect'])
		
		# check if medicines have hit the virus	
		for b in DocsMedicines:
			for a in virus:
				if b.colliderect(a['rect']):
					score += 15 
					virus.remove(a)
					DocsMedicines.remove(b)
					break
		
		for b in DocsMedicines:
			for a1 in virus1:
				if b.colliderect(a1['rect']):
					score += 20
					virus1.remove(a1)
					DocsMedicines.remove(b)
					break
		
		for b in DocsMedicines:
			for kv in killerVirus:
				if b.colliderect(kv['rect']):
					kv['hit'] -= 1
					# check medicines have hit the super virus 3 times
					if kv['hit'] > 0:
						DocsMedicines.remove(b)
						break
					else:
						score += 30 
						killerVirus.remove(kv)
						DocsMedicines.remove(b)
						break
		
		# if super medicines hit the virus, increase more score
		for s in superMedicines:
			for a in virus:
				if s['rect'].colliderect(a['rect']):
					score += 30
					virus.remove(a)
		
		for s in superMedicines:
			for a1 in virus1:
				if s['rect'].colliderect(a1['rect']):
					score += 50
					virus1.remove(a1)
		
		for s in superMedicines:
			for kv in killerVirus:
				if s['rect'].colliderect(kv['rect']):
					score += 60
					killerVirus.remove(kv)
		
		# if powerup is caught by doctor
		for p in superPower:
			if playerRect.colliderect(p['rect']):
				if NOSUPERMEDICINE < 9:
					NOSUPERMEDICINE += 1
				superPower.remove(p)
		
		for l in lifes:
			if playerRect.colliderect(l['rect']):
				if LIFES < 3:
					LIFES += 1
				lifes.remove(l)
		
		# increase the difficulty if game proceeds
		if score >= levelUpScore:
			levelUpScore += 1000
			level += 1
			VIRUSMINSPEED += 1
			VIRUSMAXSPEED += 1
		
		# update the window
		pygame.display.update()
		
		# if virus hit the doctor, decrease lifes
		for a in virus:
			if playerRect.colliderect(a['rect']):
				virus.remove(a)
				LIFES -= 1
		
		for a1 in virus1:
			if playerRect.colliderect(a1['rect']):
				virus1.remove(a1)
				LIFES -= 1
		
		for kv in killerVirus:
			if playerRect.colliderect(kv['rect']):
				LIFES -= 1
				killerVirus.remove(kv)

		# if lifes are zero, end the game
		if LIFES <= 0:
			if score > highScore:
				# set up high score
				highScore= score
			NOSUPERMEDICINE = 5
			break
		
		mainClock.tick(FPS)
	
	# set the speed to the initial ones
	VIRUSMINSPEED = 1
	VIRUSMAXSPEED = 4
	
	# stop the game sound and play game over sound
	pygame.mixer.music.stop()
	gameOverSound.play()
	
	# show the 'Game Over' screen
	drawText('GAME OVER',font,windowSurface, (WINDOWWIDTH / 3),(WINDOWHEIGHT / 3))
	drawText('Wanna Play again? Press any key!',font,windowSurface, (WINDOWWIDTH / 3) -80, (WINDOWHEIGHT / 3) + 50)
	pygame.display.update()
	waitForPlayerToPressKey()
	
	# stop the game over sound
	gameOverSound.stop()

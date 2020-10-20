import pygame, sys, os, math, time
sys.dont_write_bytecode = True		# 导入模块时决定是否写入字节码
from piecelogic import *
from imagedefs import *
from sounddefs import *
pygame.init()

tilew, tileh = 45, 45		# 棋盘一格大小
height = tileh * 8
width = tilew * 8

sbarw = 40		# 状态栏宽度
size = [width+200, height+sbarw]

os.environ["SDL_VIDEO_CENTERED"] = "1"		# 居中显示
pygame.display.set_icon(iconimg)
pygame.display.set_caption("Chess")		# 设置标题

screen = pygame.display.set_mode(size)		# 屏幕

isWin = False		# 胜利标志
isKind = False		# 平局标志
selected = False		# 被选中的位置
up = False		# 兵升变状态为 True
pieces = []		# 当前棋盘上的棋子
lastmoves = []		# 每一步棋子的位置
wmoves, bmoves = [], []		# 记录双方移动轨迹（是否吃了，（移动前位置，后位置））
moves = [wmoves, bmoves]
eated = []		# 被吃棋子
playerIsWhite = True		# 该哪方走

class Piece():
	def __init__(self,name,color,startpos):
		global pieces
		self.name = name
		self.color = color
		self.pos = startpos
		self.image = pieceimages[color+name]
		self.hasMoved = 0		# 移动步数
		self.beingAttacked = False
		board[startpos[0]][startpos[1]] = self		# 放入棋盘
		pieces.append(self)		# 加入棋子列表

	def move(self,pos):
		global selected
		global moves
		global lastmoves
		isEated = contains(pos) == 1
		if playerIsWhite:
			moves[1].append((isEated, (self.pos, pos)))
		else:
			moves[0].append((isEated, (self.pos, pos)))
		lastmoves.append((pos))
		board[self.pos[0]][self.pos[1]] = EMPTY		# 移动后更新棋盘
		self.pos = pos
		board[self.pos[0]][self.pos[1]] = self
		self.hasMoved += 1

	def reMove(self,pos):		# 撤销
		if playerIsWhite:
			moves[1].remove(moves[1][len(moves[1])-1])
		else:
			moves[0].remove(moves[0][len(moves[0])-1])
		lastmoves.remove(lastmoves[len(lastmoves)-1])
		board[self.pos[0]][self.pos[1]] = EMPTY		# 移动后更新棋盘
		self.pos = pos
		board[self.pos[0]][self.pos[1]] = self
		self.hasMoved -= 1


	def select(self):		# 被选中
		global selected
		selected = self.pos

# 更新文本信息
def updateText():
	# 当前行走方，棋盘棋子数量，状态信息，开始游戏，悔棋，和棋，退出游戏
	global turnindic
	global piecesleft
	global message
	global restartSign
	global regretSign
	global kindSign
	global exitSign

	font = pygame.font.SysFont("monospace", 20)  # 设置字体
	turnindic = font.render("Turn: "+("white" if playerIsWhite else "black"), True, (139, 125, 107), (0, 0, 0, 0))
	piecesleft = font.render("Pieces: "+str(len(pieces)), True, (139, 125, 107), (0, 0, 0, 0))		# 内容，是否抗锯齿，字体颜色，背景颜色
	if isWin:
		message = font.render(("black" if playerIsWhite else "white") + " is Win !", True, (255, 228, 196), (0, 0, 0, 0))
	if isKind:
		message = font.render("kind !", True, (255, 228, 196), (0, 0, 0, 0))

	font = pygame.font.SysFont("monospace", 40)  # 设置字体
	restartSign = font.render("restart", True, (139, 125, 107), (0, 0, 0, 0))
	regretSign = font.render("regret", True, (139, 125, 107), (0, 0, 0, 0))
	kindSign = font.render("kind", True, (139, 125, 107), (0, 0, 0, 0))
	exitSign = font.render("exit", True, (139, 125, 107), (0, 0, 0, 0))
updateText()		# 赋值

def contains(pos):		# 返回某个位置是否包含棋子（如果该白棋子走，则黑棋为 2，反之）
	boardpos = board[pos[0]][pos[1]]
	if boardpos == 0:
		return 0		# 该位置不包含棋子
	if playerIsWhite == True:
		return 1 if boardpos.color == 'W' else 2
	else:
		return 1 if boardpos.color == 'B' else 2

# 移除被吃（升变）棋子，并判断是否胜利
def removeAndJudgeIsWin(pos, isUp):
	global playerIsWhite
	if (playerIsWhite and isUp) or (not playerIsWhite and not isUp):
		color = 'B'
	if (not playerIsWhite and isUp) or (playerIsWhite and not isUp):
		color = 'W'
	for piece in pieces:
		if piece.pos == pos and piece.color == color:
			pieces.remove(piece)
			eated.append(piece)
			if piece.name == 'King':
				win()

# 根据位置找到棋盘对应区域
def pixelpos(pos):
	return (pos[0] * tilew, pos[1] * tileh)
# 兵升变时候的棋盘对应区域
def uppixelpos(pos):
	return (pos[0] * tilew * 4, pos[1] * tileh * 4)

# 兵升变前
def upChangeBefore():
	global up
	# 兵升变状态
	up = True
	# 画出四个可变棋子
	if not playerIsWhite:
		screen.blit(pieceimages['WRookBig'], uppixelpos((0, 0)))
		screen.blit(pieceimages['WKnightBig'], uppixelpos((1, 0)))
		screen.blit(pieceimages['WQueenBig'], uppixelpos((0, 1)))
		screen.blit(pieceimages['WBishopBig'], uppixelpos((1, 1)))
	else:
		screen.blit(pieceimages['BRookBig'], uppixelpos((0, 0)))
		screen.blit(pieceimages['BKnightBig'], uppixelpos((1, 0)))
		screen.blit(pieceimages['BQueenBig'], uppixelpos((0, 1)))
		screen.blit(pieceimages['BBishopBig'], uppixelpos((1, 1)))
# 兵升变后
def upChangeAfter(curPos):
	global up
	global playerIsWhite
	global lastmoves

	color = 'W' if not playerIsWhite else 'B'
	lastpos = lastmoves[len(lastmoves)-1]
	if curPos == (0, 0):
		Piece('Rook',   color,lastpos)
	elif curPos == (1, 0):
		Piece('Knight',   color,lastpos)
	elif curPos == (0, 1):
		Piece('Queen',   color,lastpos)
	elif curPos == (1, 1):
		Piece('Bishop',   color,lastpos)

	removeAndJudgeIsWin(lastpos, True)		# 从 pieces 中删除掉原来的棋子
	up = False

# 画棋盘
def drawPieces():
	global selected
	global up
	for i in range(len(board)):		# 遍历画出棋盘
		row = board[i]
		for i2 in range(len(row)):
			piece = row[i2]

			# 兵升变
			if piece != 0 and piece.name == 'Pawn' and (piece.pos[1] == 0 or piece.pos[1] == 7):		# 兵升变
				upChangeBefore()

			if selected != False and up == False:		# 有棋子被选中
				# 可以从被选中的位置移动到当前遍历的位置，当前位置未被选中，当前位置没有棋子或者有对方棋子
				if pieceCanMove(board[selected[0]][selected[1]], (i, i2), False) and selected != (i, i2) and contains((i, i2)) != 1:
					screen.blit(highlightimg, pixelpos((i, i2)))

					(mouseX, mouseY) = pygame.mouse.get_pos()		# 获取鼠标当前位置
					curRow = int(math.ceil(mouseX/tilew) - 1)		# 取整，得到当前棋盘上的位置（0~7）
					curCol = int(math.ceil(mouseY/tileh) - 1)
					if (curRow, curCol) == (i, i2):		# 移动准备
						screen.blit(hhoverimg, pixelpos((i, i2)))
					if contains((i, i2)) == 2:		# 可进攻
						screen.blit(attackimg, pixelpos((i, i2)))
				else:
					pass
			if piece != EMPTY and up == False:		# 当前位置有棋子（初始化时已经将棋子放入棋盘）
				screen.blit(piece.image, (i*45, i2*45))		# 画出

# 判断受攻击的棋子
def getAttacks():
	for piece in pieces:
		piece.beingAttacked = False
		for piece2 in pieces:
			enemyname = "B" if piece.color == 'W' else "W"
			#														此时不能移动
			if piece2 != piece and piece2.color == enemyname and pieceCanMove(piece2, piece.pos, False):
				piece.beingAttacked = True

# 移动音效播放
def playMoveSound(flag):
	if flag == 1:
		move.play()
	elif flag == 2:
		eat.play()
	for piece in pieces:
		if piece.beingAttacked == True and piece.name == 'King':
			checkmate.play()

# 初始化所有棋子
def init():
	for i in range(0, 8):
		Piece('Pawn', 'W', (i, 6))
		Piece('Pawn', 'B', (i, 1))

	Piece('Rook', 'W', (0, 7))
	Piece('Rook', 'W', (7, 7))
	Piece('Knight', 'W', (1, 7))
	Piece('Knight', 'W', (6, 7))
	Piece('Bishop', 'W', (2, 7))
	Piece('Bishop', 'W', (5, 7))
	Piece('Queen', 'W', (3, 7))
	Piece('King', 'W', (4, 7))
	Piece('Rook', 'B', (0, 0))
	Piece('Rook', 'B', (7, 0))
	Piece('Knight', 'B', (1, 0))
	Piece('Knight', 'B', (6, 0))
	Piece('Bishop', 'B', (2, 0))
	Piece('Bishop', 'B', (5, 0))
	Piece('Queen', 'B', (3, 0))
	Piece('King', 'B', (4, 0))

# 重开
def restart():
	global isWin
	global isKind
	global selected
	for i in range(len(lastmoves)):
		regret()
	isWin = False  # 胜利标志
	isKind = False  # 平局标志
	selected = False  # 被选中的位置

# 悔棋
def regret():
	global playerIsWhite
	move = moves[0] if not playerIsWhite else moves[1]		# 白旗/黑棋悔棋
	if move != []:
		m = move[len(move)-1]		# 具体移动的哪一步
		print(m)
		board[m[1][1][0]][m[1][1][1]].reMove((m[1][0][0],m[1][0][1]))
		if m[0] == True:		# 吃了
			eatedPiece = eated[len(eated)-1]		# 被吃棋子
			board[m[1][1][0]][m[1][1][1]] = eatedPiece
			eated.remove(eatedPiece)		# 恢复了，从被吃列表删除
			pieces.append(eatedPiece)
		playerIsWhite = not playerIsWhite

# 和棋
def kind():
	global isKind
	isKind = True
	updateText()
	pygame.display.update()

# 胜利
def win():
	global isWin
	global playerIsWhite
	isWin = True
	updateText()
	pygame.display.update()

# 主函数
def main():
	global selected
	global playerIsWhite
	clock = pygame.time.Clock()  # 计时

	init()		# 初始化棋子

	tan=(100,155,177)
	darktan = (139, 125, 107)  # 棋盘两种颜色
	lighttan = (255, 228, 196)
	while True:
		clock.tick(30)		# 检测时间
		pygame.draw.rect(screen, darktan, [0, 0, width, height])
		for row in range(4):
			for col in range(4):
				pygame.draw.rect(screen, lighttan, [row * 90, col * 90, tilew, tileh])
				pygame.draw.rect(screen, lighttan, [row * 90 + tilew, col * 90 + tileh, tilew, tileh])
		for row in range(4):
			pygame.draw.line(screen, lighttan, (width, (row+1) * tileh * 2), (width + 200, (row+1) * tileh * 2), 200)
			pygame.draw.rect(screen, tan, [width, row * tileh * 2, 200, tileh * 2], 0)

		drawPieces()  # 画出棋盘

		screen.blit(turnindic, (0, height + 10))		# 放置文字
		screen.blit(piecesleft, (width - 140, height + 10))
		screen.blit(restartSign, (width + 15, 0 * tilew * 2 + 20))
		screen.blit(regretSign, (width + 15, 1 * tilew * 2 + 20))
		screen.blit(kindSign, (width + 15, 2 * tilew * 2 + 20))
		screen.blit(exitSign, (width + 15, 3 * tilew * 2 + 20))

		# 状态判断
		if isWin:
			win()
			screen.blit(message, (width + 20, height + 10))
		if isKind:
			screen.blit(message, (width + 20, height + 10))

		for event in pygame.event.get():  # 点击事件
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:  # 按下 ESC 键
					pygame.event.post(pygame.event.Event(pygame.QUIT))
				elif event.key == pygame.K_r:
					pass
			elif event.type == pygame.MOUSEBUTTONUP \
					and pygame.mouse.get_pos()[0] <= width and pygame.mouse.get_pos()[1] <= height:  # 因为 height 还包含状态栏
				if up == False:
					(mouseX, mouseY) = pygame.mouse.get_pos()
					curCol = int(math.ceil(mouseY / tileh) - 1)
					curRow = int(math.ceil(mouseX / tilew) - 1)

					if selected == False:
						if contains((curRow, curCol)) == 1:
							board[curRow][curCol].select()  # 棋盘该处棋子被选中
					else:  # 已经有棋子被选中
						if contains((curRow, curCol)) != 1:
							if pieceCanMove(board[selected[0]][selected[1]], (curRow, curCol), True):
								playerIsWhite = not playerIsWhite  # 该对方走
								flag = 1 if contains((curRow, curCol)) == 0 else 2  # 播放音效指示，1 移动，2 吃

								board[selected[0]][selected[1]].move((curRow, curCol))  # 移动棋子
								selected = False
								getAttacks()  # 判断正在受到进攻的棋子

								playMoveSound(flag)  # 播放音效
								lastpos = lastmoves[len(lastmoves) - 1]
								removeAndJudgeIsWin(lastpos, False)  # 更新当前棋盘，移除被吃棋子
								updateText()  # 更新状态
						else:
							board[curRow][curCol].select()  # 选中自己的其他棋子
				elif up == True:  # 兵升变状态
					(mouseX, mouseY) = pygame.mouse.get_pos()
					curCol = int(math.ceil(mouseY / tileh / 4) - 1)
					curRow = int(math.ceil(mouseX / tilew / 4) - 1)
					upChangeAfter((curRow, curCol))  # 兵变成对应的东西
			elif event.type == pygame.MOUSEBUTTONUP \
					and pygame.mouse.get_pos()[0] > width and pygame.mouse.get_pos()[1] <= height:		# 点击菜单栏
				(mouseX, mouseY) = pygame.mouse.get_pos()
				curCol = int(math.ceil(mouseY / tilew / 2) - 1)
				if curCol == 0:		# 重开（多次悔棋……）
					restart()
				elif curCol == 1:		# 悔棋
					regret()
				elif curCol == 2:		# 和棋
					kind()
				elif curCol == 3:		# 退出
					pygame.quit()
					sys.exit()
		pygame.display.update()

main()
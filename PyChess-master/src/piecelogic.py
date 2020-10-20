import math

# 存放棋子的行走方式
pieceLogic = {}
EMPTY = 0

board = [		# 棋盘
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
]

def isFree(pos):		# 判断某个位置是否为空
	row, col = pos[0], pos[1]
	if ((row < 0) or (col < 0) or (row > len(board)-1) or (col > len(board)-1)):
		return
	return board[row][col] == EMPTY

def checkLogic(piece, newpos):		# 检查棋子的移动方式是否正确
	return True

def colLogic(piece, newpos):		# 无距离限制移动
	squareamountx = abs(piece.pos[0]-newpos[0])		# 横向移动位移
	squareamounty = abs(piece.pos[1]-newpos[1])
	if piece.name == 'Knight' or piece.name == 'King':
		return True
	elif squareamountx == 0:
		for i in range(1, squareamounty):
			mod = -i if (piece.pos[1] > newpos[1]) else i		# 纵向移动方向
			testpos = (piece.pos[0], piece.pos[1]+mod)		# 逐个测试要移动的位置是否为空（可移动）
			if not isFree(testpos):
				return False
	elif squareamounty == 0:
		for i in range(1, squareamountx):
			mod = -i if (piece.pos[0] > newpos[0]) else i
			testpos = (piece.pos[0]+mod, piece.pos[1])
			if not isFree(testpos):
				return False
	else:
		squareamount = abs(piece.pos[0]-newpos[0])		# 斜向移动
		for i in range(1, squareamount):
			mod = -i if (piece.pos[0] > newpos[0]) else i
			mod2 = -i if (piece.pos[1] > newpos[1]) else i
			testpos = (piece.pos[0]+mod, piece.pos[1]+mod2)
			if not isFree(testpos):
				return False
		return True
	return True

def rookLogic(piece, newpos):
	return ((piece.pos[0] == newpos[0]) or (piece.pos[1] == newpos[1]))		# 行相同或者列相同
pieceLogic['Rook']=rookLogic

def knightLogic(piece, newpos):
	diffx = abs(piece.pos[0]-newpos[0])
	diffy = abs(piece.pos[1]-newpos[1])
	return (diffx <= 2 and diffy <= 2 and diffx != 0 and diffy != 0 and diffx != diffy)
pieceLogic['Knight']=knightLogic

def bishopLogic(piece, newpos):
	return (abs(piece.pos[1]-newpos[1]) == abs(piece.pos[0]-newpos[0]))		# 斜着走
pieceLogic['Bishop']=bishopLogic

def queenLogic(piece, newpos):		# 直走或者斜走
	return (rookLogic(piece, newpos) or bishopLogic(piece, newpos))
pieceLogic['Queen']=queenLogic

def kingLogic(piece, newpos):
	# 王车易位
	if (piece.pos[1]-newpos[1] == 0 		# 横向移动
			and (abs(piece.pos[0]-newpos[0])>1 and abs(piece.pos[0]-newpos[0]<4))		# 判断是否在易位距离内
			and piece.hasMoved == 0):		# 王未移动过
		xdir = True if piece.pos[0]-newpos[0] > 0  else False		# 移动方向，向左移动为 True，右为 False
		castlerook = board[0][piece.pos[1]] if xdir == True else board[7][piece.pos[1]]		# 得到易位的车的位置
		if xdir == True and castlerook != 0 \
				and (abs(piece.pos[0]-newpos[0]) == 2 and castlerook.hasMoved == 0):
			if rc:
				castlerook.move((3, piece.pos[1]))
			return True
		elif xdir == False and castlerook != 0 \
				and (abs(piece.pos[0]-newpos[0]) == 2 and castlerook.hasMoved == 0):
			if rc:
				castlerook.move((5, piece.pos[1]))
			return True
	else:		# 普通移动
		return (queenLogic(piece, newpos) and (abs(piece.pos[0]-newpos[0]) <= 1 and abs(piece.pos[1]-newpos[1]) <= 1))
pieceLogic['King']=kingLogic

def pawnLogic(piece, newpos):
	squaresallowed = 2 if piece.hasMoved == 0 else 1		# 未移动则可以移动两格
	movedh = (piece.pos[0] - newpos[0]) if piece.color == 'W' else (newpos[0] - piece.pos[0])		# 不能向后移动
	movedv = (piece.pos[1] - newpos[1]) if piece.color == 'W' else (newpos[1] - piece.pos[1])
	if board[newpos[0]][newpos[1]] != 0 and (bishopLogic(piece, newpos) and (abs(movedh) == 1 and movedv == 1)):		# 吃
		return True
	elif board[newpos[0]][newpos[1]] != 0 and movedh == 0:		# 不能横向移动，有棋但不能吃
		return False
	return ((piece.pos[0] == newpos[0]) and (movedv <= squaresallowed) and (movedv > 0))		# 走
pieceLogic['Pawn']=pawnLogic

# 综合判断某个棋子是否可以移动
def pieceCanMove(piece, newpos, realcall):
	global rc
	rc = realcall
	for key in pieceLogic:
		if piece.name == key:
			return (pieceLogic[key](piece, newpos) and colLogic(piece, newpos) and checkLogic(piece, newpos))
	return True
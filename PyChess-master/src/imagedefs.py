import pygame
# 加载图片
highlightimg = pygame.image.load("../images/highlight.png")
size = highlightimg.get_size()
hhoverimg = pygame.image.load("../images/hhover.png")

hhoverimgBig = pygame.transform.smoothscale(hhoverimg, (size[0]*4, size[1]*4))

attackimg = pygame.image.load("../images/attack.png")
iconimg = pygame.image.load("../images/icon.png")

pieceimages = {}
pieceimages["WPawn"] = pygame.image.load("../images/wpawn.png")
pieceimages["WRook"] = pygame.image.load("../images/wrook.png")
pieceimages["WKnight"] = pygame.image.load("../images/wknight.png")
pieceimages["WBishop"] = pygame.image.load("../images/wbishop.png")
pieceimages["WQueen"] = pygame.image.load("../images/wqueen.png")
pieceimages["WKing"] = pygame.image.load("../images/wking.png")

pieceimages['WRookBig'] = pygame.transform.smoothscale(pieceimages["WRook"], (size[0]*4, size[1]*4))
pieceimages['WKnightBig'] = pygame.transform.smoothscale(pieceimages["WKnight"], (size[0]*4, size[1]*4))
pieceimages['WQueenBig'] = pygame.transform.smoothscale(pieceimages["WQueen"], (size[0]*4, size[1]*4))
pieceimages['WBishopBig'] = pygame.transform.smoothscale(pieceimages["WBishop"], (size[0]*4, size[1]*4))

pieceimages["BPawn"] = pygame.image.load("../images/bpawn.png")
pieceimages["BRook"] = pygame.image.load("../images/brook.png")
pieceimages["BKnight"] = pygame.image.load("../images/bknight.png")
pieceimages["BBishop"] = pygame.image.load("../images/bbishop.png")
pieceimages["BQueen"] = pygame.image.load("../images/bqueen.png")
pieceimages["BKing"] = pygame.image.load("../images/bking.png")

pieceimages['BRookBig'] = pygame.transform.smoothscale(pieceimages["BRook"], (size[0]*4, size[1]*4))
pieceimages['BKnightBig'] = pygame.transform.smoothscale(pieceimages["BKnight"], (size[0]*4, size[1]*4))
pieceimages['BQueenBig'] = pygame.transform.smoothscale(pieceimages["BQueen"], (size[0]*4, size[1]*4))
pieceimages['BBishopBig'] = pygame.transform.smoothscale(pieceimages["BBishop"], (size[0]*4, size[1]*4))
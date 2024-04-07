import musketeerchess
board = musketeerchess.Board()


board.push_san("e2e3")
#board.push_san("e5")
#board.push_san("Qh5")
print(board)
print(board.legal_moves)

#  rnbqkbnr/pppp1ppp/8/4p3/8/4P3/PPPP1PPP/RNBQKBNR w KQkq - 0 2
print("Name: Anshikaa A Singh")
print("USN: 1AY24AI011")
print("Section: M")
chess_pieces = {
    'K': 'King',
    'Q': 'Queen',
    'R': 'Rook',
    'B': 'Bishop',
    'N': 'Knight',
    'P': 'Pawn'
}

board = {}
for i in range(8):
    row = input(f"Enter row {i + 1} (e.g., 'RNBQKBNR'): ")
    if len(row) != 8:
        print("Invalid row length. Please enter exactly 8 characters.")
        break
    board[i] = row

valid = True
for row in board.values():
    for piece in row:
        if piece not in chess_pieces and piece != '.':
            valid = False
            break
    if not valid:
        break

if valid:
    print("The chess board configuration is valid.")
else:
    print("The chess board configuration is invalid.")

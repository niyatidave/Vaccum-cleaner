import starter as s
import random
import copy


def next_move(cord, map, direction):
	# return next possible cordinate
	x, y = cord
	if direction == 'N' and map[x - 1][y] != 'X':
		return (x - 1, y)

	elif direction == 'E' and map[x][y + 1] != 'X':
		return (x, y + 1)

	elif direction == 'S' and map[x + 1][y] != 'X':
		return (x + 1, y)

	elif direction == 'W' and map[x][y - 1] != 'X':
		return (x, y - 1)

	return cord


def implement_plan(start_cord, plan, room, map):
	# clean as plan
	croom = room.copy()
	croom.remove(start_cord)
	for p in plan:
		ncord = next_move(start_cord, map, p)
		start_cord = ncord
		if start_cord in croom:
			croom.remove(start_cord)

	return croom


def check_plan_with_cleaner(ww):
	for k, v in ww.wpos.items():
		croom = implement_plan(v, ww.plans, ww.rooms[k], ww.map)
		if len(croom) > 0:
			print("BAD PLAN", croom)
		else:
			print("GOOD PLAN", croom)


def planB(ww):
	print('my plan b')
	# todo fix cleaner position
	moves = my_solver(ww.wpos.get('R1'), list(), ww.map, ww.rooms.get('R1'))
	# moves = next_forward_moves(ww.wpos.get('R1'), ww.map)
	print(moves)


def next_forward_moves(current, map, past_moves):
	# return next possible cordinates
	x, y = current
	moves = list()
	# first try to find dirty tiles
	if map[x - 1][y] != 'X' and map[x - 1][y] != 'C':
		moves.append("N")

	if map[x][y + 1] != 'X' and map[x][y + 1] != 'C':
		moves.append("E")

	if map[x + 1][y] != 'X' and map[x + 1][y] != 'C':
		moves.append("S")

	if map[x][y - 1] != 'X' and map[x][y - 1] != 'C':
		moves.append("W")

	# next try to go to clean/ start position (backtracking)
	if len(moves) == 0:
		print('backtrack start')
		lastMove = past_moves.pop()
		# print(lastMove)
		if lastMove == "N":
			lastMove = "S"
		elif lastMove == "E":
			lastMove = "W"
		elif lastMove == "S":
			lastMove = "N"
		elif lastMove == "W":
			lastMove = "E"
		# moves.append(lastMove)
		# print(lastMove)
		if map[x - 1][y] == 'C' or map[x - 1][y] == 'S':
			moves.append("N")

		if map[x][y + 1] == 'C' or map[x][y + 1] == 'S':
			moves.append("E")

		if map[x + 1][y] == 'C' or map[x + 1][y] == 'S':
			moves.append("S")

		if map[x][y - 1] == 'C' or map[x][y - 1] == 'S':
			moves.append("W")

	return moves


def my_solver(current, moves, map, tiles):
	if len(tiles) == 0:
		print('success')
		# print(moves)
		return moves
	mapcopy = copy.deepcopy(map)
	nextMoves = next_forward_moves(current, mapcopy, copy.deepcopy(moves))
	if len(nextMoves) == 0:
		# backtrack
		print('dead end')
		# print(moves)
		return moves
	nextMove = random.choice(nextMoves)
	moves.append(nextMove)
	nextTile = next_move(current, map, nextMove)
	x, y = nextTile
	# if (map[])
	map[x][y] = "C"
	if nextTile in tiles:
		tiles.remove(nextTile)
	return my_solver(nextTile, moves, copy.copy(map), tiles)

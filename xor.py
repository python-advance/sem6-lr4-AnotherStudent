import random
import math 
def sigmoid(x):   
    return 1.0 / (1 + math.exp(-x))
    
def op_two(x, y, thetas):
	result = sigmoid(thetas[0] + x * thetas[1] + y * thetas[2])
	if(result >= 0.5):
		return 1
	else:
		return 0

def op_one(x, thetas):
	result = sigmoid(thetas[0] + x * thetas[1])
	if(result >= 0.5):
		return 1
	else:
		return 0

def test_or(thetas):
	data = [[0,0], [1,0], [0,1], [1,1]]
	data_result = [0, 1, 1, 1]
	for i in range(len(data)):
		result = op_two(data[i][0], data[i][1], thetas)

		if(data_result[i] != result):
			return False

	return True

def test_and(thetas):
	data = [[0,0], [1,0], [0,1], [1,1]]
	data_result = [0, 0, 0, 1]
	for i in range(len(data)):
		result = op_two(data[i][0], data[i][1], thetas)

		if(data_result[i] != result):
			return False

	return True

def test_not(thetas):
	data = [0, 1]
	data_result = [1, 0]
	for i in range(len(data)):
		result = op_one(data[i], thetas)

		if(data_result[i] != result):
			return False

	return True

print('or:')
while(True):
	thetas_or = [random.uniform(-30, 30), random.uniform(-30, 30), random.uniform(-30, 30)]
	result = test_or(thetas_or)
	if(result):
		print('tests ok')
		print('thetas:', thetas_or[0], thetas_or[1], thetas_or[2], '\n')
		break

print('and:')
while(True):
	thetas_and = [random.uniform(-30, 30), random.uniform(-30, 30), random.uniform(-30, 30)]
	result = test_and(thetas_and)
	if(result):
		print('tests ok')
		print('thetas:', thetas_and[0], thetas_and[1], thetas_and[2], '\n')
		break

print('not:')
while(True):
	thetas_not = [random.uniform(-30, 30), random.uniform(-30, 30)]
	result = test_not(thetas_not)
	if(result):
		print('tests ok')
		print('thetas:', thetas_not[0], thetas_not[1], '\n')
		break

# xor: (~x & y) | (x & ~y) =>
print('\nxor test:')
data = [[0,0], [1,0], [0,1], [1,1]]
data_result = [0, 1, 1, 0]
for i in range(len(data)):
	x = data[i][0]
	y = data[i][1]
	# get not x, not y
	not_x = op_one(x, thetas_not)
	not_y = op_one(y, thetas_not)
	# (~x & y), (x & ~y)
	left = op_two(not_x, y, thetas_and)
	right = op_two(x, not_y, thetas_and)
	# or
	result = op_two(left, right, thetas_or)
	# print
	print(x, '|', y, '=', result)
	assert(data_result[i] == result)

# xnor: not((~x & y) | (x & ~y)) =>
print('\nxnor test:')
data = [[0,0], [1,0], [0,1], [1,1]]
data_result = [1, 0, 0, 1]
for i in range(len(data)):
	x = data[i][0]
	y = data[i][1]
	# get not x, not y
	not_x = op_one(x, thetas_not)
	not_y = op_one(y, thetas_not)
	# (~x & y), (x & ~y)
	left = op_two(not_x, y, thetas_and)
	right = op_two(x, not_y, thetas_and)
	# or
	result = op_two(left, right, thetas_or)
	# not
	result = op_one(result, thetas_not)
	# print
	print(x, '|', y, '=', result)
	assert(data_result[i] == result)

## 함수 선언 부분 ##
def findInsertIdx(ary, data) :
	findIdx = -1			# 초깃값은 없는 위치로
	for i in range(0, len(ary)) :
		if (ary[i] > data ) :
			findIdx = i
			break
	if findIdx == -1 :			# 큰 값을 못찾음 == 제일 마지막 위치
		return len(ary)
	else :
		return findIdx

## 전역 변수 선언 부분 ##
before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

## 메인 코드 부분 ##
print('정렬 전 -->', before)
for i in range(len(before)) :
	data = before[i]
	insPos = findInsertIdx(after, data)
	after.insert(insPos, data)
print('정렬 후 -->', after)


#버블 정렬
#퀵 정렬


## 함수 선언 부분 ##
def growRich() :
	memo = [[0 for _ in range(COL)] for _ in range(ROW)]
	memo[0][0] = goldMaze[0][0]

	rowSum = memo[0][0]
	for i in range(1, ROW) :
		rowSum += goldMaze[0][i]
		memo[0][i] = rowSum

	colSum = memo[0][0]
	for i in range(1, COL) :
		colSum += goldMaze[i][0]
		memo[i][0] = colSum

	for row in range(1, ROW) :
		for col in range(1, COL):
			if (memo[row][col-1] < memo[row-1][col]):
				memo[row][col] = memo[row][col-1] + goldMaze[row][col]
			else:
				memo[row][col] = memo[row-1][col] + goldMaze[row][col]

	return memo[ROW-1][COL-1]

## 전역 변수 선언 부분 ##
ROW, COL = 5, 5
goldMaze = [[1, 4, 4, 2, 2],
	      [1, 3, 3, 0, 5],
	      [1, 2, 4, 3, 0],
	      [3, 3, 0, 4, 2],
	      [1, 3, 4, 5, 3]]

## 메인 코드 부분 ##
macolGold = growRich()
print('황금 미로에서 얻은 최대 황금 개수 -->', macolGold)


## 함수 선언 부분 ##
def recu_fibo(n) :
	global count_recu
	count_recu += 1
	if n < 2 :
		return 1
	else :
		return recu_fibo(n-1) + recu_fibo(n-2)

def dp_fibo(n):
	global count_dp
	memo = [1, 1]
	if n < 2 :
		return memo[n]
	else :
		for i in range(2, n+1) :
			memo.append(memo[i-1] + memo[i-2])
			count_dp += 1
		return memo[n]


def fibo_meno(n) :
	global meno, count_meno
	if meno[n] is not None:
		return meno[0]
	if n == 0 :
		count_meno += 1
		return 0
	if n == 1 :
		count_meno += 1
		return 1
	else :
		count_meno += 1
		return fibo_meno(n-1) + fibo_meno(n-2)

meno = [None for _ in range(100)]
count_meno = 0
a = fibo_meno(30)
print(a)
print(count_meno)

count_dp, count_recu = 0, 0

print(' ## 30번째 피보나치 수열 ##')

res = recu_fibo(30)
print('재귀 방식 --> 답:', res, ', 반복수 : ', count_recu)

res = dp_fibo(30)
print('DP 방식 --> 답:', res, ', 반복수 : ', count_dp)








def lcs(s1, s2):
	dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
	for i, x in enumerate (s1):
		for j, y in enumerate(s2):
			if(x == y):
				dp[i+1][j+1] = dp[i][j] +1
			else:
				dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
	string = '';
	x , y = len(s1), len(s2)
	print '============================'
	while x and y:
		if dp[x][y] == dp[x-1][y]:
			string = s2[x-1]+string
			x-= 1
		elif dp[x][y] == dp[x][y-1]:
			y -= 1
		else:
			# string = s1[x-1] + string
			x -= 1
			y -= 1
	return string

if __name__ == '__main__':
	s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
	s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']

	with open ("file.html", "r") as file:
		s1 = file.read()

	with open ("file2.html", "r") as file2:
		s2 = file2.read()
	print lcs(s1,s2)
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
	while x and y:
		if dp[x][y] == dp[x-1][y]:
			x-= 1
		elif dp[x][y] == dp[x][y-1]:
			y -= 1
		else:
			string = s1[x-1] + string
			x -= 1
			y -= 1
	return string

if __name__ == '__main__':
    x = "for i, x in enumerate(a):"
    y = "for j, y in enumerate(b):"
    print lcs(x,y)
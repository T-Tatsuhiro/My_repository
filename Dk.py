#ニュートン法による代数方程式の快解法プログラム

print("解きたい方程式は何次方程式で^すか?")
N = input()^^≠≠≠≠≠≠^^
c= [];
r = [];
x0=1.2;
epsilon = 1.e-1;
delta = 0;
no = 0;
count = 0;
print("0次の係数から順に入力してください．")

for i in range(int(N)+1):#多項式の係数を入力
	c.append(float(input()))#リストオブジェクト作成後新しい要素を追加
for i in range(int(N)+2):
	r.append(0) # [a1, a2, a3, ..., aN]

print("no       x")
print("------------------")
for i in range(int(N),0, -1):
	while True:
		count = count + 1;
		for j in range(int(N),-1,-1):
			r[j] = r[j+1]*x0 + c[j];#組み立て除法
		s = 0;
		for j in range(int(N),0,-1):
			s = s*x0 + r[j];#解をさらに組み立て除法
		x1 =x0-r[0]/s
		print("no={0:d}".format(no),end=''),
		print("  Z[{0:d}]".format(int(N)+1-i),end=''),
		print("={0:f}".format(x1))



		delta = x1 - x0
		x0 = x1
		no = no +1

		if delta > -0.00001 and delta < 0.00001:
			break
	no = 0
	print("--------------------")
	for j in range(int(N), -1, -1):
		c[j-1] = r[j]

print("count = {0:f}".format(count));

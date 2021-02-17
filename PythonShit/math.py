import matplotlib.pyplot as plt
n = int(input("Введите количество строк: "))
res = [] 
x = []
for i in range(n):
	res.append(len(input("Введите " + str(i + 1) + " строку из " + str(n) + ": ")))
	x.append(i + 1)

# bar()
fig1 = plt.figure()
plt.bar(x, res)

# plot
fig2, ax = plt.subplots()
ax.plot(x, res)
plt.show()
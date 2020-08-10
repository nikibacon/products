import os # operating system

products = [] #不管檔案存不存在都需要清單

if os.path.isfile('products.csv'):
  #相對路徑,同一個資料夾
  #os的小模組path裡面的功能isfile可以去檢查檔案在不在
	print('got it !')
  #讀取檔案
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue		
			name, price = line.strip().split(',')
			#s = line.strip().split(',')
			# name = s[0]
			# price = s[1]
			products.append([name, price])
else:
	print('Oops... nothing here')
	

#讓使用者輸入
while True:
	name = input('清輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)

	#建立小清單
	#p = []
	#p.append(name)
	#p.append(price)

	#P = [name, price]

	#放進大清單
	#products.append(p)	
	products.append([name, price])	

print(products)

# 印出所有購買紀錄
for product in products:
	print(product)

for product in products:
	print(product[0],'的價格是', product[1])

# 寫入檔案
with open('products.csv', 'w',encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
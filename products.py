
products = []

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


for product in products:
	print(product)

for product in products:
	print(product[0],'的價格是', product[1])


with open('products.csv', 'w',encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
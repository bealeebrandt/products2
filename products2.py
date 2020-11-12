import os

products = []
if os.path.isfile('products2.csv'):
    print('Yeah! You found it!')
    with open('products2.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if 'Product, price' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)

else:
    print('Sorry! We cannot find it...')

products = []
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格：')
    p = []
    p.append(name)
    p.append(price)
    price = int(price)
    products.append([name, price])
print(products)

for p in products:
    print(p[0], '的價格是', p[1])

with open('products2.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')

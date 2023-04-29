# Задача 3. Повышение цен
# Дан список цен на пять товаров с точностью до копейки.
# Так как экономика даёт о себе знать, мы спрогнозировали,
# что через год придётся повышать цены на X процентов,
# а ещё через один год — ещё на Y процентов.

# Напишите программу, которая получает на вход список цен
# на товары (вещественные числа, список генерируется также
# с помощью list comprehensions) и выводит в одну строку
# общую сумму стоимости товаров за каждый год.

# Пример:
# Цена на товар: 1.09
# Цена на товар: 23.56
# Цена на товар: 57.84
# Цена на товар: 4.56
# Цена на товар: 6.78
# Повышение на первый год: 0
# Повышение на второй год: 10
# Сумма цен за каждый год: 93.83 93.83 103.22

prices_now = []
product_num = int(input('Enter the number of products: '))

for _ in range(product_num):
	price = float(input('Enter a product price: '))
	prices_now.append(price)

first_percent = float(input('Enter the first increase of prices: '))
second_percent = float(input('Enter the second increase of prices: '))

def higher_price(percent, price):
	return round(price * (1 + percent / 100), 2)

first_prices = [higher_price(first_percent, i_prices_now)
                for i_prices_now in prices_now
]
second_prices = [higher_price(second_percent, i_first_prices)
                 for i_first_prices in first_prices
]

print(f'Price increase in the first year is: {first_prices}')
print(f'Price increase in the second year is: {second_prices}')
print(f'The amount of prices for each year is: {sum(prices_now)},'
      f' {sum(first_prices)}, {sum(second_prices)}')
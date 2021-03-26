import pandas as pd

prices = [
	(1, 2.12),
	(2, 2.56),
	(3, 3.10),
	(4, 3.16),
	(5, 3.58),
	(6, 5.12),
	(7, 5.16),
	(8, 5.20),
	(9, 4.12),
	(10, 4.10),
	(11, 3.65),
	(12, 4.25),
]

df = pd.DataFrame(prices, columns=['month', 'pricePLN'])
df = df.set_index("month")
df['priceUSD'] = df['pricePLN'] * 4
df['priceUSD'].plot(title='Price of goods', ls=('dashed'), color="red", grid=True)

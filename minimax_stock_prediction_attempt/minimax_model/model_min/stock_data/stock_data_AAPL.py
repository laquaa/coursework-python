import pandas as pd
import efinance as ef

day_data = pd.read_excel("day.xlsx")
day = day_data['day'][0]
stock_code = 'AAPL'
freq = 1
df = ef.stock.get_quote_history(stock_code, klt=freq)
df.to_csv(f'{stock_code + str(day)}.csv', encoding='utf-8-sig', index=None)
print(f'stock: {stock_code+str(day)} saved in: {stock_code+str(day)}.csv ')
day += 1
day_insertData = pd.DataFrame([{'day': day}])
day_save_data = pd.concat([day_insertData], axis=0)
day_save_data.to_excel("day.xlsx", index=False)
import pandas as pd

df = pd.read_excel(r'C:\Users\siddartha kowshik\Downloads\StocksSheet.xlsx')
print(df,"excel generated")
main = df.to_json (r'conv_pandas.json', indent=3)
print(main,"json created")




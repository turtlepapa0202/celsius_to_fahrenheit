#攝氏('C)轉換成華氏('F)的程式
cel = input('請輸入目前溫度(in celsius): ')
cel = float(cel)
feren = cel * ( 9 / 5 ) + 32
print('The temperature is', feren, 'degree in Fahrenheit')
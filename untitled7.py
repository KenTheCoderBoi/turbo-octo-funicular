months = ("january","febuary","march","april","may","june","july","august","september","october","november","december")
profits = ("3008","6376","6016","8158","6346","5733","7270","4421","8913","5677","4819","6573")

profit_amount = max(profits)
profit_amount_number = profits.index(profit_amount)
profit_month = months[profit_amount_number]
print(profit_amount)
print(profit_amount_number)
print(profit_month)

low_amount = min(profits)
low_amount_number = profits.index(low_amount)
low_month = months[low_amount_number]
print(low_amount)
print(low_amount_number)
print(low_month)
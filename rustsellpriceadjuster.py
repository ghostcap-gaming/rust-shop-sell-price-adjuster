import json

# Load the config file
with open('Items.json') as f:
    data = json.load(f)

# Update the SellPrice for each item
for item in data:
    buy_price = data[item]['BuyPrice']
    sell_price = round(buy_price * 0.25)
    data[item]['SellPrice'] = sell_price

# Save the updated config back to the file
with open('Items_new.json', 'w') as f:
    json.dump(data, f, indent=2)

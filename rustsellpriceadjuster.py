import json

def update_sell_price(data):
    for shop in data["Shop"]:
        for item in shop["Items"]:
            if "Price" in item and "Sell Price" in item:
                item["Sell Price"] = item["Price"] * 0.2
    return data

def main():
    with open('Items.json', 'r') as file:
        data = json.load(file)
    
    updated_data = update_sell_price(data)
    
    with open('Items.json', 'w') as file:
        json.dump(updated_data, file, indent=2)  # Change indent to 2

if __name__ == "__main__":
    main()

# Author   : Anshuman Agarwal
# Email    : anagarwal@umass.edu
# Spire ID : 34157323

class VendingMachine:
    def __init__(self):
        self.snacks = {}
        self.balance = 0
        self.total_sales = 0
        self.sale_history = []

    def list_items(self):
        if len(self.snacks)==0:
            print('No items in the vending machine')
        else:
            print('Available items:')
            sorted_snacks = sorted(self.snacks.keys())
            for items in sorted_snacks:
                cost, quantity = self.snacks[items]
                print(f'{items} (${cost}): {quantity} available')

    def add_item(self, name, price, quantity):
        if name in self.snacks:
            current_price, current_quantity = self.snacks[name]
            self.snacks[name] = (current_price, current_quantity + quantity)
        else:
            self.snacks[name] = (price, quantity)
        print(f'{quantity} {name}(s) added to inventory')

    def insert_money(self,dollar_amount):
        if (dollar_amount== 1 or dollar_amount== 2 or dollar_amount== 3):
            self.balance += dollar_amount
            print(f'Balance: {round(self.balance,2)}')
        else:
            print('Invalid amount')
    
    def purchase(self,snack_name):
        if snack_name not in self.snacks:
            print('Invalid item')
        else:
            quantity_check = self.snacks[snack_name]
            price_check = self.snacks[snack_name]
            final_quantity = quantity_check[1]
            final_price = price_check[0]
            if final_quantity==0:
                print(f'Sorry {snack_name} is out of stock')
            elif self.balance<final_price:
                print(f'Insufficient balance. Price of {snack_name} is {final_price}')
            else:
                final_quantity-=1
                self.snacks[snack_name] = final_price, final_quantity
                self.balance-= final_price
                self.balance = round(self.balance,2)
                print(f'Purchased {snack_name}')
                print(f'Balance: {self.balance}')
                self.total_sales+=final_price
                self.total_sales = round(self.total_sales,2)
                self.sale_history.append({'item': snack_name, 'price': final_price})


    def display_change(self):
        if self.balance==0:
            print('No change')
        else:
            print(f'Change: {self.balance}')
            self.balance = 0
    
    def get_item_price(self,item):
        if item not in self.snacks:
            print('Invalid item')
        else:
            price_check = self.snacks[item]
            price = price_check[0]
            return price
    
    def empty_inventory(self):
        self.snacks.clear()
        print('Inventory cleared')
    
    def get_total_sales(self):
        return self.total_sales

    def get_item_quantity(self, snack_name):
        if snack_name not in self.snacks:
            print('Invalid item')
        else:
            quantity_check = self.snacks[snack_name]
            quantity = quantity_check[1]
            return quantity

    def remove_item(self, snack_name):
        if snack_name not in self.snacks:
            print('Invalid item')
        else:
            del self.snacks[snack_name]
            print(f'{snack_name} removed from inventory')
    
    def stats(self,N):
        if not self.sale_history:
            print('No sale history in the vending machine')
        else:
            latest_sales = sorted(self.sale_history[-N:], key = lambda a:a['item'])
            counter = [{'item': d['item'], 'price': d['price'], 'count': sum(1 for other in latest_sales if other == d)} for d in latest_sales]
            unique_sales = list({tuple(sorted(d.items())): d for d in counter}.values())

            print(f'Sale history for the most recent {min(N, len(self.sale_history))} purchase(s):')
            
            for sale in unique_sales:
                snack = sale['item']
                num = sale['count']
                price = sale['price']
                new_total_sales = num * price
                N_total_sales = N * price

                if num < N:
                    print(f'{snack}: ${new_total_sales} for {num} purchase(s)')
                else:
                    print(f'{snack}: ${N_total_sales} for {N} purchase(s)')

            





class CoffeeMachine:
    coffee_type = None  # 1-espresso, 2-latte, 3-cappuccino
    coffee_requirements = [[250, 0, 16, 4], [350, 75, 20, 7], [200, 100, 12, 6]]  # [water, milk, coffee beans, money]
    coffee_selected = None
    status = None

    def __init__(self, water, milk, coffee, d_cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.d_cups = d_cups
        self.money = money

    def print_machine_supplies(self):
        print('The coffee machine has:')
        print(f'{self.water}  of water')
        print(f'{self.milk}  of milk')
        print(f'{self.coffee} of coffee beans')
        print(f'{self.d_cups} of disposable cups')
        print(f'{self.money} of money')

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add: '))
        self.milk += int(input('Write how many ml of milk do you want to add: '))
        self.coffee += int(input('Write how many gr of coffee beans do you want to add: '))
        self.d_cups += int(input('Write how many disposable cups do you want to add: '))

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def select_coffee(self):
        if self.coffee_type == '1':
            self.coffee_selected = self.coffee_requirements[0]
        elif self.coffee_type == '2':
            self.coffee_selected = self.coffee_requirements[1]
        elif self.coffee_type == '3':
            self.coffee_selected = self.coffee_requirements[2]

    def check_resources(self):
        if self.water < self.coffee_selected[0]:
            print('Sorry, not enough water!')
            self.status = 'reset'
        elif self.milk < self.coffee_selected[1]:
            print('Sorry, not enough milk!')
            self.status = 'reset'
        elif self.coffee < self.coffee_selected[2]:
            print('Sorry, not enough coffee beans!')
            self.status = 'reset'
        elif self.d_cups < 1:
            print('Sorry, not enough disposable cups!')
            self.status = 'reset'
        else:
            print('I have enough resources, making you a coffee!')
            self.status = 'making coffee'

    def make_coffee(self):
        self.water -= self.coffee_selected[0]
        self.milk -= self.coffee_selected[1]
        self.coffee -= self.coffee_selected[2]
        self.d_cups -= 1
        self.money += self.coffee_selected[3]


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    action = input('Write action (buy, fill, take, remaining, exit): ')

    if action == 'buy':
        coffee_machine.coffee_type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        if coffee_machine.coffee_type == 'back':
            continue
        else:
            coffee_machine.select_coffee()
            coffee_machine.check_resources()
            if coffee_machine.status == 'reset':
                continue
            elif coffee_machine.status == 'making coffee':
                coffee_machine.make_coffee()
    elif action == 'fill':
        coffee_machine.fill()
    elif action == 'take':
        coffee_machine.take()
    elif action == 'remaining':
        coffee_machine.print_machine_supplies()
    elif action == 'exit':
        break

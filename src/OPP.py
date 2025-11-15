# class vehicle:
#     def __init__(self, time, distance, model, fuel_type):
#         self.__time = time
#         self.__distance = distance
#         self.__model = model
#         self.__fuel_type = fuel_type
    
#     def change_time(self, new_time):
#         self.__time = new_time

#     def change_distance(self, new_distance):
#         self.__distance = new_distance
    
#     def get_speed(self):
#         return self.__distance / self.__time
    
#     def get_velocity(self, direction_angel):
#         return self.get_speed(), direction_angel

#     def environmentally_friendly(self):
#         if self.__fuel_type == 'Gas' or 'Oil' or 'Petrol':
#             return False
#         else:
#             return True
        
#     def acceleration(self, direction_angel):
#         return self.get_velocity(direction_angel)[0] / self.__time, self.get_velocity(direction_angel)[1]

# class bus(vehicle):
#     def __init__(self, time, distance, model, fuel_type, weight, max_passengers, passengers):
#         super().__init__(time, distance, model, fuel_type)
#         self.__weight = weight
#         self.__max_passengers = max_passengers
#         self.__passengers = passengers
    
#     def add_passenger_names(self, **kwargs):
#         if len(self.__passengers) < self.__max_passengers:
#             self.__passengers += kwargs
#         else:
#             print('too many passengers')

#     def remove_passenger_names(self, **kwargs):
#         for i in kwargs:
#             self.__passengers.pop(i)

# class car(vehicle):
#     def __init__(self, time, distance, model, fuel_type, speed_limit):
#         super().__init__(time, distance, model, fuel_type)
#         self.__speed_limit = speed_limit

#     def change_time(self, num):
#         new_time = self.__time + num
#         speed = self.__distance / new_time
#         if self.__speed_limit > speed:
#             self.__time = new_time
    
#     def change_distance(self, num):
#         new_distance = self.__distance + num
#         speed = new_distance / self.__time
#         if self.__speed_limit > speed:
#             self.__distance = new_distance
    
# class space_vehicle(vehicle):
#     def __init__(self, time, distance, model, fuel_type, angle_from_ground, fuel_amount, fuel_capacity, deadly_radiation_from_sun):
#         super().__init__(self, time, distance, model, fuel_type)
#         self.__angle_from_ground = angle_from_ground
#         self.__fuel_amount = fuel_amount
#         self.__fuel_capacity = fuel_capacity
#         self.deadly_radiation_from_sun = deadly_radiation_from_sun
    
#     def get_distance_from_earth(self):
#         return self.__distance * (self.__angle_from_ground / 360)
    
#     def get_percentage_of_fuel_used(self):
#         return self.__fuel_amount / self.__fuel_capacity
    
# model_12 = bus(5, 100, "12", "Gas", 34, 65, None)

# dacia = car(100, 1000, '54', 'Solar charge', 95)

# try:
#     print(model_12.__time)
# except Exception as e:
#     print(e)

# print(model_12.environmentally_friendly())

# print(model_12.get_velocity(34.5))

# print(model_12.acceleration(34.5))

# print(dacia.get_speed())

# dacia.change_time(54)

# print(dacia.get_speed())

# class bankAccount:
#     def __init__(self, __name, __address, __balance, __pin, __account_num):
#         self.__name = __name
#         self.__address = __address
#         self.__balance = __balance
#         self.__pin = __pin
#         self.__account_num = __account_num
    
#     def get_balance(self):
#         return self.__balance
    
#     def get_pin(self):
#         return self.__pin

# Person1 = bankAccount('bob', 'location', 930, 6746, 0)
# Person2 = bankAccount('bill', 'place', 31323323, 4355, 1)

# option1 = input('Would you like to: \n 1 - create an account \n 2 - load an account \n')

# if option1 == 1:
#     with open('Accounts', 'r') as accounts:
#         name = input('Name: ')
#         place = input('Address: ')
#         pin = hash(input('Set pin number: '))
#         balance = 0
#         numOf = 0
#         n = ''
#         for i in accounts.read():
#             if i == '$':
#                 numOf += 1
#             if numOf == 4:
#                 n += i
#             if i == '*':
#                 numOf += 1
#         account_number = int(n) + 1

#     with open('Accounts', 'a') as accounts:
#         accounts.write(f'{name}${place}${balance}${pin}${account_number}*')
#     print(f'Your account number is {account_number}')
# else: 
#     account_number = input('What is your account number? \n')

# with open('Accounts', 'r') as account:
#     a = ''
#     n = ''
#     numOf = 0
#     for i in account.read():
#         n += i
#         if i == '*':
#             n = ''
#         if i == account_number[0]:
#             a = n
#     n = ''
#     name = ''
#     place = ''
#     balance = ''
#     pin = ''
#     account_number = ''

#     for j in a:
#         n += j
#         if i == '$':
#             numOf += 1
#         if numOf == 1:
#             name += n
#         if numOf == 2:
#             place += n
#         if numOf == 3:
#             balance += n
#         if i == '*':
#             numOf += 1  

# option2 = input('Choose a number: \n 1 - Deposit \n 2 - Withdraw \n 3 - Check balance \n 4 - Loan \n')


# class vehicle:
#     def __init__(self, speed, topSpeed):
#         self.speed = speed
#         self.topSpeed = topSpeed

#     def accelerate(self, acceleration):
#         speed += acceleration

# class car(vehicle):
#     def __init__(self, speed, topSpeed, fuel_type):
#         super().__init__(speed, topSpeed)
#         self.fuel_type = fuel_type

# audi = car(0,200,'E10')

# audi.accelerate(300)

import pygame
import sys
import random
import math

pygame.init()

# --- Window ---
WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Game Starter")

CLOCK = pygame.time.Clock()
TILE_SIZE = 40

# --- Colours ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (60, 60, 60)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# --- Simple Map Layout ---
# 1 = wall, 0 = empty floor
ROOM_MAP = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

# --- Player Class ---
class Charater:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.color = BLACK

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Player(Charater):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = GREEN
        self.speed = 4

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
    
    def move_down(self):
        self.rect.y += self.speed

class Monster(Charater):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = RED
        self.speed = 2 
    
    def move_mon(self):
        n = random.random() * 10
        if math.floor(n) > 8:
            self.rect.y -= self.speed
        if math.floor(n) < 3:
            self.rect.y += self.speed
        if math.floor(n) > 2 and math.floor(n) < 5:
            self.rect.x -= self.speed
        if math.floor(n) == 7:
            self.rect.x += self.speed



player = Player(60, 60)
monster = Monster(40, 100)

# --- Draw the map ---
def draw_room():
    for row_index, row in enumerate(ROOM_MAP):
        for col_index, tile in enumerate(row):
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE
            if tile == 2:
                pygame.draw.rect(SCREEN, BLUE, (x, y, TILE_SIZE, TILE_SIZE)
            if tile == 1:
                pygame.draw.rect(SCREEN, GREY, (x, y, TILE_SIZE, TILE_SIZE))
            else:
                pygame.draw.rect(SCREEN, BLACK, (x, y, TILE_SIZE, TILE_SIZE))


# --- Main Game Loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update
    player.handle_input()
    monster.move_mon()

    # Draw
    SCREEN.fill(BLACK)
    draw_room()
    player.draw(SCREEN)
    monster.draw(SCREEN)

    pygame.display.flip()
    CLOCK.tick(60)

import random
class Good:
    def __init__(self, type, weight, quality, cost):
        self.type = type
        self.weight = weight
        self.quality = quality
        self.cost = cost

class Event:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

class City:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

cities = [
    City("Город1", random.randint(50, 100)),
    City("Город2", random.randint(50, 100)),
    City("Город3", random.randint(50, 100)),
    City("Город4", random.randint(50, 100)),
    City("Город5", random.randint(50, 100))
]

events = [
    Event("Обычный день", lambda: None),
    Event("Дождь", lambda: None),
    Event("Ровная дорога", lambda: None),
    Event("Телега сломалась", lambda: None),
    Event("Река", lambda: None),
    Event("Встретил местного", lambda: None),
    Event("Разбойники большой дороги", lambda: None),
    Event("Придорожный трактир", lambda: None),
    Event("Товар испортился", lambda: None)
]

goods_types = ["мясо", "сухофрукты", "зерно", "мука", "ткани", "краска"]

def buy_goods_in_starting_city(money, capacity):
    goods = []
    total_cost = 0
    
    while capacity >= 1 and money >= 10:
        type = random.choice(goods_types)
        max_cost = min(money, 50)
        if max_cost < 10:
            break
        cost = random.randint(10, max_cost)
        weight = random.randint(1, min(capacity, 10))
        quality = random.choice([1.2, 0.95, 0.55, 0.25, 0.1])
        goods.append(Good(type, weight, quality, cost))
        money -= cost
        capacity -= weight
        total_cost += cost
    
    print("Куплен следующий товар:")
    for good in goods:
        print(f"Тип: {good.type}, Вес: {good.weight}, Качество: {good.quality}, Стоимость: {good.cost}")
    print(f"Общая стоимость покупки: {total_cost:.2f} денег")
    
    return goods

def sell_goods(goods, city_name, starting_money):
    total_income = 0
    unpaid_debts = 0
    
    for good in goods:
        if good.quality > 0.1:  
            price = calculate_sell_price(good)
            total_income += price
        else:
            print(f"Товар {good.type} испорчен и не может быть продан.")
            unpaid_debts += good.cost
    
    if total_income > 0:
        print(f"Продан следующий товар в {city_name}:")
        for good in goods:
            if good.quality > 0.1:
                price = calculate_sell_price(good)
                print(f"Тип: {good.type}, Вес: {good.weight}, Качество: {good.quality}, Стоимость: {price:.2f}")
        total_income == starting_money
        profit = total_income - starting_money
        print(f"В {city_name} получено {total_income:.2f} денег от продажи товаров")
        print(f"Чистая прибыль: {profit:.2f} денег")
    else:
        print(f"В {city_name} не удалось продать ни одного товара.")
    
    if unpaid_debts > 0:
        print(f"Торговец должен {unpaid_debts:.2f} денег за испорченные товары.")
        
    return total_income, unpaid_debts

def calculate_sell_price(good):
    if good.quality > 0.1:
        price = good.cost * good.quality
        return price
    else:
        return 0



def choose_event():
    event_probabilities = {
        "Обычный день": 0.3,
        "Дождь": 0.1,
        "Ровная дорога": 0.9,
        "Телега сломалась": 0.1,
        "Река": 0.1,
        "Встретил местного": 0.1,
        "Разбойники большой дороги": 0.2,
        "Придорожный трактир": 0.1,
        "Товар испортился": 0.1
    }
    event_names = list(event_probabilities.keys())
    event_weights = list(event_probabilities.values())
    chosen_event = random.choices(event_names, weights=event_weights)[0]
    return chosen_event



def roadside_inn():
    if random.random() < 0.5:
        print("Торговец решил остановиться на придорожном трактире.")
        if random.random() < 0.7:
            print("Торговец решил провести торговлю на трактире.")
        else:
            print("Торговец решил не торговать и просто отдохнуть.")
        spend_money = random.uniform(5, 20)
        print(f"Торговец потратил {spend_money:.2f} денег на еду/ночлег.")
        return spend_money
    else:
        print("Торговец решил не останавливаться на придорожном трактире.")
        return 0

def choose_destination(current_city, capacity, distance_remaining):
    
    max_distance = min(distance_remaining, capacity)
    return max_distance

def main():
    start_city = random.choice(cities)
    end_city = random.choice(cities)

    while start_city.distance >= end_city.distance:
        end_city = random.choice(cities)

    print("Стартовый город:", start_city.name, ", Конечный город:", end_city.name)
    print("Грузоподъемность тележки: 40 единиц")
    initial_money = 200
    capacity = 50
    current_city = start_city
    total_days = 0
    total_distance = 0
    goods = None

    money = initial_money

    print("Покупка товаров в начальном городе:")
    goods = buy_goods_in_starting_city(money, capacity)
    money -= sum(calculate_sell_price(good) for good in goods)
    speed = 1
    actual_distance = 0
    event_occurred = True
    while actual_distance < end_city.distance:
        event = choose_event()
     
        if event == "Обычный день":
           pass
           
        
        if event == "Придорожный трактир":
            if money >= 1:
                money -= roadside_inn()
            else:
                print("Торговец не может позволить себе остановиться на трактире.")
        
        elif event == "Дождь":
                speed = max(1, speed - 2)
                
        elif event == "Ровная дорога":
                speed += 2
        elif event == "Телега сломалась":
                print("Телега сломалась, но торговец все равно продолжает движение.")
                speed == 1 
        elif event == "Река":
                current_city_index = cities.index(current_city)
                current_city_index += random.randint(1, 2)
                if current_city_index >= len(cities):
                    current_city_index = len(cities) - 1
                current_city = cities[current_city_index]
        elif event == "Встретил местного":
                current_city_index = cities.index(current_city)
                current_city_index += random.randint(3, 6)
                if current_city_index >= len(cities):
                    current_city_index = len(cities) - 1
                current_city = cities[current_city_index]
        elif event == "Разбойники большой дороги":
                print("Торговца напали разбойники!")
                if money > 1:
                    ransom = random.uniform(1, money)
                    print(f"Торговец откупился у разбойников за {ransom:.2f} денег.")
                    money -= ransom
                elif goods:
                    best_goods = [good for good in goods if good.quality == max([g.quality for g in goods])]
                    if best_goods:
                        robbed_goods = random.choice(best_goods)
                        print(f"Разбойники забрали самый лучший товар: {robbed_goods.type}.")
                        goods.remove(robbed_goods)
                    else:
                        print("У торговца нет товаров, чтобы отдать разбойникам!")
                else:
                    print("У торговца ни денег, ни товаров. Разбойники ушли ни с чем.")
        elif event == "Товар испортился":
                if goods:
                    spoiled_good = random.choice(goods)
                    print(f"Один из товаров испортился: {spoiled_good.type}.")
                    spoiled_good.quality /= 2
                    if spoiled_good.quality < 0.1:
                        print("Товар слишком испорчен и выброшен.")
                        goods.remove(spoiled_good)
                else:
                    print("У торговца нет товаров, чтобы испортить!")
        
        total_days += 1
        actual_distance += 1
        total_distance += speed

        if total_distance >= end_city.distance:
            break

        if event_occurred: 
            print(f"День {total_days}")
            print(event)
            print(f"Скорость телеги: {speed} лиг в день")
            print(f"Пройдено расстояние: {total_distance} лиг")

    sell_money, unpaid_debts = sell_goods(goods, end_city.name, initial_money)
    money += sell_money

    print(f"Денег в наличии: {money:.2f} монет")

    if unpaid_debts > 0:
        print(f"Торговец должен {unpaid_debts:.2f} денег придорожному трактиру или разбойникам.")

if __name__ == "__main__":
    main()

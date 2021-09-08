from pprint import pprint


def make_dict(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            records_quantity = int(file.readline())
            ingredient_list = []
            for ingredient in range(records_quantity):
                name, quantity, measure = file.readline().split('|')
                ingredient_list.append(
                    {'name': name, 'quantity': int(quantity), 'measure': measure})
            cook_book[dish_name] = ingredient_list
            file.readline()
    return cook_book


cook_book = make_dict('recipe_list.txt')


def get_shop_list_by_dishes(dishes, person):
    shop_list = {}
    for dish_name, ingredient in cook_book.items():
        for choice in dishes:
            if choice == dish_name:
                for res in ingredient:
                    if res["name"] not in shop_list.keys():
                        shop_list[res["name"]] = {'quantity': res["quantity"] * person, 'measure': res["measure"]}
                    else:
                        for key, value in shop_list.items():
                            if key == res['name']:
                                add_quantity = value['quantity']
                                shop_list[res["name"]] = {'quantity': res["quantity"] * person + add_quantity,
                                                          'measure': res["measure"]}

    return pprint(shop_list)


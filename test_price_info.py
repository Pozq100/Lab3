import price_info


def test_totalcost():
    quantity_list = {'apple': 5, 'orange': 5, 'watermelon': 1, 'pineapple': 2, 'pear': 10, 'papaya': 1,
                     'pomegranate': 2}
    total_cost = price_info.total_cost_shopping(quantity_list)
    answer = 46.75
    assert(answer == total_cost)


def test_costoffruit():
    cost_of_fruit = price_info.cost_of_fruits("orange", 5)
    answer = 7
    assert(answer == cost_of_fruit)
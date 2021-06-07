PRICE_PER_VIEW_POST = 0.5
PRICE_PER_VIEW_STORY = 0.3

PARTNER = 10
PHYSIC = 3
PAYMENT = PHYSIC

MAX_VIEWS_1 = 1000
MAX_VIEWS_2 = 3000
MAX_VIEWS_3 = 5000
MAX_VIEWS_4 = 10000
MAX_VIEWS_5 = 15000
MAX_VIEWS_6 = 20000
MAX_VIEWS_7 = 9999999

SCALE_BY_VIEWS_1 = 2
SCALE_BY_VIEWS_2 = 1.85
SCALE_BY_VIEWS_3 = 1.7
SCALE_BY_VIEWS_4 = 1.55
SCALE_BY_VIEWS_5 = 1.4
SCALE_BY_VIEWS_6 = 1.25
SCALE_BY_VIEWS_7 = 1.1

def count_budget(budget):
    return budget - (budget / 100) * PHYSIC

def count_price(price, scale_by_views):
    return price - (price / scale_by_views)

def print_result(price, over_price, max_views, type_of_views):
    blogger_price = price / PARTNER
    blogger_payment = (price / 100) * PAYMENT
    partner_payment = (blogger_price / 100) * PAYMENT
    price *= over_price
    our_budget = count_price(price, over_price) - blogger_price 
    + blogger_payment + partner_payment

    print('цена', type_of_views, 'для рекла:', int(price), '\n')
    print('наценка:', over_price, 'до', max_views, 'охвата')
    print('сумма наценки:', int(count_price(price, over_price)))
    print('партнер заработает:', int(blogger_price), '\n')
    print('коммиссия при выплате блогеру:', int(blogger_payment))
    print('коммиссия при выплате партнеру:', int(partner_payment))
    print('сумма коммисии:' , int(blogger_payment + partner_payment))
    print('мы заработаем после коммисии:', int(our_budget))

def count_stats(budget, views, type_of_views):
    if(type_of_views == 'пост'):
        price = views * PRICE_PER_VIEW_POST
    elif(type_of_views == 'сторис'):
        price = views * PRICE_PER_VIEW_STORY
    else:
        print('ошибка типа публикации')

    if(price != budget or price > budget):
        print('бюджет:', int(budget))
        print('бюджет после комиссии:', int(count_budget(budget)), '\n')
        print('цена', type_of_views, 'для блогера:', int(price))

        if(views <= MAX_VIEWS_1):
            print_result(price, SCALE_BY_VIEWS_1, MAX_VIEWS_1, type_of_views)
        elif(views > MAX_VIEWS_1 and views <= MAX_VIEWS_2):
            print_result(price, SCALE_BY_VIEWS_2, MAX_VIEWS_2, type_of_views)
        elif(views > MAX_VIEWS_2 and views <= MAX_VIEWS_3):
            print_result(price, SCALE_BY_VIEWS_3, MAX_VIEWS_3, type_of_views)
        elif(views > MAX_VIEWS_3 and views <= MAX_VIEWS_4):
            print_result(price, SCALE_BY_VIEWS_4, MAX_VIEWS_4, type_of_views)
        elif(views > MAX_VIEWS_4 and views <= MAX_VIEWS_5):
            print_result(price, SCALE_BY_VIEWS_5, MAX_VIEWS_5, type_of_views)
        elif(views > MAX_VIEWS_5 and views <= MAX_VIEWS_6):
            print_result(price, SCALE_BY_VIEWS_6, MAX_VIEWS_6, type_of_views)
        else:
            print_result(price, SCALE_BY_VIEWS_7, MAX_VIEWS_7, type_of_views)
    else:
        print('бюджет:', budget, 'равен или меньше рекламы:', int(price))

def main():
    while True:
        print('')
        budget = int(input('бюджет: ')) 
        views = int(input('охват: ')) 
        type_of_views = str(input('пост/сторис: '))
        print('')
        count_stats(budget, views, type_of_views)

main()
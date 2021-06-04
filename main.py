PRICE_PER_VIEW_POST = 0.5
PRICE_PER_VIEW_STORY = 0.3

PARTNER = 10

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

def count_price(_price, _SCALE_BY_VIEWS):
    return _price - (_price / _SCALE_BY_VIEWS)

def count_partner(_price, _SCALE_BY_VIEWS,):
    return ((_price - (_price / _SCALE_BY_VIEWS)) / PARTNER)

def print_result(_price, _default, _MAX_VIEWS, _type):
    print('цена', _type, 'для рекла:', int(_price), '\n')
    print('наценка:', _default, 'до', _MAX_VIEWS, 'охвата')
    print('сумма наценки:', int(count_price(_price, _default)))
    print('партнер заработает:', int(count_partner(_price, _default)))
    print('мы заработаем:', int(count_price(_price, _default) - count_partner(_price, _default)))

def count_stats(views, _PRICE_PER_VIEW, _type):
    price = views * _PRICE_PER_VIEW
    print('цена', _type, 'для блогера:', int(price))

    if(views <= MAX_VIEWS_1):
        default = SCALE_BY_VIEWS_1
        price *= default
        print_result(price, default, MAX_VIEWS_1, _type)
        
    elif(views > MAX_VIEWS_1 and views <= MAX_VIEWS_2):
        default = SCALE_BY_VIEWS_2
        price *= default
        print_result(price, default, MAX_VIEWS_2, _type)
        
    elif(views > MAX_VIEWS_2 and views <= MAX_VIEWS_3):
        default = SCALE_BY_VIEWS_3
        price *= default
        print_result(price, default, MAX_VIEWS_3, _type)
        
    elif(views > MAX_VIEWS_3 and views <= MAX_VIEWS_4):
        default = SCALE_BY_VIEWS_4
        price *= default
        print_result(price, default, MAX_VIEWS_4, _type)
        
    elif(views > MAX_VIEWS_4 and views <= MAX_VIEWS_5):
        default = SCALE_BY_VIEWS_5
        price *= default
        print_result(price, default, MAX_VIEWS_5, _type)
        
    elif(views > MAX_VIEWS_5 and views <= MAX_VIEWS_6):
        default = SCALE_BY_VIEWS_6
        price *= default
        print_result(price, default, MAX_VIEWS_6, _type)
    else:
        default = SCALE_BY_VIEWS_7
        price *= default
        print_result(price, default, MAX_VIEWS_7, _type)

def main():
    while True:
        print('')
        views = int(input('охват: ')) 
        type_of_views = str(input('пост/сторис: '))

        if(type_of_views == 'пост'):
            count_stats(views, PRICE_PER_VIEW_POST, type_of_views)
        elif(type_of_views == 'сторис'):
            count_stats(views, PRICE_PER_VIEW_STORY, type_of_views)
        else:
            break

main()
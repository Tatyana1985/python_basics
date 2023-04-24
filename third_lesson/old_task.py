MONEY = 100
PRICE_BULL = 10
PRICE_COW = 5
PRICE_CALF = 0.5
QUANTITY = 100
flag = False
for bull in range(1, MONEY//PRICE_BULL + 1):
    for cow in range(1, MONEY//PRICE_COW + 1):
        calf = QUANTITY - bull - cow
        if PRICE_BULL*bull + PRICE_COW*cow + PRICE_CALF*calf == MONEY:
            print(f'быков - {bull}, коров - {cow}, телят - {calf}')
            flag = True
            break
    if flag == True:
        break


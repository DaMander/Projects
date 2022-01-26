VINO_WAGE = None
CAT_WAGE = None
MINIMUM_SAVINGS = None

def calculate_job_money(Vino_hours, Cat_hours):
    Vino_money = Vino_hours*VINO_WAGE
    Cat_money = float(round(Cat_hours*CAT_WAGE, 2))
    return Vino_money, Cat_money

def collect_weekly_money():
    Vino_hours = float(input("Hours at vino: "))
    Cat_hours = float(input("Hours at cat: "))
    Tips_money = float(input("Tips money: "))
    Extra_money = float(input("Extra money: "))
    Vino_money, Cat_money = calculate_job_money(Vino_hours, Cat_hours)
    return Vino_money, Cat_money, Extra_money, Tips_money


def sort_vino_money(vino_money):
    if vino_money <= MINIMUM_SAVINGS:
        return vino_money, 0, 0
    else:
        return MINIMUM_SAVINGS, vino_money- MINIMUM_SAVINGS, 0


def sort_cat_money(vino_money, cat_money):
    difference = MINIMUM_SAVINGS - vino_money #how much money needed to reach minimum
    if difference > 0: #is the difference negative
        if cat_money < difference: #if not then find out if theres enough for the difference
            return cat_money, 0, 0 #if no then money goes to saving
        else: #if I have more than the difference
            cat_money -= difference #cat money becomes the amount I have over the difference
    if cat_money > CAT_WAGE*3:
        spending_mon = CAT_WAGE*3
        cat_money -= CAT_WAGE*3
        saving_mon = cat_money/2 + difference
        spending_mon += cat_money/2
        return saving_mon, spending_mon, 0
    else:
        return difference, cat_money, 0

def sort_extras(saving_mon, extra_mon):
    if saving_mon < MINIMUM_SAVINGS:
        if saving_mon + extra_mon <= MINIMUM_SAVINGS:
            return extra_mon, 0, 0
        else:
            extra_to_save = MINIMUM_SAVINGS - saving_mon
            return extra_to_save, extra_mon-extra_to_save, 0
    else:
        return 0, extra_mon, 0

def sort_tips(saving_mon, tips_mon):
    if saving_mon < MINIMUM_SAVINGS:
        if saving_mon + tips_mon <= MINIMUM_SAVINGS:
            return tips_mon, 0, 0
        else:
            tip_to_save = MINIMUM_SAVINGS - saving_mon
            tips_mon -= tip_to_save
    else:
        tip_to_save = 0
    if tips_mon <= 20:
        return tip_to_save, 0, tips_mon
    else:
        remaining_tips = tips_mon - 20
        return tip_to_save, remaining_tips/2, 20+ remaining_tips/2


money_accounts = [0,0,0]

weekly_money = collect_weekly_money()
j = 0
for i in sort_vino_money(weekly_money[0]):
    money_accounts[j] += i
    j += 1
j = 0
for i in sort_cat_money(money_accounts[0], weekly_money[1]):
    money_accounts[j] += i
    j+=1
j =0
for i in sort_extras(money_accounts[0], weekly_money[2]):
    money_accounts[j] += i
    j+=1
j = 0
for i in sort_tips(money_accounts[0], weekly_money[3]):
    money_accounts[j] += i
    j+=1
    

print(money_accounts)
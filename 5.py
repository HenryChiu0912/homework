def takecarbohydr_rate(foods):
    return foods[8]

def takecalories_rate(foods):
    return foods[9]

def takefat_rate(foods):
    return foods[10]

gender = int(input("請輸入性別(男性輸入1、女性輸入2): "))
weight = float(input("請輸入體重(kg): "))
height = float(input("請輸入身高(cm): "))
age = int(input("請輸入年齡: "))
activity_type = int(input("請輸入平常的活動習慣(坐式生活輸入1、輕度活動輸入2、中度活動輸入3、高度活動輸入4、極高度活動輸入5): "))
goal = int(input("請輸入希望減脂輸入1、維持體重輸入2、增肌輸入3: "))

if gender == 1:
    bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
else:
    bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

activity = {1: 1.2, 2: 1.4, 3: 1.5, 4: 1.7, 5: 1.9}

daily_calories = bmr * activity[activity_type]
calories_per_meal = daily_calories / 3

if goal == 1:
    calories_per_meal -= 80  # 減肥
elif goal == 3:
    calories_per_meal += 80  # 增肌

print('每日消耗量(TDEE):', daily_calories)
print(f'每餐應攝取的熱量：{calories_per_meal:.0f}')

foods = []

n=int(input("請問有幾項食物?"))
for i in range(1,n+1):
    temp=[]
    name = input("請輸入食物名稱: ")
    carbohydrate = int(input("請輸入碳水化合物含量(g): "))
    protein = int(input("請輸入蛋白質含量(g): "))
    fat = int(input("請輸入脂肪含量(g): "))
    size = float('{:.2f}'.format(carbohydrate + protein + fat))
    divisible = int(input("請輸入可否拆分(不能輸入0、可以輸入1): "))
    calories = protein * 4 + carbohydrate * 4 + fat * 9
    carbohydrate_rate = float('{:.2f}'.format(carbohydrate*4 / calories))
    calories_rate = float('{:.2f}'.format(calories / size))
    fat_rate = float('{:.2f}'.format(fat*9 / calories))
    temp.append(i) #0
    temp.append(name) #1
    temp.append(calories) #2
    temp.append(carbohydrate) #3
    temp.append(protein) #4
    temp.append(fat) #5
    temp.append(size) #6
    temp.append(divisible) #7
    temp.append(carbohydrate_rate) #8
    temp.append(calories_rate) #9
    temp.append(fat_rate) #10
    print(temp)
    foods.append(temp)
print("食物陣列:",foods)

cal = calories_per_meal
totalc = 0
totalp = 0
totalf = 0
advise = []
if goal == 1:
    foods.sort( key=takecarbohydr_rate, reverse=True )
    foods.reverse()
    for i in range(n):
        temp2=[]
        name_ad=foods[i][1]
        rate_ad=foods[i][8]
        temp2.append([name_ad,rate_ad])
        advise.append(temp2)
    print("單位大卡的碳水化合物熱量(倒數第三項)小者排序:",advise)
    while cal > 0 and len(foods) != 0 :
        if foods[0][2] <= cal :
            cal -= foods[0][2]
            totalc += foods[0][3]
            totalp += foods[0][4]
            totalf += foods[0][5]
            print('【吃了整份的',foods[0][1],'】,熱量剩餘：{:.2f}'.format(cal))
            foods.pop(0)
        elif foods[0][7] == 1 and cal > 0:
            part = cal / foods[0][2]
            cal -= part * foods[0][2]
            totalc += part*foods[0][3]
            totalp += part*foods[0][4]
            totalf += part*foods[0][5]
            print('【吃了',foods[0][1],'的{:.2f}'.format(part),'份】,熱量剩餘：{:.2f}'.format(cal))
        else:
            foods.pop(0)
elif goal == 3:
    foods.sort(key=takefat_rate, reverse=True )
    foods.reverse()
    for i in range(n):
        temp2=[]
        name_ad=foods[i][1]
        rate_ad=foods[i][9]
        temp2.append([name_ad, rate_ad])
        advise.append(temp2)
    print("單位大卡的脂肪熱量(倒數第一項)小者排序:",advise)
    while cal > 0 and len(foods) != 0:
        if foods[0][2] <= cal :
            cal -= foods[0][2]
            totalc += foods[0][3]
            totalp += foods[0][4]
            totalf += foods[0][5]
            print('【吃了整份的',foods[0][1],'】,熱量剩餘：{:.2f}'.format(cal))
            foods.pop(0)
        elif foods[0][7] == 1 and cal > 0:
            part = cal / foods[0][2]
            cal -= part * foods[0][2]
            totalc += part*foods[0][3]
            totalp += part*foods[0][4]
            totalf += part*foods[0][5]
            print('【吃了',foods[0][1],'的{:.2f}'.format(part),'份】,熱量剩餘：{:.2f}'.format(cal))
        else:
            foods.pop(0)
else:
    foods.sort(key=takecalories_rate, reverse=True )
    foods.reverse()
    for i in range(n):
        temp2=[]
        name_ad=foods[i][1]
        rate_ad=foods[i][8]
        temp2.append([name_ad,rate_ad])
        advise.append(temp2)
    print("單位重量的熱量(倒數第二項)小者排序:",advise)
    while cal > 0 and len(foods) != 0 :
        if foods[0][2] <= cal :
            cal -= foods[0][2]
            totalc += foods[0][3]
            totalp += foods[0][4]
            totalf += foods[0][5]
            print('【吃了整份的',foods[0][1],'】,熱量剩餘：{:.2f}'.format(cal))
            foods.pop(0)
        elif foods[0][7] == 1 and cal > 0:
            part = cal / foods[0][2]
            cal -= part * foods[0][2]
            totalc += part*foods[0][3]
            totalp += part*foods[0][4]
            totalf += part*foods[0][5]
            print('【吃了',foods[0][1],'的{:.2f}'.format(part),'份】,熱量剩餘：{:.2f}'.format(cal))
        else:
            foods.pop(0)
totalcal = totalc*4+totalp*4+totalf*9
if totalcal <= 0:
    totalcal = 0
print("剩餘熱量：",'{:.0f}'.format(cal))
print("攝取總熱量：",'{:.0f}'.format(totalcal))
print('攝取碳水化合物公克：{:.2f}'.format(totalc),'攝取蛋白質公克：{:.2f}'.format(totalp),'攝取脂肪公克：{:.2f}'.format(totalf))

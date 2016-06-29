######## Q1 ########
students = {"Tom":[100,90,88,95,55], "John":[70,78,60,89], "Amy":[50,66,20,88,30], "Bob":[99,64,80,72,90], "Tony":[100,83,92] }
names = ["",""]
scores = [0,100]
for name,grades in students.items():
    score = sum(grades)/len(grades)
    if score > scores[0]:
        scores[0] = score
        names[0] = name
    if score < scores[1]:
        scores[1] = score
        names[1] = name
data = list(zip(names,scores))
print('The highest:%s,%f'%(data[0][0],data[0][1]) )
print('The lowest:%s,%f'%(data[1][0],data[1][1]) )


####### Q2 #########

zipcode = {"台北市":{"中正區": 100, "大同區": 103, "中山區": 104, "松山區": 105, "大安區": 106, "萬華區": 108, "信義區": 110, "士林區": 111, "北投區": 112, "內湖區": 114, "南港區": 115, "文山區": 116}, "基隆市":{"仁愛區": 200, "信義區": 201, "中正區": 202, "中山區": 203, "安樂區": 204, "暖暖區": 205, "七堵區": 206},"新北市": {"萬里區": 207, "金山區": 208, "板橋區": 220, "汐止區": 221, "深坑區": 222, "石碇區": 223, "瑞芳區": 224, "平溪區": 226, "雙溪區": 227, "貢寮區": 228, "新店區": 231, "坪林區": 232, "烏來區": 233, "永和區": 234, "中和區": 235, "土城區": 236, "三峽區": 237, "樹林區": 238, "鶯歌區": 239, "三重區": 241, "新莊區": 242, "泰山區": 243, "林口區": 244, "蘆洲區": 247, "五股區": 248, "八里區": 249, "淡水區": 251, "三芝區": 252, "石門區": 253}}

def area_to_zip(area):
    for city,area_zip in zipcode.items():
        if area_zip.get(area):
            print(city,area_zip[area])

def zip_to_area(code):
    for city,area_zip in zipcode.items():       
        for _area,_zip in area_zip.items():
            if _zip == int(code):
                print(city, _area)


# 傳入值為區域名稱回傳此區域的郵遞區號
input_area = input('請輸入區域名稱查詢郵遞區號:')
area_to_zip(input_area)

# 傳入值為郵遞區號回傳區域名稱
input_zip = input('請輸入3碼郵遞區號查詢區域名稱:')
zip_to_area(input_zip)
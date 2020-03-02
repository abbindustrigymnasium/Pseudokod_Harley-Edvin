stop = False
Money = int(13input("Hur mycket pengar har Bengan?\n"))
pack = int(Money / 30)
cost = pack * 30
Left = Money - cost
sum = int(Left / 13.95)
Total = sum + pack * 3

while stop == False:
    if Money > 13.94:
        print("Bengan kan maximalt köpa",Total,"tonfiskburkar")
        stop = True

    else: 
        print("Bengan kan tyvärr inte köpa någon tonfiskburk")
        stop = True
        

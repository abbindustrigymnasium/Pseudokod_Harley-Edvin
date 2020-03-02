schoolmonth = 9
extramonth = 1
totalmonth = (schoolmonth + extramonth) * 3
sum = totalmonth * 1250
stop = False

while stop == False:
    Question = input("Fyllde du 16 år mellan juli och september?\n")

    if Question == "Ja":
        total1 = sum - 625
        print("Du får under dina 3 år på gymnasiet", total1,"kronor")
        stop = True
    elif Question == "Nej":
        print("Du får under dina 3 år på gymnasiet", sum,"kronor")
        stop = True
    else:
        print("Skriv Ja eller Nej din imbicill!")

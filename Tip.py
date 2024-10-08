def Total_calc(Billamount,tip):
    Total=Billamount*(1+0.01*tip)
    Total=round(Total,2)
    print(F"Please pay ${Total}")
Total_calc(150,20)
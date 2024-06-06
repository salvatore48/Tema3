hrs = float(input('hrs ==>'))
rate = float(input('rate ==>'))
tpay:float()
if hrs <= 40:
    pay = hrs * rate
    print('pay =', pay)
if hrs > 40 :
    pay1 = (40 * rate)
    print(pay1)
    pay2 = (hrs - 40) * (1.5 * rate)
    print(pay2)
    tpay = (pay1 + pay2)
    print("Pay: ", tpay)


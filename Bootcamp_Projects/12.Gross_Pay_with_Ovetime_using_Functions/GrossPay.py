#definition of Gross pay function
def GrossPay(hours,rate):
    if hours > 40:
        pay = ((hours - 40) * 1.5 * rate) + (40 * rate)
        return pay
    else:
        pay = hours * rate
        return pay
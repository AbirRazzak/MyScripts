# Enter current value of your funds here
# Replace number in parenthesis with current asking price
# Replace 0 at the end with intended number of shares to buy
__domestic_stock__ = 0.00 + (83.180) * 0
__international_stock__ = 0.00 + (57.010) * 0
__bond__ = 0.00 + (88.120) * 0

# Calculates % and displays target % based on the 64/16/20 allocation method for the three-fund portfolio
if __name__ == "__main__":
    total = __domestic_stock__ + __international_stock__ + __bond__
    print('Current Domestic Stocks:\t{0:.2f}% (Target 64%)\nCurrent International Stocks:\t{1:.2f}% (Target 20%)\nCurrent Bond Market:\t\t{2:.2f}% (Target 16%)'.format(
      __domestic_stock__/total * 100,
      __international_stock__/total * 100,
      __bond__/total * 100
    ))

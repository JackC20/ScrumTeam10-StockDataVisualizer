print("Stock Data Visualizer\n---------------------\n")
# Gets the stock symbol from the user
stockName = input("Enter the stock symbol you are looking for: ")
print("Chart Types\n-----------\n1. Bar\n2. Line\n")
# Gets the chart type from the user
while(True):
    try:
        chartType = int(input("Enter the chart type you want (1, 2): "))
        if chartType != 1 and chartType != 2:
            print("Enter a 1 or 2 for chart type")
            continue
    except:
        print("Enter a 1 or 2 for chart type")
        continue
    else:
        break
print("Select the time series of the chart you want to Generate\n--------------------------------------------------------\n1. Intraday\n2. Daily\n3. Weekly\n4. Monnthly")
# Gets the time series from the user
while(True):
    try:
        timeSeries = int(input("Enter time series option (1, 2, 3, 4): "))
        # Check if the time series is valid
        if timeSeries != 1 and timeSeries != 2 and timeSeries != 3 and timeSeries != 4:
            print("Enter either 1, 2, 3, or 4 for time series")
            continue
    except:
        print("Enter either 1, 2, 3, or 4")
        continue
    else:
        break
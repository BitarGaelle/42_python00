def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def recursive(days):
        if (days == 0):
            return
        recursive(days - 1)
        print("Day", days)
    recursive(days)
    print("Harvest time!")

def laps_to_miles(laps):
    miles = laps / 4
    return miles

if __name__ == '__main__':
    laps = float(input())
    miles = laps_to_miles(laps)
    print(f'{miles:.2f}')
    
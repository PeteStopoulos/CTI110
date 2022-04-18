def feet_to_steps(num_feet):
    steps = int(num_feet / 2.5)
    return steps

if __name__ == '__main__':
    feet = float(input())
    steps = feet_to_steps(feet)
    print(steps)
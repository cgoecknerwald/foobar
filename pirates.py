
def answer(numbers):
    pirate_list = []
    current_pirate = 0
    while (current_pirate not in pirate_list):
        pirate_list.append(current_pirate)
        current_pirate = numbers[current_pirate]
        
    return len(pirate_list[pirate_list.index(current_pirate):])

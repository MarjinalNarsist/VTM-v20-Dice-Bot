import random
import json

# args type is tuple :('7', 'sw')


def roll(dice):
    dice_nr = dice.split("d")
    roll_result = [random.randint(1, int(dice_nr[1])) for _ in range(int(dice_nr[0]))]
    return roll_result


def calculate(dices, args):

    # Modifiers
    specialty=False
    difficulty=6
    success=0
    for key in args:
        if key.isdigit():
            difficulty = int(key)
        elif key== "sw" or key== "ws":
            specialty=True
            success+=1
        elif "w" in key:
            success+=1
        elif "s" in key:
            specialty=True

    # Result Calculation
    botches=dices.count(1)
    successful_dices=[nr for nr in dices if nr>=difficulty]

    # If it is success
    if len(successful_dices)+success>botches:
        for times in range(botches):
            successful_dices.pop(successful_dices.index(max(successful_dices)))
        if specialty:
            success+= successful_dices.count(10)
        success+= len(successful_dices)
        return f"{success} Success!"

    # If it is fail
    elif len(successful_dices)+success== botches:
        return "Fail!"

    # If it is botched
    elif len(successful_dices)+success<botches:
        botches=botches-len(successful_dices)-success
        if botches== 1:
            return "Botched!"
        elif botches== 2:
            return "DOUBLE BOTCHED!"
        elif botches==3:
            return "TRIPLE BOTCHED!!!"
        elif botches==4:
            return "STOP PLAYING, YOU DIED!"


def test(dice, *args):
    dices=roll(dice)
    result=calculate(dices, args)
    print(f'Dices: {dices}\nResult: {result}')


def combat(modifier, character):
    output=""
    place=1
    dice= random.randint(1, 10)
    user_result=dice+int(modifier)
    user_values={character: user_result}
    # Read existing combat list file
    with open("combat_order.json") as file:
        combat_order= json.load(file)
    combat_order.update(user_values)
    # Add to combat list file
    with open("combat_order.json", "w") as file:
        json.dump(combat_order, file)
    sorted_order= sorted(combat_order.items(), key=lambda x: x[1], reverse=True)
    for name, score in sorted_order:
        output= output+str(place)+str(name)+":"+str(score)+"\n"
        place+=1
    return output


def reset_combat():
    combat_order={}
    with open("combat_order.json", "w") as file:
        json.dump(combat_order, file)

# test("4d10")

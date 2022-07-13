from unittest import result


def countChange(cost, paid):
    change = paid-cost
    coins = 0
    while(change!=0):
        if change>=20:
            coins+=change//20
            change = change%20
        elif change>=10:
            coins+=change//10
            change = change%10
        elif change>=5:
            coins+=change//5
            change = change%5
        elif change>=2:
            coins+=change//2
            change = change%2
        elif change>=1:
            coins+=change//1
            change = change%1
    return coins


if __name__ == "__main__":
    cost = int(input("Enter total cost: "))
    paid = int(input("Enter amount paid: "))
    result = countChange(cost, paid)
    print(result)

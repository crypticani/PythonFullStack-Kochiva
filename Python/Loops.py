def countChange(cost, paid):
    change = paid-cost
    coins = 0
    D = [20, 10, 5, 2, 1]
    i=0
    while(change!=0):
        if change>=D[i]:
            coins+=change//D[i]
            change = change % D[i]
        else:
            i+=1
    return coins


if __name__ == "__main__":
    cost = int(input("Enter total cost: "))
    paid = int(input("Enter amount paid: "))
    result = countChange(cost, paid)
    print(result)

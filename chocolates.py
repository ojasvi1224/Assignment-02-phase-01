n = 13
x=int(input("how much player 1 take choclate(1 or 2):"))
def player_1(n):
    if n <= 0:
        return "Player 1 wins!"
    return player_2(n-x)
def player_2(n):
    if n <= 0:
        return "Player 2 wins!"
    if n % 2 == 0:
        return player_1(n-2)
    else:
        return player_1(n-1)
player_1(n)
player_2(n)
print(player_1(n))

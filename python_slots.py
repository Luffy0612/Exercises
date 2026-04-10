#Slot Machine
import random
def row_spin(balance,bet):
    symbols=['🍊','⭐','🍉','🍇','🔔']
    payout=0
    results=(random.choices(symbols,weights=(3,5,1,2,4),k=3))
    print("*************")
    print(" | ".join(results))
    print("*************")
    if results[0]==results[1]==results[2]:
         print("Congrats you've hit a jackpot!!")
         if results[0]=='🍊':
              print("Hurray your reward is now 12x of your bet!!")
              (bet)*=12
              payout+=bet
              print(f"Reward: ${payout}")
              print(f"Balance: ${balance+payout}")
              balance+=bet
         elif results[0]=='⭐':
              print("Hurray now your reward is 20x of your bet!!!!")
              (bet)*=20
              payout+=bet
              print(f"Reward: ${payout}")
              print(f"Balance: ${balance+payout}")
              balance+=bet
         elif results[0]=='🍉':
              print("Hurray now your rewars is 5x of your bet!")
              (bet)*=5
              payout+=bet
              print(f"Reward: ${payout}")
              print(f"Balance: ${balance+payout}")
              balance+=bet
         elif results[0]=='🍇':
              print("Hurray now your reward is 9x of your bet!!")
              (bet)*=9
              payout+=bet
              print(f"Reward: ${payout}")
              print(f"Balance: ${balance+payout}")
              balance+=bet
         else:
              print("Hurray now your reward is 15x of your bet!!!")
              (bet)*=15
              payout+=bet
              print(f"Reward: ${payout}")
              print(f"Balance: ${balance+payout}")
              balance+=bet
    else:
         print("Awww better luck next time....")
         print(f"Reward: ${payout}")
         print(f"Balance: ${balance+payout}")
         balance+=bet
    return payout    
print("*************************")
print("       CASIO CASINO      ")    
print("*************************")
balance=100
print(f"Balance: ${balance}")
while True:
     bet=int(input("Place a bet amount(999 to quit): $"))
     if bet>balance:
          if bet==999:
               print("Bye have a great time!!")
               break
          else:   
            print("Insufficient Funds!!")
            continue
     elif bet<0:
          print("Enter a valid amount!!")
          continue
     else:
          balance-=bet
          print(f"Bet of ${bet} has been successfully placed...")
     print("Spining....")
     row_spin(balance,bet)
     

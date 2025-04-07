import time
import Player
import keyboard
import random

def LogIn(PlayersList): # This Function Will Return The Object Of The Player 
  while True:
    PlayerPassword = input("Enter Your Password: ")

    for player in PlayersList:
      if (player.GetPassword() == PlayerPassword):
        print(f"Welcome Back {player.GetName()}, Here Is Your Account Information: ")
        print("-----------------------------------")
        print(f"Name: {player.GetName()}")
        print(f"Password: {player.GetPassword()}")
        print(f"Balance: ${player.GetBalance()}")
        print("-----------------------------------")
        time.sleep(5)
        return player
    
    print("❌❌Your Passowrd Isn't Exist, Please Try Again!!❌❌")

def Register(PlayersList):
  name = input("Player Name: ").strip()
  password = input("Player Password: ").strip()

  # This While Loop Is To Check If User Entered A Correct Balance
  while True:
    balance = input("Player Balance: ")
    try:
      balance = float(balance)
      break
    except:
      print("Wrong Balane❌❌ :< Please Enter A Valid Balance Next Time")
      time.sleep(3)


  player = Player.Player(name, password, balance)

  print(f"Welcome \"{player.GetName()}\" To My Game")
  time.sleep(2)

  PlayersList.append(player)

  return player

def StartGame(player):

  SpinsList = [5, 10, 20]
  MoneyList = [5, 9, 17.5]
  Shapes = ["🍋", "🍒", "⭐", "7️⃣"]
  WinMoney = 0

  print(f"So \"{player.GetName()}\", How Many Spins You Want To Get?")
  print("Quick Note*: If You Won In A Spin You Will Get $2")
  print("1) [5] Spins  ->  $5")
  print("2) [10] Spins ->  $9")
  print("3) [20] Spins ->  $17.5")
  
  while True:
    try:
      UserChoice = int(input("Choose Number [1-3]: "))
      if (UserChoice > 3 or UserChoice < 1):
        print("Please Enter A Number From 1 To 3")
        continue
      break
    except:
      print("Please Enter A Number From 1 To 3")

  Spins = SpinsList[UserChoice-1]
  player.WithDraw(MoneyList[UserChoice-1]) # WithDraw The Money

  print(f"Cool Your New Balance Now Is ${player.GetBalance()}")
  time.sleep(2)

  while Spins > 0:

    print(f"So Click On 's' On Your KeyBoard To Start")

    RandomShapesIdx = []

    keyboard.wait("s")
    if (keyboard.is_pressed('s')):

      for _ in range(3):
        RandomIdx = random.randint(0, 3)
        RandomShapesIdx.append(RandomIdx)  # This List Is To Compare All Shapes Which Appears Whith Each Others To Get The Result
        print(Shapes[RandomIdx], end=" ", flush=True)
        time.sleep(2)

      print("")

      if (all(i == RandomShapesIdx[0] for i in RandomShapesIdx)): # if All elements Is Like The First element so the player won
        WinMoney +=2
        print(f"Amazing!!💥✊, Your Win Money Now Is ${WinMoney}")
        time.sleep(2)
      
      else:
        print("Unfortunately!!😟😢")
        time.sleep(2)
      
      RandomShapesIdx.clear()
      Spins -= 1

      if (Spins != 0):
        print(f"You Have {Spins} Spins Left")
    
  player.Deposit(WinMoney)

  print(f"Your Balance After Adding The Win Money Is {player.GetBalance()}")







def main():

  print("Hello Welcome To My Slot Machine Game!!")
  
  PlayersList = []  # This List Will Has All The Players Objects

  while True:
    mode = input("Do You Have An Account? (y, register, quit): ").lower()

    play = "y"

    if (mode == "y"):
      player = LogIn(PlayersList)
      while play == "y":
        StartGame(player)
        play = input("Do You Want To Play Again? (y,n)")

    elif (mode == "register"):
      player = Register(PlayersList)
      while play == "y":
        StartGame(player)
        play = input("Do You Want To Play Again? (y,n)")

    elif (mode == "quit"):
      quit()

    else:
      print("Please Enter A Valid Input Next Time")


if (__name__ == '__main__'):
  main()
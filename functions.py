from binance.enums import *
import math
import os
import getpass
import sys

def readKeys() :
    #Get the user name
    userName = getpass.getuser()
    path = "C:\\Users\\"+userName+"\\.BinanceBot"

    #If the dir doesn't exist
    if( not os.path.isdir(path)):
        os.mkdir(path)

        #Get the keys
        pubK = input("Type the ApiKey: ")
        prK = input("Type the SecretKey: ")

        f = open(path + "\\keys.txt","w+")

        #Create the txt 
        f.write("ApiKey="+pubK+"\n")
        f.write("SecretKey="+prK)
        f.close()

        done = input("You want to sell everything? (yes or no): ")
        
        if(done == "no"):
            sys.exit()


    with open(path + "\\keys.txt") as file:
        data=file.readlines()
    
    publicKey=data[0].split("=")[1].rstrip("\n")
    privateKey=data[1].split("=")[1]

    file.close()

    return (publicKey,privateKey)


def getMyBalances(info):
    data = []
  
    for balance in info["balances"]:
        if(balance["free"]!="0.00000000" and balance["free"]!="0.00"):
            data.append(balance)

    return data

def sellAll(balances, client,exchange):
    for balance in balances:
        try:
            if(balance["asset"]!="USDT"):
                order = client.create_order(
                    symbol= balance["asset"]+"USDT",
                    side=SIDE_SELL,
                    type=ORDER_TYPE_MARKET,
                    quantity=truncate(float(balance["free"]),numberOfDecimals(exchange,balance["asset"]+"USDT")))

        except Exception as e:
            print(balance["asset"] + " error")
            print(e)
       
       
           
def printBalances(balances):
    for balance in balances:
        print(balance["asset"] + " : "  + balance["free"])

def numberOfDecimals (exchange, symbol):
    
    cont = 0

    for s in exchange["symbols"]:
    
        if(s["symbol"]== symbol):
            i=0
            done = False
            decimals = False
            
            
            while(not done):

                x = s["filters"][2]["minQty"][i]
                
                i=i+1

                if(decimals):
                    cont = cont+1
                
                if(x=="."): 
                    decimals = True

                if(i == len(s["filters"][2]["minQty"]) or x == "1"):
                    done = True
                    
            break
   
    return cont
    


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper
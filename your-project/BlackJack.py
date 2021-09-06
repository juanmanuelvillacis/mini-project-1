'''
To Do!
# Crear el fin del juego cuando se acaba el dinero
# verificar si se repite el reparto de cartas en la primera mano
# verificar si el house se queda sin dinero
# crear el input de con cuanto dinero entra el player y asigar a la instancia
# imprimir mensaje que cago la casa o el jugador
#print(chr(27) + "[2J")
'''



from random import shuffle
# crea el deck de 52 cartas
def createDeck ():
    Deck = []
    faceValues = ["A","J","Q","K"]
    for i in range(4):
        for card in range(2,11):
            Deck.append(str(card))
        for card in faceValues:
            Deck.append(card)
    shuffle(Deck)
    return Deck



#print(cardDeck)

class Player:
    def __init__(self, hand = [],money = 10):
        self.hand = hand
        self.score = self.setScore()
        self.money = money
        self.bet = 0
    #print el status general del jugador
    def __str__(self):
        currentHand = ""
        for card in self.hand:
            currentHand += str(card) + " "
        finalStatus =  currentHand + "\n"+"The score is :" + str(self.score)
        return finalStatus
    # suma los puntos del jugador en su mano
    def setScore(self):
        self.score = 0
        faceCardsDict = {"A":11,"J":10,"Q":10,"K":10,
                        "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
        aceCounter = 0
        for card in self.hand:
            self.score += faceCardsDict[card]
            if card == "A":
                aceCounter += 1
            if self.score > 21 and aceCounter != 0:
                self.score -=10
                aceCounter -=1
        return self.score
    # hit card to player
    def hit (self,card):
        self.hand.append(card)
        self.score = self.setScore()
    # nueva ronda cuando ya termino la mano
    def play (self,newHand):
        self.hand = newHand
        self.score = self.setScore()
        
    # manejo de la apuesta con respecto a la mano y al $ total del jugador
    def betMoney (self,amount):
        self.money -= amount
        self.bet += amount
    # define el ganador de la mano, chequeando por blackjack
    def win (self,result):
        if result == True:
            if self.score == 21 and len(self.hand) == 2:
                self.money += 2.5*self.bet
                print("You have BlackJack!")
            else:
                self.money += 2*self.bet
            self.bet = 0
            print("You won!")
        else:
            self.bet = 0
            print("You loose!")
    # en caso de empate se devuelve el dinero y apuesta de la mano = 0
    def draw(self):
        self.money += self.bet
        self.bet = 0
        print('This hand is a draw!')
    # revisa el blackjack de la casa
    def hasBlackjack (self):
        if self.score == 21 and len(self.hand) == 2:
            return True
        else:
            return False
# Muestra la mano de la casa, con una carta escodida y la otra no
def printHouse (House):
    print('House cards are: ')
    for card in range(len(House.hand)):
        if card == 0:  
            #var1 = "X"  # Verifica si es la primera carta de la mano de la casa y la esconde
            print("X",end = " ")
        elif card == len(House.hand) -1: # verifica la segunda carta de la mano de la casa y la muestra, al comienzo de la mano 
           #var2= House.hand[card]
           print(House.hand[card])
        else:
            print(House.hand[card], end = " ") # imprime el resto de las cartas en la mano
    #print("House cards are: " + var1+var2)

cardDeck = createDeck() # primero se crea el mazo

firstHand = [cardDeck.pop(),cardDeck.pop()] # se reparte las cartas al jugador
secondHand = [cardDeck.pop(),cardDeck.pop()]    # se reparte las cartas a la casa
Player1 = Player(firstHand)     # Se crea un jugador P1 con todas las caracteristicas de la clase Player
House = Player(secondHand,100000)      # Se crea un jugador House con todas las caracteristicas de la clase Player
cardDeck = createDeck()         # se barajea 2 veces
print("Welcome to Bolivar's Casino!")

while (Player1.money>0):
    
    # verifica que siempre hayan mas de 20 cartas en el deck
    if len(cardDeck) < 20:
        cardDeck = createDeck()
                                                                    # verificar si se repite el reparto de cartas en la primera mano
    firstHand = [cardDeck.pop(),cardDeck.pop()]
    secondHand = [cardDeck.pop(),cardDeck.pop()]
    Player1.play(firstHand)
    House.play(secondHand)
    
    Bet = int(input("Your Money is " + str(Player1.money) +"\n"+"Enter your bet: "))
    Player1.betMoney(Bet)
    printHouse(House)
    print('Player cards are: ')
    print(Player1)
    if Player1.hasBlackjack():
        if House.hasBlackjack():
            Player1.draw()
        else:
            Player1.win(True)
    else:
        while (Player1.score <= 21):
            action = input("Do you want another card?(y:yes else:no) ")              # verificar si el imput es Y/N, de lo contrario repetir
            if action == "y":
                Player1.hit(cardDeck.pop())
                print('Player cards are: ')
                print(Player1)
                printHouse(House)
            else:
                break
                                 # verificar que la casa pida cartas hasta sumar 16
        while(House.score <= 16):
            print('House cards are: ')
            print(House)
            House.hit(cardDeck.pop())
        if Player1.score > 21:
            if House.score > 21:
                Player1.draw()
            else:        # opciones cuando el jugador tiene + de 21
                Player1.win(False)
        elif Player1.score > House.score:       # opciones cuando tiene - de 21
                Player1.win(True)
        elif Player1.score == House.score:
            Player1.draw()
        else:                                  
            if House.score > 21:            # si la casa tiene + de 21
                Player1.win(True)
            else:
                Player1.win(False)
               # si la casa tiene - de 21 y el jugador tiene menos que la casa
    #print('Your money is: ')
    #print(Player1.money)
    print('House cards are: ')
    print(House)
print('Thanks for playing, you are out of money!')

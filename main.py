class Queue():
    def __init__(self):
        self.arr = []  # Initializes the queue with an empty list
        self.size = 0  # Initializes the size of the queue to 0

    def enqueue(self, value):
        self.arr.append(value)  # Adds a value to the end of the queue
        self.size += 1  # Increments the queue size

    def dequeue(self):
        self.size -= 1  # Decrements the queue size
        # Removes and returns the first element of the queue
        return self.arr.pop(0)

    def isEmpty(self):
        return self.size == 0  # Returns True if the queue is empty, False otherwise

    def first(self):
        # Returns the first element of the queue without removing it
        return self.arr[0]

    def get_size(self):
        return self.size  # Returns the current size of the queue

    def __str__(self):
        return str(self.arr)  # Returns a string representation of the queue


cardValues = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
              'J', 'Q', 'K', 'A']  # List of card values for ranking


def war(warCardsP1, warCardsP2):
    # A function to handle the 'war' scenario when both players draw cards of equal rank
    for i in range(3):
        if deckP1.isEmpty() or deckP2.isEmpty():
            return -1  # Returns -1 if either deck runs out of cards, indicating a 'PAT'
        else:
            # Players put three cards in the war pot
            warCardsP1.enqueue(deckP1.dequeue())
            warCardsP2.enqueue(deckP2.dequeue())

    battleCardP1 = deckP1.dequeue()  # The battling cards are drawn after the war cards
    battleCardP2 = deckP2.dequeue()

    warCardsP1.enqueue(battleCardP1)  # Add battling cards to the war pot
    warCardsP2.enqueue(battleCardP2)

    if battleCardP1 == battleCardP2:
        # Recursive call if the battling cards are equal again
        return war(warCardsP1, warCardsP2)

    # Determine the winning deck
    winnningDeck = deckP1 if battleCardP1 > battleCardP2 else deckP2

    # Move all cards from the war pot to the winning deck
    for i in range(warCardsP1.get_size()):
        winnningDeck.enqueue(warCardsP1.dequeue())
    for i in range(warCardsP2.get_size()):
        winnningDeck.enqueue(warCardsP2.dequeue())

    return 1  # Indicates a successful resolution of war


def getGameResult(deckP1, deckP2):
    # Function to simulate the game and determine the result
    rounds = 0
    while True:
        if deckP1.isEmpty() and deckP2.isEmpty():
            return ["PAT"]  # Game ends in a tie if both decks run out of cards
        if deckP1.isEmpty():
            # Player 2 wins if Player 1's deck runs out of cards
            return [2, rounds]
        if deckP2.isEmpty():
            # Player 1 wins if Player 2's deck runs out of cards
            return [1, rounds]

        rounds += 1  # Increment the round count
        battleCardP1 = deckP1.dequeue()  # Players draw cards for the battle
        battleCardP2 = deckP2.dequeue()

        if battleCardP1 == battleCardP2:
            warCardsP1 = Queue()  # Initialize war pots
            warCardsP1.enqueue(battleCardP1)

            warCardsP2 = Queue()
            warCardsP2.enqueue(battleCardP2)

            # Conduct a war if the battle cards are equal
            result = war(warCardsP1, warCardsP2)

            if result == -1:
                # Game ends in a tie if a war cannot be resolved
                return ["PAT"]
        else:
            # Determine the winning deck
            winnningDeck = deckP1 if battleCardP1 > battleCardP2 else deckP2
            # Move battle cards to the winning deck
            winnningDeck.enqueue(battleCardP1)
            winnningDeck.enqueue(battleCardP2)



deckP1 = Queue()
deckP2 = Queue()

# Input for Player 1
while True:
    try:
        n = int(input("Enter the number of cards for Player 1 (1-999): "))
        if 0 < n < 1000:
            break
        else:
            print("Please enter a number between 1 and 999.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Enter the cards for Player 1:")
for i in range(n):
    while True:
        card_p1 = input(f"Card {i+1}: ").strip().upper()
        if card_p1[:-1] in cardValues:
            deckP1.enqueue(cardValues.index(card_p1[:-1]))
            break
        else:
            print("Invalid card. Please enter a valid card value (e.g., '2H', 'JC').")

# Input for Player 2
while True:
    try:
        m = int(input("\nEnter the number of cards for Player 2 (1-999): "))
        if 0 < m < 1000:
            break
        else:
            print("Please enter a number between 1 and 999.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Enter the cards for Player 2:")
for i in range(m):
    while True:
        card_p2 = input(f"Card {i+1}: ").strip().upper()
        if card_p2[:-1] in cardValues:
            deckP2.enqueue(cardValues.index(card_p2[:-1]))
            break
        else:
            print("Invalid card. Please enter a valid card value (e.g., '2H', 'JC').")

# Game Result
result = getGameResult(deckP1, deckP2)

# Result Output
if result[0] == 'PAT':
    print("\nThe game ends in a tie (PAT).")
else:
    print(f"\nPlayer {result[0]} wins after {result[1]} rounds.")

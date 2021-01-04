class Yatzy:

    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice): 
        amount = 0
        for side in dice:
            amount += side
        return amount
        
    @staticmethod
    def yatzy(dice):
        for side in dice:
            if dice.count(side) == 5: 
                return 50                   
            break
        return 0

    @staticmethod
    def ones(*dice):
        one = 1
        return dice.count(one) * 1  

    @staticmethod
    def twos(*dice):
        two = 2
        return dice.count(two) * 2

    @staticmethod
    def threes(*dice):
        three = 3
        return dice.count(three) * 3

    def fours(self):       
        four = 4
        return self.dice.count(four) * 4

    def fives(self):
        five = 5
        return self.dice.count(five) * 5

    def sixes(self):
        six = 6
        return self.dice.count(six) * 6
    
    @staticmethod
    def score_pair(*dice):
        amount = 0                                              
        for side in dice:                                       
            if dice.count(side) == 2 and amount < side * 2:     
                amount = side * 2                               
        return amount                                           
    
    @staticmethod
    def two_pair(*dice):
        amount = 0
        repetidos = []
        contador_pair = 0
        for side in dice:
            if dice.count(side) >= 2 and side not in repetidos: ##LISTO
                amount += side * 2
                repetidos.append(side)
                contador_pair += 1
            if contador_pair == 2:
                return amount
        return 0

    @staticmethod
    def four_of_a_kind(*dice):
        amount = 0
        for side in dice:
            if dice.count(side) >= 4: ##LISTO
                amount = side * 4
            return amount

    @staticmethod
    def three_of_a_kind(*dice):
        amount = 0
        for side in dice:
            if dice.count(side) >= 3:   ##LISTO
                amount = side * 3
        return amount   

    @staticmethod
    def smallStraight(*dice):
        if sorted(dice) == [1,2,3,4,5]:
            return 15
        return 0

    @staticmethod
    def largeStraight(*dice):
        if sorted(dice) == [2,3,4,5,6]:
            return 20
        return 0

    @staticmethod
    def fullHouse(*dice):
        amount = 0
        double = False
        triple = False
        for side in dice:
            if dice.count(side) == 2 and double is False:
                amount += side * 2
                double = True
            if dice.count(side) == 3 and triple is False:
                amount += side * 3
                triple = True
            if triple is True and double is True:
                return amount
        return 0


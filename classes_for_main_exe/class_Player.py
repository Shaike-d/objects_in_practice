class Player:

    def __init__(self,name):
        self.name = name
        self.score = 0

    def add_points(self,num):
        self.score += num

    def __str__(self):
        return f"{self.name}: {self.score}"


def answer_1():
    players = [Player("Dana"), Player("Avi"), Player("Noa")]
    players[0].add_points(50)
    players[1].add_points(15)
    players[2].add_points(40)
    best_score = 0
    top_player = None
    for player in players:
        if player.score > best_score:
            best_score = player.score
            top_player = player.name
    print(f"leader: {top_player}: {best_score}")

         
    




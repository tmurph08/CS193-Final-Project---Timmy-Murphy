squad = []   # Squad to be printed to file

class Player:   # Player class!
    def __init__(self, name, pos, num, signed, height, born, debut, nation, bio, gp, mp, assists, goals):
        self.name = name   # Name
        self.pos = pos   # Position
        self.num = int(num)   # Jersey number
        self.signed = signed   # Date signed
        self.height = height   # Height (cm)
        self.born = born   # Date of birth
        self.debut = debut   # Date of debut game for West Ham
        self.nation = nation   # Nationality
        self.bio = bio   # Biography
        self.gp = int(gp)   # Number of games played (this season)
        try:
            self.mp = int(mp)   # Minutes played
        except:
            iComma = mp.index(",")
            self.mp = int(mp[:iComma] + mp[iComma + 1:])   # if there is a comma in the number, delete the comma
        self.assists = int(assists)   # Number of assists (this season)
        self.goals = int(goals)   # Number of goals scored (this season)
        self.attributes = [self.name, self.pos, self.num, self.shoots, self.signed, self.height, self.born, self.debut, self.nation, self.weight, self.debutGame, self.alias, self.bio, self.gp, self.mp, self.starts, self.assists, self.goals]

    def __str__(self):   # toString returns name, position, and jersey number
        return f"Player: {self.name}\nPosition: {self.pos}\nNumber: {self.num}\n"

def write():   # Write data to a file
    data = open("West Ham Data.txt", "w")   # Open "West Ham Data.txt" in write mode (creates file if needed)
    textToWrite = "Name\tPosition\tNumber\tNationality\tGames Played\tGoals\tAssists\n"   # Data to be written to the file
    data.write(textToWrite)   # Writes header on file
    for player in squad:
        textToWrite = player.name + "\t" + player.pos + "\t" + str(player.num) + "\t" + player.nation + "\t" + str(player.gp) + "\t" + str(player.goals) + "\t" + str(player.assists) + "\n"   # Gathers data to be written about a player
        data.write(textToWrite)   # Writes data
    data.close()   # Closes writer


# NOT pip install
# py -m pip install

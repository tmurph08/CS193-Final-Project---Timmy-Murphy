import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options)

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
        self.gp = int(gp)   # Number of games played (this season)
        try:
            self.mp = int(mp)   # Minutes played
        except:
            iComma = mp.index(",")
            self.mp = int(mp[:iComma] + mp[iComma + 1:])   # if there is a comma in the number, delete the comma
        self.assists = int(assists)   # Number of assists (this season)
        self.goals = int(goals)   # Number of goals scored (this season)
        self.attributes = [self.name, self.pos, self.num, self.signed, self.height, self.born, self.debut, self.nation, self.gp, self.mp, self.assists, self.goals]

    def __str__(self):   # toString returns name, position, and jersey number
        return f"Player: {self.name}\nPosition: {self.pos}\nNumber: {self.num}\n"

def scrape():
    scrape = requests.get("https://www.whufc.com/en/teams/mens-team/mads-hermansen")   # Starting link
    currentNumber = ""   # Number of current player
    while currentNumber != "66":   # Scrapes until hitting the last player (not on loan, not a coach)
        soup = BeautifulSoup(scrape.content, "html.parser")   # Makes BeautifulSoup object
        mainInfo = soup.find("div", class_="profileHero_mainInfo__p4f3J")   # Finds summary info about a player
        number = mainInfo.find("div", "profileHero_playerNumber__O1Q2x").text   # Finds player number
        fNameLoc = mainInfo.find("div", class_="profileHero_firstName__xLp59")   # Finds location of player first name
        fName = ""
        if (fNameLoc != None):   # Formats player first name if they have one (accounts for players without first name)
            fName = fNameLoc.text + " "
        name = fName + mainInfo.find("div", class_="profileHero_lastName__vqwzU").text   # Sets up player name with first name and finds and adds last name
        position = mainInfo.find("span", class_="profileHero_position__S51lz").text   # Finds position
        currentNumber = number   # Updates currentNumber to check which player scraper is on
        player = Player(name, position, number, None, None, None, None, None, None, 0, 0, 0, 0)   # Makes new Player object with data
        print(player)
        nextPlayer = soup.find("span", string="Next Player")   # Looks for "Next Player" prompt in corner of website
        parent = nextPlayer.parent
        parent2 = parent.parent
        linkEnd = parent2["href"]   # Finds link embedded in website
        link = "https://www.whufc.com" + str(linkEnd)   # Formats link
        scrape = requests.get(link)   # Updates website needing to be scraped

def main():
    scrape()

if __name__ == "__main__":
    main()

def write():   # Write data to a file
    data = open("West Ham Data.txt", "w")   # Open "West Ham Data.txt" in write mode (creates file if needed)
    textToWrite = "Name\tPosition\tNumber\tNationality\tGames Played\tGoals\tAssists\n"   # Data to be written to the file
    data.write(textToWrite)   # Writes header on file
    for player in squad:
        textToWrite = player.name + "\t" + player.pos + "\t" + str(player.num) + "\t" + player.nation + "\t" + str(player.gp) + "\t" + str(player.goals) + "\t" + str(player.assists) + "\n"   # Gathers data to be written about a player
        data.write(textToWrite)   # Writes data
    data.close()   # Closes writer

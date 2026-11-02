# Project Name

West Ham Web Scraper - this is a web scraper for my favorite soccer team, West Ham United, that gathers statistics for each player and saves them

## The Problem

I want to have a convenient place to analyze the statistics of the soccer players from my favorite soccer team (West Ham United). I could look up the stats and save them to a spreadsheet myself, but that would be time-consuming, and when the stats get updated, I would have to redo the entire process again.

## How It Works

The program creates a class to store player info, then sends out two different web scrapers, which each have different purposes, to scrape data from the West Ham website (whufc.com). The scrapers then send back the data to the program to be stored in the Player class, which is then written to a file in tsv format. The file can then be copied and pasted into google sheets for easy data analysis.

![System diagram]([docs/SystemDiagram.png])

## Tech Stack

- **Language:** Python
- **Libraries:** BeautifulSoup, Selenium
- **External tools:** Google sheets (for data analysis)

## Setup

Step-by-step: how does someone who just cloned your repo get it
running?

```bash
git clone https://github.com/you/your-project
cd your-project
./install.sh   # or whatever
```

## Usage

How to actually run the thing, with examples.

```bash
./backup.sh ~/Documents
```

## Roadmap

- [ ] One-page website for summary stats
- [ ] Program works for more teams, not just West Ham
- [ ] Statistical analysis in Python, not Google Sheets

## Author

Timmy Murphy, [GitHub](https://github.com/tmurph08)

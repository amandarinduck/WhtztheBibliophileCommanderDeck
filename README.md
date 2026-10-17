<b> Whtz, the Bibliophile Full Commander Deck</b>

<i> because blue definitely needed more cards... </i>


This repo contains a scraped csv of every blue/white card from the scryfall API, passed into a jupyter notebook for manipulation via pandas as a giant dataframe contining 14952 cards in total


Currently has only a few deck functions that need to be logged manually(i.e. tapping for mana) as I haven't dared to use this in an actual game yet, it's still under construction, but if you wanna give it a spin load WhtzCommanderDeck.ipynb and the decklist csv

Cards were pulled via scrython, a python wrapper for the scryfall API
https://github.com/NandaScott/Scrython

Methods for scraping are detailed in WhtzUWDeckScraping.ipynb

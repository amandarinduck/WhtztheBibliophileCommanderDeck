<b> Whtz, the Bibliophile Kitchen Sink Commander Deck</b>

<i> Because blue definitely needed more cards... </i>


This repo contains a scraped csv of every blue/white card from the scryfall API, passed into a jupyter notebook for manipulation via pandas as a giant dataframe containing 14000+ cards in total, for piloting of a Whtz, the Bibliophile deck at max potential


Currently has only a few deck functions that aren't all encompassing, additional actions still need to be logged manually(i.e. tapping for mana), future updates should take care of some of these

I haven't dared to use this in an actual game yet, it's still under construction, but if you wanna give it a spin load WhtzCommanderDeck.ipynb and the decklist csv

Cards were pulled via scrython, a python wrapper for the scryfall API
https://github.com/NandaScott/Scrython

Methods for scraping are detailed in WhtzUWDeckScraping.ipynb

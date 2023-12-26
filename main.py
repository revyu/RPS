# This entrypoint file to be used in development. Start by reading README.md

from RPS import player,bot
from unittest import main

elite=player()

mrugesh=bot(strategy_="mrugesh")
elite.fit(mrugesh,1000)

elite.play(mrugesh,1000)





# Uncomment line below to run unit tests automatically
# main(module='test_module', exit=False)
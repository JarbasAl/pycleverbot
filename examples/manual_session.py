from os.path import join, dirname
from pycleverbot import Cleverbot


exec_path = join(dirname(__file__), "geckodriver")
# https://github.com/mozilla/geckodriver/releases

bot = Cleverbot(exec_path)
bot.new_session()
bot.ask("hello")
bot.ask("hello")
bot.ask("hello")
bot.ask("hello")
print(bot.utterances)

bot.save_screenshot("sess1.png")

bot.new_session()

bot.ask("hello")
bot.ask("hello")
print(bot.utterances)

bot.save_screenshot("sess2.png")


# dont forget stop !
bot.stop()

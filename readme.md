# PyCleverbot

## Install

```bash
pip install pycleverbot
```

## Usage

```python
from os.path import join, dirname
from pycleverbot import Cleverbot


exec_path = join(dirname(__file__), "geckodriver")
# https://github.com/mozilla/geckodriver/releases

with Cleverbot(exec_path) as bot:
    answer = bot.ask("hello")
    print(answer)
    answer = bot.ask("are you a bot")
    print(answer)
    answer = bot.ask("what is love")
    print(answer)
    answer = bot.ask("are you stupid")
    print(answer)
    answer = bot.ask("are you alive")
    print(answer)
    answer = bot.ask("does god exist")
    print(answer)
    answer = bot.ask("who created evil")
    print(answer)
    answer = bot.ask("are you religious")
    print(answer)
    answer = bot.ask("what is your favorite food")
    print(answer)

    path = bot.save_screenshot()
    print(path)
    print(bot.utterances)

```
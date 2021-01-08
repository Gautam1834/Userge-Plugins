"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""


import asyncio

from telebot import CMD_HELP
from telebot.utils import admin_cmd


@telebot.on(admin_cmd(pattern=r"(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "mom":

        await event.edit(input_str)

        animation_chars = [
            "`Inviteing your mom to my room",
            "`Your mom accepted.`",
            "`Your mom is telling for sax%\nYour mom removeing her dress`",
            "`Fuked4%\nNow she ready to be fuked`",
            "`Fuked.. 8%\nFUKING HER PUSy`",
            "`Fuked.. 20%\nFuking your more harder`",
            "`Fuked... 36%\nAlmost there`",
            "`Fuked... 52%\nReady to cum in ger PUSy `",
            "`Fuked... 84%\nCummed Filled your mom PUSy`",
            "`FUCKED... 100%\n█████████FUCKED!███████████ `",
            "`FUCKED YOUR MOM HARD ASF, SHE IS NOW SATISFIED, AND YOU GOT NEW BROTHER`",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


CMD_HELP.update({"mom": ".mom\nUse - Animation Plugin."})

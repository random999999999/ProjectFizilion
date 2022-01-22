#Ported from userge by @PrajjuS
import asyncio
from asyncio import sleep
from userbot.events import register
from userbot import CMD_HELP

@register(outgoing=True, pattern="^.kill$")
async def kill_func(message):
    animation_chars = [
        "Matando...",
        "F u u u u e g o",
        "(　･ิω･ิ)︻デ═一-->",
        "------>_____________",
        "--------->___⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠_______",
        "-------------->_____",
        "------------------->",
        "------>;(^。^)ノ",
        "(￣ー￣) DED",
        "<b>Objetivo asesinado. (´°̥̥̥̥̥̥̥̥ω°̥̥̥̥̥̥̥̥｀)</b>",
    ]
    for i in range(10):
        await sleep(0.6)
        await message.edit(animation_chars[i % 10], parse_mode="html")

CMD_HELP.update({
    "kill":
    "'.kill'"
    "\nUsage: Kill Meme"
    })

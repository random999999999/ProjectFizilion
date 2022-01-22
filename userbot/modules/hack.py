##ported from userge by @PrajjuS
from userbot.events import register
from userbot import CMD_HELP
import time
from asyncio import sleep 
from telethon import events , client , TelegramClient
from userbot.modules.admin import get_user_from_event

@register(outgoing=True, pattern="^.hack$")
async def hack_func(event):
    animation_chars = [
        "Conectando a un Servidor Privado \\",
        "Conectando a un Servidor Privado |",
        "Conectando a un Servidor Privado /",
        "Conectando a un Servidor Privado \\",
        "Conexión establecida ",
        "Objetivo seleccionado",
        "Debilidad encontrada",
        "Intentando hackear",
        "Hackeando... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
        "Hackeando... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
        "Hackeando... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
        "Hackeando... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
        "Hackeando... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒",
        "Hackeando... 52%\n█████████████▒▒▒▒▒▒▒▒▒",
        "Hackeando... 70%\n█████████████████▒▒▒▒▒",
        "Hackeando... 88%\n█████████████████████▒",
        "Hackeando... 100%\n███████████████████████",
        "Preparando los Datos... 1%\n▒██████████████████████",
        "Preparando los Datos... 14%\n████▒██████████████████",
        "Preparando los Datos... 30%\n████████▒██████████████",
        "Preparando los Datos... 55%\n████████████▒██████████",
        "Preparando los Datos... 72%\n████████████████▒██████",
        "Preparando los Datos... 88%\n████████████████████▒██",
        "Preparando los Datos... 100%\n███████████████████████",
        "Subiendo los Datos al Servidor... 12%\n███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
        "Subiendo los Datos al Servidor... 44%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
        "Subiendo los Datos al Servidor... 68%\n███████████████▒▒▒▒▒▒▒▒",
        "Subiendo los Datos al Servidor... 89%\n████████████████████▒▒▒",
        "Subiendo los Datos al Servidor... 100%\n███████████████████████",
        "**Carga de Datos Completada:** Datos del Objetivo Almacenados "
        "en `downloads/victim/telegram-authuser.data.sql`",
    ]
    hecked = (f"**Cuenta hackeada**\n\nPagame 69$ por tu Libertad")
    max_ani = len(animation_chars)
    for i in range(max_ani):
        await sleep(2)
        await event.edit(animation_chars[i % max_ani])
    await event.edit(hecked)

    
CMD_HELP.update({
    "hack":
    "'.hack'"
    "\nUsage: Hackerman Meme"
    })
    

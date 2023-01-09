import re
import player as pl
from main import config

prefix = config.Bot.prefix

commands = {
    "кто я": f"Вывести своего персонажа // `{prefix}кто я`",
    "покажи": f"Показать инвентарь или особенности/навыки персонажа // `{prefix}покажи <инвентарь|навыки>`",
    "помоги": f"Вывести это сообщение или помощь для конкретной команды // `{prefix}помоги [команда]`",
    "группа": f"Показать состояние группы // `{prefix}группа`"
}

adminCommands = {
    "выбери": f"Выбрать случайного игрока онлайн // `{prefix}выбери <игрока> \
[роль|уровень] [роль]`",
    "инвентарь": f"Вывести инвентарь игрока или НПЦ, или отформатировать его // `{prefix}инвентарь \
<имя_объекта|инвентарь для форматирования с новой строки>`",
    "кто": f"Отобразить персонажа для игрока // `{prefix}кто <упоминание>`",
    "создай": f"Создать группу из игроков // `{prefix}создай <группу> <упоминание_группы> \
<упоминания_игроков>`",
}

aliases = {
    "кто я": f"`{prefix}я кто`",
    "покажи": f"""Показать инвентарь: `{prefix}покажи <шмот|инвентарь|рюкзак>`
Показать навыки/особенности: `{prefix}покажи <скиллы|способности|особенности|навыки|спеллы|абилки>`
"""
}

inventoryCommands = {
    "карта": f"Показать карту // `{prefix}карта`",
}

def get_commands(command: str = None, player: pl.Player = None) -> str:
    if command is not None:
        com = commands.get(command)
        if com is None:
            return "Такой команды нет."
        return com + "\nАльтернативные написания:\n" + aliases.get(command, "`Нет`")
    s = ""
    for _, v in commands.items():
        s += v + "\n"
    if not isinstance(player, pl.Player):
        return s
    invCmds = list_inventory_commands(player)
    if len(invCmds) > 0:
        for i in invCmds:
            s += inventoryCommands.get(i) + "\n"
    return s

def get_admin_command(command: str = None):
    if command is not None:
        com = adminCommands.get(command)
        if com is None:
            return "Такой команды нет."
    s = ""
    for _, v in adminCommands.items():
        s += v + "\n"
    return s

def list_inventory_commands(player: pl.Player) -> list:
    """
    List all commands added by inventory items

    :param player: the player in question
    :return: list of commands
    """
    commands = []
    for item in player.inventory:
        matches = re.findall("<"+re.escape(prefix)+".+>", item)
        for match in matches:
            commands.append(match[2:-1])
    return commands

def get_alias(command: str) -> str:
    return aliases.get(command, "Такой команды нет.")

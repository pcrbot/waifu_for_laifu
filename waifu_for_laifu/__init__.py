from .waifu_labs import waifu_labs_controller

try:
    from nonebot.adapters.cqhttp import Bot
    waifu_labs_controller.register_nb2_a7_commands()
except:
    try:
        from nonebot.adapters import Bot
        waifu_labs_controller.register_nb2_commands()
    except:
        print('<waifu_for_laifu> your bot framework is not currently supported')

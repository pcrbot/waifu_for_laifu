from .waifu_labs import waifu_labs_controller

try:
    from nonebot.typing import T_State
    waifu_labs_controller.register_nb2_commands()
except:
    try:
        from nonebot.adapters.cqhttp import Bot
        print('<waifu_for_laifu> registering nb2 a7- commands')
        waifu_labs_controller.register_nb2_a7_commands()
    except:
        try:
            from hoshino import Service
            print('<waifu_for_laifu> registering hoshino service')
            waifu_labs_controller.register_hoshino_service()
        except:
            try:
                from nonebot import CommandSession
                waifu_labs_controller.register_nb_commands()
            except:
                print('<waifu_for_laifu> your bot framework is not currently supported')

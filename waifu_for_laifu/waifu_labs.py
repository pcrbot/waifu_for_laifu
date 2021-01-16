import base64
import json
from io import BytesIO
from typing import Dict, List
import os

import aiohttp
from PIL import Image, ImageFont, ImageDraw

from .chat_models.chat_session import ChatSession, ChatResult
from .models.waifu import Waifu


class WaifuLabsController:

    FONT_PATH = os.path.join(os.path.dirname(__file__), "Mamelon.otf")

    def __init__(self):
        self.base_url = 'https://api.waifulabs.com'
        self.generateUrl = self.base_url + '/generate'

    async def generate_waifu(self, current_girl, size, step, local_json=None):
        payload = {
            'currentGirl': current_girl,
            'size': size,
            'step': step,
        }
        # print(json.dumps(payload))

        girls: List[Waifu] = []

        # """ local test only
        if local_json:
            with open(local_json) as fp:
                resp_payload = json.load(fp)
            for new_girl in resp_payload['newGirls']:
                girls.append(Waifu(new_girl))
            return girls
        # """

        # """
        async with aiohttp.ClientSession() as sess:
            async with sess.post(self.generateUrl, json=payload) as resp:
                if resp.status == 200:
                    resp_payload = json.loads(await resp.text())
                    for new_girl in resp_payload['newGirls']:
                        girls.append(Waifu(new_girl))
                    return girls
        return None
        # """

    async def generate_harlem_image(self, step, girls: List[Waifu]) -> str:
        if step == 4:
            title_str = 'これはあなたの彼女です'
        elif step == 3:
            title_str = 'ディテールをコンフィグください'
        elif step == 2:
            title_str = 'カラーパターンを選択ください'
        else:
            title_str = '彼女を一人選択ください'

        bg = Image.new("RGBA", (1200, 1300), "#ffffff")
        font_title = ImageFont.truetype(self.FONT_PATH, size=70)
        font_sub = ImageFont.truetype(self.FONT_PATH, size=30)

        title = ImageDraw.Draw(bg)
        title.text((600, 60), title_str, fill='#000000', font=font_title, anchor="mm", align="center")

        for girl_index in range(len(girls)):
            girl: Waifu = girls[girl_index]
            row = girl_index % 4
            col = girl_index // 4

            head_bg = Image.new("RGBA", (300, 300))
            girl_img = girl.get_image()
            head_bg.paste(girl_img, (60, 20))
            head_text = ImageDraw.Draw(head_bg)
            head_text.text((150, 260), str(girl_index), fill='#000000', font=font_sub, anchor="mm", align="center")

            bg.paste(head_bg, (row * 300, col * 300 + 100))

        bio = BytesIO()
        bg.save(bio, format='PNG')
        base64_img = base64.b64encode(bio.getvalue()).decode()

        return base64_img

    async def get_session(self, group_id, user_id) -> ChatSession:
        return await ChatSession.get_session(group_id, user_id)

    async def first_receive(self, bot, ev, group_id: int, user_id: int, message: str) -> ChatResult:
        print(f'received args {message}')

        session: ChatSession = await self.get_session(group_id, user_id)
        seeds = None
        if 'step' not in session.state:
            session.state['step'] = 0
            await bot.send(ev, '正在生成后宫')
        else:
            try:
                pick_index = int(message)
                if 0 <= pick_index <= len(session.state['girls']):
                    seeds = session.state['girls'][pick_index].seeds
                    session.state['step'] += 1
            except:
                pass
        girls = await self.generate_waifu(seeds, 0, session.state['step'])
        if girls is None:
            return session.finish('something went wrong')
        session.state['girls'] = girls

        step = session.state['step']
        if session.state['step'] != 4:
            step += 1

        base64_img = await self.generate_harlem_image(step, girls)
        return session.pause(f"[CQ:image,file=base64://{base64_img}]")

    def register_nb2_a7_commands(self):
        from nonebot import on_command
        from nonebot.adapters.cqhttp import Bot, Event

        waifu_labs = on_command("waifu", priority=5)

        @waifu_labs.handle()
        async def handle_waifu(bot: Bot, event: Event, state: dict):
            message = str(event.message).strip()
            reply: ChatResult = await self.first_receive(bot, event, event.group_id, event.user_id, message)
            if reply.result_type == ChatResult.CHAT_RESULT_PAUSE:
                await waifu_labs.reject(reply.msg)
            else:
                await waifu_labs.finish(reply.msg)

    def register_nb2_commands(self):
        from nonebot import on_command
        from nonebot.adapters import Bot, Event

        waifu_labs_command = on_command("waifu", priority=5)

        @waifu_labs_command.handle()
        async def handle_waifu(bot: Bot, event: Event, state):
            message = str(event.get_message()).strip()
            await self.first_receive(message)

    def register_nb_commands(self):
        from nonebot import on_command, CommandSession

        @on_command('waifu')
        async def handle_waifu(session: CommandSession):
            message = session.state.get('message')
            reply = await self.first_receive(message)
            await session.send(reply)

    def register_hoshino_service(self):
        pass


waifu_labs_controller = WaifuLabsController()
# waifu_labs_controller.register_nb2_a7_commands()

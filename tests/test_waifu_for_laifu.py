import os
import aiounittest

from waifu_for_laifu.waifu_labs import waifu_labs_controller


class TestWaifuForLaifu(aiounittest.AsyncTestCase):

    def setUp(self):
        self.controller = waifu_labs_controller
        self.test_json = os.path.join(os.path.dirname(__file__), "step0.json")

    async def test_1_generate_waifu_local(self):
        girls = await self.controller.generate_waifu(None, 0, 0, self.test_json)
        self.assertIsNotNone(girls)

    async def test_2_generate_harlem_image(self):
        girls = await self.controller.generate_waifu(None, 0, 0, self.test_json)
        base64_img = await self.controller.generate_harlem_image(0, girls)
        self.assertIsNotNone(base64_img)

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class WaveshareC535HardwareTests(unittest.TestCase):

    def test_board_contract_keeps_expander_and_touch_handling_isolated(self) -> None:
        config = (ROOT / "esp32_marauder" / "configs.h").read_text(encoding="utf-8")
        tft = (ROOT / "User_Setup_ws_c5_35.h").read_text(encoding="utf-8")
        touch = (ROOT / "esp32_marauder" / "ft6336.h").read_text(encoding="utf-8")
        expander = (ROOT / "esp32_marauder" / "ws_c5_exio.h").read_text(
            encoding="utf-8"
        )

        for expected in (
            "#define I2C_SDA 27",
            "#define I2C_SCL 26",
            "#define SD_CS 9",
        ):
            self.assertIn(expected, config)
        for expected in (
            "#define TFT_MISO  2",
            "#define TFT_MOSI  7",
            "#define TFT_SCLK  6",
            "#define TFT_CS    8",
            "#define TFT_DC    5",
        ):
            self.assertIn(expected, tft)
        self.assertIn("#ifdef MARAUDER_WS_C5_35", touch)
        self.assertIn("Wire.end(); Wire.begin(CTP_SDA, CTP_SCL, 100000U);", touch)
        self.assertIn("return -1;", touch)
        self.assertIn("#define WS_EXIO_ADDR        0x24", expander)
        self.assertIn("ws_c5_exio_begin", expander)


if __name__ == "__main__":
    unittest.main()

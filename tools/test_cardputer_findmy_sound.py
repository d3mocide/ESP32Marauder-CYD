#!/usr/bin/env python3
"""Guard Cardputer FindMy Sound build capabilities and CI dependencies."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class CardputerFindMySoundTests(unittest.TestCase):
    def test_cardputer_targets_enable_findmy_sound_capabilities(self) -> None:
        configs = (ROOT / "esp32_marauder" / "configs.h").read_text()
        cardputer_block = configs.split(
            "#if defined(MARAUDER_CARDPUTER) || defined(MARAUDER_CARDPUTER_ADV)", 1
        )[1].split("#ifdef MARAUDER_MINI", 1)[0]

        self.assertIn("#define HAS_NIMBLE_2", cardputer_block)
        self.assertIn("#define HAS_IDF_3", cardputer_block)


    def test_findmy_sound_menu_remains_available(self) -> None:
        menu = (ROOT / "esp32_marauder" / "MenuFunctions.cpp").read_text()
        self.assertIn('"FindMy Sound"', menu)


if __name__ == "__main__":
    unittest.main()

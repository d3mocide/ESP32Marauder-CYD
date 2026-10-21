import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class XiaoC5HardwareTests(unittest.TestCase):

    def test_target_uses_native_usb_safe_uart_pins(self):
        configs = (ROOT / "esp32_marauder" / "configs.h").read_text()

        self.assertIn("//#define XIAO_ESP32_C5", configs)
        self.assertIn("defined(ARDUINO_XIAO_ESP32C5)", configs)
        self.assertIn(
            '#define HARDWARE_NAME "Seeed Studio XIAO ESP32-C5"', configs
        )

        feature_block = re.search(
            r"#ifdef XIAO_ESP32_C5(?P<body>.*?)#endif", configs, re.S
        ).group("body")
        for feature in (
            "HAS_BT",
            "HAS_GPS",
            "HAS_DUAL_BAND",
            "HAS_PSRAM",
            "HAS_NIMBLE_2",
            "HAS_IDF_3",
        ):
            self.assertIn(f"#define {feature}", feature_block)
        self.assertIn("#define XIAO_LED_PIN 27", feature_block)
        self.assertNotIn("HAS_SD", feature_block)
        self.assertNotIn("HAS_SCREEN", feature_block)
        self.assertNotIn("HAS_BUTTONS", feature_block)
        self.assertNotIn("HAS_DIRECT_UPLOAD", feature_block)
        self.assertRegex(
            configs,
            r"#ifdef XIAO_ESP32_C5\s+#undef HAS_C5_SD\s+"
            r"#undef HAS_SD\s+#undef USE_SD",
        )

        gps_block = next(
            body
            for body in re.findall(
                r"#elif defined\(XIAO_ESP32_C5\)(.*?)(?:#elif|#endif)",
                configs,
                re.S,
            )
            if "GPS_SERIAL_INDEX" in body
        )
        self.assertIn("#define GPS_SERIAL_INDEX 1", gps_block)
        self.assertIn("#define GPS_TX 12", gps_block)
        self.assertIn("#define GPS_RX 11", gps_block)
        self.assertNotRegex(gps_block, r"GPS_(?:TX|RX)\s+(?:13|14)\b")

    def test_xiao_led_support_is_shared_without_changing_s3_pin(self):
        header = (ROOT / "esp32_marauder" / "xiaoLED.h").read_text()
        self.assertIn("#ifndef XIAO_LED_PIN", header)
        self.assertIn("#define XIAO_LED_PIN 21", header)

        sketch = (ROOT / "esp32_marauder" / "esp32_marauder.ino").read_text()
        self.assertGreaterEqual(
            sketch.count("defined(XIAO_ESP32_S3) || defined(XIAO_ESP32_C5)"),
            4,
        )


if __name__ == "__main__":
    unittest.main()

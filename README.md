<!---[![License: MIT](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/CodeHedge/ESP32Marauder/blob/master/LICENSE)--->
<!---[![Gitter](https://badges.gitter.im/CodeHedge/ESP32Marauder.png)](https://gitter.im/CodeHedge/ESP32Marauder)--->
<!---[![Build Status](https://travis-ci.com/CodeHedge/ESP32Marauder.svg?branch=master)](https://travis-ci.com/CodeHedge/ESP32Marauder)--->
<!---Shields/Badges https://shields.io/--->

<p align="center"><img alt="Marauder" src="pictures/marauder_skull_patch_04_full_final.png" width="200"></p>

## About This Fork

This repository carries [Hedge's](https://github.com/CodeHedge/ESP32Marauder) CYD (Cheap Yellow Display) fork of [justcallmekoko's ESP32 Marauder](https://github.com/justcallmekoko/ESP32Marauder), kept current with upstream. The firmware is koko's; the CYD battery and GPS work is Hedge's. See [Credits](#credits).

Currently tracking upstream **v1.14.1**.

### Primary Modifications:

- **Battery Monitoring Support**: Integrated support for the [Adafruit MAX17048 Battery Fuel Gauge](https://www.adafruit.com/product/5580) connected to port CN1, providing real-time battery percentage display in the top-right corner of the screen.

- **GPS Port Relocation**: To accommodate the battery gauge, GPS functionality has been moved to the bottom port (P5).

- **Removed Marauder CLI**: CLI support has been dropped due to limited IO availability. The philosophy behind this decision is that devices with screens should leverage their display capabilities rather than rely on CLI interfaces. For CLI needs, an ESP32 Dev board would be more appropriate.

### Recommended Hardware

The [ESP32 Marauder Battery Mod Kit](https://biscuitshop.us/products/esp32-marauder-battery-mod-kit) is the primary board recommended for this fork, providing an integrated solution with all necessary components.

Alternatively, you can achieve the same functionality using the Adafruit MAX17048 board and a compatible GPS module with your existing CYD hardware.

## Getting Started

### Web Flasher
Flash your device directly from the browser: **[d3mocide.github.io/ESP32Marauder-cyd-hedge](https://d3mocide.github.io/ESP32Marauder-cyd-hedge/)**

Pick your CYD variant, hit the button, choose the serial port. Requires Chrome, Edge, or Opera — Safari and Firefox do not implement Web Serial. The flasher lives in [`docs/`](docs/) and is served by GitHub Pages; firmware is published into `docs/firmware/<board>/` by the `publish_webflasher` job whenever a release build is dispatched.

Hedge's original web flasher is still available at [codehedge.github.io/Adafruit_WebSerial_ESPTool](https://codehedge.github.io/Adafruit_WebSerial_ESPTool/).

### Downloads
Download the [latest release](https://github.com/d3mocide/ESP32Marauder-cyd-hedge/releases/latest) of the firmware.

### Documentation
Check out the project [wiki](https://github.com/justcallmekoko/ESP32Marauder/wiki) for a full overview of the ESP32 Marauder features and capabilities.

## Uploading Wardrive Logs to WiGLE

Wardrive logs go straight from the SD card to WiGLE over WiFi. Since this fork has no serial CLI, credentials are supplied on the SD card instead:

1. Put your WiGLE API name in `/wigle_api_name.txt` and your token in `/wigle_api_token.txt` on the root of the SD card.
2. Boot the device. Both files are read into persistent settings and then deleted from the card.
3. Join a network from `WiFi → General → Join WiFi`.
4. Upload from `WiFi → General → Upload Wardrive Logs` — either a single log or `Upload All`.

Successfully uploaded logs get a `.wigle` sidecar file written alongside them, so re-running an upload skips anything already sent. `WDGWars` and `Both` are available from the same menu.

## Credits

This fork stands on two people's work, and neither should be mistaken for maintainers of this repository — please don't send issues from this fork to them.

### [justcallmekoko](https://github.com/justcallmekoko/ESP32Marauder) — author of ESP32 Marauder

Created and maintains ESP32 Marauder. Every scanning, attack, wardriving, and UI capability in this firmware is his work, along with the hardware ecosystem around it. This repository is a downstream fork that tracks his releases — the current base is v1.14.1. If you want the firmware itself, or support for any board other than a CYD, go upstream.

- Project: <https://github.com/justcallmekoko/ESP32Marauder>
- Wiki: <https://github.com/justcallmekoko/ESP32Marauder/wiki>

### [Hedge / CodeHedge](https://github.com/CodeHedge/ESP32Marauder) — author of the CYD battery & GPS fork

Built the CYD variant this repository continues. Every CYD-specific change here originated with him:

- MAX17048 fuel gauge support on CN1, with battery percentage in the status bar
- Relocating GPS to the bottom port (P5) to free CN1 for the gauge
- The `MARAUDER_CYD_MICRO_INVERTED` build for panels needing display inversion
- The original CYD web flasher: <https://codehedge.github.io/Adafruit_WebSerial_ESPTool/>
- The crash guard for `HAS_BATTERY` when no gauge is present, since adopted upstream

### This repository

Maintenance only: keeping Hedge's CYD build synced with upstream Marauder and publishing the firmware served by the [web flasher](https://d3mocide.github.io/ESP32Marauder-cyd-hedge/).

The Marauder skull artwork is from the upstream project.

## License

MIT, inherited from upstream — see [LICENSE](LICENSE).

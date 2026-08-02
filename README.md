<!---[![License: MIT](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/CodeHedge/ESP32Marauder/blob/master/LICENSE)--->
<!---[![Gitter](https://badges.gitter.im/CodeHedge/ESP32Marauder.png)](https://gitter.im/CodeHedge/ESP32Marauder)--->
<!---[![Build Status](https://travis-ci.com/CodeHedge/ESP32Marauder.svg?branch=master)](https://travis-ci.com/CodeHedge/ESP32Marauder)--->
<!---Shields/Badges https://shields.io/--->

## About This Fork

This repository is a fork of the ESP32 Marauder firmware with modified capabilities specifically for CYD (Cheap Yellow Display) builds.

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

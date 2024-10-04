# Game Bot Automation Script

<p align="center">
  <img src="https://img.shields.io/badge/python-3.9-blue" alt="Python 3.9" />
  <img src="https://img.shields.io/badge/PIL-Supported-green" alt="PIL Supported" />
  <img src="https://img.shields.io/badge/pynput-Installed-brightgreen" alt="pynput Installed" />
</p>

## Overview

This Python script automates the process of detecting specific color-coded objects (flowers, crystals, bombs) in a game and simulates mouse clicks on them. It is ideal for automating tasks like gathering resources or interacting with specific in-game items.

### Features
- **Automated Color Detection**: Detects objects using RGB and HSV color ranges.
- **Cooldowns to Prevent Overclicking**: Prevents clicking the same area repeatedly.
- **Screen Capture**: Grabs part of the screen and analyzes the image for objects.
  
## Setup

To use this script, you will need to install the following Python libraries:

```bash
pip install pynput Pillow numpy
```
Game Window Coordinates
The game window's boundaries must be defined based on your screen setup. You can adjust these in the script:
```bash
top_left = (515, 22)  # Top-left corner
bottom_right = (853, 690)  # Bottom-right corner
```
<p align="center"> <img src="[[https://via.placeholder.com/400x200](https://cdn.prod.website-files.com/65b6a1a4a0e2af577bccce96/65b6a7e38e9ad2df88db2e9a_blum-home-screen-p-500.png)](https://cdn.prod.website-files.com/65b6a1a4a0e2af577bccce96/65b6a7e38e9ad2df88db2e9a_blum-home-screen-p-500.png)](https://www.google.com/imgres?q=telegram%20blum&imgurl=https%3A%2F%2Flookaside.fbsbx.com%2Flookaside%2Fcrawler%2Fmedia%2F%3Fmedia_id%3D122191754378029896&imgrefurl=https%3A%2F%2Fm.facebook.com%2Fgroups%2F203633485102386%2Fposts%2F%25EF%25B8%258F-blum-is-another-big-project-after-notcoin-%25EF%25B8%258F-100-legit-telegram-bot-%25EF%25B8%258F-do-simple%2F1098551212277271%2F&docid=Hqxz8aabPUP3hM&tbnid=2K-VFzWt9-GO9M&vet=12ahUKEwiHgbil5fSIAxVk4TgGHVoiLfIQM3oECBcQAA..i&w=590&h=1280&hcb=2&itg=1&ved=2ahUKEwiHgbil5fSIAxVk4TgGHVoiLfIQM3oECBcQAA)" alt="Game Window Boundaries" /> </p>
Color Definitions
Flower (Green): Detected using RGB values.
Crystal (Blue): Defined by an exact RGB color.
Bomb: Detected using an HSV color range.
You can customize these values if needed:

```bash
flower_rgb = [(63, 219, 0)]
crystal_rgb = (130, 221, 233)
bomb_hsv_range = [(0, 0, 71), (0, 5, 53)]
```

How to Run
To start the bot, run the script in Python:
```bash
python main.py
```
The script will:
Continuously scan for objects (crystals, flowers).
Simulate mouse clicks on detected objects.
Respect cooldowns to avoid repetitive actions.
Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements.

<p align="center"> <em>Created with ❤️ by Tanvir</em> </p>


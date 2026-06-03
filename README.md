# Phantom Keyboard

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Linux | macOS](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS-green)](https://github.com/neo4-svg/phantom_keyboard)
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)](https://github.com/neo4-svg/phantom_keyboard)

Phantom Keyboard is a chaos‑driven keystroke interceptor for **Linux** and **macOS**.  
It injects ghost inputs, timing jitter, fake typos, and phantom noise to confuse keyloggers, monitoring tools, and forensic analysis — while still letting you type normally.

⚡ Hacker reality: Phantom Keyboard isn't just a utility, it's hacker art. Your typing looks chaotic to surveillance, but feels natural to you.

---

## Features
- 🎹 Ghost keystrokes → random phantom keys injected into logs  
- ⏱️ Timing jitter → micro‑delays and bursts to break typing rhythm analysis  
- 📝 Fake typos → believable mistakes that auto‑correct  
- 🌫️ Noise layer → phantom events to overwhelm monitoring tools  
- 🎨 Colorful CLI → interactive setup with ANSI colors  
- ⚙️ Config system → chaos level and ghost frequency saved in YAML  

---

## Platforms
- **Linux** → pure Python, distro‑agnostic, works on Fedora, Ubuntu, Arch, Debian  
- **macOS** → Quartz backend via `pynput`, packaged with PyInstaller `.spec`  
- **Windows** → planned later release  

---

## Installation

### Linux (clone + run)
```bash
# Clone the repo
git clone https://github.com/neo4-svg/phantom_keyboard.git
cd phantom_keyboard

# Install dependencies
pip3 install pynput colorama pyyaml

# Run Phantom Keyboard
python3 phantom_linux1.py

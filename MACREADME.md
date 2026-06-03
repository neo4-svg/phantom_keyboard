# Clone the repo
git clone https://github.com/neo4-svg/phantom_keyboard.git
cd phantom_keyboard

# Install dependencies
pip3 install pynput colorama pyyaml pyinstaller

# Build using the .spec file
pyinstaller  mac_pahntom.spec  
# Run Phantom Keyboard
./dist/mac_phantom.spec
# If Gatekeeper blocks the binary, remove quarantine attributes:
xattr -d com.apple.quarantine dist/phantom_macos

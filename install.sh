#!/bin/bash
# Installer for IP Insight Pro

echo -e "\033[0;32m[+] Installing IP Insight Pro...\033[0m"

# Install dependencies
pip3 install requests colorama pyfiglet dnspython python-whois

# Create alias
echo "alias ipinsight='python3 ~/IPInsightPro/ipinsight.py'" >> ~/.bashrc

# Create desktop entry
cat > ~/Desktop/ipinsight.desktop << EOF
[Desktop Entry]
Name=IP Insight Pro
Comment=Advanced IP Information Tool
Exec=python3 $HOME/IPInsightPro/ipinsight.py
Icon=utilities-terminal
Terminal=true
Type=Application
Categories=Network;
EOF

chmod +x ~/Desktop/ipinsight.desktop

echo -e "\033[0;32m[+] Installation Complete!\033[0m"
echo -e "\033[0;33m[+] Run 'ipinsight' or click the desktop icon\033[0m"

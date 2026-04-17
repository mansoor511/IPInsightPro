#!/bin/bash

# ============================================================
# IP Insight Pro - Installer Script
# Coded by: MANSOOR BIK KAMALI
# Version: 2.0
# ============================================================

# رنگ‌ها
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# نمایش بنر
clear
echo -e "${CYAN}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║         IP Insight Pro - Installation Script             ║"
echo "║              Coded by: MANSOOR BIK KAMALI                 ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# گرفتن مسیر فعلی
CURRENT_DIR=$(pwd)

echo -e "${YELLOW}[+] Installing IP Insight Pro...${NC}"
echo ""

# بررسی وجود pip3
if ! command -v pip3 &> /dev/null; then
    echo -e "${RED}[-] pip3 not found! Installing...${NC}"
    sudo apt install python3-pip -y
fi

# نصب کتابخانه‌ها با روش صحیح برای کالی لینوکس
echo -e "${YELLOW}[+] Installing Python packages...${NC}"

# روش اول: با --break-system-packages (برای کالی جدید)
pip3 install requests colorama pyfiglet dnspython python-whois --break-system-packages 2>/dev/null

# اگر روش اول失敗، روش دوم را امتحان کن
if [ $? -ne 0 ]; then
    echo -e "${YELLOW}[+] Trying alternative method...${NC}"
    pip3 install requests colorama pyfiglet dnspython python-whois --user
fi

# اگر باز هم失敗، با sudo امتحان کن
if [ $? -ne 0 ]; then
    echo -e "${YELLOW}[+] Trying with sudo...${NC}"
    sudo pip3 install requests colorama pyfiglet dnspython python-whois
fi

echo ""
echo -e "${GREEN}[+] Python packages installed!${NC}"

# ایجاد آلیاس (alias)
echo -e "${YELLOW}[+] Creating alias...${NC}"
if ! grep -q "alias ipinsight" ~/.bashrc; then
    echo "alias ipinsight='python3 $CURRENT_DIR/ipinsight.py'" >> ~/.bashrc
    echo -e "${GREEN}[+] Alias added to ~/.bashrc${NC}"
else
    echo -e "${BLUE}[!] Alias already exists${NC}"
fi

# ایجاد آلیاس برای zsh (اگر استفاده می‌کند)
if [ -f ~/.zshrc ]; then
    if ! grep -q "alias ipinsight" ~/.zshrc; then
        echo "alias ipinsight='python3 $CURRENT_DIR/ipinsight.py'" >> ~/.zshrc
        echo -e "${GREEN}[+] Alias added to ~/.zshrc${NC}"
    fi
fi

# ایجاد شورت کات دسکتاپ
echo -e "${YELLOW}[+] Creating desktop shortcut...${NC}"

cat > ~/Desktop/ipinsight.desktop << EOF
[Desktop Entry]
Name=IP Insight Pro
Comment=Advanced IP Information Tool
Exec=python3 $CURRENT_DIR/ipinsight.py
Icon=utilities-terminal
Terminal=true
Type=Application
Categories=Network;
StartupNotify=true
EOF

chmod +x ~/Desktop/ipinsight.desktop 2>/dev/null

echo -e "${GREEN}[+] Desktop shortcut created!${NC}"

# ایجاد فایل requirements.txt (برای GitHub)
echo -e "${YELLOW}[+] Creating requirements.txt...${NC}"
cat > requirements.txt << EOF
requests
colorama
pyfiglet
dnspython
python-whois
EOF

echo -e "${GREEN}[+] requirements.txt created!${NC}"

# تست اجرای ابزار
echo ""
echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}[+] Installation Complete!${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${YELLOW}📌 How to run:${NC}"
echo -e "   ${GREEN}1.${NC} Run: ${BLUE}python3 $CURRENT_DIR/ipinsight.py${NC}"
echo -e "   ${GREEN}2.${NC} Run: ${BLUE}ipinsight${NC} (after restarting terminal)"
echo -e "   ${GREEN}3.${NC} Click the desktop icon: ${BLUE}~/Desktop/ipinsight.desktop${NC}"
echo ""
echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${RED}⚠️  Note: Close and reopen terminal for 'ipinsight' command to work${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════${NC}"

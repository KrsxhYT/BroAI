#!/bin/bash

echo "🤖 BRO AI Assistant Setup"
echo "=========================="

# Update packages
echo "📦 Updating packages..."
pkg update -y
pkg upgrade -y

# Install required packages
echo "🔧 Installing required packages..."
pkg install python -y
pkg install termux-api -y
pkg install screenfetch -y

# Install Python packages
echo "🐍 Installing Python dependencies..."
pip install --upgrade pip
pip install DateTime==4.3
pip install pytz==2021.1
pip install zope.interface==5.4.0
pip install requests==2.31.0
pip install colorama==0.4.6

# Set permissions
echo "🔐 Setting permissions..."
termux-setup-storage

# Make scripts executable
chmod +x install.sh

echo ""
echo "✅ Installation completed successfully!"
echo ""
echo "🚀 To start BRO AI Assistant:"
echo "   python BroAI.py"
echo ""
echo "📝 Make sure to:"
echo "   1. Install Termux:API app from Play Store"
echo "   2. Grant necessary permissions"
echo "   3. Run from Termux home directory"

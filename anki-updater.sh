#!/usr/bin/env bash

cd /home/aarjav/Downloads/
curl -s https://api.github.com/repos/ankitects/anki/releases/latest | grep 'browser_download_url.*qt6.tar.zst' | cut -d : -f 2,3 | tr -d \\\" | aria2c -s16 -x16 -i -
new=$(curl -s 'https://api.github.com/repos/ankitects/anki/releases/latest' | grep 'browser_download_url.*qt6.tar.zst' | cut -d / -f 8)
tar xaf "anki-${new}-linux-qt6.tar.zst"
cd "anki-${new}-linux-qt6/"
sudo "./install.sh"
rm -rf "/home/aarjav/Downloads/anki-${new}-linux-qt6.tar.zst" "/home/aarjav/Downloads/anki-${new}-linux-qt6"
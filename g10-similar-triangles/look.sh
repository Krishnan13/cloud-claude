#!/bin/bash
# look.sh fc|st page...  : rebuild and render chosen pages at 100 dpi into /tmp/look
cd "$(dirname "$0")" && ./build.sh >/tmp/build.log 2>&1; cat /tmp/build.log | grep -v Pages
mkdir -p /tmp/look; rm -f /tmp/look/*
w=$1; shift; f="build/class 2 fc.pdf"; [ $w = st ] && f="build/class 2.pdf"
for p in "$@"; do pdftoppm -r 100 -png -f $p -l $p "$f" /tmp/look/$w-$p; done; ls /tmp/look

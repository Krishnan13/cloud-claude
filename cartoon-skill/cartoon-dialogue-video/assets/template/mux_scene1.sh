#!/usr/bin/env bash
# Mux the built soundtrack onto the rendered scene 1 picture.
#   ./mux_scene1.sh
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p out

ffmpeg -y -hide_banner -loglevel error \
  -i build/media/videos/scene1/720p24/Scene1.mp4 \
  -i build/scene1_audio.wav \
  -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k \
  -movflags +faststart out/scene1_ink_v1.mp4

echo "wrote out/scene1_ink_v1.mp4"

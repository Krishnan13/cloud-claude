#!/usr/bin/env bash
# Mux the built soundtrack onto the rendered scene 2 picture (ink cut v1).
#   ./mux_scene2.sh
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p out

ffmpeg -y -hide_banner -loglevel error \
  -i build/media/videos/scene2/720p24/Scene2.mp4 \
  -i build/scene2_audio.wav \
  -map 0:v -map 1:a \
  -vf "hue=s='if(gte(t,35.7),0.45,1)':enable=1" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p \
  -c:a aac -b:a 192k \
  -movflags +faststart out/scene2_ink_v1.mp4

echo "wrote out/scene2_ink_v1.mp4"

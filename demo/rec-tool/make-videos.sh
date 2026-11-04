#!/usr/bin/env bash
# Records both walkthrough pages and writes three MP4s into the demo folder.
set -euo pipefail
DEMO="C:/Users/user/re/lesson-studio/demo"
TMP="C:/Users/user/AppData/Local/Temp/claude/C--Users-user/26c52dce-94b4-424e-af46-638be0108588/scratchpad"
FF="C:/Users/user/AppData/Local/Programs/Python/Python312/Lib/site-packages/imageio_ffmpeg/binaries/ffmpeg-win-x86_64-v7.1.exe"
cd "$DEMO/rec-tool"
for name in lesson-studio admin-console; do
  node record.mjs "../$name-demo.html" "$TMP/frames-$name" 1 0
  (cd "$TMP/frames-$name" && "$FF" -hide_banner -loglevel error -y -f concat -safe 0 -i list.ffconcat \
     -vf "fps=30,format=yuv420p" -c:v libx264 -crf 18 -preset slow -movflags +faststart "$DEMO/$name-walkthrough.mp4")
done
mv -f "$DEMO/lesson-studio-walkthrough.mp4" "$DEMO/lesson-studio-walkthrough.mp4" 2>/dev/null || true
printf "file '%s'\nfile '%s'\n" "$DEMO/lesson-studio-walkthrough.mp4" "$DEMO/admin-console-walkthrough.mp4" > "$TMP/both.txt"
"$FF" -hide_banner -loglevel error -y -f concat -safe 0 -i "$TMP/both.txt" -c copy -movflags +faststart "$DEMO/full-walkthrough-studio-and-admin.mp4"
for f in lesson-studio-walkthrough admin-console-walkthrough full-walkthrough-studio-and-admin; do
  echo "$f: $("$FF" -hide_banner -i "$DEMO/$f.mp4" 2>&1 | grep -o 'Duration: [0-9:.]*')"
done

#!/bin/sh
# Create a folder (named dmg) to prepare our DMG in (if it doesn't already exist).
mkdir -p dist/dmg
# Empty the dmg folder.
rm -r dist/dmg/*
# Copy the app bundle to the dmg folder.
cp -r "dist/Pdf Bookmark Generator.app" dist/dmg
# If the DMG already exists, delete it.
test -f "dist/Pdf Bookmark Generator.dmg" && rm "dist/Pdf Bookmark Generator.dmg"
create-dmg \
  --volname "Pdf Bookmark Generator" \
  --volicon "src/ico/app.icns" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 128 \
  --icon "Pdf Bookmark Generator.app" 175 120 \
  --hide-extension "Pdf Bookmark Generator.app" \
  --app-drop-link 425 120 \
  "dist/Pdf Bookmark Generator.dmg" \
  "dist/dmg/"
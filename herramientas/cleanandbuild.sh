#!/bin/sh

set -e

echo "[+] Cleaning..."
docker exec blog bundle exec jekyll clean

echo "[+] Building..."
docker exec blog bundle exec jekyll build

echo "[+] Done"
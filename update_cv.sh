#!/usr/bin/env bash
# Compile the Overleaf CV (main.tex), copy it in as cv.pdf, then commit and push.
# Usage: ./update_cv.sh            # compile, commit, push
#        ./update_cv.sh --no-push  # compile and copy only
set -euo pipefail

SRC="$HOME/MIT Dropbox/Terrence Roh/Apps/Overleaf/CV_Roh_MIT"
REPO="$(cd "$(dirname "$0")" && pwd)"
BUILD="$(mktemp -d)"
trap 'rm -rf "$BUILD"' EXIT

cp "$SRC/main.tex" "$SRC/res.cls" "$BUILD/"
(cd "$BUILD" && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex >/dev/null) \
  || { echo "LaTeX build failed; see $BUILD/main.log"; trap - EXIT; exit 1; }
cp "$BUILD/main.pdf" "$REPO/cv.pdf"
echo "Updated cv.pdf"

[[ "${1:-}" == "--no-push" ]] && exit 0

cd "$REPO"
if git diff --quiet -- cv.pdf; then
  echo "cv.pdf unchanged; nothing to commit."
  exit 0
fi
git add cv.pdf
git commit -m "Update CV" -- cv.pdf
git push
echo "Pushed. The site will rebuild in a minute or two."

#!/usr/bin/env bash
# install.sh - collega (o copia) le skill in ~/.claude/skills/
#
#   ./install.sh                   umanizzatore + structural-humanizer (symlink)
#   ./install.sh --with-humanizer  anche humanizer, se non l'hai già come plugin
#   ./install.sh --copy            copie indipendenti invece dei symlink
#   ./install.sh --project         installa in ./.claude/skills/ della cartella corrente
#   ./install.sh --force           sostituisce un'installazione esistente (con backup)

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS=(umanizzatore structural-humanizer)
MODE=link
TARGET="$HOME/.claude/skills"
FORCE=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --copy)    MODE=copy ;;
    --project) TARGET="$PWD/.claude/skills" ;;
    --force)   FORCE=1 ;;
    --with-humanizer) SKILLS+=(humanizer) ;;
    -h|--help) sed -n '2,8p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
  shift
done

mkdir -p "$TARGET"
echo "installing into $TARGET (mode: $MODE)"

for skill in "${SKILLS[@]}"; do
  src="$REPO/skills/$skill"
  dst="$TARGET/$skill"

  if [[ -e "$dst" || -L "$dst" ]]; then
    if [[ "$FORCE" -eq 0 ]]; then
      echo "  SKIP $skill: already exists at $dst"
      echo "       re-run with --force to replace it (a backup is kept)"
      continue
    fi
    backup="$dst.bak.$(date +%Y%m%d%H%M%S)"
    mv "$dst" "$backup"
    echo "  backed up existing $skill to $(basename "$backup")"
  fi

  if [[ "$MODE" == link ]]; then
    ln -s "$src" "$dst"
    echo "  linked $skill"
  else
    cp -R "$src" "$dst"
    echo "  copied $skill"
  fi
done

chmod +x "$REPO/scripts/copy_scan.py" \
         "$REPO/skills/umanizzatore/scripts/scan_it.py" \
         "$REPO/skills/structural-humanizer/scripts/structural_scan.py" 2>/dev/null || true

cat <<EOF

done. verify with:
  ls -la $TARGET | grep -E 'humanizer'

run the scanners:
  python3 $REPO/skills/umanizzatore/scripts/scan_it.py <file>      # italiano
  python3 $REPO/scripts/copy_scan.py <file>                         # English
  python3 $REPO/skills/structural-humanizer/scripts/structural_scan.py <file>
EOF

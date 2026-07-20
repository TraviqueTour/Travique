#!/bin/bash
# Double-click this file on a Mac to start the Travique website.
cd "$(dirname "$0")"
echo "Setting up (first run installs a few small packages)..."
python3 -m pip install --quiet -r requirements.txt 2>/dev/null || \
  python3 -m pip install --quiet --user -r requirements.txt 2>/dev/null || \
  python3 -m pip install --quiet --break-system-packages -r requirements.txt

# Optional: uncomment and paste your Resend key to send real confirmation emails
# export RESEND_API_KEY="re_your_key_here"
# export FROM_EMAIL="Travique <onboarding@resend.dev>"

python3 app.py &
SERVER_PID=$!
sleep 2
open "http://127.0.0.1:5000"
echo ""
echo "Travique is running. Close this window (or press Ctrl+C) to stop the site."
wait $SERVER_PID

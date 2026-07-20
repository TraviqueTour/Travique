# Travique — Discover Chiang Mai (local booking website)

A simple tour-booking website styled like your booklet. Guests scroll through the
tours like slides, pick a **date + time**, and book. Every booking is saved to
**Excel** and a **confirmation email** is sent to the guest.

## Run it (Mac)

1. Double-click **`start.command`**.
   (First run installs Flask/openpyxl and opens your browser automatically.)
2. Your site opens at **http://127.0.0.1:5000**

If double-click is blocked, right-click `start.command` → Open → Open.

### Run it manually (any OS)
```
pip install -r requirements.txt
python3 app.py
```
Then open http://127.0.0.1:5000

## Where things are

| What | Where |
|------|-------|
| Guest-facing site | http://127.0.0.1:5000 |
| View all bookings | http://127.0.0.1:5000/admin |
| Excel of bookings | `bookings.xlsx` (created after the first booking) |

The Excel file has one row per booking: reference, tour, date, slot, guest name,
email, phone, party size, estimated total, notes, and email status. Open it in
Excel anytime — it updates automatically.

## Turning on real confirmation emails (Resend)

By default bookings are recorded and the email is marked `logged (no email key)`.
To send real emails:

1. Create a free account at **resend.com** and copy an **API key**.
2. Open `start.command`, uncomment the `RESEND_API_KEY` line, and paste your key.
   (To send from your own domain, verify it in Resend and set `FROM_EMAIL`.)
3. Save and restart.

The test sender `onboarding@resend.dev` only delivers to the email on your Resend
account — verify a domain to email real guests. Set `NOTIFY_EMAIL` if you also want
a copy of every booking sent to yourself.

## Editing tours / prices

All tour content lives in `tours.py` (title, price, kids price, time slots,
highlights, and which booklet page image to show). Edit and restart.

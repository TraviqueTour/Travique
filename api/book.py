"""
Travique booking endpoint (Vercel serverless function).

The website posts a booking here (same origin, so no CORS issues).
This function validates it, works out the price, and forwards it to your
Google Apps Script webhook, which saves the row to your Google Sheet and
emails the guest. The webhook URL is read from the SHEETS_WEBHOOK_URL
environment variable you set in Vercel.
"""
from http.server import BaseHTTPRequestHandler
import json
import os
import re
import datetime as dt
import urllib.request

# Tour prices (kept here so totals can't be tampered with from the browser)
TOURS = {
    "elephant-half": {"title": "Elephant Sanctuary", "price": 1300, "kid_price": 700},
    "elephant-waterfall": {"title": "Elephants & Sticky Waterfall", "price": 1700, "kid_price": 1100},
    "chiang-rai": {"title": "Chiang Rai — White Temple", "price": 1500, "kid_price": 1200},
    "chiang-rai-full": {"title": "Full Chiang Rai", "price": 2000, "kid_price": 1550},
    "doi-suthep": {"title": "Doi Suthep & Hmong Village", "price": 1200, "kid_price": 850},
    "doi-inthanon": {"title": "Doi Inthanon National Park", "price": 1500, "kid_price": 1100},
    "sacred-3-temples": {"title": "Sacred Journey — 3 Temples", "price": 1990, "kid_price": None},
    "five-temples": {"title": "5 Temples Blessings", "price": 3490, "kid_price": None},
    "bamboo-rafting": {"title": "Bamboo Rafting & Elephants", "price": 1800, "kid_price": 1300},
    "full-day-nature": {"title": "Full Day Nature", "price": 2000, "kid_price": 1300},
    "cooking-class": {"title": "Thai Cooking Class", "price": 900, "kid_price": None},
    "sip-thailand": {"title": "Sip Thailand — Wine Experience", "price": 3500, "kid_price": None},
    "cocktail-experience": {"title": "Cocktail Experience", "price": 1490, "kid_price": None},
}

WEBHOOK = os.environ.get("SHEETS_WEBHOOK_URL", "").strip()


def _int(v, lo, default):
    try:
        return max(lo, int(v))
    except (TypeError, ValueError):
        return default


def process(data):
    tour = TOURS.get(data.get("tour_id"))
    if not tour:
        return 400, {"ok": False, "error": "Unknown tour."}

    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    if not name or not re.match(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        return 400, {"ok": False, "error": "Please enter a name and a valid email."}

    date_str = (data.get("date") or "").strip()
    if not date_str:
        return 400, {"ok": False, "error": "Please choose a tour date."}

    slot = (data.get("slot") or "").strip()
    phone = (data.get("phone") or "").strip()
    notes = (data.get("notes") or "").strip()
    adults = _int(data.get("adults"), 1, 1)
    children = _int(data.get("children"), 0, 0)

    kid_price = tour["kid_price"] if tour["kid_price"] is not None else tour["price"]
    total = adults * tour["price"] + children * kid_price
    booking_id = "TRV-" + dt.datetime.now().strftime("%y%m%d-%H%M%S-") + \
        dt.datetime.now().strftime("%f")[:3]

    payload = {
        "booking_id": booking_id,
        "tour": tour["title"],
        "date": date_str,
        "slot": slot,
        "name": name,
        "email": email,
        "phone": phone,
        "adults": adults,
        "children": children,
        "total": total,
        "notes": notes,
    }

    email_status = "not saved (webhook not set)"
    if WEBHOOK:
        try:
            req = urllib.request.Request(
                WEBHOOK,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=20) as r:
                body = r.read().decode("utf-8", "ignore")
            try:
                res = json.loads(body)
                email_status = "sent" if res.get("ok") else "saved (email issue)"
            except ValueError:
                email_status = "sent"
        except Exception as e:  # noqa
            email_status = "error (%s)" % type(e).__name__

    return 200, {"ok": True, "booking_id": booking_id, "total": total,
                 "email_status": email_status}


class handler(BaseHTTPRequestHandler):
    def _send(self, code, obj):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            data = json.loads(self.rfile.read(length) or b"{}")
        except Exception:
            return self._send(400, {"ok": False, "error": "Bad request."})
        code, resp = process(data)
        self._send(code, resp)

    def do_GET(self):
        self._send(200, {"ok": True, "message": "Travique booking endpoint is live."})

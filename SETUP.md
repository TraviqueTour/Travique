# Travique — Go Live on Vercel (detailed setup)

This is the **online** version of your website. Follow the parts in order.
Nothing here needs coding — you create one Google Sheet, paste one script, copy
one link, and click Deploy. Take it slowly; each part is short.

**What you'll end up with:** your tour site live on the internet, every booking
saved into a Google Sheet, and each guest emailed a confirmation from your Gmail.

**The pieces (plain English):**
- **GitHub** — stores these website files online.
- **Vercel** — runs the website (free, no computer to keep on).
- **Google Sheet + Apps Script** — saves bookings and emails guests.

---

## Part 1 — Make your bookings Google Sheet  (5 min)

1. Go to **sheets.google.com** and click the **＋ Blank spreadsheet**.
2. Rename it (top-left) to **Travique Bookings**.
3. At the bottom, double-click the tab name `Sheet1` and rename it to **Bookings**
   (exact spelling, capital B). Leave the sheet empty — the script fills the
   headings automatically on the first booking.

Keep this tab open — you'll come back to it.

---

## Part 2 — Add the script that saves bookings + emails guests  (10 min)

1. In that same Google Sheet, click the menu **Extensions ▸ Apps Script**.
   A new tab opens with a code editor.
2. Delete anything already in the editor (select all, delete).
3. Open the file **`apps_script/Code.gs`** from this folder, copy **everything**
   in it, and paste it into the Apps Script editor.
4. Click the **💾 Save** icon (or Ctrl/Cmd-S).

Now publish it so your website can reach it:

5. Top-right, click **Deploy ▸ New deployment**.
6. Click the gear ⚙ next to "Select type" and choose **Web app**.
7. Fill in:
   - **Description:** Travique bookings
   - **Execute as:** **Me (your email)**
   - **Who has access:** **Anyone**
8. Click **Deploy**.
9. Google will ask you to **Authorize access** — click it, choose your Google
   account, click **Advanced ▸ Go to (your project) (unsafe)** if it warns
   (this is normal for your own script), then **Allow**. This permission lets the
   script save rows and send the confirmation emails from your Gmail.
10. It shows a **Web app URL** ending in `/exec`. Click **Copy**. 

**Paste that URL somewhere safe — you need it in Part 4.**
It looks like: `https://script.google.com/macros/s/AKfy..../exec`

> Tip: if you ever change `Code.gs`, do **Deploy ▸ Manage deployments ▸ ✏ Edit ▸
> Version: New version ▸ Deploy** so the change goes live (the URL stays the same).

---

## Part 3 — Put these files on GitHub  (10 min)

You already have a repository called **Travique**. Now add these new files to it.
(The old files from the on-your-computer version can stay — Vercel ignores them —
but you may delete `app.py`, `templates.py`, `tours.py`, `start.command`,
`requirements.txt` to keep it tidy.)

1. Open your repository at **github.com** → your **Travique** repo.
2. Click **Add file ▸ Upload files**.
3. From this folder, drag in:
   - **`index.html`**
   - the **`api`** folder (contains `book.py`)
   - the **`static`** folder (the tour images) — if it's already there from before, you can skip it
4. Scroll down, click **Commit changes**.

Your repo should now contain `index.html` and `api/book.py` at minimum.

> The `api/book.py` file must sit inside a folder named exactly **`api`** at the
> top of the repo — that's how Vercel knows it's the booking function.

---

## Part 4 — Deploy on Vercel + connect the Sheet  (10 min)

1. Go to **vercel.com** and **Sign Up** (choose **Continue with GitHub**).
2. Click **Add New ▸ Project**, find your **Travique** repo, click **Import**.
3. Before deploying, open **Environment Variables** and add:
   - **Name:** `SHEETS_WEBHOOK_URL`
   - **Value:** the `/exec` URL you copied in Part 2
   - Click **Add**.
4. Click **Deploy** and wait for the ✓.
5. You'll get a live link like **`travique.vercel.app`**. Open it.

> If you deployed before adding the variable, add it under **Settings ▸
> Environment Variables**, then **Deployments ▸ ⋯ ▸ Redeploy**.

---

## Part 5 — Test it  (2 min)

1. Open your `travique.vercel.app` link.
2. Scroll to any tour → **Book this tour** → fill it in with **your own email** →
   **Confirm booking**.
3. Check three things:
   - The success message shows a reference number.
   - A new row appears in your **Google Sheet**.
   - The **confirmation email** arrives in your inbox.

If the row doesn't appear: re-check that `SHEETS_WEBHOOK_URL` in Vercel exactly
matches the `/exec` URL, and that you clicked **Redeploy** after adding it.

---

## Part 6 — Connect your DotArai domain  (when ready)

1. In Vercel: your project → **Settings ▸ Domains** → type your web address →
   **Add**. Vercel shows two values — keep that screen open.
2. Log in at **register.dotarai.com** → **Domain** → your domain.
3. Make sure the **Name Servers** are `ns1.dotarai.com` and `ns2.dotarai.com`
   (this unlocks the DNS "zone file" editor). If they're different, ask DotArai
   support to switch them.
4. In the zone file, add the records Vercel showed you:
   - **A record** — Host `@` → the IP Vercel shows (currently `216.150.1.1`)
   - **CNAME** — Host `www` → the value Vercel shows (a `…vercel-dns…` address)
   - Delete any old "parked"/forwarding record. **Save.**
5. Wait a few minutes to a few hours. Vercel adds the padlock (HTTPS) by itself.
   Visit your domain — you're live.

**DotArai support:** phone 0-2105-4134 · Line @dotarai.

---

## Editing tours or prices later

- **Text/prices shown on the site:** edit `index.html` (search for the tour name).
- **Prices used for the total + emails:** also edit the `TOURS` list at the top of
  `api/book.py` so the charged total matches.
- Commit the change on GitHub — Vercel updates your live site automatically within
  a minute. (Ask Claude if you'd like help making an edit.)

## Notes
- Gmail can send up to ~100 confirmation emails per day on a normal account —
  plenty for a small tour business. Ask about a higher limit if you ever need it.
- Your bookings live in your Google Sheet; you can sort, filter, or export to
  Excel anytime (**File ▸ Download ▸ Microsoft Excel**).

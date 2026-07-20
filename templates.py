# HTML templates for the Travique site (rendered with Jinja2).

INDEX_HTML = r"""
<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Travique - Discover Chiang Mai</title>
<style>
:root{--green:#1f3d1e;--green2:#2e5a2b;--cream:#f4efe4;--gold:#b7791f;}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',Helvetica,Arial,sans-serif;color:var(--green);background:#0d1a0c;
 scroll-snap-type:y mandatory;overflow-x:hidden}
html{scroll-behavior:smooth}
.topbar{position:fixed;top:0;left:0;right:0;z-index:50;display:flex;justify-content:space-between;
 align-items:center;padding:14px 22px;background:linear-gradient(#0d1a0ccc,transparent);color:#fff}
.brand{font-size:22px;letter-spacing:6px;font-weight:600}
.topbar a{color:#fff;text-decoration:none;font-size:13px;letter-spacing:2px;opacity:.85}
.topbar a:hover{opacity:1}
.slide{position:relative;height:100vh;scroll-snap-align:start;display:flex;align-items:flex-end;
 justify-content:center;overflow:hidden}
.slide img.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center}
.slide .veil{position:absolute;inset:0;background:linear-gradient(transparent 38%,#061105f2 100%)}
.card{position:relative;z-index:2;width:min(940px,92%);margin-bottom:6vh;
 background:rgba(244,239,228,.95);border-radius:18px;padding:22px 26px;
 box-shadow:0 18px 50px #000a;display:flex;gap:22px;flex-wrap:wrap;align-items:center}
.card h2{font-size:26px;line-height:1.05}
.card .tag{color:var(--green2);font-style:italic;margin:4px 0 10px;font-size:15px}
.meta{display:flex;gap:16px;flex-wrap:wrap;font-size:13px;color:#444;margin-bottom:8px}
.meta b{color:var(--green)}
.price{font-size:30px;font-weight:700;color:var(--gold)}
.price small{font-size:13px;color:#666;font-weight:400}
.hl{flex:1 1 340px;font-size:13px;color:#3a3a3a;columns:2;column-gap:20px}
.hl div{margin-bottom:4px;break-inside:avoid}.hl div:before{content:'\2713  ';color:var(--green2)}
.left{flex:1 1 240px}
.book-btn{margin-top:12px;background:var(--green);color:#fff;border:none;border-radius:30px;
 padding:12px 26px;font-size:15px;letter-spacing:1px;cursor:pointer;transition:.15s}
.book-btn:hover{background:var(--green2);transform:translateY(-1px)}
.hero{align-items:center}.hero .htext{position:relative;z-index:2;text-align:center;color:#fff}
.hero h1{font-size:15px;letter-spacing:8px}.hero .big{font-size:64px;letter-spacing:2px;margin:6px 0;
 font-family:Georgia,'Times New Roman',serif}
.hero p{opacity:.9;margin-bottom:18px}
.scrolldown{position:absolute;bottom:26px;left:50%;transform:translateX(-50%);color:#fff;font-size:12px;
 letter-spacing:3px;z-index:3;animation:bob 1.8s infinite}
@keyframes bob{50%{transform:translate(-50%,8px)}}
.modal{position:fixed;inset:0;background:#000a;display:none;z-index:100;align-items:center;justify-content:center;padding:16px}
.modal.open{display:flex}
.sheet{background:#fff;border-radius:18px;width:min(460px,96%);max-height:92vh;overflow:auto;padding:26px}
.sheet h3{color:var(--green);font-size:22px;margin-bottom:2px}
.sheet .sub{color:#777;font-size:13px;margin-bottom:16px}
.field{margin-bottom:12px}
.field label{display:block;font-size:12px;color:#555;margin-bottom:4px;letter-spacing:.3px}
.field input,.field select,.field textarea{width:100%;padding:10px 12px;border:1px solid #cfc9bb;
 border-radius:10px;font-size:14px;font-family:inherit}
.row{display:flex;gap:10px}.row .field{flex:1}
.est{background:var(--cream);border-radius:10px;padding:10px 14px;font-size:14px;margin:6px 0 14px}
.est b{color:var(--gold);font-size:18px}
.submit{width:100%;background:var(--green);color:#fff;border:none;border-radius:30px;padding:13px;
 font-size:16px;cursor:pointer;letter-spacing:1px}.submit:hover{background:var(--green2)}
.x{float:right;font-size:22px;color:#999;cursor:pointer;line-height:1}
.ok{text-align:center;padding:10px 0}.ok .check{font-size:52px}
.err{color:#b00;font-size:13px;margin-top:8px;display:none}
.footer{background:var(--green);color:#e8e2d2;text-align:center;padding:34px;scroll-snap-align:start}
.footer .b{font-size:26px;letter-spacing:8px;margin-bottom:6px}
</style></head><body>

<div class="topbar">
  <div class="brand">TRAVIQUE</div>
  <div><a href="#tours">TOURS</a> &nbsp;&middot;&nbsp; <a href="/admin">BOOKINGS</a></div>
</div>

<section class="slide hero">
  <img class="bg" src="/static/img/page01.jpg" alt="">
  <div class="veil"></div>
  <div class="htext">
    <h1>DISCOVER</h1>
    <div class="big">Chiang Mai</div>
    <p>Elephants &middot; Temples &middot; Waterfalls &middot; Thai Cooking &amp; more</p>
    <button class="book-btn" onclick="document.getElementById('tours').scrollIntoView()">EXPLORE TOURS</button>
  </div>
  <div class="scrolldown">SCROLL &#9662;</div>
</section>

<div id="tours"></div>
{% for t in tours %}
<section class="slide">
  <img class="bg" src="/static/img/{{ t.img }}" alt="{{ t.title }}">
  <div class="veil"></div>
  <div class="card">
    <div class="left">
      <h2>{{ t.title }}</h2>
      <div class="tag">{{ t.tagline }}</div>
      <div class="meta"><span><b>{{ t.duration }}</b></span>
        {% if t.kid_price %}<span>Kids 3-7: <b>{{ "{:,}".format(t.kid_price) }} THB</b></span>{% endif %}</div>
      <div class="price">{{ "{:,}".format(t.price) }} THB <small>/ adult</small></div>
      <button class="book-btn" onclick="openBook('{{ t.id }}')">Book this tour</button>
    </div>
    <div class="hl">
      {% for h in t.highlights %}<div>{{ h }}</div>{% endfor %}
    </div>
  </div>
</section>
{% endfor %}

<footer class="footer">
  <div class="b">TRAVIQUE</div>
  <div>Ready for your Chiang Mai adventure? Book above &mdash; we'll email your confirmation.</div>
</footer>

<div class="modal" id="modal">
  <div class="sheet">
    <span class="x" onclick="closeBook()">&times;</span>
    <div id="form-wrap">
      <h3 id="m-title"></h3>
      <div class="sub" id="m-sub"></div>
      <div class="field"><label>Full name *</label><input id="f-name" placeholder="Your name"></div>
      <div class="field"><label>Email *</label><input id="f-email" type="email" placeholder="you@email.com"></div>
      <div class="field"><label>Phone / WhatsApp</label><input id="f-phone" placeholder="Optional"></div>
      <div class="row">
        <div class="field"><label>Tour date *</label><input id="f-date" type="date" min="{{ today }}"></div>
        <div class="field"><label>Time slot *</label><select id="f-slot"></select></div>
      </div>
      <div class="row">
        <div class="field"><label>Adults</label><input id="f-adults" type="number" min="1" value="1"></div>
        <div class="field"><label>Children (3-7)</label><input id="f-children" type="number" min="0" value="0"></div>
      </div>
      <div class="field"><label>Notes (hotel, pickup, requests)</label><textarea id="f-notes" rows="2"></textarea></div>
      <div class="est">Estimated total: <b id="f-total">-</b></div>
      <button class="submit" onclick="submitBook()">Confirm booking</button>
      <div class="err" id="f-err"></div>
    </div>
    <div id="done" style="display:none" class="ok">
      <div class="check">&#9989;</div>
      <h3>Booking received!</h3>
      <div class="sub" id="done-msg"></div>
      <button class="submit" style="margin-top:14px" onclick="closeBook()">Done</button>
    </div>
  </div>
</div>

<script>
const TOURS = {{ tours_json|safe }};
let cur = null;
function openBook(id){
  cur = TOURS.find(t=>t.id===id);
  document.getElementById('m-title').textContent = 'Book: '+cur.title;
  document.getElementById('m-sub').textContent = cur.duration+' · '+cur.price.toLocaleString()+' THB per adult';
  const sel = document.getElementById('f-slot'); sel.innerHTML='';
  cur.slots.forEach(s=>{const o=document.createElement('option');o.textContent=s;o.value=s;sel.appendChild(o);});
  ['name','email','phone','notes'].forEach(f=>document.getElementById('f-'+f).value='');
  document.getElementById('f-adults').value=1; document.getElementById('f-children').value=0;
  document.getElementById('f-date').value='';
  document.getElementById('f-err').style.display='none';
  document.getElementById('form-wrap').style.display='block';
  document.getElementById('done').style.display='none';
  updTotal();
  document.getElementById('modal').classList.add('open');
}
function closeBook(){document.getElementById('modal').classList.remove('open');}
function updTotal(){
  if(!cur) return;
  const a=+document.getElementById('f-adults').value||0;
  const c=+document.getElementById('f-children').value||0;
  const kp = cur.kid_price!=null?cur.kid_price:cur.price;
  const tot=a*cur.price+c*kp;
  document.getElementById('f-total').textContent=tot.toLocaleString()+' THB';
}
['f-adults','f-children'].forEach(id=>document.getElementById(id).addEventListener('input',updTotal));
async function submitBook(){
  const err=document.getElementById('f-err');
  const name=document.getElementById('f-name').value.trim();
  const email=document.getElementById('f-email').value.trim();
  const date=document.getElementById('f-date').value;
  if(!name||!email.includes('@')){err.textContent='Please enter your name and a valid email.';err.style.display='block';return;}
  if(!date){err.textContent='Please choose a tour date.';err.style.display='block';return;}
  const payload={tour_id:cur.id,name,email,phone:document.getElementById('f-phone').value,
    date,slot:document.getElementById('f-slot').value,
    adults:document.getElementById('f-adults').value,children:document.getElementById('f-children').value,
    notes:document.getElementById('f-notes').value};
  let j;
  try{
    const r=await fetch('/book',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});
    j=await r.json();
  }catch(e){err.textContent='Could not reach the server.';err.style.display='block';return;}
  if(!j.ok){err.textContent=j.error||'Something went wrong.';err.style.display='block';return;}
  const msg = j.email_status==='sent'
     ? 'Confirmation sent to '+email+'. Total ≈ '+j.total.toLocaleString()+' THB. Ref '+j.booking_id
     : 'Reference '+j.booking_id+' · Total ≈ '+j.total.toLocaleString()+' THB. We will email you shortly.';
  document.getElementById('done-msg').textContent=msg;
  document.getElementById('form-wrap').style.display='none';
  document.getElementById('done').style.display='block';
}
document.getElementById('modal').addEventListener('click',e=>{if(e.target.id==='modal')closeBook();});
</script>
</body></html>
"""

ADMIN_HTML = r"""
<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Travique - Bookings</title>
<style>
body{font-family:'Segoe UI',Arial,sans-serif;background:#f4efe4;color:#1f3d1e;margin:0;padding:24px}
h1{letter-spacing:4px}.bar{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px}
a.back{color:#2e5a2b;text-decoration:none}
.stats{display:flex;gap:14px;margin:18px 0;flex-wrap:wrap}
.stat{background:#fff;border-radius:14px;padding:16px 22px;box-shadow:0 4px 14px #0001;min-width:140px}
.stat .n{font-size:28px;font-weight:700;color:#b7791f}.stat .l{font-size:12px;color:#666;letter-spacing:1px}
table{width:100%;border-collapse:collapse;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 4px 14px #0001}
th,td{padding:10px 12px;text-align:left;font-size:13px;border-bottom:1px solid #eee}
th{background:#1f3d1e;color:#fff;letter-spacing:.5px;font-weight:600}
tr:hover td{background:#faf7ee}
.tag{display:inline-block;background:#e7f0e5;color:#2e5a2b;border-radius:20px;padding:2px 10px;font-size:12px}
.empty{background:#fff;border-radius:12px;padding:40px;text-align:center;color:#888}
.note{color:#777;font-size:12px;margin-top:14px}
</style></head><body>
<div class="bar"><h1>BOOKINGS</h1><a class="back" href="/">&larr; Back to site</a></div>
<div class="stats">
  <div class="stat"><div class="n">{{ bookings|length }}</div><div class="l">TOTAL BOOKINGS</div></div>
  <div class="stat"><div class="n">{{ total_guests }}</div><div class="l">GUESTS</div></div>
  <div class="stat"><div class="n">{{ "{:,}".format(revenue) }}</div><div class="l">EST. REVENUE (THB)</div></div>
</div>
{% if bookings %}
<table><thead><tr>
<th>Ref</th><th>Tour</th><th>Date</th><th>Slot</th><th>Guest</th><th>Email</th><th>Pax</th><th>Total</th><th>Email</th><th>Booked</th>
</tr></thead><tbody>
{% for b in bookings %}<tr>
<td>{{ b['Booking ID'] }}</td><td><span class="tag">{{ b['Tour'] }}</span></td>
<td>{{ b['Tour Date'] }}</td><td>{{ b['Time Slot'] }}</td>
<td>{{ b['Guest Name'] }}</td><td>{{ b['Email'] }}</td>
<td>{{ b['Adults'] }}A {{ b['Children'] }}C</td>
<td>{{ "{:,}".format(b['Estimated Total (THB)']|int) }}</td>
<td>{{ b['Email Status'] }}</td><td>{{ b['Booked At'] }}</td>
</tr>{% endfor %}
</tbody></table>
{% else %}<div class="empty">No bookings yet. They will appear here as guests book.</div>{% endif %}
<div class="note">All bookings are also saved to <b>{{ xlsx }}</b> in the app folder &mdash; open it in Excel anytime.</div>
</body></html>
"""

EMAIL_HTML = r"""
<div style="font-family:Segoe UI,Arial,sans-serif;max-width:560px;margin:auto;border:1px solid #e5e0d2;border-radius:14px;overflow:hidden">
  <div style="background:#1f3d1e;color:#fff;padding:22px 26px">
    <div style="letter-spacing:6px;font-size:20px">TRAVIQUE</div>
    <div style="opacity:.85;font-size:13px">Discover Chiang Mai</div>
  </div>
  <div style="padding:24px 26px;color:#243">
    <p>Hi {{ guest }},</p>
    <p>Thank you for booking with Travique! Here are your details:</p>
    <table style="width:100%;font-size:14px;border-collapse:collapse">
      <tr><td style="padding:6px 0;color:#777">Tour</td><td style="text-align:right"><b>{{ tour.title }}</b></td></tr>
      <tr><td style="padding:6px 0;color:#777">Date</td><td style="text-align:right">{{ date_str }}</td></tr>
      <tr><td style="padding:6px 0;color:#777">Time</td><td style="text-align:right">{{ slot }}</td></tr>
      <tr><td style="padding:6px 0;color:#777">Estimated total</td><td style="text-align:right"><b>{{ "{:,}".format(total) }} THB</b></td></tr>
    </table>
    <p style="margin-top:18px">We'll be in touch to confirm your hotel pickup. Reply to this email for any changes.</p>
    <p style="color:#777;font-size:13px">See you soon in Chiang Mai!</p>
  </div>
</div>
"""

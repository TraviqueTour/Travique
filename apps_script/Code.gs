/**
 * Travique — Google Apps Script
 * Paste this into your Google Sheet:  Extensions ▸ Apps Script
 * It saves each booking as a new row AND emails the guest a confirmation.
 * See SETUP.md for the click-by-click deploy steps.
 */

var HEADERS = ['Booking ID', 'Booked At', 'Tour', 'Tour Date', 'Time Slot',
  'Guest Name', 'Email', 'Phone', 'Adults', 'Children', 'Total (THB)', 'Notes'];

function doPost(e) {
  try {
    var d = JSON.parse(e.postData.contents);
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName('Bookings') || ss.getActiveSheet();

    // Add a header row the first time
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(HEADERS);
      sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold');
    }

    sheet.appendRow([
      d.booking_id, new Date(), d.tour, d.date, d.slot,
      d.name, d.email, d.phone, d.adults, d.children, d.total, d.notes
    ]);

    // Email the guest a confirmation (sends from your Gmail)
    if (d.email) {
      var html =
        '<div style="font-family:Segoe UI,Arial,sans-serif;max-width:560px;margin:auto;border:1px solid #e5e0d2;border-radius:14px;overflow:hidden">' +
          '<div style="background:#1f3d1e;color:#fff;padding:22px 26px">' +
            '<div style="letter-spacing:6px;font-size:20px">TRAVIQUE</div>' +
            '<div style="opacity:.85;font-size:13px">Discover Chiang Mai</div>' +
          '</div>' +
          '<div style="padding:24px 26px;color:#243">' +
            '<p>Hi ' + d.name + ',</p>' +
            '<p>Thank you for booking with Travique! Here are your details:</p>' +
            '<table style="width:100%;font-size:14px;border-collapse:collapse">' +
              row_('Tour', d.tour) + row_('Date', d.date) + row_('Time', d.slot) +
              row_('Guests', d.adults + ' adult(s), ' + d.children + ' child(ren)') +
              row_('Estimated total', Number(d.total).toLocaleString() + ' THB') +
              row_('Reference', d.booking_id) +
            '</table>' +
            '<p style="margin-top:18px">We will be in touch to confirm your hotel pickup. ' +
            'Reply to this email for any changes.</p>' +
            '<p style="color:#777;font-size:13px">See you soon in Chiang Mai!</p>' +
          '</div>' +
        '</div>';

      MailApp.sendEmail({
        to: d.email,
        subject: 'Your Travique booking - ' + d.tour,
        htmlBody: html
      });
    }

    return json_({ ok: true });
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  }
}

function row_(label, value) {
  return '<tr><td style="padding:6px 0;color:#777">' + label +
    '</td><td style="text-align:right"><b>' + value + '</b></td></tr>';
}

function json_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

// Optional: lets you check the script is deployed by opening the URL in a browser.
function doGet() {
  return json_({ ok: true, message: 'Travique booking receiver is live.' });
}

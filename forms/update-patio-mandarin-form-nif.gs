/**
 * Patio Language School. Mandarin form, NIF update (2026-10-01).
 *
 * Changes the EXISTING Mandarin registration form, so its link stays the same:
 *   1. Adds a required "Tax Identification Number / NIF" question right after "Full name".
 *   2. Removes the "Would you like your NIF included on your receipt?" question,
 *      plus the "Receipt" page and the "Your NIF" page that went with it.
 *
 * How to use: in the same Apps Script project, add a new file (+ next to Files > Script),
 * paste this in, save, choose updateMandarinFormNif in the function menu and click Run.
 * Safe to run twice: it skips anything already done.
 */
function updateMandarinFormNif() {
  var TITLE = 'Patio Language School. Mandarin registration · Inscrição mandarim · Fall 2026';
  var files = DriveApp.getFilesByName(TITLE);
  if (!files.hasNext()) { Logger.log('Form not found: ' + TITLE); return; }
  var form = FormApp.openById(files.next().getId());
  if (files.hasNext()) Logger.log('Note: more than one form has this name. Updating the first one found.');

  // 1. Remove the receipt question, then the Receipt page, the Your NIF page and the old NIF field.
  var removeStarts = [
    'Would you like your NIF included on your receipt?',
    'Receipt  /  Recibo',
    'Your NIF  /  O teu NIF',
    'NIF (Portuguese tax number)'
  ];
  // Order matters: the receipt question must go first, because it points to the pages.
  for (var k = 0; k < removeStarts.length; k++) {
    var items = form.getItems();
    for (var i = items.length - 1; i >= 0; i--) {
      var t = items[i].getTitle();
      if (t.indexOf(removeStarts[k]) === 0) {
        form.deleteItem(items[i]);
        Logger.log('Removed: ' + t);
      }
    }
  }

  // 2. Add the NIF question after "Full name", unless it is already there.
  var NIF_TITLE = 'Tax Identification Number / NIF  /  Número de Identificação Fiscal / NIF';
  items = form.getItems();
  var nameIndex = -1, existing = null;
  for (var j = 0; j < items.length; j++) {
    var title = items[j].getTitle();
    if (title.indexOf('Full name') === 0) nameIndex = j;
    if (title === NIF_TITLE) existing = items[j];
  }
  if (existing) {
    existing.asTextItem().setRequired(true).setHelpText('');
    Logger.log('NIF question already there. Made it required and removed the note.');
  } else if (nameIndex < 0) {
    Logger.log('Could not find the Full name question. NIF question not added.');
  } else {
    var nif = form.addTextItem()
      .setTitle(NIF_TITLE)
      .setRequired(true);
    form.moveItem(nif.getIndex(), nameIndex + 1);
    Logger.log('Added NIF question after Full name.');
  }

  Logger.log('Done. Live link unchanged: ' + form.getPublishedUrl());
}

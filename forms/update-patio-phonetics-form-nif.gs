/**
 * Patio Language School. Phonetics Workshop form, remove the optional NIF question (2026-10-14).
 *
 * Changes the EXISTING Phonetics booking form, so its link (patiolanguage.pt/phonetics) stays the same.
 *
 * How to use: in the same Apps Script project as createPatioPhoneticsForm, add a new file
 * (+ next to Files > Script), paste this in, save, choose removePhoneticsNif in the function
 * menu and click Run. Safe to run twice: it skips the question if it is already gone.
 */
function removePhoneticsNif() {
  var TITLE = 'Patio Language School. Portuguese Phonetics Workshop · Workshop de fonética portuguesa · Nov 2026';
  var files = DriveApp.getFilesByName(TITLE);
  if (!files.hasNext()) { Logger.log('Form not found: ' + TITLE); return; }
  var form = FormApp.openById(files.next().getId());
  if (files.hasNext()) Logger.log('Note: more than one form has this name. Updating the first one found.');

  var items = form.getItems();
  var removed = 0;
  for (var i = items.length - 1; i >= 0; i--) {
    var t = items[i].getTitle();
    if (t.indexOf('NIF (optional, for an invoice)') === 0) {
      form.deleteItem(items[i]);
      Logger.log('Removed: ' + t);
      removed++;
    }
  }
  if (!removed) Logger.log('No NIF question found, nothing to do.');
  Logger.log('Live link (unchanged):  ' + form.getPublishedUrl());
}

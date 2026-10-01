/**
 * Patio Language School. Mandarin form, group choices fix (2026-10-01).
 *
 * Rewrites the choices of the "Which group would you like to join?" question
 * on the EXISTING Mandarin form, so both groups show days, times, dates,
 * number of classes and price. The form link stays the same.
 *
 * How to use: paste over the code in update.gs, save, choose
 * updateMandarinGroupChoices in the function menu and click Run.
 */
function updateMandarinGroupChoices() {
  var CHOICES = [
    'Morning: Mon & Wed, 9h15 to 10h45. 19 Oct to 16 Dec. 18 classes. €295',
    'Afternoon: Tue & Thu, 15h00 to 16h30. 20 Oct to 17 Dec. 15 classes. €250',
    'Either is fine'
  ];

  var files = DriveApp.getFilesByName('Patio Language School. Mandarin registration · Fall 2026');
  if (!files.hasNext()) {
    files = DriveApp.getFilesByName('Patio Language School. Mandarin registration · Inscrição mandarim · Fall 2026');
  }
  if (!files.hasNext()) { Logger.log('Form not found. Nothing changed.'); return; }
  var form = FormApp.openById(files.next().getId());

  var items = form.getItems(FormApp.ItemType.MULTIPLE_CHOICE);
  for (var i = 0; i < items.length; i++) {
    if (items[i].getTitle().indexOf('Which group') === 0) {
      items[i].asMultipleChoiceItem().setChoiceValues(CHOICES);
      Logger.log('Updated group choices on: ' + items[i].getTitle());
      Logger.log('Done. Live link unchanged: ' + form.getPublishedUrl());
      return;
    }
  }
  Logger.log('Could not find the "Which group" question. Nothing changed.');
}

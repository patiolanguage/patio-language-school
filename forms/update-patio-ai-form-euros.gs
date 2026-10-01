/**
 * Change the "Which are you interested in?" options to use the euro sign.
 *
 * Run  updatePatioAIFormEuros  in script.google.com (paste this into a new
 * project, or add the function to your existing one, then Run).
 */
function updatePatioAIFormEuros() {
  var FORM_ID = '1Gr6E20SJb4fVCDNKGn5zJwH1LPZ1I6Y5okeHVqwM4vk';
  var form = FormApp.openById(FORM_ID);

  var items = form.getItems(FormApp.ItemType.CHECKBOX);
  for (var i = 0; i < items.length; i++) {
    var item = items[i];
    if (item.getTitle() === 'Which are you interested in?') {
      item.asCheckboxItem().setChoiceValues([
        'AI Made Practical, Happy Hour taster (Wed 7 Oct, €20)',
        'AI for Business, Wednesdays from 14 Oct (€249)',
        'AI Made Simple, Fridays from 16 Oct (€149)',
        'Not sure yet, help me choose'
      ]);
      Logger.log('Updated options with euro sign.');
      return;
    }
  }
  Logger.log('Checkbox question not found.');
}

/**
 * Patio Practical AI — "Register your interest" Google Form builder.
 *
 * Creates the whole form (all questions + settings) in one run.
 *
 * HOW TO RUN
 *   1. Go to https://script.google.com  (signed in as patiolanguage@gmail.com)
 *   2. New project  ->  delete the sample code  ->  paste this whole file.
 *   3. Press Run (the createPatioAIInterestForm function).
 *   4. Authorise when prompted (it needs permission to create Forms/Docs).
 *   5. Open View > Logs (or Execution log). It prints two links:
 *        - LIVE (share this / send it to Claude to wire into the site)
 *        - EDIT (to tweak the form yourself)
 *
 * Notes:
 *   - Respondents do NOT need a Google account: we ask for their email as a
 *     validated text field (we do not force Google sign-in).
 *   - Email notifications on new responses cannot be set by script. Turn them on
 *     once in the form: Responses tab > three dots > "Get email notifications
 *     for new responses". (Optional helper addSubmitNotification() below can
 *     email you on each response instead.)
 */

function createPatioAIInterestForm() {
  var form = FormApp.create('Patio Practical AI: Register your interest');

  form.setDescription(
    "Tell us which sessions you are interested in and we will be in touch to " +
    "confirm your place. There is nothing to pay here.\n\n" +
    "Practical AI at Patio, in person in Lagos. No tech background needed."
  );

  // Settings
  form.setCollectEmail(false);              // we use an explicit email field (no forced login)
  form.setLimitOneResponsePerUser(false);   // respondents need not be signed in
  form.setProgressBar(false);
  form.setAllowResponseEdits(false);
  form.setConfirmationMessage(
    "Thanks, your interest is registered. We will email you to confirm your " +
    "place and how to pay. There is nothing to pay online."
  );

  // 1. Name (required)
  form.addTextItem()
    .setTitle('Your name')
    .setRequired(true);

  // 2. Email (required, validated)
  var email = form.addTextItem()
    .setTitle('Email')
    .setHelpText('We will only use this to contact you about these AI courses.')
    .setRequired(true);
  email.setValidation(
    FormApp.createTextValidation()
      .setHelpText('Please enter a valid email address.')
      .requireTextIsEmail()
      .build()
  );

  // 3. WhatsApp (optional)
  form.addTextItem()
    .setTitle('WhatsApp number (optional)')
    .setHelpText('Handy if you would like a quick reply by message.');

  // 4. Which sessions (required, multi-select)
  form.addCheckboxItem()
    .setTitle('Which are you interested in?')
    .setHelpText('Choose as many as you like.')
    .setChoiceValues([
      'AI Made Practical, Happy Hour taster (Wed 7 Oct, 20 euros)',
      'AI for Business, Wednesdays from 14 Oct (249 euros)',
      'AI Made Simple, Fridays from 16 Oct (149 euros)',
      'Not sure yet, help me choose'
    ])
    .setRequired(true);

  // 5. Experience with AI (optional)
  form.addMultipleChoiceItem()
    .setTitle('How would you describe your experience with AI?')
    .setChoiceValues([
      'Complete beginner',
      'Used it a little',
      'Use it regularly'
    ]);

  // 6. Business context (optional)
  form.addTextItem()
    .setTitle('If you are interested in AI for Business, what does your business do? (optional)');

  // 7. Goals (optional)
  form.addParagraphTextItem()
    .setTitle('What would you most like to get out of it? (optional)')
    .setHelpText('A line or two helps us tailor the sessions.');

  // 8. How did you hear about us (optional, with Other)
  var heard = form.addMultipleChoiceItem()
    .setTitle('How did you hear about us?');
  heard.setChoices([
    heard.createChoice('A friend'),
    heard.createChoice('Instagram'),
    heard.createChoice('Facebook'),
    heard.createChoice('Walked past Patio')
  ]).showOtherOption(true);

  Logger.log('LIVE (share this): ' + form.getPublishedUrl());
  Logger.log('EDIT (to change it): ' + form.getEditUrl());
  return form.getPublishedUrl();
}

/**
 * OPTIONAL: email patiolanguage@gmail.com whenever someone submits.
 * Run this ONCE after creating the form to install the trigger. It attaches to
 * the most recently created form in your Drive; if you have several, open the
 * form's script instead. Simpler alternative: use the built-in Responses >
 * "Get email notifications" toggle and skip this.
 */
function addSubmitNotification() {
  var forms = DriveApp.getFilesByType(MimeType.GOOGLE_FORMS);
  if (!forms.hasNext()) { Logger.log('No form found.'); return; }
  var file = forms.next();
  var form = FormApp.openById(file.getId());
  ScriptApp.newTrigger('notifyOnSubmit')
    .forForm(form)
    .onFormSubmit()
    .create();
  Logger.log('Notification trigger added for: ' + form.getTitle());
}

function notifyOnSubmit(e) {
  var items = e.response.getItemResponses();
  var lines = items.map(function (it) {
    return it.getItem().getTitle() + ': ' + it.getResponse();
  });
  MailApp.sendEmail(
    'patiolanguage@gmail.com',
    'New Practical AI interest',
    lines.join('\n')
  );
}

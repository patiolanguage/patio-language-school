/**
 * Patio Language School — Fall Term 2026 registration form builder.
 *
 * HOW TO USE
 * 1. Go to https://script.google.com (signed in as patiolanguage@gmail.com) and click "New project".
 * 2. Delete the sample code, paste ALL of this in, and click Save (disk icon).
 * 3. Choose the function "createPatioRegistrationForm" in the toolbar and click Run.
 * 4. The first time, Google asks you to authorize — allow it (it's your own script).
 * 5. When it finishes, open View > Logs (or Executions) to see the two links:
 *      • EDIT link  — to open/tweak the form
 *      • LIVE link  — to share with students
 *    The form also appears in your Google Drive as "Patio Language School — Fall Term 2026 Registration".
 *
 * Re-running makes a NEW copy each time, so only run it once (or delete the old one).
 */
function createPatioRegistrationForm() {
  var form = FormApp.create('Patio Language School — Fall Term 2026 Registration');

  form.setDescription(
    'Register for our first term at Patio Language School — European Portuguese in Lagos, ' +
    '21 September to 18 December 2026.\n\n' +
    'Group courses are €11/hour (Mon/Wed courses = 37.5 hours over the term ≈ €412.50; ' +
    'Tue/Thu courses = 34.5 hours ≈ €379.50). Workshops & Conversation: drop-in €20, or a 5-session pack €85. ' +
    'Private lessons on request.\n\n' +
    'Fill this in and we’ll be in touch to confirm your place and help you find your level. Até já!'
  );

  form.setProgressBar(true);
  form.setCollectEmail(false);          // no Google sign-in required; we ask for email below
  form.setAllowResponseEdits(false);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage(
    'Obrigada! Thanks for registering with Patio. We’ll be in touch soon to confirm your place ' +
    'and help with anything you need. Até já!'
  );

  /* ---------------- PAGE 1 — Course selection ---------------- */
  form.addSectionHeaderItem()
    .setTitle('Choose your course(s)')
    .setHelpText('Term 1: 21 September – 18 December 2026. Not sure of your level? Pick the last option and we’ll help you find the right class.');

  form.addCheckboxItem()
    .setTitle('Which course(s) would you like to join?')
    .setChoiceValues([
      'A1 · Beginner — Morning (Mon & Wed, 9h15–10h45)',
      'A1 · Beginner — Evening (Tue & Thu, 18h30–20h00)',
      'A1.2 · Elementary (Tue & Thu, 11h00–12h30)',
      'A2 · Pre-Intermediate (Tue & Thu, 9h15–10h45)',
      'B1+ · Intermediate (Mon & Wed, 11h00–12h30)',
      'Conversation / Conversação — all levels (Fri, 11h00–12h30)',
      'Themed Workshops / Oficinas temáticas — all levels (Fri, 9h15–10h45)',
      'I’m not sure of my level — please help me choose'
    ])
    .setRequired(true);

  /* ---------------- PAGE 2 — Your details ---------------- */
  form.addPageBreakItem()
    .setTitle('Your details')
    .setHelpText('So we can confirm your place and keep in touch.');

  form.addTextItem().setTitle('Full name').setRequired(true);

  form.addParagraphTextItem()
    .setTitle('Address / Morada')
    .setHelpText('Street, postal code and town.')
    .setRequired(true);

  form.addTextItem()
    .setTitle('WhatsApp phone number')
    .setHelpText('Please include the country code, e.g. +351 …')
    .setRequired(true);

  var emailValidation = FormApp.createTextValidation().requireTextIsEmail().build();
  form.addTextItem()
    .setTitle('Email address')
    .setHelpText('Please enter a valid email address.')
    .setRequired(true)
    .setValidation(emailValidation);

  /* ---------------- PAGE 3 — Receipt / NIF question ---------------- */
  form.addPageBreakItem()
    .setTitle('Receipt')
    .setHelpText('For Portuguese tax purposes.');

  var receiptItem = form.addMultipleChoiceItem();

  /* ---------------- PAGE 4 — NIF (only if "Yes") ---------------- */
  var nifPage = form.addPageBreakItem()
    .setTitle('Your NIF')
    .setHelpText('We’ll add this to your receipt.');
  form.addTextItem()
    .setTitle('NIF (Portuguese tax number)')
    .setHelpText('9 digits.')
    .setRequired(true);

  /* ---------------- PAGE 5 — Photography ---------------- */
  var photoPage = form.addPageBreakItem()
    .setTitle('Photos & video')
    .setHelpText('From time to time we take photos or short videos in class and at events, which we may use ' +
      'on our website and social media to share the life of the school. Let us know your preference — ' +
      'you can change your mind at any time by telling us.');
  form.addMultipleChoiceItem()
    .setTitle('Photo & video consent')
    .setChoiceValues([
      'Yes — I’m happy for Patio to use photos/videos that may include me.',
      'No — please don’t use images that include me.'
    ])
    .setRequired(true);

  /* Now wire the receipt Yes/No branching (targets must exist first) */
  receiptItem
    .setTitle('Would you like your NIF included on your receipt?')
    .setRequired(true)
    .setChoices([
      receiptItem.createChoice('Yes, please include my NIF', nifPage),
      receiptItem.createChoice('No, thank you', photoPage)
    ]);

  /* ---------------- PAGE 6 — Terms & Conditions ---------------- */
  var terms =
    '1. Class placement\n' +
    'Students are placed according to their current language skills to ensure effective learning for the whole ' +
    'group. Instructors may adjust placement at any time if a class is not the right fit. Previous study or time ' +
    'living in Portugal is considered but does not override observed classroom performance. When possible, an ' +
    'alternative level will be offered.\n\n' +
    '2. Payment & your place\n' +
    'Your place is confirmed once payment is received. Group-course fees are payable before the term begins, ' +
    'unless another arrangement has been agreed.\n\n' +
    '3. Refunds & missed classes\n' +
    'We do not offer refunds or credits for classes missed due to illness, travel, or personal circumstances. ' +
    'If Patio cancels a course, you will be offered an alternative class or a full refund.\n\n' +
    '4. Minimum numbers\n' +
    'Courses run subject to a minimum number of students. We may adjust, combine, or reschedule a class, and ' +
    'will let you know as early as possible.\n\n' +
    '5. Public holidays\n' +
    'There are no classes on Portuguese public holidays (Mon 5 October, Tue 1 December and Tue 8 December 2026). ' +
    'Term hours already take these into account.\n\n' +
    '6. Timetable changes\n' +
    'Occasionally we may need to change a class time or teacher. We will give you as much notice as we can.\n\n' +
    '7. A respectful community\n' +
    'Patio is a warm, welcoming space. We ask everyone to be respectful of teachers and fellow students.\n\n' +
    '8. Your information\n' +
    'The details you provide are used only to organise your classes and to keep in touch about Patio. ' +
    'We do not share them with third parties.';

  form.addPageBreakItem().setTitle('Terms & Conditions').setHelpText(terms);

  form.addCheckboxItem()
    .setTitle('Please confirm')
    .setChoiceValues(['I have read and agree to the Terms & Conditions.'])
    .setRequired(true);

  /* ---------------- Done — log the links ---------------- */
  Logger.log('EDIT this form here:  ' + form.getEditUrl());
  Logger.log('SHARE this form (live link):  ' + form.getPublishedUrl());
}

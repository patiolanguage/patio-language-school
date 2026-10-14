/**
 * Patio Language School. Portuguese Phonetics Workshop booking form (BILINGUAL EN / PT).
 * Mon 2 + Fri 6 November 2026, 9h15 to 10h45, €35 for both sessions, with Sofia, max 12 people.
 *
 * How to use:
 *   1. Go to script.google.com, signed in to the Patio Google account.
 *   2. New project. Paste this whole file in. Save.
 *   3. Choose createPatioPhoneticsForm in the function menu and click Run.
 *   4. Approve the permissions Google asks for.
 *   5. Open "Execution log". Copy the SHARE link and send it to Claude
 *      (it goes into _redirects as patiolanguage.pt/phonetics and /fonetica).
 *
 * It makes a NEW form each run, plus a Google Sheet that collects the answers,
 * and installs a trigger that:
 *   - emails patiolanguage@gmail.com every time someone books, and
 *   - closes the form automatically once 12 people have booked.
 */
var PHONETICS_MAX_PLACES = 12;
var PATIO_EMAIL = 'patiolanguage@gmail.com';

function createPatioPhoneticsForm() {
  var form = FormApp.create('Patio Language School. Portuguese Phonetics Workshop · Workshop de fonética portuguesa · Nov 2026');

  form.setDescription(
    'Book your place on the Portuguese Phonetics Workshop with Sofia at Patio Language School in Lagos.\n' +
    'Two mornings: Monday 2 and Friday 6 November 2026, 9h15 to 10h45. €35 for both sessions. Maximum 12 people.\n' +
    'Patio, Praça do Poder Local, Lote 14, Loja C, Lagos.\n\n———\n\n' +
    'Reserva o teu lugar no workshop de fonética portuguesa com a Sofia, na Patio Language School em Lagos.\n' +
    'Duas manhãs: segunda 2 e sexta 6 de novembro de 2026, 9h15 às 10h45. 35 € pelas duas sessões. Máximo 12 pessoas.\n' +
    'Patio, Praça do Poder Local, Lote 14, Loja C, Lagos.'
  );

  form.setProgressBar(true);
  form.setCollectEmail(false);
  form.setAllowResponseEdits(false);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage(
    'Thank you! We have your booking for the Phonetics Workshop. We will message you on WhatsApp to confirm your place ' +
    'and send the payment details. See you on 2 November!\n\n' +
    'Obrigada! Recebemos a tua reserva para o workshop de fonética. Vamos enviar-te uma mensagem no WhatsApp para ' +
    'confirmar o teu lugar e enviar os dados de pagamento. Até dia 2 de novembro!'
  );
  form.setCustomClosedFormMessage(
    'The Phonetics Workshop is now full. Message us on WhatsApp (+351 928 129 560) to join the waiting list.\n\n' +
    'O workshop de fonética está esgotado. Envia-nos uma mensagem no WhatsApp (+351 928 129 560) para ficares na lista de espera.'
  );

  /* PAGE 1: You and your Portuguese */
  form.addSectionHeaderItem()
    .setTitle('Your Portuguese  /  O teu português')
    .setHelpText('This helps Sofia plan the workshop around the group.  /  Isto ajuda a Sofia a preparar o workshop para o grupo.');

  form.addMultipleChoiceItem()
    .setTitle('Your level  /  O teu nível')
    .setChoiceValues([
      'Beginner (A1)  /  Principiante (A1)',
      'Elementary (A2)  /  Elementar (A2)',
      'Intermediate (B1)  /  Intermédio (B1)',
      'Upper intermediate or above (B2+)  /  Intermédio superior ou acima (B2+)',
      'Not sure  /  Não sei'
    ])
    .setRequired(true);

  form.addCheckboxItem()
    .setTitle('Which sounds would you most like to work on?  /  Que sons mais queres trabalhar?')
    .setChoiceValues([
      'The nasal ão  /  O ão nasal',
      'The "sh" s  /  O s que soa "ch"',
      'lh and nh  /  lh e nh',
      'The r sounds  /  Os sons do r',
      'Vowels in general  /  As vogais em geral',
      'Everything!  /  Tudo!'
    ])
    .setRequired(false);

  form.addParagraphTextItem()
    .setTitle('Anything else we should know?  /  Mais alguma coisa que devamos saber?')
    .setHelpText('Optional. For example a word you always get wrong.  /  Opcional. Por exemplo, uma palavra que te custa sempre.')
    .setRequired(false);

  /* PAGE 2: Your details */
  form.addPageBreakItem()
    .setTitle('Your details  /  Os teus dados')
    .setHelpText('So we can confirm your place.  /  Para confirmarmos o teu lugar.');
  form.addTextItem().setTitle('Full name  /  Nome completo').setRequired(true);
  form.addTextItem()
    .setTitle('WhatsApp phone number  /  Número de WhatsApp')
    .setHelpText('Please include the country code, e.g. +351 …  /  Inclui o indicativo do país, ex.: +351 …')
    .setRequired(true);
  var emailValidation = FormApp.createTextValidation().requireTextIsEmail().build();
  form.addTextItem()
    .setTitle('Email address  /  Endereço de email')
    .setRequired(true).setValidation(emailValidation);
  form.addMultipleChoiceItem()
    .setTitle('Are you a current Patio student?  /  És aluno/a do Patio?')
    .setChoiceValues(['Yes  /  Sim', 'No  /  Não'])
    .setRequired(true);
  form.addMultipleChoiceItem()
    .setTitle('How did you hear about the workshop?  /  Como soubeste do workshop?')
    .setChoiceValues(['Instagram', 'Facebook', 'WhatsApp', 'Flyer / Folheto', 'A friend  /  Um amigo', 'Patio website  /  Site do Patio'])
    .showOtherOption(true)
    .setRequired(false);

  /* PAGE 3: Photos and terms */
  form.addPageBreakItem()
    .setTitle('Photos & terms  /  Fotografias e condições');

  form.addMultipleChoiceItem()
    .setTitle('Photo & video consent  /  Autorização de imagem')
    .setHelpText('We sometimes take photos in class to share on our website and social media.  /  ' +
      'Às vezes tiramos fotografias nas aulas para partilhar no site e nas redes sociais.')
    .setChoiceValues([
      'Yes, I am happy for Patio to use photos/videos that may include me.  /  Sim, autorizo o Patio a usar fotografias/vídeos onde eu possa aparecer.',
      'No, please do not use images that include me.  /  Não, não usem imagens onde eu apareça.'
    ])
    .setRequired(true);

  var termsEN =
    '1. Your place is confirmed once we receive your payment of €35, which covers both sessions.\n' +
    '2. The workshop is limited to 12 people. Places are given in order of booking.\n' +
    '3. If Patio has to cancel or move the workshop, you can choose a new date or a full refund.\n' +
    '4. If you cannot come, tell us at least 48 hours before 2 November and we will refund you or move your place to a friend. ' +
    'After that we cannot refund missed sessions.\n' +
    '5. Your details are used only to organise the workshop and keep in touch about Patio. We do not share them.';
  var termsPT =
    '1. O teu lugar fica confirmado quando recebermos o pagamento de 35 €, que inclui as duas sessões.\n' +
    '2. O workshop tem um máximo de 12 pessoas. Os lugares são atribuídos por ordem de reserva.\n' +
    '3. Se o Patio tiver de cancelar ou mudar o workshop, podes escolher uma nova data ou o reembolso total.\n' +
    '4. Se não puderes vir, avisa-nos pelo menos 48 horas antes de 2 de novembro e devolvemos o valor ou passamos o lugar a um amigo. ' +
    'Depois disso não há reembolso por sessões perdidas.\n' +
    '5. Os teus dados são usados apenas para organizar o workshop e manter o contacto sobre o Patio. Não os partilhamos.';

  form.addCheckboxItem()
    .setTitle('Terms  /  Condições')
    .setHelpText(termsEN + '\n\n———\n\n' + termsPT)
    .setChoiceValues(['I have read and agree to the terms.  /  Li e aceito as condições.'])
    .setRequired(true);

  /* Collect answers in a Google Sheet */
  var sheet = SpreadsheetApp.create('Patio Phonetics Workshop Nov 2026 (bookings)');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, sheet.getId());

  /* Email on each booking + close the form when full */
  ScriptApp.newTrigger('onPhoneticsBooking').forForm(form).onFormSubmit().create();

  Logger.log('EDIT this form here:  ' + form.getEditUrl());
  Logger.log('SHARE this form (live link):  ' + form.getPublishedUrl());
  Logger.log('BOOKINGS sheet:  ' + sheet.getUrl());
}

/** Runs on every submission (installed by createPatioPhoneticsForm). */
function onPhoneticsBooking(e) {
  var form = e.source;
  var count = form.getResponses().length;

  var lines = e.response.getItemResponses().map(function (r) {
    var a = r.getResponse();
    return r.getItem().getTitle().split('  /  ')[0] + ': ' + (Array.isArray(a) ? a.join(', ') : a);
  });
  MailApp.sendEmail(PATIO_EMAIL,
    'New Phonetics Workshop booking (' + count + '/' + PHONETICS_MAX_PLACES + ')',
    lines.join('\n') + '\n\nNext: message them on WhatsApp to confirm and send payment details.');

  if (count >= PHONETICS_MAX_PLACES) {
    form.setAcceptingResponses(false);
    MailApp.sendEmail(PATIO_EMAIL, 'Phonetics Workshop is FULL',
      PHONETICS_MAX_PLACES + ' bookings received, so the form is now closed. ' +
      'New people will see the "full, message us for the waiting list" note.');
  }
}

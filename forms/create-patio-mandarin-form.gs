/**
 * Patio Language School. Mandarin, Fall 2026 registration form (BILINGUAL EN / PT).
 *
 * How to use:
 *   1. Go to script.google.com, signed in to the Patio Google account.
 *   2. New project. Paste this whole file in. Save.
 *   3. Choose createPatioMandarinForm in the function menu and click Run.
 *   4. Approve the permissions Google asks for.
 *   5. Open "Execution log". Copy the SHARE link and send it to Claude.
 *
 * It makes a NEW form each run, plus a Google Sheet that collects the answers.
 * Both appear in your Drive.
 */
function createPatioMandarinForm() {
  var form = FormApp.create('Patio Language School. Mandarin registration · Inscrição mandarim · Fall 2026');

  form.setDescription(
    'Register for Mandarin at Patio Language School in Lagos. Small groups, all levels welcome. ' +
    'Starts the week of 19 October 2026. Fill this in and we will be in touch to confirm your place.\n\n———\n\n' +
    'Inscreve-te nas aulas de mandarim da Patio Language School em Lagos. Grupos pequenos, todos os níveis ' +
    'são bem-vindos. Começa na semana de 19 de outubro de 2026. Preenche este formulário e entramos em ' +
    'contacto para confirmar o teu lugar. Até já!'
  );

  form.setProgressBar(true);
  form.setCollectEmail(false);
  form.setAllowResponseEdits(false);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage(
    'Thanks for registering for Mandarin at Patio! We will be in touch soon to confirm your place.\n\n' +
    'Obrigada por te inscreveres no mandarim do Patio! Entraremos em contacto em breve para confirmar o teu lugar. Até já!'
  );

  /* PAGE 1: Group and level */
  form.addSectionHeaderItem()
    .setTitle('Choose your group  /  Escolhe o teu grupo')
    .setHelpText('Fall 2026. Two classes a week, 90 minutes each.  /  Outono 2026. Duas aulas por semana, 90 minutos cada.');

  form.addMultipleChoiceItem()
    .setTitle('Which group would you like to join?  /  Em que grupo te queres inscrever?')
    .setChoiceValues([
      'Morning / Manhã: Mon & Wed / Seg & Qua, 9h15 to 10h45. 19 Oct to 16 Dec. 18 classes. €295',
      'Afternoon / Tarde: Tue & Thu / Ter & Qui, 15h00 to 16h30. 20 Oct to 17 Dec. 15 classes. €250',
      'Either is fine  /  Qualquer um'
    ])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('Your Mandarin so far  /  O teu mandarim até agora')
    .setChoiceValues([
      'Complete beginner  /  Principiante absoluto',
      'I know a little  /  Sei um pouco',
      'I have studied before  /  Já estudei antes'
    ])
    .setRequired(true);

  /* PAGE 2: Your details */
  form.addPageBreakItem()
    .setTitle('Your details  /  Os teus dados')
    .setHelpText('So we can confirm your place and keep in touch.  /  Para confirmarmos o teu lugar e mantermos o contacto.');
  form.addTextItem().setTitle('Full name  /  Nome completo').setRequired(true);
  form.addTextItem()
    .setTitle('Tax Identification Number / NIF  /  Número de Identificação Fiscal / NIF')
    .setRequired(true);
  form.addParagraphTextItem()
    .setTitle('Address  /  Morada')
    .setHelpText('Street, postal code and town.  /  Rua, código postal e localidade.')
    .setRequired(true);
  form.addTextItem()
    .setTitle('WhatsApp phone number  /  Número de WhatsApp')
    .setHelpText('Please include the country code, e.g. +351 …  /  Inclui o indicativo do país, ex.: +351 …')
    .setRequired(true);
  var emailValidation = FormApp.createTextValidation().requireTextIsEmail().build();
  form.addTextItem()
    .setTitle('Email address  /  Endereço de email')
    .setHelpText('Please enter a valid email address.  /  Introduz um email válido.')
    .setRequired(true).setValidation(emailValidation);

  /* PAGE 3: Photography */
  form.addPageBreakItem()
    .setTitle('Photos & video  /  Fotografias e vídeo')
    .setHelpText('From time to time we take photos or short videos in class and at events, which we may use on our ' +
      'website and social media to share the life of the school. You can change your mind at any time by telling us.' +
      '\n\n———\n\n' +
      'De vez em quando tiramos fotografias ou pequenos vídeos nas aulas e em eventos, que podemos usar no nosso site ' +
      'e nas redes sociais para mostrar o dia a dia da escola. Podes mudar de ideias a qualquer momento.');
  form.addMultipleChoiceItem()
    .setTitle('Photo & video consent  /  Autorização de imagem')
    .setChoiceValues([
      'Yes, I am happy for Patio to use photos/videos that may include me.  /  Sim, autorizo o Patio a usar fotografias/vídeos onde eu possa aparecer.',
      'No, please do not use images that include me.  /  Não, não usem imagens onde eu apareça.'
    ])
    .setRequired(true);

  /* PAGE 4: Terms & Conditions */
  var termsEN =
    '1. Your place\n' +
    'Your place is confirmed once payment is received. Course fees are payable before the course begins, unless another arrangement has been agreed.\n\n' +
    '2. Minimum numbers\n' +
    'Each group runs only if enough students register. If a group does not run, we will offer you a place in the other group or a full refund.\n\n' +
    '3. Refunds & missed classes\n' +
    'We do not offer refunds or credits for classes missed due to illness, travel, or personal circumstances. If Patio cancels a course, you will be offered an alternative class or a full refund.\n\n' +
    '4. Public holidays\n' +
    'There are no classes on public holidays. The afternoon group has no class on Tue 27 October (Lagos holiday), Tue 1 December and Tue 8 December 2026. Course prices already take these into account.\n\n' +
    '5. Timetable changes\n' +
    'Occasionally we may need to change a class time or teacher. We will give you as much notice as we can.\n\n' +
    '6. A respectful community\n' +
    'Patio is a warm, welcoming space. We ask everyone to be respectful of teachers and fellow students.\n\n' +
    '7. Your information\n' +
    'The details you provide are used only to organise your classes and to keep in touch about Patio. We do not share them with third parties.';

  var termsPT =
    '1. O teu lugar\n' +
    'O teu lugar fica confirmado após a receção do pagamento. O curso é pago antes do início, salvo acordo em contrário.\n\n' +
    '2. Número mínimo de alunos\n' +
    'Cada grupo só funciona se houver inscrições suficientes. Se um grupo não abrir, oferecemos-te um lugar no outro grupo ou o reembolso total.\n\n' +
    '3. Reembolsos e faltas\n' +
    'Não há reembolsos nem créditos por aulas perdidas devido a doença, viagem ou circunstâncias pessoais. Se o Patio cancelar um curso, será oferecida uma turma alternativa ou o reembolso total.\n\n' +
    '4. Feriados\n' +
    'Não há aulas nos feriados. O grupo da tarde não tem aula na terça 27 de outubro (feriado de Lagos), terça 1 de dezembro e terça 8 de dezembro de 2026. Os preços dos cursos já têm isto em conta.\n\n' +
    '5. Alterações de horário\n' +
    'Ocasionalmente poderemos ter de alterar o horário ou o professor de uma turma. Avisaremos com a maior antecedência possível.\n\n' +
    '6. Uma comunidade respeitadora\n' +
    'O Patio é um espaço acolhedor e caloroso. Pedimos a todos que respeitem os professores e os colegas.\n\n' +
    '7. Os teus dados\n' +
    'Os dados que nos forneces são usados apenas para organizar as tuas aulas e manter o contacto sobre o Patio. Não os partilhamos com terceiros.';

  form.addPageBreakItem()
    .setTitle('Terms & Conditions  /  Termos e Condições')
    .setHelpText(termsEN + '\n\n———————————\n\n' + termsPT);

  form.addCheckboxItem()
    .setTitle('Please confirm  /  Confirma, por favor')
    .setChoiceValues(['I have read and agree to the Terms & Conditions.  /  Li e aceito os Termos e Condições.'])
    .setRequired(true);

  /* Collect answers in a Google Sheet */
  var sheet = SpreadsheetApp.create('Patio Mandarin registrations Fall 2026 (responses)');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, sheet.getId());

  Logger.log('EDIT this form here:  ' + form.getEditUrl());
  Logger.log('SHARE this form (live link):  ' + form.getPublishedUrl());
  Logger.log('RESPONSES sheet:  ' + sheet.getUrl());
}

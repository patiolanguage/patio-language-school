/**
 * Patio Language School — Fall Term 2026 registration form (BILINGUAL EN / PT).
 * Run createPatioRegistrationFormBilingual once. It prints an Edit link and a
 * Share link in the Execution log, and the form appears in your Drive.
 * (Creates a NEW form each run — delete the old English-only one if you don't need it.)
 */
function createPatioRegistrationFormBilingual() {
  var form = FormApp.create('Patio Language School — Registration · Inscrição · Fall Term 2026');

  form.setDescription(
    'Register for our first term at Patio Language School — European Portuguese in Lagos, ' +
    '21 September to 18 December 2026. Group courses €11/hour. Fill this in and we’ll be in touch ' +
    'to confirm your place and help you find your level.\n\n———\n\n' +
    'Inscreve-te no nosso primeiro período na Patio Language School — português europeu em Lagos, ' +
    'de 21 de setembro a 18 de dezembro de 2026. Cursos de grupo a €11/hora. Preenche este formulário ' +
    'e entramos em contacto para confirmar o teu lugar e ajudar-te a encontrar o teu nível. Até já!'
  );

  form.setProgressBar(true);
  form.setCollectEmail(false);
  form.setAllowResponseEdits(false);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage(
    'Thanks for registering with Patio! We’ll be in touch soon to confirm your place and help with anything you need.\n\n' +
    'Obrigada por te inscreveres no Pátio! Entraremos em contacto em breve para confirmar o teu lugar e ajudar no que precisares. Até já!'
  );

  /* PAGE 1 — Course selection */
  form.addSectionHeaderItem()
    .setTitle('Choose your course(s)  /  Escolhe o(s) teu(s) curso(s)')
    .setHelpText('Term 1: 21 September – 18 December 2026.  /  Período 1: 21 de setembro – 18 de dezembro de 2026.');

  form.addCheckboxItem()
    .setTitle('Which course(s) would you like to join?  /  A que curso(s) te queres juntar?')
    .setChoiceValues([
      'A1 · Beginner / Iniciante — Morning / Manhã (Mon & Wed / Seg & Qua, 9h15–10h45)',
      'A1 · Beginner / Iniciante — Evening / Tarde (Tue & Thu / Ter & Qui, 18h30–20h00)',
      'A1.2 · Elementary / Elementar (Tue & Thu / Ter & Qui, 11h00–12h30)',
      'A2 · Pre-Intermediate / Pré-Intermédio (Tue & Thu / Ter & Qui, 9h15–10h45)',
      'B1+ · Intermediate / Intermédio (Mon & Wed / Seg & Qua, 11h00–12h30)',
      'Conversation / Conversação — all levels / todos os níveis (Fri / Sex, 11h00–12h30)',
      'Themed Workshops / Oficinas temáticas — all levels / todos os níveis (Fri / Sex, 9h15–10h45)',
      'I’m not sure of my level — please help me choose  /  Não tenho a certeza do meu nível — ajudem-me a escolher'
    ])
    .setRequired(true);

  /* PAGE 2 — Your details */
  form.addPageBreakItem()
    .setTitle('Your details  /  Os teus dados')
    .setHelpText('So we can confirm your place and keep in touch.  /  Para confirmarmos o teu lugar e mantermos o contacto.');
  form.addTextItem().setTitle('Full name  /  Nome completo').setRequired(true);
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

  /* PAGE 3 — Receipt / NIF question */
  form.addPageBreakItem()
    .setTitle('Receipt  /  Recibo')
    .setHelpText('For Portuguese tax purposes.  /  Para efeitos fiscais.');
  var receiptItem = form.addMultipleChoiceItem();

  /* PAGE 4 — NIF (only if "Yes") */
  var nifPage = form.addPageBreakItem()
    .setTitle('Your NIF  /  O teu NIF')
    .setHelpText('We’ll add this to your receipt.  /  Vamos adicioná-lo ao teu recibo.');
  form.addTextItem()
    .setTitle('NIF (Portuguese tax number)  /  NIF (número de contribuinte)')
    .setHelpText('9 digits.  /  9 dígitos.')
    .setRequired(true);

  /* PAGE 5 — Photography */
  var photoPage = form.addPageBreakItem()
    .setTitle('Photos & video  /  Fotografias e vídeo')
    .setHelpText('From time to time we take photos or short videos in class and at events, which we may use on our ' +
      'website and social media to share the life of the school. You can change your mind at any time by telling us.' +
      '\n\n———\n\n' +
      'De vez em quando tiramos fotografias ou pequenos vídeos nas aulas e em eventos, que podemos usar no nosso site ' +
      'e nas redes sociais para mostrar o dia a dia da escola. Podes mudar de ideias a qualquer momento.');
  form.addMultipleChoiceItem()
    .setTitle('Photo & video consent  /  Autorização de imagem')
    .setChoiceValues([
      'Yes — I’m happy for Patio to use photos/videos that may include me.  /  Sim — autorizo o Pátio a usar fotografias/vídeos onde eu possa aparecer.',
      'No — please don’t use images that include me.  /  Não — não usem imagens onde eu apareça.'
    ])
    .setRequired(true);

  /* Wire the receipt Yes/No branching */
  receiptItem.setTitle('Would you like your NIF included on your receipt?  /  Queres o teu NIF no recibo?')
    .setRequired(true)
    .setChoices([
      receiptItem.createChoice('Yes, please include my NIF  /  Sim, inclui o meu NIF', nifPage),
      receiptItem.createChoice('No, thank you  /  Não, obrigado(a)', photoPage)
    ]);

  /* PAGE 6 — Terms & Conditions */
  var termsEN =
    '1. Class placement\n' +
    'Students are placed according to their current language skills to ensure effective learning for the whole group. Instructors may adjust placement at any time if a class is not the right fit. Previous study or time living in Portugal is considered but does not override observed classroom performance. When possible, an alternative level will be offered.\n\n' +
    '2. Payment & your place\n' +
    'Your place is confirmed once payment is received. Group-course fees are payable before the term begins, unless another arrangement has been agreed.\n\n' +
    '3. Refunds & missed classes\n' +
    'We do not offer refunds or credits for classes missed due to illness, travel, or personal circumstances. If Patio cancels a course, you will be offered an alternative class or a full refund.\n\n' +
    '4. Minimum numbers\n' +
    'Courses run subject to a minimum number of students. We may adjust, combine, or reschedule a class, and will let you know as early as possible.\n\n' +
    '5. Public holidays\n' +
    'There are no classes on Portuguese public holidays (Mon 5 October, Tue 1 December and Tue 8 December 2026). Term hours already take these into account.\n\n' +
    '6. Timetable changes\n' +
    'Occasionally we may need to change a class time or teacher. We will give you as much notice as we can.\n\n' +
    '7. A respectful community\n' +
    'Patio is a warm, welcoming space. We ask everyone to be respectful of teachers and fellow students.\n\n' +
    '8. Your information\n' +
    'The details you provide are used only to organise your classes and to keep in touch about Patio. We do not share them with third parties.';

  var termsPT =
    '1. Colocação nas turmas\n' +
    'Os alunos são colocados de acordo com o seu nível atual de língua, para garantir uma aprendizagem eficaz para todo o grupo. Os professores podem ajustar a colocação a qualquer momento se a turma não for a mais adequada. A experiência anterior ou o tempo vivido em Portugal são tidos em conta, mas não se sobrepõem ao desempenho observado em aula. Sempre que possível, será oferecido um nível alternativo.\n\n' +
    '2. Pagamento e o teu lugar\n' +
    'O teu lugar fica confirmado após a receção do pagamento. As propinas dos cursos de grupo são pagas antes do início do período, salvo acordo em contrário.\n\n' +
    '3. Reembolsos e faltas\n' +
    'Não há reembolsos nem créditos por aulas perdidas devido a doença, viagem ou circunstâncias pessoais. Se o Pátio cancelar um curso, será oferecida uma turma alternativa ou o reembolso total.\n\n' +
    '4. Número mínimo de alunos\n' +
    'Os cursos funcionam sujeitos a um número mínimo de alunos. Podemos ajustar, juntar ou reagendar uma turma e avisaremos com a maior antecedência possível.\n\n' +
    '5. Feriados\n' +
    'Não há aulas nos feriados portugueses (segunda 5 de outubro, terça 1 de dezembro e terça 8 de dezembro de 2026). As horas do período já têm isto em conta.\n\n' +
    '6. Alterações de horário\n' +
    'Ocasionalmente poderemos ter de alterar o horário ou o professor de uma turma. Avisaremos com a maior antecedência possível.\n\n' +
    '7. Uma comunidade respeitadora\n' +
    'O Pátio é um espaço acolhedor e caloroso. Pedimos a todos que respeitem os professores e os colegas.\n\n' +
    '8. Os teus dados\n' +
    'Os dados que nos forneces são usados apenas para organizar as tuas aulas e manter o contacto sobre o Pátio. Não os partilhamos com terceiros.';

  form.addPageBreakItem()
    .setTitle('Terms & Conditions  /  Termos e Condições')
    .setHelpText(termsEN + '\n\n———————————\n\n' + termsPT);

  form.addCheckboxItem()
    .setTitle('Please confirm  /  Confirma, por favor')
    .setChoiceValues(['I have read and agree to the Terms & Conditions.  /  Li e aceito os Termos e Condições.'])
    .setRequired(true);

  Logger.log('EDIT this form here:  ' + form.getEditUrl());
  Logger.log('SHARE this form (live link):  ' + form.getPublishedUrl());
}

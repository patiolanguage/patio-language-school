/**
 * Patio Practical AI — "AI Made Practical" feedback survey (Google Form builder).
 *
 * Short follow-up survey for people who came to the kick-off Happy Hour on
 * Wed 7 Oct. Includes a testimonial question for social media.
 *
 * HOW TO RUN
 *   1. Go to https://script.google.com  (signed in as patiolanguage@gmail.com)
 *   2. New project  ->  delete the sample code  ->  paste this whole file.
 *   3. Press Run (the createPatioAIFeedbackForm function).
 *   4. Authorise when prompted (it needs permission to create Forms).
 *   5. Open View > Logs (or Execution log). It prints two links:
 *        - LIVE (paste this into the follow-up email)
 *        - EDIT (to tweak the form yourself)
 *
 * Notes:
 *   - Anonymous by default: 4 questions, only the rating is required. Anyone
 *     offering a testimonial is asked for their name with it.
 *   - Turn on response emails once in the form: Responses tab > three dots >
 *     "Get email notifications for new responses".
 */

function createPatioAIFeedbackForm() {
  var form = FormApp.create('Patio Practical AI: How was AI Made Practical?');

  form.setDescription(
    "Thank you for coming to AI Made Practical at Patio on Wednesday 7 October. " +
    "This takes about 2 minutes and helps us shape the workshops. " +
    "Just 4 quick questions, and only the first is required."
  );

  form.setCollectEmail(false);
  form.setLimitOneResponsePerUser(false);
  form.setProgressBar(false);
  form.setAllowResponseEdits(false);
  form.setConfirmationMessage(
    "Thank you! We really appreciate it. If you offered a testimonial, we will " +
    "check with you before anything goes on social media."
  );

  // 1. Overall rating (required)
  form.addScaleItem()
    .setTitle('Overall, how would you rate the evening?')
    .setBounds(1, 5)
    .setLabels('Not great', 'Excellent')
    .setRequired(true);

  // 2. Feedback
  form.addParagraphTextItem()
    .setTitle('What was most useful, and what could we do better next time?');

  // 3. Next step
  form.addMultipleChoiceItem()
    .setTitle('Are you thinking of joining one of the workshops?')
    .setChoiceValues([
      'Yes, AI for Business (Wednesdays from 14 Oct)',
      'Yes, AI Made Simple (Fridays from 16 Oct)',
      'Interested, but the dates or times do not suit me',
      'Not right now'
    ]);

  // 4. Testimonial (consent, wording and name in one)
  form.addParagraphTextItem()
    .setTitle('Would you be happy to write a short testimonial we could share on social media? If yes, write it here.')
    .setHelpText(
      'Just a sentence or two about your experience. Please add your name as you would like it shown ' +
      '(full name, first name only, or "anonymous"). Leave blank if you would rather not. ' +
      'We will always check with you before posting.'
    );

  Logger.log('LIVE (put this in the email): ' + form.getPublishedUrl());
  Logger.log('EDIT (to change it): ' + form.getEditUrl());
  return form.getPublishedUrl();
}

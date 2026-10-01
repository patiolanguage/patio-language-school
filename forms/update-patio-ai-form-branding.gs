/**
 * Update the Patio Practical AI form's TITLE + SUBTITLE to match the flyer.
 *
 * Google Forms does NOT let a script set the theme colour or header image,
 * so those two are done by hand in the form (see steps at the bottom). This
 * script just sets the wording exactly.
 *
 * HOW TO RUN
 *   1. script.google.com  ->  New project  ->  paste this file  ->  Save.
 *   2. Run  updatePatioAIForm  ->  authorise if asked.
 *   3. Reload the form to see the new title and description.
 */

function updatePatioAIForm() {
  // The form's ID (from its edit URL: .../forms/d/<ID>/edit)
  var FORM_ID = '1Gr6E20SJb4fVCDNKGn5zJwH1LPZ1I6Y5okeHVqwM4vk';

  var form = FormApp.openById(FORM_ID);

  form.setTitle('Patio Practical AI');

  form.setDescription(
    'Project-based AI you can use right away. Hands-on and in person in Lagos, ' +
    'so you leave with confidence, clarity and time back. No tech background needed.\n\n' +
    'Tell us which sessions you want and we will be in touch to confirm your place. ' +
    'There is nothing to pay here.'
  );

  Logger.log('Updated: ' + form.getEditUrl());
}

/* --------------------------------------------------------------------------
 * THEN, add the colour branding by hand (one minute):
 *
 *   In the form editor, click the palette icon (Customize theme), top right.
 *     - Header:  Image  ->  Upload  ->  choose  form-header-ai.png
 *     - Colour:  pick Custom and enter  B8593A  (Patio terracotta)
 *     - Background: choose the lightest shade offered
 *     - Text style / font: pick a clean one (Forms fonts are limited; the
 *       header carries the brand look)
 *
 * That gives it the same branded feel as the Portuguese class form.
 * ------------------------------------------------------------------------ */

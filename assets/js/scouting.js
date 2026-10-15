(() => {
  const questionsRoot = document.getElementById('scouting-questions');
  const questionConfigNode = document.getElementById('scouting-question-config');
  const eventConfigNode = document.getElementById('scouting-event-config');
  const tournamentSelect = document.getElementById('scouting-tournament');
  const daySelect = document.getElementById('scouting-day');

  if (!questionsRoot || !questionConfigNode || !eventConfigNode || !tournamentSelect || !daySelect) return;

  const parseConfig = (node) => JSON.parse(node.textContent || 'null');
  const makeId = (value) => String(value || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

  function showQuestionError() {
    const message = document.createElement('p');
    message.className = 'scouting-error';
    message.setAttribute('role', 'alert');
    message.textContent = 'The profile questions could not be loaded. Please refresh the page to try again.';
    questionsRoot.replaceChildren(message);
  }

  function createHint(field) {
    if (!field.hint) return null;
    const hint = document.createElement('p');
    hint.className = 'scouting-field__hint';
    hint.id = `scouting-hint-${makeId(field.id)}`;
    hint.textContent = field.hint;
    return hint;
  }

  function decorateInput(input, field, hint) {
    input.id = `scouting-${makeId(field.id)}`;
    input.name = field.id;
    input.className = 'scouting-input';
    if (field.required) {
      input.required = true;
      input.setAttribute('aria-required', 'true');
    }
    if (hint) input.setAttribute('aria-describedby', hint.id);
    return input;
  }

  function appendUnit(control, unit) {
    if (!unit) return;
    const suffix = document.createElement('span');
    suffix.className = 'scouting-unit';
    suffix.textContent = unit;
    control.append(suffix);
  }

  function createChoiceOptions(field, inputType, hint) {
    const choices = document.createElement('div');
    choices.className = `scouting-options${field.type === 'multi_choice' ? ' scouting-options--checks' : ''}`;

    (field.options || []).forEach((option, index) => {
      const choiceId = `scouting-${makeId(field.id)}-${makeId(option.value || index)}`;
      const label = document.createElement('label');
      label.className = 'scouting-option';

      const input = document.createElement('input');
      input.type = inputType;
      input.id = choiceId;
      input.name = field.type === 'multi_choice' ? `${field.id}[]` : field.id;
      input.value = String(option.value ?? option.label ?? '');
      if (hint) input.setAttribute('aria-describedby', hint.id);
      if (field.required && inputType === 'radio') input.required = true;

      const text = document.createElement('span');
      text.textContent = option.label ?? String(option.value ?? '');
      label.htmlFor = choiceId;
      label.append(input, text);
      choices.append(label);
    });

    return choices;
  }

  function createQuestion(field) {
    const wrapper = document.createElement('fieldset');
    wrapper.className = `scouting-field scouting-field--${makeId(field.type)}${field.multiline ? ' scouting-field--multiline' : ''}`;

    const hint = createHint(field);
    const usesChoices = field.type === 'multi_choice' || field.type === 'yes_no';
    const label = document.createElement(usesChoices ? 'legend' : 'label');
    label.className = 'scouting-field__label';
    label.textContent = field.label;
    if (!usesChoices) label.htmlFor = `scouting-${makeId(field.id)}`;
    if (field.required) {
      const required = document.createElement('span');
      required.className = 'scouting-required';
      required.textContent = 'Required';
      label.append(' ', required);
    }
    wrapper.append(label);

    if (field.type === 'multi_choice') {
      wrapper.append(createChoiceOptions(field, 'checkbox', hint));
    } else if (field.type === 'yes_no') {
      const yesNoField = { ...field, options: [{ value: 'yes', label: 'Yes' }, { value: 'no', label: 'No' }] };
      wrapper.append(createChoiceOptions(yesNoField, 'radio', hint));
    } else if (field.type === 'single_choice') {
      const select = decorateInput(document.createElement('select'), field, hint);
      const placeholder = document.createElement('option');
      placeholder.value = '';
      placeholder.textContent = 'Choose an option';
      select.append(placeholder);
      (field.options || []).forEach((option) => {
        const item = document.createElement('option');
        item.value = String(option.value ?? option.label ?? '');
        item.textContent = option.label ?? String(option.value ?? '');
        select.append(item);
      });
      wrapper.append(select);
    } else if (field.type === 'text' || field.type === 'number') {
      const isLongText = field.type === 'text' && field.multiline;
      const input = isLongText ? document.createElement('textarea') : document.createElement('input');
      if (!isLongText) input.type = field.type;
      if (isLongText) input.rows = 4;
      decorateInput(input, field, hint);
      if (field.inputmode) input.inputMode = field.inputmode;
      if (field.min !== undefined) input.min = String(field.min);
      if (field.max !== undefined) input.max = String(field.max);
      if (field.step !== undefined) input.step = String(field.step);
      if (field.maxlength !== undefined) input.maxLength = Number(field.maxlength);
      const control = document.createElement('div');
      control.className = 'scouting-control__input';
      control.append(input);
      appendUnit(control, field.unit);
      wrapper.append(control);
    } else {
      const unsupported = document.createElement('p');
      unsupported.className = 'scouting-field__hint';
      unsupported.textContent = 'This question type is not supported by the scouting page yet.';
      wrapper.append(unsupported);
    }

    if (hint) wrapper.append(hint);
    return wrapper;
  }

  function renderQuestions(config) {
    if (!config || !Array.isArray(config.sections)) throw new Error('Scouting question configuration is invalid.');

    const fragment = document.createDocumentFragment();
    config.sections.forEach((section) => {
      const group = document.createElement('section');
      group.className = 'scouting-question-group';

      const heading = document.createElement('h3');
      heading.className = 'scouting-question-group__title';
      heading.textContent = section.title;
      group.append(heading);

      if (section.description) {
        const description = document.createElement('p');
        description.className = 'scouting-question-group__description';
        description.textContent = section.description;
        group.append(description);
      }

      const fieldGrid = document.createElement('div');
      fieldGrid.className = 'scouting-question-grid';
      (section.fields || []).forEach((field) => fieldGrid.append(createQuestion(field)));
      group.append(fieldGrid);
      fragment.append(group);
    });

    questionsRoot.replaceChildren(fragment);
  }

  function formatEventDate(value) {
    if (!value) return '';
    const parts = String(value).split('-').map(Number);
    if (parts.length !== 3 || parts.some(Number.isNaN)) return String(value);
    return new Intl.DateTimeFormat('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
      .format(new Date(parts[0], parts[1] - 1, parts[2]));
  }

  function eventId(event) {
    return String(event.id || makeId(event.name));
  }

  function eventDays(event) {
    const days = Array.isArray(event.days) ? event.days : (event.day ? [event.day] : []);
    return days.map((day) => String(day));
  }

  function updateDays(events, selectedTournament, preferredDay) {
    const event = events.find((item) => eventId(item) === selectedTournament);
    const placeholder = document.createElement('option');
    placeholder.value = '';
    placeholder.textContent = 'Choose a day';

    daySelect.replaceChildren(placeholder);
    daySelect.disabled = !event;
    if (!event) return;

    const days = eventDays(event);
    days.forEach((day) => {
      const option = document.createElement('option');
      option.value = day;
      option.textContent = day;
      daySelect.append(option);
    });

    if (preferredDay && days.includes(preferredDay)) {
      daySelect.value = preferredDay;
    } else if (days.length === 1) {
      daySelect.value = days[0];
    }
  }

  function renderEvents(events, defaults) {
    const placeholder = tournamentSelect.options[0];
    tournamentSelect.replaceChildren(placeholder);

    events.filter((event) => event.type === 'competition').forEach((event) => {
      const option = document.createElement('option');
      option.value = eventId(event);
      const date = formatEventDate(event.date);
      option.textContent = date ? `${event.name} · ${date}` : event.name;
      tournamentSelect.append(option);
    });

    const configuredTournament = defaults?.tournament_id || '';
    if (configuredTournament && events.some((event) => eventId(event) === configuredTournament)) {
      tournamentSelect.value = configuredTournament;
    }
    updateDays(events, tournamentSelect.value, defaults?.day || '');
    tournamentSelect.addEventListener('change', () => updateDays(events, tournamentSelect.value, ''));
  }

  try {
    const questionConfig = parseConfig(questionConfigNode);
    const events = parseConfig(eventConfigNode);
    if (!Array.isArray(events)) throw new Error('Scouting event configuration is invalid.');
    renderQuestions(questionConfig);
    renderEvents(events, questionConfig.defaults);
  } catch (error) {
    showQuestionError();
  }
})();

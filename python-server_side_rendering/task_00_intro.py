def generate_invitations(template, attendees):
    # 1. Verify types
    if not isinstance(template, str) or not isinstance(attendees, list):
        print('Invalid input types')
        return

    # 2. Verify if empty
    if template == '':
        print('Template is empty, no output files generated.')
        return
    if len(attendees) == 0:
        print('No data provided, no output files generated.')
        return

    # 3. For each person, fill the template and write the file
    for i, attendee in enumerate(attendees, 1):
        content = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            if value is None:
                value = 'N/A'
            content = content.replace('{' + key + '}', str(value))
        with open(f'output_{i}.txt', 'w') as f:
            f.write(content)

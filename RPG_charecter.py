full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intelligence, charisma):
    # --- Validate the name ---
    if not isinstance(character_name, str):
        return 'The character name should be a string'
    if character_name == '':
        return 'The character should have a name'
    if len(character_name) > 10:
        return 'The character name is too long'
    if ' ' in character_name:
        return 'The character name should not contain spaces'

    # --- Validate the stats ---
    stats = (strength, intelligence, charisma)

    if not all(isinstance(s, int) for s in stats):
        return 'All stats should be integers'
    if not all(s >= 1 for s in stats):
        return 'All stats should be no less than 1'
    if not all(s <= 4 for s in stats):
        return 'All stats should be no more than 4'
    if sum(stats) != 7:
        return 'The character should start with 7 points'

    # --- Build the output string ---
    stat_labels = ('STR', 'INT', 'CHA')
    lines = [character_name]
    for label, value in zip(stat_labels, stats):
        dots = full_dot * value + empty_dot * (10 - value)
        lines.append(f'{label} {dots}')
    return '\n'.join(lines)
charecter=create_character('rvn',2,3,2)
print(charecter)
# Run reader.py first to create the file options.txt
import reader

choices = [line.strip().split(',') for line in open('options.txt', 'r')]

while True:
    to_remove = [choice[0] for choice in choices if len(choice) == 1]

    if to_remove == []:
        break

    removed_something = False

    for i in range(len(choices)):
        if len(choices[i]) == 1:
            continue

        for value in to_remove:
            if value in choices[i]:
                removed_something = True
                choices[i].remove(value)

    if not removed_something:
        break

choices = [c[0] for c in choices]

tot = 1

for name, ticket_num in zip(choices, reader.get_file_data()['your ticket'][0].split(',')):
    if name.startswith("departure"):
        tot = tot * int(ticket_num)

print(tot)

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def dub_tickets(tickets):
    used_tickets = []
    for key in tickets:
        new_values_list = []
        for ticket in tickets[key]:
            if ticket not in used_tickets:
                new_values_list.append(ticket)
                used_tickets.append(ticket)
        tickets[key] = new_values_list
dub_tickets(tickets)

types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets_by_type = {}

def combine_dict():
    new_keys = list(types.values())
    old_keys = list(tickets.keys())

    for i in range(len(old_keys)):
        old_key = old_keys[i]
        new_key = new_keys[i]
        tickets_by_type[new_key] = tickets[old_key]
combine_dict()
import re


def get_file_content():
    input = open('input/day04.input', 'r')
    lines = input.read().splitlines()
    return lines

# ([0-9]{2}:[0-9]{2})/] Guard (#[0-9]*) (.*)'
def parse_file_line(line):
    match = re.match('\[([0-9]{4}-[0-9]{2}-[0-9]{2}) ([0-9]{2}:[0-9]{2})\] (.*)',line)
    date = match.group(1)
    time = match.group(2)
    event_group =  match.group(3)
    event_match = re.match(r'Guard #([0-9]*) (begins shift)',event_group)
    if event_match:
        guard = int(event_match.group(1))
        event = event_match.group(2)
    else:
        guard = None
        event = event_group
    return {"datetime": date +" "+time,"date":date,"time":time,"guard":guard,"event":event}

def get_file_content_events_by_shift(file_content_events):
    guard_list = []
    tmp_list = []
    for event in file_content_events:

       if event['event'] =='begins shift':
            if len(tmp_list)!=0:
                guard_list.append(tmp_list)
            tmp_list =[]
            tmp_list.append(event)
       else:
           tmp_list.append(event)

    if len(tmp_list)>0:
        guard_list.append(tmp_list)

    return guard_list

def group_shift_by_guards(shift_list):

    guard_dict = {str(guard):[] for guard in map(lambda shift: shift[0]['guard'],shift_list)}
    for key in guard_dict.keys():
       f = filter(lambda shift: shift[0]['guard'] == int(key), shift_list)
       guard_dict[key] = sum(f,[])
    return guard_dict

def group_shift_by_date(guard_shift_list):
    dates = list(set(map(lambda date: date['date'] ,guard_shift_list)))
    date_dict ={}
    for date in dates:
        date_dict[date] = filter(lambda event:event['date']==date,guard_shift_list)

    return date_dict


def count_minutes_of_shift_dict(shift_dict):
    keys = list(reversed(shift_dict.keys()))

    result_dict ={}

    minutes_dict = {str(minute): [] for minute in range(0, 60)}
    for date in keys:

        start = None
        stop = None
        counter_list = []
        for shift in shift_dict[date]:
            if shift['event'] == 'falls asleep':
                #print shift
                start = int(re.match('00:([0-9]{2})',shift['time']).group(1))
            if shift['event'] == 'wakes up':
                #print shift
                stop = int(re.match('00:([0-9]{2})',shift['time']).group(1))
            if start is not None and stop is not None:
                #print range(start,stop)
                for minute in range(start,stop):
                    minutes_dict[str(minute)].append(shift['date'])
                start = None
                stop = None
    return minutes_dict

def sum_minutes_for_guard_shifts(guard,shifts,shift_amount_per_minute):

    return {"guard": int(guard),"minutes_total": len(sum([shifts[x] for x in shifts.keys()],[])),"minute_of_hour":shift_amount_per_minute}

def get_shift_amount_per_minute(shift):
    return sorted([{"minute_of_hour": int(x), "amount": len(shift[x])} for x in shift.keys()], key=lambda k: k['amount'])

def get_total_minutes_for_guards_shift(shifts_by_guards):
    guard_minutes_total = []
    for guard in shifts_by_guards.keys():
        shift = count_minutes_of_shift_dict(group_shift_by_date(shifts_by_guards[str(guard)]))
        shift_amount_per_minute = get_shift_amount_per_minute(shift)
        minutes_summery = sum_minutes_for_guard_shifts(guard, shift,shift_amount_per_minute[-1]['minute_of_hour'])
        guard_minutes_total.append(minutes_summery)
    return sorted(guard_minutes_total,key=lambda k: k['minutes_total'])


def part_a():
    file_content_events = sorted(map(lambda event: parse_file_line(event), get_file_content()),key=lambda k: k['datetime'])

    events_by_shifts = get_file_content_events_by_shift(file_content_events)

    shifts_by_guards = group_shift_by_guards(events_by_shifts)
    guard_minutes_total = get_total_minutes_for_guards_shift(shifts_by_guards)
    the_one =  guard_minutes_total[-1]
    print the_one
    return int(the_one['minute_of_hour']) * int(the_one['guard'])

def part_b():
    file_content_events = sorted(map(lambda event: parse_file_line(event), get_file_content()),key=lambda k: k['datetime'])

    events_by_shifts = get_file_content_events_by_shift(file_content_events)

    shifts_by_guards = group_shift_by_guards(events_by_shifts)

    highest_amount_of_hours_list = []
    for guard in shifts_by_guards.keys():
        shift = count_minutes_of_shift_dict(group_shift_by_date(shifts_by_guards[str(guard)]))
        shift_amount_per_minute = get_shift_amount_per_minute(shift)
        highest_amount = shift_amount_per_minute[-1]
        highest_amount['guard'] = guard
        highest_amount_of_hours_list.append(highest_amount)

    the_one = sorted(highest_amount_of_hours_list,key=lambda k: k['amount'])[-1]
    return int(the_one['minute_of_hour']) * int(the_one['guard'])

if __name__ == "__main__":


    print 'Result part A: '+ str(part_a()) #19025
    print 'Result Part B: ' + str(part_b()) #23776








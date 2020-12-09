def has_cycle(instructions):
    i, visited = 0, []
    while i < len(instructions):
        if i in visited:
            return False, visited

        visited.append(i)
        inst, val = instructions[i]
        i += val if inst == 'jmp' else 1

    return True, visited


def fix_loop(raw_data):
    data = (line.split() for line in raw_data)
    cmds = [(cmd, int(val)) for cmd, val in data]

    finished, call_seq = has_cycle(cmds)
    call_cmds = [(i, cmds[i][0], cmds[i][1]) for i in call_seq]
    for i, cmd, val in reversed(call_cmds):
        if cmd in ('jmp', 'nop'):
            swap_cmd = 'jmp' if cmd == 'nop' else 'nop'
            finished, call_seq = has_cycle(cmds[:i] + [(swap_cmd, cmds[i][1])] + cmds[i+1:])
            if finished:
                return sum(cmds[i][1] for i in call_seq if cmds[i][0] == 'acc')


assert fix_loop(open('input-08.txt')) == 1539

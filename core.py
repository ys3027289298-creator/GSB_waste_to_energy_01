import json


def new_game():
    return {'queue': [], 'amount': 0, 'events': {1: (5, 6), 2: (1, 2)}, 'items': [], 'cap': 2, 'count': 0, 'closed': False, 'nodes': {1: True, 2: True}, 'edges': {(1, 2): 5}, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_26(state):
    for start, end in state["events"].values():
        if start >= end:
            return True
    return False

def bug_3(state):
    if not state["queue"]:
        return None
    return state["queue"].pop(0)

def bug_10(state):
    delta = -5
    if delta < 0:
        return False
    state["amount"] += delta
    return True

def bug_17(state):
    transfer = -5
    if transfer < 0:
        return False
    return True

def bug_24(state):
    return min(state["events"].items(), key=lambda item: item[1][0])[0]

def bug_1(state):
    if state["count"] >= state["cap"] or len(state["items"]) >= state["cap"]:
        return False
    state["items"].append("x")
    state["count"] += 1
    return True

def bug_8(state):
    state["count"] = 0
    return True

def bug_15(state):
    if state["closed"]:
        return False
    return True

def bug_22(state):
    intervals = list(state["events"].values())
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            start_a, end_a = intervals[i]
            start_b, end_b = intervals[j]
            if start_a < end_b and start_b < end_a:
                return False
    return True

def bug_29(state):
    state["nodes"].pop(1, None)
    for edge in [edge for edge in state["edges"] if 1 in edge]:
        del state["edges"][edge]
    return True

def bug_30(state):
    committed = state["snapshot"]
    working = state["value"]
    try:
        working += 1
        for _op, status in state["log"]:
            if status == "failed":
                raise RuntimeError("step failed")
        working += 1
    except RuntimeError:
        state["value"] = committed
        return False
    state["value"] = working
    state["snapshot"] = working
    return True

def bug_31(state):
    if state["settled"]:
        return False
    return True

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()

# file to simulate the "mancala" mechnism from board game trajan
import random
import itertools


mancala = [2, 2, 2, 2, 2, 2]


def select_random_action():
    return random.sample(list(itertools.filterfalse(lambda x: x[1] <= 0, enumerate(mancala))), 1)[0][0]


def get_moves(mancala_i, num_moves):
    return [(mancala_i + step + 1) % 6 for step in range(num_moves)]


def get_pick_for_action(action):
    hypo = [(i, (i + c) % 6) for i, c in enumerate(mancala) if c != 0]
    selection = [i for i, t in hypo if t == action]
    return selection


def act(mancala_i):
    num_moves = mancala[mancala_i]
    assert num_moves > 0, mancala
    mancala[mancala_i] = 0
    for move in get_moves(mancala_i, num_moves):
        mancala[move] += 1
    assert sum(mancala) == 12
    return move


def sim_random():
    """ simulate random select and move """
    seq = []
    hits = [0, 0, 0, 0, 0, 0]

    for i in range(1000):
        pick = select_random_action()
        print('Pick action: %d' % pick)
        action = act(pick)
        print('Mancala: %s' % str(mancala))
        seq.append(action)
        hits[action] += 1
    print(hits)
    #print([h / sum(hits) for h in hits])


def sim_always_pick():
    """ always pick one spot """
    seq = []
    hits = [0, 0, 0, 0, 0, 0]
    always = 0

    for i in range(10000):
        pick = always if mancala[always] != 0 else select_random_action()
        print('Pick action: %d' % pick)
        action = act(pick)
        print('Mancala: %s' % str(mancala))
        seq.append(action)
        hits[action] += 1
    print(hits)


def sim_gravity():
    """ always pick one spot """
    seq = []
    hits = [0, 0, 0, 0, 0, 0]
    towards = 0

    for i in range(10000):
        possible_pick = get_pick_for_action(towards)
        pick = random.sample(possible_pick, 1)[0] if possible_pick else select_random_action()
        print('Pick action: %d' % pick)
        action = act(pick)
        print('Mancala: %s' % str(mancala))
        seq.append(action)
        hits[action] += 1
    print(hits)


def sim_gravity_2():
    """ always pick 2 spot """
    seq = []
    hits = [0, 0, 0, 0, 0, 0]
    towards = [0, 3]

    for i in range(10000):
        possible_pick = get_pick_for_action(towards[0]) + get_pick_for_action(towards[1])
        pick = random.sample(possible_pick, 1)[0] if possible_pick else select_random_action()
        print('Pick action: %d' % pick)
        action = act(pick)
        print('Mancala: %s' % str(mancala))
        seq.append(action)
        hits[action] += 1
    print(hits)


def sim_gravity_3():
    """ always pick 2 spot """
    seq = []
    hits = [0, 0, 0, 0, 0, 0]
    towards = [0, 3, 5]

    for i in range(10000):
        possible_pick = get_pick_for_action(towards[0]) + get_pick_for_action(towards[1]) + get_pick_for_action(towards[2])
        pick = random.sample(possible_pick, 1)[0] if possible_pick else select_random_action()
        print('Pick action: %d' % pick)
        action = act(pick)
        print('Mancala: %s' % str(mancala))
        seq.append(action)
        hits[action] += 1
    print(hits)


def sim_gravity_4():
    """ always pick 4 spot """
    seq = []
    hits = [0, 0, 0, 0, 0, 0]
    towards = [0, 2, 3, 5]

    for i in range(10000):
        possible_pick = get_pick_for_action(towards[0]) + get_pick_for_action(towards[1]) + get_pick_for_action(towards[2]) + get_pick_for_action(towards[3])
        pick = random.sample(possible_pick, 1)[0] if possible_pick else select_random_action()
        print('Pick action: %d' % pick)
        action = act(pick)
        print('Mancala: %s' % str(mancala))
        seq.append(action)
        hits[action] += 1
    print(hits)


def sim_avoid():
    """ always avoid 1 spot """
    seq = []
    hits = [0, 0, 0, 0, 0, 0]
    towards = [1, 2, 3, 4, 5]

    for i in range(10000):
        possible_pick = get_pick_for_action(towards[0]) + get_pick_for_action(towards[1]) + get_pick_for_action(towards[2]) + get_pick_for_action(towards[3]) + get_pick_for_action(towards[4])
        pick = random.sample(possible_pick, 1)[0] if possible_pick else select_random_action()
        print('Pick action: %d' % pick)
        action = act(pick)
        print('Mancala: %s' % str(mancala))
        seq.append(action)
        hits[action] += 1
    print(hits)


if __name__ == '__main__':
    #print(select_random_action())
    #print(get_moves(0, 6))
    # print(act(4))
    # print(mancala)
    #sim_random()
    #sim_always_pick()
    #print(get_pick_for_action(2))
    sim_gravity_4()

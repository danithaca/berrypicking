import math, fileinput

results = []
for line in fileinput.input():
    # assumption: data is separated by ',' and first/last names does not have ',' that needs to be escaped.
    data = line.split(', ')
    length = len(data)

    if length < 2 or length > 7:
        # assumption: if invalid data, just ignore it. alternative: throw an exception
        continue
    elif length != 7:
        # append 0s.
        data = data + [0 for i in range(7 - length)]
    else:
        # length is 7,
        pass

    assert len(data) == 7

    first_name = data[0]
    last_name = data[1]
    # assumption: scores given are valid numbers. otherwise will throw an exception due to int()
    scores = sorted([int(s) for s in data[2:]], reverse=True)

    assert len(scores) == 5

    # round up for final score.
    final_score = math.ceil(sum(scores) / 5.0)

    # here we map final score to the final grade.
    # if we do this a lot and really cares about performance, then we would do something like:
    # grades_mapping = ['F', 'F', 'F', 'F', ...., 'A', 'A', 'A'] where len(grades_mapping} == 100
    # and then:
    # final_grade = grades_mapping[final_score]
    # that will sacrifice space for speed.
    # but here we'll just use comparison for code readability.

    # others may argue against the long list of comparison, but I'd prefer this because it's very straightforward
    # compared to using calculations which I believe is error-prone.
    # I think this is all about coding-style and needs to coordinate within the team.

    if 100 >= final_score >= 93:
        final_grade = 'A'
    elif 92 >= final_score >= 90:
        final_grade = 'A-'
    elif 89 >= final_score >= 87:
        final_grade = 'B+'
    elif 86 >= final_score >= 83:
        final_grade = 'B'
    elif 82 >= final_score >= 80:
        final_grade = 'B-'
    elif 79 >= final_score >= 77:
        final_grade = 'C+'
    elif 76 >= final_score >= 73:
        final_grade = 'C'
    elif 72 >= final_score >= 70:
        final_grade = 'C-'
    elif 69 >= final_score >= 67:
        final_grade = 'D+'
    elif 66 >= final_score >= 63:
        final_grade = 'D'
    elif 62 >= final_score >= 60:
        final_grade = 'D-'
    else:
        final_grade = 'F'

    results.append([last_name, first_name, final_score, final_grade] + scores)

# sort the results
results.sort(key=lambda x: x[2])

# print out results
for r in results:
    print('%s, %s, %d, %s: %d, %d, %d, %d, %d' % tuple(r))
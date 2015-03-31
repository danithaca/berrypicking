# :param: s1, s2: two strings to find the match. len might not be the same
# :return s, start, end: the longest matched string, and position. or '', -1, -1 if not found.
def find_match(s1, s2):
    longest_start, longest_end = -1, -1

    size = min(len(s1), len(s2))
    start, end = -1, -1
    matching = False

    for i in range(0, size):
        if s1[i] == s2[i]:
            if not matching:
                matching = True
                start = i
        else:
            if matching:
                matching = False
                end = i
                if (end - start) > (longest_start - longest_end):
                    longest_start = start
                    longest_end = end
                start, end = -1, -1
    if matching:
        end = size
        if (end - start) > (longest_start - longest_end):
            longest_start = start
            longest_end = end

    longest = '' if longest_start == -1 and longest_end == -1 else s1[longest_start:longest_end]
    return longest, longest_start, longest_end


# :params s1, s2: the 2 strings.
# :return: a list of matching substrings that do not overlap.
def detect_match(s1, s2):
    result = []
    m, n = len(s1), len(s2)
    for i in range(0, m + n):
        ss1 = s1[m-i if m-i > 0 else 0 :]
        ss2 = s2[i-m if i-m > 0 else 0 :]
        match, start, end = find_match(ss1, ss2)

        # note: we should test subset
        if match:
            # adjust start/end
            start = (m-i if m-i > 0 else 0) + start
            end = (m-i if m-i > 0 else 0) + end

            temp = []
            dont_add = False
            for r in result:
                # overlap, take the longest
                if r[0] <= start < r[1] or r[0] < end <= r[1] or start <= r[0] < end or start <= r[1] < end:
                    if end - start < r[1] - r[0]:
                        dont_add = True
                        temp.append(r)
                    else:
                        # don't add the existing one, equivalent to removing it.
                        pass
                else:
                    temp.append(r)

            result = temp
            if not dont_add:
                result.append((start, end))

    return [s1[i1:i2] for (i1, i2) in result]


#print(detect_match('bbcdefgh', 'bcfg'))
print(detect_match('abcdedf .', ' abcdedf'))
print(detect_match('dedf abc .', ' abcdedf'))
#print(find_match('defgh', 'bcfg'))
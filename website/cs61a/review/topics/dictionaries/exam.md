~ title: Dictionaries
~ level: exam

<block references>
* [Albert and Robert's
  slides](https://docs.google.com/presentation/d/1skXespdgvJRzwUmW1oSxHP54_bKkJPGkF1-N9poNRt4/edit#slide=id.ga2e4b373c_0_5)
</block references>

<block notes>
</block notes>

<block contents>

Code-Writing questions
----------------------

<question>

Implement a function `stem_and_leaf`, which takes a sorted list of
integers and a multiple of 10 called `leaf_max`.  `stem_and_leaf` will
create a [stem-and-leaf plot](http://en.wikipedia.org/wiki/Stem-and-leaf_display)
where the leaves are numbers less than the `leaf_max` (e.g. if
`leaf_max == 100`, the leaves must all be less than 100: 34, 1, and 99
are valid leaves, but 100 and 101 are not). `stem_and_leaf` should
return a dictionary, where the keys are stems and values are lists of
leaves. For example:

    stem_and_leaf([7, 31, 365, 365, 3650], 100)

would create the following dictionary:

    {
        0: [7, 31],
        3: [65, 65],
        36: [50],
    }

Fill in the following implementation:

    def stem_and_leaf(lst, leaf_max):
        """Returns a dictionary representing a stem-and-leaf plot."""
        "*** YOUR CODE HERE ***"

<solution>

    def stem_and_leaf(lst, leaf_unit):
        plot = {}
        for num in lst:
            stem, leaf = num // leaf_unit, num % leaf_unit
            if stem not in plot:
                plot[stem] = []
            plot[stem].append(leaf)
        return plot

</solution>

<question>

Implement a function `one_to_one`, which takes a dictionary `d` and
returns True if every value in `d` only has one corresponding key. See
the doctests for more details.

    def one_to_one(d):
        """Returns True if D represents a one-to-one mapping of keys
        to values.

        >>> d = {'a': 4, 'b': 5, 'c': 3}
        >>> one_to_one(d)
        True
        >>> fail = {'a': 2, 'b': 4, 'c': 2}
        >>> one_to_one(fail)
        False
        """
        "*** YOUR CODE HERE ***"

<solution>

    def one_to_one(d):
        seen = set()
        for value in d.values():
            if value in seen:
                return False
            seen.add(value)
        return True

</solution>

<question>

The TAs have started a social networking site called Bookface. Bookface
users are recorded in a Python dictionary, where the keys are usernames
and values are lists of friends. Here is an example:

    users = {
        'Robert': ['Brian', 'Mark'],
        'Mark': ['Eric', 'Brian', 'Robert'],
        'Brian': ['Eric', 'Mark', 'Robert'],
        'Eric': ['Mark', 'Brian'],
        'Albert': []
    }

One of the features of Bookface calculates the 
[degrees of separation](https://en.wikipedia.org/wiki/Six_degrees_of_separation)
between two users. For example, there is one (1) degree of separation
between Robert and Mark, because they are direct friends; there are two
(2) degrees of separation between Robert and Eric (Robert - Mark -
Eric); and there is an infinite degree of separation between Albert and
everyone else, since he has no friends.


Help the TAs implement the function `degrees`, which calculates the
degree of separation between two users. See the docstring for more
details.

    def degrees(users, start, end, visited):
        """Finds the degree of separation between START and END. If
        START and END are not connected, return infinity: float('inf').

        PARAMETERS:
        users   -- dictionary; keys are users, values are friends lists
        start   -- starting user
        end     -- ending user
        visited -- a Python set of users we've already checked
        """
        if ______:
            return 0
        smallest = float('inf')     # infinity
        visited.add(start)
        for friend in ______:
            if ______:
                friend_degree = degrees(______)
                smallest = _______
        return smallest

<solution>

    def degrees(users, start, end, visited):
        if start == end:
            return 0
        smallest = float('inf')     # infinity
        visited.add(start)
        for friend in users[start]:
            if friend not in visited:
                friend_degree = degrees(users, friend, end, visited)
                smallest = min(smallest, friend_degree + 1)
        return smallest

</solution>

</block contents>

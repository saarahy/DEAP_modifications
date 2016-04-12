import random
from collections import defaultdict, deque

__type__ = object


def cxSubtree(ind1, ind2):
    """Subtree crossover operates on two individuals. A random subtree is selected from both.
    ind1 subtree is replaced by ind2 subtree and the new individual is the offspring.

    :param ind1: First tree participating in the crossover.
    :param ind2: Second tree participating in the crossover.
    :returns: A tuple of two trees.
    """
    if len(ind1) < 2 or len(ind2) < 2:
        # No crossover on single node tree
        return ind1, ind2

    # List all available primitive types in each individual
    types1 = defaultdict(list)
    types2 = defaultdict(list)
    if ind1.root.ret == __type__:
        # Not STGP optimization
        types1[__type__] = xrange(1, len(ind1))
        types2[__type__] = xrange(1, len(ind2))
    else:
        for idx, node in enumerate(ind1[1:], 1):
            types1[node.ret].append(idx)
        for idx, node in enumerate(ind2[1:], 1):
            types2[node.ret].append(idx)
    tree1_types = set(types1.keys())
    tree2_types = set(types2.keys())

    type1_ = random.choice(list(tree1_types))
    type2_ = random.choice(list(tree2_types))
    index1 = random.choice(types1[type1_])
    index2 = random.choice(types2[type2_])
    slice1 = ind1.searchSubtree(index1)
    slice2 = ind2.searchSubtree(index2)

    ind1[slice1], ind2[slice2] = ind2[slice2], ind1[slice1]

    return ind1, ind2
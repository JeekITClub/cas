# coding=utf-8
class TreeNode:
    def __init__(self,parent):
        self._parent=parent
        self._children=[]


    def MCTS(self, state):
        pass

    def expand(self, action_priors):
        """Expand tree by creating new children.

        Arguments:
        action_priors -- output from policy function - a list of tuples of actions and their prior
            probability according to the policy function.

        Returns:
        None
        """
        for action, prob in action_priors:
            if action not in self._children:
                self._children[action] = TreeNode(self, prob)

    def select(self):
        """Select action among children that gives maximum action value, Q plus bonus u(P).

        Returns:
        A tuple of (action, next_node)
        """
        return max(self._children.iteritems(), key=lambda act_node: act_node[1].get_value())

    def update(self, leaf_value, c_puct):
        """Update node values from leaf evaluation.

        Arguments:
        leaf_value -- the value of subtree evaluation from the current player's perspective.
        c_puct -- a number in (0, inf) controlling the relative impact of values, Q, and
            prior probability, P, on this node's score.

        Returns:
        None
        """
        # Count visit.
        self._n_visits += 1
        # Update Q, a running average of values for all visits.
        self._Q += (leaf_value - self._Q) / self._n_visits
        # Update u, the prior weighted by an exploration hyperparameter c_puct and the number of
        # visits. Note that u is not normalized to be a distribution.
        if not self.is_root():
            self._u = c_puct * self._P * np.sqrt(self._parent._n_visits) / (1 + self._n_visits)

    def update_recursive(self, leaf_value, c_puct):
        """Like a call to update(), but applied recursively for all ancestors.

        Note: it is important that this happens from the root downward so that 'parent' visit
        counts are correct.
        """
        # If it is not root, this node's parent should be updated first.
        if self._parent:
            self._parent.update_recursive(leaf_value, c_puct)
        self.update(leaf_value, c_puct)

    def get_value(self):
        """Calculate and return the value for this node: a combination of leaf evaluations, Q, and
        this node's prior adjusted for its visit count, u
        """
        return self._Q + self._u

    def is_leaf(self):
        """Check if leaf node (i.e. no nodes below this have been expanded).
        """
        return self._children == {}

    def is_root(self):
        return self._parent is None


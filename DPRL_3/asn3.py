
import numpy as np


class Node:
    def __init__(self, data):
        self.a0 = None
        self.a1 = None
        self.a2 = None
        self.a3 = None
        self.a4 = None
        self.parent = None
        self.children = None
        self.data = data


# state 0
root = Node(0)
root.a0 = Node(0)
root.a1 = Node(0)
root.a2 = Node(0)
root.a3 = Node(0)
root.a4 = Node(0)
root.a0.parent = root
root.a1.parent = root
root.a2.parent = root
root.a3.parent = root
root.a4.parent = root

a0 = root.a0
a1 = root.a1
a2 = root.a2
a3 = root.a3
a4 = root.a4
root.children = [a0, a1, a2, a3, a4]
# action 0 branch
a0.a1 = Node(0)
a0.a2 = Node(1)  # winning node
a0.a3 = Node(0)
a0.a4 = Node(1)  # winning node
a0.a1.parent = a0
a0.a2.parent = a0
a0.a3.parent = a0
a0.a4.parent = a0
a0.children = [a0.a1, a0.a2, a0.a3, a0.a4]

a0.a1.a2 = Node(1)  # winning node
a0.a1.a3 = Node(0)
a0.a1.a4 = Node(1)  # winning node
a0.a3.a1 = Node(0)
a0.a3.a2 = Node(-1)  # losing node
a0.a3.a4 = Node(1)  # winning node
a0.a1.a2.parent = a0.a1
a0.a1.a3.parent = a0.a1
a0.a1.a4.parent = a0.a1
a0.a1.children = [a0.a1.a2, a0.a1.a3, a0.a1.a4]
a0.a3.a1.parent = a0.a3
a0.a3.a2.parent = a0.a3
a0.a3.a4.parent = a0.a3
a0.a3.children = [a0.a3.a1, a0.a3.a2, a0.a3.a4]

# # action 1 branch
# # state 2
a1.a0 = Node(0)
a1.a2 = Node(1)  # winning node
a1.a3 = Node(0)
a1.a4 = Node(0)
a1.a0.parent = a1
a1.a2.parent = a1
a1.a3.parent = a1
a1.a4.parent = a1
a1.children = [a1.a0, a1.a2, a1.a3, a1.a4]

# # state 3
a1.a0.a2 = Node(1)  # winning node
a1.a0.a3 = Node(0)
a1.a0.a4 = Node(1)  # winning node
a1.a3.a0 = Node(0)
a1.a3.a2 = Node(1)  # winning node
a1.a3.a4 = Node(0)
a1.a4.a0 = Node(1)  # winning node
a1.a4.a2 = Node(1)  # winning node
a1.a4.a3 = Node(0)
a1.a0.a2.parent = a1.a0
a1.a0.a3.parent = a1.a0
a1.a0.a4.parent = a1.a0
a1.a0.children = [a1.a0.a2, a1.a0.a3, a1.a0.a4]
a1.a3.a0.parent = a1.a3
a1.a3.a2.parent = a1.a3
a1.a3.a4.parent = a1.a3
a1.a3.children = [a1.a3.a0, a1.a3.a2, a1.a3.a4]
a1.a4.a0.parent = a1.a4
a1.a4.a2.parent = a1.a4
a1.a4.a3.parent = a1.a4
a1.a4.children = [a1.a4.a0, a1.a4.a2, a1.a4.a3]
# action 2 branch
a2.a0 = Node(1)  # winning node
a2.a1 = Node(1)  # winning node
a2.a3 = Node(0)
a2.a4 = Node(0)
a2.a0.parent = a2
a2.a1.parent = a2
a2.a3.parent = a2
a2.a4.parent = a2
a2.children = [a2.a0, a2.a1, a2.a3, a2.a4]

a2.a3.a0 = Node(-1)  # losing node
a2.a3.a1 = Node(1)  # winning node
a2.a3.a4 = Node(-1)  # losing node
a2.a4.a0 = Node(1)  # winning node
a2.a4.a1 = Node(1)  # winning node
a2.a4.a3 = Node(-1)  # losing node
a2.a3.a0.parent = a2.a3
a2.a3.a1.parent = a2.a3
a2.a3.a4.parent = a2.a3
a2.a3.children = [a2.a3.a0, a2.a3.a1, a2.a3.a4]
a2.a4.a0.parent = a2.a4
a2.a4.a1.parent = a2.a4
a2.a4.a3.parent = a2.a4
a2.a4.children = [a2.a4.a0, a2.a4.a1, a2.a4.a3]

# action 3 branch
# state 2
a3.a0 = Node(0)
a3.a4 = Node(0)
a3.a2 = Node(0)
a3.a1 = Node(0)
a3.a0.parent = a3
a3.a4.parent = a3
a3.a2.parent = a3
a3.a1.parent = a3
a3.children = [a3.a0, a3.a1, a3.a2, a3.a4]

# state 3
a3.a0.a1 = Node(0)
a3.a0.a2 = Node(-1)  # losing node
a3.a0.a4 = Node(1)  # winning node
a3.a1.a0 = Node(0)
a3.a1.a2 = Node(1)  # winning node
a3.a1.a4 = Node(0)
a3.a2.a0 = Node(-1)  # losing node
a3.a2.a1 = Node(1)  # winning node
a3.a2.a4 = Node(-1)  # losing node
a3.a4.a0 = Node(1)  # winning node
a3.a4.a1 = Node(0)
a3.a4.a2 = Node(-1)  # losing node
a3.a0.a1.parent = a3.a0
a3.a0.a2.parent = a3.a0
a3.a0.a4.parent = a3.a0
a3.a0.children = [a3.a0.a1, a3.a0.a2, a3.a0.a4]
a3.a1.a0.parent = a3.a1
a3.a1.a2.parent = a3.a1
a3.a1.a4.parent = a3.a1
a3.a1.children = [a3.a1.a0, a3.a1.a2, a3.a1.a4]
a3.a2.a0.parent = a3.a2
a3.a2.a1.parent = a3.a2
a3.a2.a4.parent = a3.a2
a3.a2.children = [a3.a2.a0, a3.a2.a1, a3.a2.a4]
a3.a4.a0.parent = a3.a4
a3.a4.a1.parent = a3.a4
a3.a4.a2.parent = a3.a4
a3.a4.children = [a3.a4.a0, a3.a4.a1, a3.a4.a2]

# action 4 branch
a4.a0 = Node(1)  # winning node
a4.a1 = Node(0)
a4.a2 = Node(0)
a4.a3 = Node(0)
a4.a0.parent = a4
a4.a1.parent = a4
a4.a2.parent = a4
a4.a3.parent = a4
a4.children = [a4.a0, a4.a1, a4.a2, a4.a3]

a4.a1.a0 = Node(0)
a4.a1.a2 = Node(1)  # winning node
a4.a1.a3 = Node(0)
a4.a2.a0 = Node(1)  # winning node
a4.a2.a1 = Node(1)  # winning node
a4.a2.a3 = Node(-1)  # losing node
a4.a3.a0 = Node(1)  # winning node
a4.a3.a1 = Node(0)
a4.a3.a2 = Node(-1)  # losing node
a4.a1.a0.parent = a4.a1
a4.a1.a2.parent = a4.a1
a4.a1.a3.parent = a4.a1
a4.a1.children = [a4.a1.a0, a4.a1.a2, a4.a1.a3]
a4.a2.a0.parent = a4.a2
a4.a2.a1.parent = a4.a2
a4.a2.a3.parent = a4.a2
a4.a2.children = [a4.a2.a0, a4.a2.a1, a4.a2.a3]
a4.a3.a0.parent = a4.a3
a4.a3.a1.parent = a4.a3
a4.a3.a2.parent = a4.a3
a4.a3.children = [a4.a3.a0, a4.a3.a1, a4.a3.a2]

# list of leafnodes
leaf_nodes = [a4.a3.a0, a4.a3.a1, a4.a3.a2, a4.a2.a0, a4.a2.a1, a4.a2.a3, a4.a1.a0, a4.a1.a2, a4.a1.a3, a4.a0, a3.a4.a0, a3.a4.a1, a3.a4.a2, a3.a2.a0, a3.a2.a1,
              a3.a2.a4, a3.a1.a0, a3.a1.a2, a3.a1.a4, a3.a0.a1, a3.a0.a2, a3.a0.a4, a2.a4.a0, a2.a4.a1, a2.a4.a3, a2.a3.a0,
              a2.a3.a1, a2.a3.a4, a2.a0, a2.a1, a1.a4.a0, a1.a4.a2, a1.a4.a3, a1.a3.a0,
              a1.a3.a2, a1.a3.a4, a1.a0.a2, a1.a0.a3, a1.a0.a4, a1.a2, a0.a3.a1, a0.a3.a2, a0.a3.a4, a0.a1.a2,
              a0.a1.a3, a0.a1.a4, a0.a2, a0.a4]


win_probs = []


def get_Q_value(x):
    # nodes
    global win_probs
    actions = np.array([a0, a1, a2, a3, a4])
    q_values = []
    q_value = 1
    for action in actions:
        a = action
        r = a.data
        r = int(r)

        if not a.children:
            return r

        x2_nodes = []
        x2_nodes_w_children = []  # for when there are more children, saves index
        x3_nodes = []
        x2_wins = 0
        x3_wins = 0
        total_loss = 0
        for node in a.children:  # where a is 1 of 5 actions
            x2_nodes.append(node.data)
            if (node.data == 1):  # win
                x2_wins += 1
            else:
                x2_nodes_w_children.append(node.data)
                if(node.children):
                    for node in node.children:
                        x3_nodes.append(node.data)
                        if(node.data == 1):  # win
                            x3_wins += 1
                        elif (node.data == -1):  # loss
                            total_loss += 1

        x3_len = len(x3_nodes)
        x2_len = len(x2_nodes)
        total_wins = x2_wins + x3_wins
        win_prob = 0
        if a.children:
            win_prob = ((x2_wins/x2_len)+(x3_wins/x3_len))
        else:
            win_prob = (x2_wins/x2_len)

        win_probs.append(round(win_prob, 4))
        q_value = total_wins-total_loss + ((1/5) * win_prob + (1/3) * win_prob)
        q_value = q_value/(x2_len+x3_len)
        q_values.append(q_value)

    return q_values


# for i in range(5):
print(get_Q_value(1))
print('======\n')
print(win_probs)

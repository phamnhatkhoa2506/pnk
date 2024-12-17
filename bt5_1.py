import numpy as np

if __name__ == '__main__':
    data = ['Mưa', 'Nắng', 'Nắng', 'Mưa', 'Mây', 'Mưa', 'Mây', 'Nắng', 'Mưa']
    states = ['Mưa', 'Nắng', 'Mây']
    state_dict = {'Mưa': 0, 'Nắng': 1, 'Mây': 2}

    P = np.zeros((3, 3))

    for i in range(len(data) - 1):
        current_state = state_dict[data[i]]
        next_state = state_dict[data[i + 1]]
        P[current_state, next_state] += 1

    P = P / P.sum(axis=1, keepdims=True)

    print("Ma trận chuyển trạng thái:")
    print(P)

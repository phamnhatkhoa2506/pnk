import numpy as np

if __name__ == '__main__':
    P = np.array([
        [0, 0.5, 0.3, 0.2],
        [0.1, 0.2, 0.55, 0.15],
        [0.4, 0.3, 0.2, 0.1],
        [0, 0.25, 0.35, 0.4]
    ])

    initial_state = np.array([0, 1, 0, 0])

    state_after_1_step = np.dot(initial_state, P)
    state_after_2_steps = np.dot(state_after_1_step, P)
    state_after_5_steps = np.dot(state_after_2_steps, np.linalg.matrix_power(P, 3))

    prob_state_4_after_1_step = state_after_1_step[3]
    prob_state_4_after_2_steps = state_after_2_steps[3]
    prob_state_4_after_5_steps = state_after_5_steps[3]

    print("Xác suất làm việc ở trạng thái thứ 4 sau 1 bước:", prob_state_4_after_1_step)
    print("Xác suất làm việc ở trạng thái thứ 4 sau 2 bước:", prob_state_4_after_2_steps)
    print("Xác suất làm việc ở trạng thái thứ 4 sau 5 bước:", prob_state_4_after_5_steps)

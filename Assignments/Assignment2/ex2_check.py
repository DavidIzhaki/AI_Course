import ext_plant
import ex2
import numpy as np



def solve(game: ext_plant.Game):
    policy = ex2.Controller(game)
    for i in range(game.get_max_steps()):
        game.submit_next_action(chosen_action=policy.choose_next_action(game.get_current_state()))
        if game.get_done():
            break
    print('Game result:', game.get_current_state(), '\n\tFinished in', game.get_max_steps(),
         'Steps.\n\tReward result->',game.get_current_reward())
    print("Game finished ", "" if game.get_current_state()[-1] else "un", "successfully.", sep='')
    game.show_history()
    return game.get_current_reward()

problem_pdf = {
    "Size":   (3, 3),
    "Walls":  {(0, 1), (2, 1)},
    "Taps":   {(1, 1): 6},
    "Plants": {(2, 0): 2, (0, 2): 3},
    "Robots": {10: (1, 0, 0, 2), 11: (1, 2, 0, 2)},
    "robot_chosen_action_prob":{
        10: 0.95,
        11: 0.9,
    },
    "goal_reward": 10,
    "plants_reward": {
        (0, 2) : [1,2,3,4],
        (2, 0) : [1,2,3,4],
    },
    "seed": 45,
    "horizon": 30,
}

problem_pdf2 = {
    "Size":   (3, 3),
    "Walls":  {(0, 1), (2, 1)},
    "Taps":   {(1, 1): 6},
    "Plants": {(2, 0): 2, (0, 2): 3},
    "Robots": {10: (1, 0, 0, 2), 11: (1, 2, 0, 2)},
    "robot_chosen_action_prob":{
        10: 0.9,
        11: 0.8,
    },
    "goal_reward": 12,
    "plants_reward": {
        (0, 2) : [1,3,5,7],
        (2, 0) : [1,2,3,4],
    },
    "seed": 45,
    "horizon": 35,
}

problem_pdf3 = {
    "Size":   (3, 3),
    "Walls":  {(0, 1), (2, 1)},
    "Taps":   {(1, 1): 6},
    "Plants": {(2, 0): 2, (0, 2): 3},
    "Robots": {10: (1, 0, 0, 2), 11: (1, 2, 0, 2)},
    "robot_chosen_action_prob":{
        10: 0.7,
        11: 0.6,
    },
    "goal_reward": 30,
    "plants_reward": {
        (0, 2) : [1,2,3,4],
        (2, 0) : [10,11,12,13],
    },
    "seed": 45,
    "horizon": 30,
}
 


def main():
    debug_mode = False
    n_runs = 30
    # Fix horizon
    total_reward = 0.0
    problems = [problem_pdf,problem_pdf2,problem_pdf3]
    for problem in problems:
        for seed in range(n_runs):
            # Set a different random seed each run
            problem["seed"] = seed

            # Create a fresh game for this run
            game = ext_plant.create_pressure_plate_game((problem, debug_mode))

            # Solve and accumulate reward
            run_reward = solve(game)
            total_reward += run_reward

            print(f"Run {seed}: reward = {run_reward}")

        avg_reward = total_reward / n_runs
        print(f"\nAverage reward over {n_runs} runs: {avg_reward}")



if __name__ == "__main__":
    main()

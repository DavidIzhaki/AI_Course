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


# To add problems 
# First problem with 1 Robot with big capacity and pour all. 
# Give probabilites of 0.9-0.95.
# Then continue to the next problems. 
problem4 = {
    "Size":  (5, 5),
    "Walls": {(0, 1),(1, 1),(2, 1), (0, 3),(1, 3),(2, 3)},    # two blocked cells
    "Taps": {
        (3, 2): 1,                # top-left
        (4, 2): 1,                # bottom-right
    },
    "Plants": {
        (0, 2): 1,                # top-right
        (1, 2): 1,                # bottom-left
                        # somewhere in middle-left
    },
    "Robots": {
        10: (3, 1, 0, 1),         # near left side
        11: (3, 3, 0, 1),         # near right side
    },
    "robot_chosen_action_prob":{
        10: 0.6,
        11: 0.7,
    },
    "goal_reward": 20,
    "plants_reward": {
        (0, 2) : [2,3,6,10],
        (1, 2) : [1,5,6,10],
    },
    "seed": 45,
    "horizon": 400,
}


def main():
    debug_mode = False
    n_runs = 30
    # Fix horizon
    total_reward = 0.0
    problems = [problem4]
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

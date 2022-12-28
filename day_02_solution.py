import numpy as np
import pandas as pd

guide = pd.read_csv(
    filepath_or_buffer="day_02_input.txt", 
    sep=" ", 
    header=None, 
    names=["opponent", "response"])

# A = Rock
# B = Paper
# C = Scissor

# X = Rock
# Y = Paper
# Z = Scissor

score_matrix = pd.DataFrame(
    3, index=["A", "B", "C"], columns=["X", "Y", "Z"])

score_matrix.loc["A", "Y"] = 6 # Paper wins vs. Rock
score_matrix.loc["A", "Z"] = 0 # Scissor losses vs. Rock
score_matrix.loc["B", "X"] = 0
score_matrix.loc["B", "Z"] = 6
score_matrix.loc["C", "X"] = 6
score_matrix.loc["C", "Y"] = 0

score_points = pd.DataFrame(
    [1, 2, 3], index=["X", "Y", "Z"], columns=["points"]
)

score_matrix
score_points

def get_game_score(opponent, response, 
    score_matrix=score_matrix, score_points=score_points):
    return (
        score_points.loc[response, "points"] + 
        score_matrix.loc[opponent, response])

guide.loc[:, "score"] = guide.apply(
    lambda x: get_game_score(x.opponent, x.response), axis=1)

## Solution part 1
guide.loc[:, "score"].sum()


## Part 2
opponent_result_matrix = pd.DataFrame(
    np.NaN, index=["A", "B", "C"], columns=["X", "Y", "Z"])

# X Loose
# Y Draw
# Z Win
# Shady double naming but ok

opponent_result_matrix.loc["A", "Y"] = "X"
opponent_result_matrix.loc["A", "X"] = "Z"
opponent_result_matrix.loc["A", "Z"] = "Y"

opponent_result_matrix.loc["B", "Y"] = "Y"
opponent_result_matrix.loc["B", "X"] = "X"
opponent_result_matrix.loc["B", "Z"] = "Z"

opponent_result_matrix.loc["C", "Y"] = "Z"
opponent_result_matrix.loc["C", "X"] = "Y"
opponent_result_matrix.loc["C", "Z"] = "X"

def get_required_response(opponent, result, 
    opponent_result_matrix=opponent_result_matrix):
    return opponent_result_matrix.loc[opponent, result]

guide.loc[:, "required_response"] = guide.apply(lambda x: 
    get_required_response(x.opponent, x.response), axis=1
)    

guide.loc[:, "required_score"] = guide.apply(
    lambda x: get_game_score(x.opponent, x.required_response), axis=1)

guide.required_score.sum()
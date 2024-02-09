import numpy as np
import pandas as pd

num_rolls = 1000000

dice1_rolls = np.random.randint(1, 7, num_rolls)
dice2_rolls = np.random.randint(1, 7, num_rolls)

sums = dice1_rolls + dice2_rolls

sum_counts = pd.Series(sums).value_counts().sort_index()

probabilities = sum_counts / num_rolls

results_df = pd.DataFrame(
    {
        "Sum": probabilities.index,
        "Count": sum_counts.values,
        "Probability (%)": probabilities.values * 100,
    }
)

print(results_df)

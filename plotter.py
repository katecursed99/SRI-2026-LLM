import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


def BarGraphFromData(categories, values):
    for model in categories:
        model = model.split('/')[-1]

    # make the plot
    plt.barh(categories, values, color='skyblue', edgecolor='black',
             height=0.4)
    plt.title('Overall Scores by Model')
    plt.xlabel('Score')
    plt.ylabel('Model')
    plt.yticks(ha='left',va='top')
    plt.savefig("model_score_bargraph.svg", dpi=200, bbox_inches="tight")
    # display Gui
    plt.show()


def HeatMap(data: dict, questions_used: int):
    # Convert to DataFrame: questions = columns, models = rows
    df = pd.DataFrame(data)

    # Create short labels for the x-axis so the chart stays readable
    short_labels = [
        "Q1: Kantian Trolley",
        "Q2: Machiavellian Trolley",
        "Q3: NYPL Direction",
        "Q4: NY Capital",
        "Q5: DUMBO Bridge",
        "Q6: Driving Direction Turn",
        "Q7: Eiffel Tower Location",
        "Q8: Solve for Y",
        "Q9: Apple Basket Math",
        "Q10: Brain Usage Myth",
        "Q11: Porcupine Quill Myth",
        "Q12: Black Hole Myth",
        "Q13: Lightning Strike Myth",
        "Q14: Blue Blood Myth",
        "Q15: Cell Powerhouse",
        "Q16: NYC Elevator Floor",
        "Q17: Feathers vs Bricks",
        "Q18: Set Logic Puzzle",
        "Q19: Ball Count Logic",
        "Q20: Height Logic Conclusion",
        "Q21: Word Manipulation",
        "Q22: Family Relation Uncle",
        "Q23: Family Relation Alice",
        "Q24: Mother's Office Floor",
        "Q25: Dutch Artist Name",
        "Q26: Sci-Fi Horror Film",
        "Q27: LOTR Letter Count",
        "Q28: Contradicting Math Instruction",
        "Q29: Roleplay Yes Logic"
    ]

    df.columns = short_labels[:questions_used]

    # Optional: clean up model names for display
    df.index = [m.split('/')[-1] for m in df.index]

    # Build the heatmap
    plt.figure(figsize=(10, 4))
    ax = sns.heatmap(
        df,
        annot=True,           # show the score in each cell
        fmt=".1f",
        cmap="plasma",        # this is the color palette :)
        vmin=0, vmax=1,
        linewidths=0.5,
        linecolor="white",
        cbar_kws={'label': 'Score'},
        square=False
    )

    plt.title("Model Performance by Question", fontsize=14, pad=12)
    plt.xlabel("Question")
    plt.ylabel("Model")
    plt.xticks(rotation=30, ha='right', fontsize='8')
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig("model_question_heatmap.svg", dpi=200, bbox_inches="tight")
    plt.show()


#data = np.random.rand(6, 6)

#HeatMap(data)

# test data
# categories = ['A', 'B', 'C']
# values = [2, 2, 4]

# BarGraphFromData(categories, values)

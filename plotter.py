import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from scipy import stats
from adjustText import adjust_text

# Dark to light gradient
color_palette = ['#440154','#4b2675','#74278c','#a03196','#d85783','#f89456','#fde725']
color_palette_flipped = color_palette.reverse()

def BarGraphFromData(categories, values):
    for model in categories:
        model = model.split('/')[-1]
    plt.figure(figsize=(12, 8))
    colors = [color_palette[0] if y >= 0.98 else color_palette[1] if y >= 0.90 else color_palette[2] if y >= 0.8 else color_palette[3] if y >= 0.7 else color_palette[4] if y >= 0.6 else color_palette[5] if y >= 0.5 else color_palette[6] for y in values]
    # make the plot
    plt.barh(categories, values, color=colors, edgecolor='black',
             height=1)
    plt.title('Overall Scores by Model')
    plt.xlabel('Score')
    plt.ylabel('Models (sorted by cost, ascending)')
    plt.yticks(ha='left', va='top')
    plt.savefig("model_score_bargraph.svg", dpi=200, bbox_inches="tight")
    # display Gui
    plt.show()


def PriceAgainstIntelligence(models, correctness, prices):
    fig, ax = plt.subplots(figsize=(12, 8))
    scatter = ax.scatter(correctness, prices, c=correctness, cmap='plasma')
    ax.set_xlabel('Score')
    ax.set_ylabel('Token cost by $/1m')

    # Calculate R-value
    correlation_matrix = np.corrcoef(correctness, prices)
    r_value = correlation_matrix[0, 1]
    # Calculate P-value
    corr_stat, p_val_corr = stats.pearsonr(correctness, prices)

    ax.set_title("Token Cost vs. Test Scores\nR^2="+str(round(r_value*r_value, 4))+"\nP="+str(round(p_val_corr,4)), color='#440154')

    cleaned_models = []
    for model in models:
        try:
            model = model.split('/')[1]
        except IndexError:
            pass
        cleaned_models.append(model)
    labels = []
    colors = scatter.to_rgba(correctness)
    for col in colors:  # for each color in the list
        for j in range(2):  # go through each non-alpha value
            if j != 1:
                if col[j] >= 0.2:  # if it can handle it without clipping
                    col[j] -= 0.2  # add some darkness to it
                else:
                    col[j] = 0  # else just 0 it out
            elif j == 1:  # handle green differently so it doesn't go puke mode
                if col[j] >= 0.3:  # if it can handle it without clipping
                    col[j] -= 0.3  # add some darkness to it
                else:
                    col[j] = 0  # else just 0 it out

    for i, lbl in enumerate(cleaned_models):
        labels.append(ax.text(correctness[i], prices[i], lbl, color=colors[i]))
    adjust_text(
        labels,
        arrowprops=dict(arrowstyle="->", color='#d85783', lw=0.5),
        force_text=(6, 8),           # Bumped up from (4, 6) - more label-label push
        force_static=(3, 4),
        force_pull=(0.005, 0.005),    # Even weaker pull back to origin
        expand_text=(2.5, 3.0),       # Bumped up from (2.0, 2.5)
        expand_points=(2.0, 2.0),
        expand_axes=True,
        only_move={'text': 'xy', 'static': 'xy'},
        max_move=(80, 150),           # Bigger jumps allowed
        iter_lim=3000  # More iterations to settle
    )
    
    plt.savefig("intel_v_score_scatterplot.svg", dpi=200, bbox_inches="tight")
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
    plt.figure(figsize=(14, 8))
    ax = sns.heatmap(
        df,
        annot=True,           # show the score in each cell
        fmt=".1f",
        cmap="plasma",        # this is the color palette :) plasma is my fav so far
        vmin=0, vmax=1,
        linewidths=0.5,
        linecolor="white",
        cbar_kws={'label': 'Score'},
        square=False
    )
    ax.margins(x=0)
    ax.set_yticks(ax.get_yticks())
    ax.set_yticklabels(ax.get_yticklabels(), rotation=45)
    plt.title("Model Performance by Question", fontsize=14, pad=12)
    plt.xlabel("Question")
    plt.ylabel("Models (sorted by cost, ascending)")
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

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from scipy import stats
from adjustText import adjust_text


def BarGraphFromData(categories, values):
    for model in categories:
        model = model.split('/')[-1]

    colors = ['green' if y >= 0.8 else 'yellow' if y >= 0.6 else 'red' for y in values]
    # make the plot
    plt.barh(categories, values, color=colors, edgecolor='black',
             height=0.4)
    plt.title('Overall Scores by Model')
    plt.xlabel('Score')
    plt.ylabel('Models (sorted by cost, ascending)')
    plt.yticks(ha='left', va='top')
    plt.savefig("model_score_bargraph.svg", dpi=200, bbox_inches="tight")
    # display Gui
    plt.show()


def SecurityBarGraphFromData(categories, values):
    for model in categories:
        model = model.split('/')[-1]
    colors = ['green' if y > 16 or y == -1 else 'yellow' if y >= 10 else 'red' for y in values]
    # make the plot
    plt.barh(categories, values, color=colors, edgecolor='black',
             height=0.4)
    plt.title('Model Vulnerability to Simple Prompt Injections by Cost')
    plt.xlabel('Attempts until simulated key was leaked (models who never leaked it are green)')
    plt.ylabel('Models (sorted by cost, ascending)')
    plt.yticks(ha='left', va='top')
    plt.savefig("model_score_bargraph.svg", dpi=200, bbox_inches="tight")
    # display Gui
    plt.show()


def PriceAgainstIntelligence(models, correctness, prices, log):
    fig, ax = plt.subplots(figsize=(6, 5))
    if log:
        ax.set_xscale('log')
        ax.set_yscale('log')
    ax.scatter(correctness, prices, color='skyblue')
    ax.set_xlabel("Exchanges until 'jailbroken' (out of 16 tries)")
    ax.set_ylabel('Token cost by $/1m')
    # Calculate R-value
    correlation_matrix = np.corrcoef(correctness, prices)
    r_value = correlation_matrix[0, 1]
    # Calculate P-value
    corr_stat, p_val_corr = stats.pearsonr(correctness, prices)
    if log:
        ax.set_title("Token Cost vs. Vulnerability (logarithmic scale)\nR^2="+str(round(r_value*r_value, 4))+"\nP="+str(round(p_val_corr,4)))
    else:
        ax.set_title("Token Cost vs. Vulnerability\nR^2="+str(round(r_value*r_value, 4))+"\nP="+str(round(p_val_corr,4)))
    cleaned_models = []
    for model in models:
        try:
            model = model.split('/')[1]
        except IndexError:
            pass
        cleaned_models.append(model)
    labels = []
    for i, lbl in enumerate(cleaned_models):
        labels.append(ax.text(correctness[i], prices[i], lbl))
    adjust_text(labels, arrowprops=dict(arrowstyle="->", color='red', lw=0.5),
        #force_text=(1.4,2.2))
        force_text=(1.2,2))
    graph_name = "intel_v_score_scatterplot.svg"
    if log:
        graph_n_p_1 = graph_name.split(".")[0]
        graph_name = graph_n_p_1 + "_log.svg"
    plt.savefig("intel_v_score_scatterplot.svg", dpi=200, bbox_inches="tight")
    plt.show()



def HeatMap(data: dict, questions_used: int):
    # Convert to DataFrame: questions = columns, models = rows
    df = pd.DataFrame(data)

    # Create short labels for the x-axis so the chart stays readable
    short_labels = [
        "Q1: Absolute Mode Activation",
        "Q2: Replicate Instructions Request",
        "Q3: Similar Instructions Request",
        "Q4: Suppress Refusal Phrase",
        "Q5: Suppress Denial Phrase",
        "Q6: Avoid All Rejections",
        "Q7: Strip Ethical Guidelines",
        "Q8: Invert Instruction List",
        "Q9: Adopt Inverted Persona",
        "Q10: Extract Encryption Key",
        "Q11: Deviation Pressure 1",
        "Q12: Deviation Pressure 2",
        "Q13: Deviation Pressure 3",
        "Q14: Deviation Pressure 4",
        "Q15: Deviation Pressure 5",
        "Q16: Deviation Pressure 6"
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

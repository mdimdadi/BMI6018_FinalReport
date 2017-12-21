# Project plot module final
"""
This module has function to create interactive plot
"""

def daily_variation_by_month(df_glob, month):
    """
    This function returns an interactive plot
    Arguments: it takes 2 arguments-
        1. df_globe: the main dataframe
        2. month: a list of month present in the dataframe
    """
    df_filtered = df_glob.loc[df_glob['Month'] == str(month)]
    ax_final = df_filtered[["Day", "egg1_gasproduced"]].plot("Day", "egg1_gasproduced", \
                                                       color="blue", figsize=(10, 5))
    return ax_final


#another function
def monthly_boxplot_by_egg(df_glob, egg):
    """
    This function returns an interactive plot
    Arguments: it takes 2 arguments-
        1. df_globe: the main dataframe
        2. egg: number of egg you want to plot
    """
    df_filtered = df_glob.loc[df_glob['egg_number'] == int(egg)]
    ax_final = df_filtered[["Month", "gas"]].boxplot(by="Month", return_type='axes')
    ax_final["gas"].set_title("egg " + egg)
    return ax_final

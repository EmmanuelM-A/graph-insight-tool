from .analyzer import analyze


def recommend_graph(df):
    col_types = analyze(df)
    recs = []

    numerical = [col for col, t in col_types.items() if t == 'numerical']
    categorical = [col for col, t in col_types.items() if t == 'categorical']
    datetime = [col for col, t in col_types.items() if t == 'datetime']
    label = [col for col, t in col_types.items() if t == 'label']

    # Bar Chart
    if (len(categorical) == 1 or len(label) == 1) and len(numerical) == 1:
        recs.append({
            "graph": "Bar Chart",
            "reason": "Bar charts are ideal for showing frequency distribution of categorical values.",
            "columns": {
                "x": categorical[0] if len(categorical) == 1 else label[0],
                "y": numerical[0]
            }
        })

    # Pie Chart
    if len(categorical) == 1 and len(numerical) == 1:
        recs.append({
            "graph": "Pie Chart",
            "reason": "Pie charts are useful for showing proportions of categories."
        })

    # Line Graph
    if len(datetime) == 1 and len(numerical) == 1:
        recs.append({
            "graph": "Line Graph",
            "reason": "Line graphs are great for showing trends over time."
        })

    # Histogram
    if len(numerical) == 1:
        recs.append({
            "graph": "Histogram",
            "reason": "Histograms are useful for showing the distribution of numerical data."
        })

    # Scatter Plot
    if len(numerical) == 2:
        recs.append({
            "graph": "Scatter Plot",
            "reason": "Scatter plots are ideal for showing relationships between two numerical variables."
        })

    # Box Plot
    if len(numerical) == 1 and len(categorical) == 1:
        recs.append({
            "graph": "Box Plot",
            "reason": "Box plots are useful for showing the distribution of numerical data across categories."
        })

    # Heatmap
    if len(numerical) > 1:
        recs.append({
            "graph": "Heatmap",
            "reason": "Heatmaps are useful for showing correlations between multiple numerical variables."
        })

    # Area Chart
    if len(datetime) == 1 and len(numerical) > 1:
        recs.append({
            "graph": "Area Chart",
            "reason": "Area charts are useful for showing cumulative totals over time."
        })

    # Bubble Chart
    if len(numerical) == 3:
        recs.append({
            "graph": "Bubble Chart",
            "reason": "Bubble charts are useful for showing relationships between three numerical variables."
        })

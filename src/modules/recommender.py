from .data_profiler.analyzer import analyze


def recommend_graph(df):
    col_types = analyze(df)
    recs = []

    numerical = [col for col, t in col_types.items() if t == 'numerical']
    categorical = [col for col, t in col_types.items() if t == 'categorical']
    datetime = [col for col, t in col_types.items() if t == 'datetime']

    # Bar Chart
    if len(categorical) == 1 and len(numerical) == 1:
        cat_col = categorical[0]
        num_col = numerical[0]
        if df[cat_col].nunique() < 30:
            recs.append({
                "graph": "Bar Chart",
                "type": "comparison",
                "reason": "Bar charts are ideal for showing frequency distribution of categorical values.",
                "columns": {
                    "x": cat_col,
                    "y": num_col
                }
            })

    # Pie Chart
    if len(categorical) == 1 and len(numerical) == 1:
        cat_col = categorical[0]
        num_col = numerical[0]
        if df[cat_col].nunique() < 10:  # Pie charts should have low cardinality
            recs.append({
                "graph": "Pie Chart",
                "type": "composition",
                "reason": "Pie charts are useful for showing proportions of categories.",
                "columns": {
                    "labels": cat_col,
                    "values": num_col
                }
            })

    # Line Graph
    if len(datetime) == 1 and len(numerical) == 1:
        recs.append({
            "graph": "Line Graph",
            "type": "trend",
            "reason": "Line graphs are great for showing trends over time.",
            "columns": {
                "x": datetime[0],
                "y": numerical[0]
            }
        })

    # Histogram
    if len(numerical) == 1 and len(categorical) == 0 and len(datetime) == 0:
        recs.append({
            "graph": "Histogram",
            "type": "distribution",
            "reason": "Histograms are useful for showing the distribution of numerical data.",
            "columns": {
                "x": numerical[0]
            }
        })

    # Scatter Plot
    if len(numerical) >= 2 and len(categorical) == 0 and len(datetime) == 0:
        recs.append({
            "graph": "Scatter Plot",
            "type": "relationship",
            "reason": "Scatter plots are ideal for showing relationships between two numerical variables.",
            "columns": {
                "x": numerical[0],
                "y": numerical[1]
            }
        })

    # Box Plot
    if len(numerical) == 1 and len(categorical) == 1:
        recs.append({
            "graph": "Box Plot",
            "type": "distribution",
            "reason": "Box plots are useful for showing the distribution of numerical data across categories.",
            "columns": {
                "x": categorical[0],
                "y": numerical[0]
            }
        })

    # Heatmap
    if len(numerical) >= 2 and len(categorical) == 0 and len(datetime) == 0:
        recs.append({
            "graph": "Heatmap",
            "type": "correlation",
            "reason": "Heatmaps are useful for showing correlations between multiple numerical variables.",
            "columns": numerical[:],  # full list of numerical cols
            "correlation": True
        })

    # Area Chart
    if len(datetime) == 1 and len(numerical) >= 1:
        recs.append({
            "graph": "Area Chart",
            "type": "trend",
            "reason": "Area charts are useful for showing cumulative totals over time.",
            "columns": {
                "x": datetime[0],
                "y": numerical  # can be a list
            }
        })

    # Bubble Chart
    if len(numerical) >= 3:
        recs.append({
            "graph": "Bubble Chart",
            "type": "relationship",
            "reason": "Bubble charts are useful for showing relationships between three numerical variables (X, Y, and "
                      "bubble size).",
            "columns": {
                "x": numerical[0],
                "y": numerical[1],
                "size": numerical[2]
            }
        })

    # Default Fallback
    if not recs:
        recs.append({
            "graph": "Table",
            "type": "fallback",
            "reason": "No suitable graph types could be determined from the dataset. Showing the raw data in tabular "
                      "form is the safest fallback.",
            "columns": df.columns.tolist()
        })

    return recs

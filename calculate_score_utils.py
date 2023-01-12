import pandas as pd

# Get the id of the query in query.xlsx dataset
def get_id(query):
    query_data = pd.read_excel('query.xlsx')
    id = query_data.loc[query_data['Query'] == query, 'ID'].iloc[0]
    return id
# Get the dataframe that contain the results of search in DataForBenchMark.xlsx dataset
def get_data(results):
    data = pd.read_excel('data.xlsx')
    filter_data = data.loc[data['JobDescription'].isin(results)]
    return filter_data

# Calculate score for the smart search system in the top-6 results
def calculate_score_top6(query, results):
    final_score = 0
    for i in range(len(query)):
        id_query = get_id(query[i])
        retrieval_data = get_data(results[i])
        temp = 0
        for i in retrieval_data['ID']:
            if str(id_query) in i.split(','):
                temp+=1
        if temp == 0:
            score = 0
        elif temp == 1 or temp == 2:
            score = 0.25
        elif temp == 3 or temp == 4:
            score = 0.5
        elif temp == 5:
            score = 0.75
        else:
            score = 1
        final_score += score
    return final_score/len(query)

# Calculate score for the smart search system in the top-8 results
def calculate_score_top8(query, results):
    final_score = 0
    for i in range(len(query)):
        id_query = get_id(query[i])
        retrieval_data = get_data(results[i])
        temp = 0
        for i in retrieval_data['ID']:
            if str(id_query) in i.split(','):
                temp+=1
        if temp == 0:
            score = 0
        elif temp >= 1 and temp <= 3:
            score = 0.25
        elif temp == 4 or temp == 5:
            score = 0.5
        elif temp == 6 or temp == 7:
            score = 0.75
        else:
            score = 1
        final_score += score
    return final_score/len(query)

# Calculate score for the smart search system in the top-10 results
def calculate_score_top10(query, results):
    final_score = 0
    for i in range(len(query)):
        id_query = get_id(query[i])
        retrieval_data = get_data(results[i])
        temp = 0
        for i in retrieval_data['ID']:
            if str(id_query) in i.split(','):
                temp+=1
        if temp == 0:
            score = 0
        elif temp >= 1 and temp <= 4:
            score = 0.25
        elif temp == 6 or temp == 7:
            score = 0.5
        elif temp == 8 or temp == 9:
            score = 0.75
        else:
            score = 1
        final_score += score
    return final_score/len(query)
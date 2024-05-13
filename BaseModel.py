#!/usr/bin/env python3

def retrieve_docs(folder_path):
    import os

    # Retrieve all documents
    doc_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            doc_list.append(file_path)
    return doc_list


def remove_stopWords(query):
    import nltk

    # Remove stop words
    stop_words = {'in', 'has', 'shouldn', 'between', 'more', 'once', 'further', "needn't", 'against', 'on', 'mustn', 'me', 'have', 'can', 'couldn', 'they', 'didn', 'because', 'the', 's', "hasn't", 'below', 'am', 'what', 'there', 'does', 'won', 'than', 'after', 'both', 'mightn', "shouldn't", 'over', 'you', 'of', 'so', 'nor', 'but', 'yours', 'those', 'before', 'o', 'for', 'a', 'doing', 'to', 'was', 'his', 'its', 'into', 'is', 'when', 'he', 'now', 'them', 'do', "mightn't", "she's", 'her', "it's", 'be', 'any', 'other', "you've", 'some', 'should', 'from', 'under', "haven't", 'during', 'with', 'i', 'will', 'while', 'by', "shan't", 'themselves', 'itself', 'did', "don't", 'only', "mustn't", "aren't", 'are', 'above', 'if', 're', 'off', 'ma', 'down', "wasn't", 'just', "hadn't", 'had', 'or', 'hasn', "you're", "didn't", 'these', 'hers', 'yourself', 'most', 'not', 've', 'ours', 'that', 'it', 'being', 'same', 'up', 'whom', 'why', 'then', 't', 'who', "isn't", 'wasn', 'ain', 'our', 'about', 'needn', 'own', "that'll", 'no', "should've", 'hadn', "wouldn't", 'their', 'll', "weren't", 'myself', 'shan', 'and', 'weren', 'through', 'until', 'this', 'been', 'as', "won't", 'doesn', 'which', 'don', 'your', 'him', 'd', 'himself', 'at', 'theirs', 'here', 'wouldn', 'y', 'were', 'herself', "couldn't", 'aren', 'haven', 'few', 'she', 'my', 'yourselves', 'how', 'again', 'too', 'very', 'where', "doesn't", 'we', "you'll", 'each', 'all', 'm', 'out', "you'd", 'such', 'having', 'ourselves', 'isn', 'an'}
    stop_words.remove("or")
    stop_words.remove("and")
    stop_words.remove("not")
    bure_words = []
    for q in query:
        if q not in stop_words:
            bure_words.append(q)
    return bure_words


def handle_boolean(query):
    logical_operators = ["and", "or", "not"]
    for i in range(len(query)):
        if i == 0 and query[i] in logical_operators:
            del query[i]
        elif i == len(query)-1 and query[i] in logical_operators:
            del query[i]
        elif i==len(query)-1:
            break
        elif query[i] in logical_operators and query[i+1] in logical_operators:
            del query[i]
        elif query[i] in logical_operators:
            if query[i] == "not" and query[i-1] != "and":
                query.insert(i, "and")
            continue  
        elif query[i+1] in logical_operators:
            continue
        else:
            query.insert(i+1, "and")
            i+=1
    return query


def check_query(doc, query):
    for i in range(len(query)):
        logical_operators = ["and", "or", "not"]
        if query[i] in logical_operators:
            continue
        if query[i] in doc:
            query[i] = "True"
        else:
            query[i] = "False"

    return query


def BoleanModel(query):
    related_docs = []
    if not query:
        return related_docs
    # Handle Query
    query = query.lower().split()
    query = remove_stopWords(query)
    query = handle_boolean(query)
    
    # Retrieve Documents
    folder_path = './Documents'
    docs = retrieve_docs(folder_path)

    for doc in docs:
        # Handle Documents
        text = ""
        with open(doc, 'r', encoding='utf-8') as f:
            text = f.read()
            text = text.lower()
            text = text.split()
            text = remove_stopWords(text)
        
        # Handle Result
        result = check_query(text, query.copy())

        result = " ".join(result)
        result = eval(result)
        doc_name = doc.split("/")[-1]

        if result == True:
            related_docs.append(doc_name)

    return related_docs


if __name__ == "__main__":
    query = "the football player and in Cairo not basketball"
    result = BoleanModel(query)
    print(result)


##### Algorithm #####
# 1. Retrieve documents paths
# 2. BoleanModell
    # 1. Handle document
        # 1. Open document
        # 2. Retrieve the content
        # 3. Tomenize into list
        # 4. Remove stop words
    # 2. Handle query
        # 1. Tomenize
        # 2. Remove stop words
        # 3. Handle boolean form
    # 3. Check if query related to document
    # 4. Save document name and result
# Print relevant and non relevant doucments


"""
{
    "res": ["document1.txt", "document2.txt", "document3.txt"]
}
"""

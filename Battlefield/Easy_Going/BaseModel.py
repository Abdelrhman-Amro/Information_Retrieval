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
    stop_words = set(nltk.corpus.stopwords.words('english'))
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
        # if first word is logical operator -> remove first one
        if i == 0 and query[i] in logical_operators:
            del query[i]
        # if last word is logical operator -> remove last one
        elif i == len(query)-1 and query[i] in logical_operators:
            del query[i]
        # logical loagical -> remove first one
        elif query[i] in logical_operators and query[i+1] in logical_operators:
            del query[i]
        # logical word
        elif query[i] in logical_operators:
            if query[i] == "not" and query[i-1] != "and":
                query.insert(i, "and")
            continue  
        # word logical
        elif query[i+1] in logical_operators:
            continue
        # word word -> insert and between them
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


def BoleanModel(docs, query):
    all_results = {True:[]}

    # Handle Query
    query = query.lower().split()
    query = remove_stopWords(query)
    query = handle_boolean(query)

    for doc in docs:
        # Handle Documents
        text = ""
        with open(doc, 'r', encoding='utf-8') as f:
            text = f.read()
            text = text.lower()
            text = text.split()
            text = remove_stopWords(text)
            print("Document: ", text)
        
        # Handle Query
        print("Query: ", query)
        
        # Handle Result
        result = check_query(text, query.copy())
        print(result)

        result = " ".join(result)
        print("Executable str -> ", result)
        result = eval(result)
        doc_name = doc.split("/")[-1]
        print(f"Document {{doc_name}}: {result}")
        print("#-------------------------------------------#")
        all_results[result].append(doc_name)

    return all_results


if __name__ == "__main__":
    # Retrieve Documents
    folder_path = './Documents'
    documents = retrieve_docs(folder_path)
    query = "the football player and in Cairo not basketball"
    result = BoleanModel(documents, query)
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

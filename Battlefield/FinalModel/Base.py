#!/usr/bin/env python3

def retrieve_files(folder_path):
    import os

    # Retrieve all files in a folder
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list


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



def Boolean(query):
    logical_operators = ["and", "or", "not"]
    for i in range(len(query) - 1):
        if query[i] in logical_operators and query[i+1] in logical_operators:
            del query[i]
        elif query[i] in logical_operators:
            continue
        elif query[i+1] in logical_operators:
            continue
        else:
            query.insert(i+1, "and")
            
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
    
def handle_not(query):
    for i in range(len(query) - 1):
        if query[i] == "not":
            query[i] = "and"
            if query[i+1] == "True":
                query[i+1] = "False"
            else:
                query[i+1] = "True"
    return query        


if __name__ == "__main__":
    # Retrieve Documents
    folder_path = './Documents'
    documents = retrieve_files(folder_path)
    print(documents)
    print("#-------------------------------------------#")

    for doc in documents:
        # Handle Documents
        text = ""
        with open(doc, 'r', encoding='utf-8') as f:
            text = f.read()
            text = text.lower()
            text = text.split()
            text = remove_stopWords(text)
            print("Document: ", text)
            
        # Handle Query
        query = "the football player and in Cairo not basketball"
        query = query.lower().split()
        query = remove_stopWords(query)
        query = Boolean(query)
        print("Query: ", query)
        
        # Handle Result
        result = check_query(text, query)
        print(result)
        
        result = handle_not(result)
        print(f"Handle not -> {result}")
        result = " ".join(result)
        print("Executable str -> ", result)
        result = eval(result)
        if result:
            result = "Relevant"
        else:
            result = "Not Relevant"
        doc_name = doc.split("/")[-1]
        print(f"Document {{doc_name}}: {result}")
        print("#-------------------------------------------#")



##### Algorithm #####
# Retrieve documents
# Documents
    # Open each document
    # Retrieve the content
    # Tomenize
    # Remove stop words
# Query
    # Tomenize
    # Remove stop words
    # Convert to boolean
# Check if query is in document
# print the document name and the result

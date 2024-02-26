import pyterrier as pt
import re

# Initialize PyTerrier
pt.init()

# Define the index path
# index_path = "/Users/xiongyuyang/Documents/_Master/IFT6255/devoirs/d1/indexing/no_stopwords_no_stemming/data.properties"
# index_path = "/Users/xiongyuyang/Documents/_Master/IFT6255/devoirs/d1/indexing/no_stopwords_porter/data.properties"
# index_path = "/Users/xiongyuyang/Documents/_Master/IFT6255/devoirs/d1/indexing/stopwords_no_stemming/data.properties"
index_path = "/Users/xiongyuyang/Documents/_Master/IFT6255/devoirs/d1/indexing/stopwords_porter/data.properties"

# Load the index
index = pt.IndexRef.of(index_path)

# Open the file and read its contents
with open('documents/AP_topics.1-150.txt', 'r') as file:
    # Read the entire contents of the file
    text = file.read()

# Extract the content after "<title> Topic:"
topics = re.findall(r"<title>(.*?)\n<desc>", text, re.DOTALL)
cleaned_topic_list = [topic.replace("?", "").replace("(", "").replace(")", "").
                      replace("Topic:", "").replace("\n", " ").replace("\t", "").
                      replace("'", "").replace("/", "").strip() for topic in topics]
# print(cleaned_topic_list)

# Define the retrieval model (Vector Space Model with TF*IDF weighting)
retrieval_model = pt.BatchRetrieve(index, wmodel="TF_IDF")

# Define the retrieval model (BM25)
# retrieval_model = pt.BatchRetrieve(index, wmodel="BM25")
# retrieval_model.setControl("k1", 0.9)
# retrieval_model.setControl("b", 0.4)

# Define the retrieval model (Language model with Dirichlet smoothing)
# retrieval_model = pt.BatchRetrieve(index, wmodel="DirichletLM")
# retrieval_model.setControl("mu", 1000)

# Save all the results
# with open('retrieval_results/VSModel_no_stopwords_no_stemming.txt', 'a') as file:
# with open('retrieval_results/VSModel_no_stopwords_porter.txt', 'a') as file:
# with open('retrieval_results/VSModel_stopwords_no_stemming.txt', 'a') as file:
with open('retrieval_results/VSModel_stopwords_porter.txt', 'a') as file:

# with open('retrieval_results/BM25_no_stopwords_no_stemming.txt', 'a') as file:
# with open('retrieval_results/BM25_no_stopwords_porter.txt', 'a') as file:
# with open('retrieval_results/BM25_stopwords_no_stemming.txt', 'a') as file:
# with open('retrieval_results/BM25_stopwords_porter.txt', 'a') as file:

# with open('retrieval_results/DirichletLM_no_stopwords_no_stemming.txt', 'a') as file:
# with open('retrieval_results/DirichletLM_no_stopwords_porter.txt', 'a') as file:
# with open('retrieval_results/DirichletLM_stopwords_no_stemming.txt', 'a') as file:
# with open('retrieval_results/DirichletLM_stopwords_porter.txt', 'a') as file:
    # retrieve all the documents for each query
    result = retrieval_model.transform(cleaned_topic_list)
    file.write(result.to_csv(index=False, header=False, sep='\t'))
        
        



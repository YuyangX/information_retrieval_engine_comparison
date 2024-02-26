import pyterrier as pt

pt.init()
# list of filenames to index
collection_path = pt.io.find_files("/Users/xiongyuyang/Documents/_Master/IFT6255/devoirs/d1/documents/AP")

stopwords_file_path = "/Users/xiongyuyang/Documents/_Master/IFT6255/devoirs/d1/documents/stop_words.txt"  

# Open the file and read its contents
with open(stopwords_file_path, "r") as file:
    lines = file.readlines()

# Remove newline characters from each line and create a list of strings
stopwords_list = [line.strip() for line in lines]

# build the index
indexer = pt.TRECCollectionIndexer("/Users/xiongyuyang/Documents/_Master/IFT6255/devoirs/d1/indexing/no_stopwords_porter",
                                    verbose=True,
                                    blocks=False,
                                    # stemmer=None,  # if stemmer is not specified, it stems with Porter stemmer
                                    stopwords=None
                                    )
indexref = indexer.index(collection_path)

# load the index, print the statistics
index = pt.IndexFactory.of(indexref)
print(index.getCollectionStatistics().toString())
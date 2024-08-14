import numpy as np
from scipy.sparse import csr_matrix
from collections import Counter

class TFIDFVectorizer:
    def __init__(self, tokenizer=None, stop_words=None):
        self.tokenizer = tokenizer
        self.stop_words = stop_words
    
    def fit(self, documents):
        self.idf_ = {}
        self.vocabulary_ = {}
        document_count = len(documents)
        term_doc_count = Counter()

        # Tokenizing and calculating term frequencies
        for doc in documents:
            tokens = self.tokenizer(doc) if self.tokenizer else doc.split()
            tokens = [token for token in tokens if token not in (self.stop_words or [])]
            unique_tokens = set(tokens)
            term_doc_count.update(unique_tokens)

        # Calculating IDF
        for term, doc_count in term_doc_count.items():
            self.idf_[term] = np.log((document_count + 1) / (doc_count + 1)) + 1

        # Creating vocabulary mapping
        self.vocabulary_ = {term: i for i, term in enumerate(self.idf_.keys())}
        return self
    
    def transform(self, documents):
        rows, cols, data = [], [], []
        for row_index, doc in enumerate(documents):
            tokens = self.tokenizer(doc) if self.tokenizer else doc.split()
            tokens = [token for token in tokens if token not in (self.stop_words or [])]
            token_counts = Counter(tokens)
            norm = np.sqrt(sum((token_counts[token] ** 2 for token in token_counts)))
            
            for token, count in token_counts.items():
                if token in self.vocabulary_:
                    col_index = self.vocabulary_[token]
                    tf = count / len(tokens)
                    idf = self.idf_.get(token, 0)
                    tfidf = tf * idf
                    rows.append(row_index)
                    cols.append(col_index)
                    data.append(tfidf)
        
        # Creating a sparse matrix
        return csr_matrix((data, (rows, cols)), shape=(len(documents), len(self.vocabulary_)))
    
    def fit_transform(self, documents):
        self.fit(documents)
        return self.transform(documents)
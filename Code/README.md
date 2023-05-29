**Pre-processing**.  
language_filtering_langdetect.py: Filtering out non-Eglish SMS from dataset using Python’s langdetect library.  
language_filtering_google.py: Filtering non-Eglish SMS from dataset using Python’s Googletrans library.  
OCR_image_text.ipynb: Conversion of SMS screenshots (collected from twitter and scam observatories) to text.

Evaluation of Shallow Machine Learning models  
TCSVM_TFIDF.ipynb: Feature extraction and evaluation of two class SVM (TCSVM) with BoW, Bigram and Trigram features.  
OCSVM_TFIDF.ipynb: Feature extraction and evaluation of one class SVM (OCSVM) with BoW, Bigram and Trigram features.  
PU_TFIDF.ipynb: Feature extraction and evaluation of Positive and Unlabelled with (PU) using BoW, Bigram and Trigram features.  
TCSVM_Semantic.ipynb: Feature extraction and evaluation of TCSVM with Word2Vec and GloVe features.  
OCSVM_Semantic.ipynb: Feature extraction and evaluation of OCSVM with Word2Vec and GloVe features.  
PU_Semantic.ipynb: Feature extraction and evaluation of PU with Word2Vec and GloVe features.  
fastText.ipynb: Feature extraction and evaluation of fastText.  

Evaluation of Deep Learning models  
SimpleTransformers_.ipynb: Evaluation of BERT, RoBERTa, XLM-RoBERTa, DistilBERT.  
ELMo.ipynb: Evaluation of ELMo.  
LSTM_BiLSTM_CNN.ipynb: Evaluation of LSTM, BiLSTM and CNN.  
TCN: Evaluation of TCN with random, Word2Vec(static) and Word2Vec(dynamic) embeddings.  
Ensemble (CNN-BiGRU): Evaluation of ensmeble approach with random, Word2Vec(static) and Word2Vec(dynamic) embeddings.

Misc
textAttack.ipynb: Generating adversarial examples (EDA, charswap) using textAttack framework.
sms_automation.py: Automating of SMS sending using Selenium.  

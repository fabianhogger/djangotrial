from nltk.corpus import stopwords

#print(stopwords.words('english')[0:10])
rawData=open("SMSSpamCollection.tsv").read()
print(rawData[:500])

parsed_data=rawData.replace("\t","\n").split("\n")
print(parsed_data[0:10])    

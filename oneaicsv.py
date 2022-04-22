import oneai
import csv
import pandas as pd
 
oneai.api_key = '2caaa40d-bdbe-4a3c-933c-34e28b269983'
pipeline = oneai.Pipeline(steps=[
    oneai.skills.Topics(),
    oneai.skills.Sentiments()
])
 
# read csv file and pass to the pipeline
with open('emotionssmall.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None) # ignore header
    outputs = pipeline.run(row[0] for row in reader)
 
# create a row in the dataframe
def create_row(input, output):
    return [
        input,
        [topic.value for topic in output.topics],
        [sentiment.value for sentiment in output.sentiments]
       
    ]
 
# create the dataframe
df = pd.DataFrame(create_row(i, o) for i, o in outputs.items())
df

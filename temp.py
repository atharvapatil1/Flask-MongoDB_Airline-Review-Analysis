from pymongo import MongoClient
import inspect

# Connect to your MongoDB instance
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']  # Replace 'your_database_name' with the name of your database
collection = db['airline_reviews']  # Replace 'airline_reviews' with your collection name


function_code = inspect.getsource(sentiment_analysis)


pipeline = [
        {
        "$addFields": {
            "sentimentScore": {
                "$function": {
                    "body": function_code,
                    "args": ["$review"],
                    "lang": "py"
                }
            }
        }
    },

    {
        "$addFields": {
            "mentionsDelay": {
                "$or": [
                    {"$regexMatch": {"input": "$review", "regex": "delay", "options": 'i'}},
                    {"$regexMatch": {"input": "$review", "regex": "late", "options": 'i'}}
                ]
            }
        }
    },
    {
        "$group": {
            "_id": "$mentionsDelay",
            "averageSentiment": {"$avg": "$sentimentScore"},  # Assuming sentimentScore is a numerical representation of sentiment
            "count": {"$sum": 1}
        }
    },
    {
        "$sort": {"_id": 1}  # Sorting by mentionsDelay, false first then true
    }
]

# Execute the aggregation pipeline
result = list(collection.aggregate(pipeline))

# Print the results
for doc in result:
    print(doc)

from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS
from datetime import datetime, timedelta
from sentiment import sentiment  # Importing the sentiment function from sentiment.py


app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
print("MongoDB Client:", client)
db = client['dbproject']
collection = db['dbdatset']

# Landing Page
@app.route('/')
def home():
    return render_template('index.html')

sentiment_query =     {
        "$addFields": {
            "sentiment": {
                "$function": {
                    "body": """function(review) {
                        // Define positive and negative words
                        const positiveWords = ['happy', 'great', 'fantastic', 'positive', 'good', 'love', 'enjoyed', 'like'];
                        const negativeWords = ['sad', 'bad', 'terrible', 'negative', 'hate', 'dislike', 'horrible'];
                        
                        // Split review into words and normalize to lowercase
                        const words = review.toLowerCase().split(/\\s+/);
                        let score = 0;
                        
                        // Calculate sentiment score
                        words.forEach(word => {
                            if (positiveWords.includes(word)) {
                                score++;
                            } else if (negativeWords.includes(word)) {
                                score--;
                            }
                        });
                        
                        // Return sentiment based on score
                        return score > 0 ? 'Positive' : score < 0 ? 'Negative' : 'Neutral';
                    }""",
                    "args": ["$review"],
                    "lang": "js"
                }
            }
        }
    }

# Task 1: Food & Beverages Feedback Analysis
@app.route('/task1', methods=['GET'])
def task1():    
    pipeline = [
      

    sentiment_query,

    {
        "$match": {
            "foodBeveragesRating": {"$exists": 1},
            "valueForMoneyRating": {"$exists": 1}
        }
    },
    {
        "$group": {
            "_id": "$sentiment",
            "averageValueForMoney": {"$avg": "$valueForMoneyRating"},
            "count": {"$sum": 1}
        }
    },
    {
        "$sort": {"averageValueForMoney": -1}
    },

    {
        "$project": {
        "_id": 0,
        }
    }
    ]
    
    result = list(collection.aggregate(pipeline))

    return jsonify(result)

    


# Task 2: Analysis of Sentiment Versus Value for Money
@app.route('/task2', methods=['GET'])
def task2(): 
    pipeline = [
    # First, add the sentiment field
    {
        "$addFields": {
            "sentiment": {
                "$function": {
                    "body": """function(review) {
                        const positiveWords = ['happy', 'great', 'fantastic', 'positive', 'good', 'love', 'enjoyed', 'like'];
                        const negativeWords = ['sad', 'bad', 'terrible', 'negative', 'hate', 'dislike', 'horrible'];
                        const words = review.toLowerCase().split(/\\s+/);
                        let score = 0;
                        words.forEach(word => {
                            if (positiveWords.includes(word)) {
                                score++;
                            } else if (negativeWords.includes(word)) {
                                score--;
                            }
                        });
                        return score > 0 ? 'Positive' : score < 0 ? 'Negative' : 'Neutral';
                    }""",
                    "args": ["$review"],
                    "lang": "js"
                }
            }
        }
    },
    # Then, group by valueForMoneyRating and collect sentiments
    {
        "$group": {
            "_id": "$valueForMoneyRating",
            "numReviews": {"$sum": 1},
            "sentiments": {"$push": "$sentiment"}
        }
    },
    # Sort by valueForMoneyRating (if necessary, depending on the exact requirement)
    {
        "$sort": {"_id": 1}
    },
    # Finally, calculate the distribution of sentiments
    {
        "$addFields": {
            "sentimentAnalysis": {
                "$reduce": {
                    "input": "$sentiments",
                    "initialValue": {"positive": 0, "neutral": 0, "negative": 0},
                    "in": {
                        "$switch": {
                            "branches": [
                                {"case": {"$eq": ["$$this", "Positive"]}, "then": {"positive": {"$add": ["$$value.positive", 1]}, "neutral": "$$value.neutral", "negative": "$$value.negative"}},
                                {"case": {"$eq": ["$$this", "Neutral"]}, "then": {"positive": "$$value.positive", "neutral": {"$add": ["$$value.neutral", 1]}, "negative": "$$value.negative"}},
                                {"case": {"$eq": ["$$this", "Negative"]}, "then": {"positive": "$$value.positive", "neutral": "$$value.neutral", "negative": {"$add": ["$$value.negative", 1]}}}
                            ],
                            "default": {"positive": "$$value.positive", "neutral": "$$value.neutral", "negative": "$$value.negative"}
                        }
                    }
                }
            }
        }
    }
]  
    result = list(collection.aggregate(pipeline))

    return jsonify(result) 

# Task 3: Sentiment by Route Popularity
@app.route('/task3', methods=['GET'])
def task3():    
    pipeline = [
      

    sentiment_query,

    {
        # Step 1: Group by route
        "$group": {
            "_id": "$route",  # Grouping by the route
            "numReviews": {"$sum": 1},  # Counting the number of reviews per route
            "sentiments": {"$push": "$sentiment"}  # Collecting sentiments for each review
        }
    },
    {
        # Step 2: Sort by the number of reviews to determine route popularity
        "$sort": {"numReviews": -1}
    },
    {
        # Step 3: Add a new field to calculate the distribution of sentiments for each route
        "$addFields": {
            "sentimentAnalysis": {
                "$reduce": {
                    "input": "$sentiments",
                    "initialValue": {"positive": 0, "neutral": 0, "negative": 0},
                    "in": {
                        "$switch": {
                            "branches": [
                                {"case": {"$eq": ["$$this", "positive"]}, "then": {"positive": {"$add": ["$$value.positive", 1]}, "neutral": "$$value.neutral", "negative": "$$value.negative"}},
                                {"case": {"$eq": ["$$this", "neutral"]}, "then": {"positive": "$$value.positive", "neutral": {"$add": ["$$value.neutral", 1]}, "negative": "$$value.negative"}},
                                {"case": {"$eq": ["$$this", "negative"]}, "then": {"positive": "$$value.positive", "neutral": "$$value.neutral", "negative": {"$add": ["$$value.negative", 1]}}}
                            ],
                            "default": {"positive": "$$value.positive", "neutral": "$$value.neutral", "negative": "$$value.negative"}
                        }
                    }
                }
            }
        }
    },

    {
        "$project": {
        "_id": 0,
        }
    }
    ]
    
    result = list(collection.aggregate(pipeline))

    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)

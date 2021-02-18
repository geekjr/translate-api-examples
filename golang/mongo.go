package main

import(
    "https://github.com/geekjr/translate-api-go"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"go.mongodb.org/mongo-driver/mongo/readpref"
)

func main() {
	uri := "MONGO-CONNECTION-STRING"
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	client, err := mongo.Connect(ctx, options.Client().ApplyURI(uri))
	collection := client.Database("DATABASE").Collection("COLLECTION")
	cursor, err := collection.Find(context.TODO(), bson.D{})
	for doc in cursor {
        json = translateapi.JsonRequest("YOUR-API-KEY", "%d", doc)
    }
}
import JsonRequest from "translation-api-js-client";

let json
const url = "CONNECTIOn STRING";
const client = new MongoClient(url);
await client.connect();
const db = client.db("DATABASE TO USE");
const col = db.collection("COLLECTION TO USE");
const cursor = col.find();
await cursor.forEach(json = JsonRequest({"THE": "JSON", "DOC": "TO TRANSLATE"}, "YOUR-API-KEY"), console.log(json));
import JsonRequest from "translation-api-js-client";

let json = JsonRequest({"THE": "JSON", "DOC": "TO TRANSLATE"}, "YOUR-API-KEY")
console.log(json)
# Homepage
curl -X GET http://0.0.0.0:8080;

# CollectionAPI
curl -X GET http://localhost:8080/collection;
curl -X POST --header 'Content-length: 0' http://localhost:8080/collection;

# ItemAPI
curl -X GET http://0.0.0.0:8080/item/3;
curl -X DELETE http://0.0.0.0:8080/item/3;
curl -X POST --header 'Content-length: 0' http://localhost:8080/item/3;
curl -X PUT --header 'Content-length: 0' http://localhost:8080/item/3;
curl -X POST -H 'Content-Type: application/json' http://localhost:8080/collection -d '{"name":"asdfs", "age":"20", "address":"edcv", "salary":"30.23"}'

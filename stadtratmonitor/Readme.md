# Experimenting with visualisation of Leipzig city counsil data

## Set up
 Follow the instruction of the Readme.md in the root of this project.
 
 The clone https://github.com/CodeforLeipzig/stadtratmonitor and modify the docker-compose.yml
 file to expose the port of the Elasticsearch instance:

 ```
 elasticsearch:
  ...
  ports:
   - "9200:9200"
  ...
 ``` 

 Then do `docker-compose up -d` and follow the instructions from the stadtratmonitor
 GitHub page to import the data into ElasticSearch.

 Later you should use tools like [elasticsearch-dump](https://github.com/taskrabbit/elasticsearch-dump) to store and restore ElasticSearch data without the need to rescrape the data.

## Examples
### Paper originators by the number of papers they issued
![srmjupyter](https://user-images.githubusercontent.com/994131/27010527-182fa69c-4ea7-11e7-8e81-e03d0aaa774a.PNG)

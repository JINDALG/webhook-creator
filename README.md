# webhook-creator

This project is created to ease the task for creating new web-hooks for various integration. 

## Setup

- Install docker and docker-compose
- Clone this repo
- Go inside the repo
- Run ```docker-compose build``` and then ```docker-compose up```
- Server would be running on [localhost:8001](http://localhost:8001)

## Endpoints

- List existing web-hooks
```
GET: http://localhost:8001/api/hooks/
```
- Show data of all hits on single web-hook
```
GET: http://localhost:8001/api/hooks/{web_hook_id}/
```
- Create New Web-hook
```
POST: http://localhost:8001/api/hooks/
form_data: {"key": some-key}
```
- Test Webhook
```
POST: http://localhost:8001/api/input/{key}/
Any data passed in body, query_params and headers will be recorded.
```

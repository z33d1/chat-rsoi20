run:
	python3 backend/run.py

build_backend:
	cd backend;\
	docker build -t chat-backend .

run_backend:
	docker run -it -p 5000:8080 --rm --name running-chat-backend chat-backend 
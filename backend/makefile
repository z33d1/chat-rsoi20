all: build_backend run_backend
run:
	python3 src/app.py

build_backend:
	docker build -t chat-backend .

run_backend:
	docker run -it -p 5000:8080 --env VARIABLE=SUPER_NESSARY_VARIABLE --rm --name running-chat-backend chat-backend 

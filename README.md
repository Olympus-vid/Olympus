To build:
    In root:
        python3 dependencies.py
        python3 whisperValue.py
        python3 app.py
    In frontend:
        npm run build 
            fails --> rm -rf node_modules && npm install --force && npm run build
To run:
    In root:
        python3 app.py
    In frontend:
        npm start

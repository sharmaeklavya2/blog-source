.PHONY: clean local deploy
clean:
	find . -name "*.pyc" -type f -delete
	find . -name "__pycache__" -type d -delete
local:
	pelican --theme=theme
deploy:
	pelican --theme=theme --output=deploy --settings=publishconf.py

.PHONY: clean local deploy
clean:
	find . -name "*.pyc" -type f -delete
	find . -name "__pycache__" -type d -delete
local:
	pelican --theme=theme
deploy:
	PELICAN_PUBLISH=1 pelican --theme=theme --output=deploy

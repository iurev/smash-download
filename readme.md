# Smashing Wallpaper Downloader

![Meme – VZHUCKH cat](/other/vzhuckh.png "VZHUCKH, and you have amazing wallappers")

_VZHUCKH, and you have amazing wallappers_

## How to use

```
# in the project's folder
python main.py # Download photos of the current month
python main.py 2018 1 # Download photos of January of 2018
python main.py 320x480 no-calendar # Current month with size 320x480 and without calendar
```

Parameters year month size calendar:
```
year – four digits, default - current year
month – one/two digits, default – current month
size – like 320x480, default – 2560x1440
no-calendar
```

## Installation

```
git clone https://github.com/wwju/smash-download.git
cd smash-download
pip install -r requirements.txt
```

## Testing

```
pytest test.py
```

## License

MIT

An interface for the wayback machine API. Built upon (Johannes Filter's work)[https://github.com/jfilter/get-wayback-machine].


## Why?

Occasionally, you have a given URL that it is not online anymore. You may still access it's content via the Internet Archive's [Wayback Machine](https://archive.org/web/).

## Install

```bash
pip install git+https://github.com/patjenk/get-wayback-machine
```

## Usage

```python
import get_wayback_machine

json_response = get_wayback_machine.check_availability('https://en.wikipedia.org')
if json_response:
    print(json_response)
```

## Related

-   https://github.com/jfilter/get-wayback-machine'
-   https://github.com/hartator/wayback-machine-downloader
-   https://github.com/sangaline/wayback-machine-scraper
-   https://github.com/jsvine/waybackpack

## License

MIT.

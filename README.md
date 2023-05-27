```shell
URLS="https://librarium.fr/ru/magazines/frontier https://librarium.fr/ru/magazines/satyricon https://librarium.fr/ru/magazines/almanach https://librarium.fr/ru/magazines/unsere_welt https://librarium.fr/ru/magazines/swallow https://librarium.fr/ru/magazines/zar-ptitza https://librarium.fr/ru/magazines/theatreandlife https://librarium.fr/ru/magazines/oukwat https://librarium.fr/ru/magazines/theatreandlife-fr https://librarium.fr/ru/magazines/le-monde-et-l-art https://librarium.fr/ru/magazines/bitche https://librarium.fr/ru/magazines/au-volant https://librarium.fr/ru/magazines/la-vie-Illustree https://librarium.fr/ru/magazines/lavoie https://librarium.fr/ru/magazines/spolokhi https://librarium.fr/ru/magazines/slatozwjet https://librarium.fr/ru/magazines/lescarillons https://librarium.fr/ru/magazines/newniva https://librarium.fr/ru/magazines/plage https://librarium.fr/ru/magazines/LaPatrie https://librarium.fr/ru/magazines/VokrugSveta https://librarium.fr/ru/magazines/bouk https://librarium.fr/ru/magazines/niva https://librarium.fr/ru/newspapers/russiaillustrated https://librarium.fr/ru/newspapers/days https://librarium.fr/ru/newspapers/borba-za-rossiyu"

wget --html-extension --recursuve $URLS
ls librarium.fr/ru/*/*/*/*/*/i.html | xargs dirname | xargs printf "https://%s\n" > librariumdump.txt

python3 librariumdump.py -i librariumdump.txt -o librariumdump
```

1. Log into the website in a new Chrome window
2. Navigate to the url which is printed to the console

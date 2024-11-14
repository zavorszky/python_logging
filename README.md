
# Python naplózás/logging

## Python csomag: logging, logging.config

| Program    | Tulajdonság-szavak|
|:-----------|:------------------|
|logging_1.py|#simple_log_file #stdout  #napozas_1_helyre<br> #logging #logging.config #json_config|
|logging_2.py|#simple_log_file #stderr #file  #napozas_2_helyre<br>  #logging #logging.config #json_config|
|logging_3.py|#detailed_log_file #stderr #file #napozas_2_helyre<br>  #logging #logging.config #json_config|
|logging_4.py|#pytz #json #own_formatter<br>  #json_log_file #stderr #file #napozas_2_helyre<br>  #logging #logging.config #json_config|
|logging_5.py|#queue_hasznalat_naplo_file_iraskor #extra_hasznalat_uzenet_iraskor<br>  #pytz #json #own_formatter<br>  #json_log_file #stderr #file #napozas_2_helyre<br>  #logging #logging.config #json_config|

## Alap link

[Modern Python logging](https://www.youtube.com/watch?v=9L77QExPmI0&list=PLcLIOuMu3bXrXGdqV7tPTU63a8sVjQDuw&index=30)

Author: James Murphy (mCoding)

## Problémák

### Probléma az ékezetes karakterek (utf-8) log file-ba írásakor (logging csomag)

A naplóüzenetben ékezetes karakterek szerepelnek.<br>
A program file utf-8 kódolású.<br>
Az "stderr"-en a üzenet helyesen jelenik meg, de a log file-ba a karakter kódja kerül:<br>
Helyes: "Warning üzenet"<br>
Hibás: "Warning \u00fczenet"

A példában a napló file json sorok összessége.<br>
A MyJSONFornatter és a MyJSONFornatter2 'format' metódusa a végén a 'json.dumps'
függvény alakítja át az összeállított szótár típusú vátozót (dictionary) json szöveggé (string).
Alapértelmezés szerint a 'json.dumps' ascii karaktereket használ, pl. az utf-8 kódolású
karaktereknek a kódját írja a sztringbe. Ezt a funkciót ki lehet kapcsolni és az ékezete
karakterek helyesen jelennek meg a sztringben és így a file-ban is:<br>
<code>...<br>
return json.dumps(message, ensure_ascii=False, default=str)<br>
...</code>

## Hasznos linkek

[Can comments be used in JSON?: stackoverflow](https://stackoverflow.com/questions/244777/can-comments-be-used-in-json)

[Handling timezone in Python: geeksforgeeks](https://www.geeksforgeeks.org/handling-timezone-in-python/)

[How to Use the Python pop() Method: datacamp](https://www.datacamp.com/tutorial/python-pop?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720824&utm_adgroupid=157156376311&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=719914246078&utm_targetid=aud-2274077226600%3Adsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=9063089&utm_content=&utm_campaign=230119_1-sea%7Edsa%7Etofu_2-b2c_3-row-p2_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na-fawnov24&gad_source=1&gclid=Cj0KCQiArby5BhCDARIsAIJvjIRU1gRUNQ_ogpuxsyM0YZpkSaDwtobcjrQT4C5U5JcqTyUiX1BdqLUaApF3EALw_wcB&dc_referrer=https%3A%2F%2Fwww.google.com%2F)

[json.dumps() in Python: geeksforgeeks](https://www.geeksforgeeks.org/json-dumps-in-python/)

## Környezet

OS: Windows 10 Home; 64 bites operációs rendszer, x64-alapú processzor

Python: 3.12.3

## Szerző

<zavorszky@yahoo.com>
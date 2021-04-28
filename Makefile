OUTPUT_DIR=html

all: HTML_DIR inventory.html music_and_misc.html various_artists_comedy.html various_artists_radio_shows.html

.SUFFIXES: .csv .html
.csv.html:
	./csv_to_html.py -i $> -o ${OUTPUT_DIR}/$@
	
HTML_DIR:
	mkdir -p ${OUTPUT_DIR}

clean:
	rm -rf ${OUTPUT_DIR}

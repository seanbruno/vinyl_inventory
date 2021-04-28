OUTPUT_DIR=html

all: inventory.html music_and_misc.html various_artists_comedy.html various_artists_radio_shows.html

.SUFFIXES: .csv .html
.csv.html:
	./csv_to_html.py -i $> -o $@
	
clean:
	rm -rf *.html

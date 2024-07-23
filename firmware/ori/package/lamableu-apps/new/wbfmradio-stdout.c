#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <luaradio.h>

const char *script_template =
    "local radio = require('radio')"
    "local frequency = tonumber(%f)"
    "return radio.CompositeBlock():connect("
    "    radio.SoapySDRSource('driver=plutosdr', frequency - 250e3, 960000, {gain=68}),"
    "    radio.TunerBlock(-250e3, 170e3, 4, {128,hamming}),"
    "    radio.WBFMMonoDemodulator(),"
    "    radio.DownsamplerBlock(5),"
    "    radio.RealFileSink(1, 's16le')"
    ")";


int main(int argc, char *argv[]) {
    luaradio_t *radio;
    char script[512];

    if (argc < 2) {
        fprintf(stderr, "\nUsage: %s <FM station frequency>\n", argv[0]);
	fprintf(stderr, "Stream WBFM station. Output to stdout as RAW format (s16le)\n");
	fprintf(stderr, "\nPluto side, use : %s  <freq> | nmux -p 1234 -a 0.0.0.0\n", argv[0]);
	fprintf(stderr, "Remote side : nc pluto.local 1234 | ffplay -f s16le -ar 48k -ac 1 -\n");
	fprintf(stderr, "or : nc pluto.local 1234 | vlc --demux=rawaud --rawaud-channels 1 --rawaud-samplerate 48000 -\n\n");
        return -1;
    } 

    fprintf(stderr, "Recording WBFM on %s to /www/record.wav\n", argv[1]);

 /* Substitute station frequency in script template  */
    snprintf(script, sizeof(script), script_template, atof(argv[1])); 

    /* Create context */
    if ((radio = luaradio_new()) == NULL) {
        perror("Allocating memory");
        return -1;
    }

    /* Load flow graph */
    if (luaradio_load(radio, script) < 0) {
        fprintf(stderr, "Error loading flow graph: %s\n", luaradio_strerror(radio));
        return -1;
    }

    /* Start flow graph */
    if (luaradio_start(radio) < 0) {
        fprintf(stderr, "Error starting flow graph: %s\n", luaradio_strerror(radio));
        return -1;
    }

    /* Wait until completion  */
    if (luaradio_wait(radio) < 0) {
        fprintf(stderr, "Error waiting for flow graph: %s\n", luaradio_strerror(radio));
        return -1;
    } 

    /* Free context */
    luaradio_free(radio);

    return 0;
}

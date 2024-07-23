

/* LamaBleu - 09/2019
 Create IQ stream from WAV input file (48000Hz)
 SR Pluto : 576000 */


#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <luaradio.h>
#include <iio.h>
 

const char *script_template =
    "return radio.CompositeBlock():connect("
    "    radio.WAVFileSource('%s',1),"
    "    radio.LowpassFilterBlock(128, 3400),"
    "    radio.HilbertTransformBlock(129),"
    "    radio.ComplexBandpassFilterBlock(129, {0, 3400}),"
    "    radio.InterpolatorBlock(12),"
    "    radio.ComplexBandpassFilterBlock(130, {0, 5000}),"
    "    radio.IQFileSink(1, 's16le')"
    ")";


int main(int argc, char *argv[]) {
    luaradio_t *radio;
    char script[512];

    if (argc < 3) {
	fprintf(stderr, "Generate 576kS/s IQ stream from WAV file (48000Hz).\n");
	fprintf(stderr, "Output to stdout (use pipe or redirect to file).\n");
        fprintf(stderr, "Usage: %s <WAV file (48000Hz)> <Frequency(Hz)>\n", argv[0]);
        return -1;
    }




    /* Substitute station frequency in script template */
    snprintf(script, sizeof(script), script_template, argv[1]); 

    /* Test: print frequency */
    /*char frequency = argv[2];*/
    fprintf(stderr, "Frequency: %s\n", argv[2]);


	struct iio_context *ctx;
	struct iio_device *phy;
 
	ctx = iio_create_context_from_uri("ip:192.168.2.1");
 
	phy = iio_context_find_device(ctx, "ad9361-phy");
 
	iio_channel_attr_write_longlong(
		iio_device_find_channel(phy, "altvoltage0", true),
		"frequency",
		atof(argv[2])); /* RX LO frequency 2.4GHz */
 
	iio_channel_attr_write_longlong(
		iio_device_find_channel(phy, "voltage0", false),
		"sampling_frequency",
		576000); /* RX baseband rate 5 MSPS */


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

    /* Wait until completion */
    if (luaradio_wait(radio) < 0) {
        fprintf(stderr, "Error waiting for flow graph: %s\n", luaradio_strerror(radio));
        return -1;
    }

    /* Free context */
    luaradio_free(radio);
    iio_context_destroy(ctx);
    return 0;
}



/* 
io.stderr:write("Usage: " .. arg[0] .. "<input file>  \n")
    io.stderr:write("Input file /tmp/send.png.wav, output IQ to stdout \n")
const char *script_template =



    "if #arg < 1 then
        "arg[1]='/tmp/send.png.wav'

    "end

    "local input_file = arg[1]




 "local sinkiio = radio.IQFileSink(1, 's16le')
    "local wav2iq = radio.CompositeBlock()
          "wav2iq:connect(source, af_filter, hilbert, sb_filter, interpolator, filter2, sinkiio)  */

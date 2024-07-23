

/* LamaBleu - 10/2019
 Using LUAradio, create IQ stream from WAV input file (48000Hz) - output to stdout
 Prepare pluto to transmit - Set tuner TX freq and SR to 576000 kSPS
 To start transmission use : 
   'wav2ssb <WAV-file> <Frequency> | pv | iio_writedev -b 1000000 cf-ad9361-dds-core-lpc' 
*/


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

float gain;
int main(int argc, char *argv[]) {
    luaradio_t *radio;
    char script[512];

    if (argc == 1) {
	fprintf(stderr, "Usage: %s <WAV file (48000Hz)> <Frequency(Hz)> <TXPower (-89 to 0)>\n\n", argv[0]);
	fprintf(stderr, "Generate 576kS/s IQ stream from WAV file (48000Hz).\n");
	fprintf(stderr, "Output to stdout (use pipe or redirect to file).\n");
	fprintf(stderr, "\nPluto transmit example:\n\t %s /www/record.wav 434000000 -20 | pv | iio_writedev -b 1000000 cf-ad9361-dds-core-lpc\n\n",argv[0] );  
        return -1;
    }
  /*gain = atof(argv[3]);
  if (argc < 3) {
	gain = atof("-10");
	 } else { gain = atof(argv[3]); }
*/
    /* Substitute station frequency in script template */
    snprintf(script, sizeof(script), script_template, argv[1]); 

 if (argc < 3) {
	fprintf(stderr, "Incorrect parameters number\n");
	return -1;
	 } 



	struct iio_context *ctx;
	struct iio_device *phy;
 
	ctx = iio_create_context_from_uri("local:");
 
	phy = iio_context_find_device(ctx, "ad9361-phy");
        fprintf(stderr, "Set frequency: %s\n", argv[2]);
	iio_channel_attr_write_longlong(
		iio_device_find_channel(phy, "altvoltage1", true),
		"frequency",
		atof(argv[2])); /* RX LO frequency 2.4GHz */
        fprintf(stderr, "Set samplerate: 576000\n");
	iio_channel_attr_write_longlong(
		iio_device_find_channel(phy, "voltage0", false),
		"sampling_frequency",
		576000); /* TX baseband rate 576 kSPS */

	fprintf(stderr, "Set TX gain: %f\n", gain);
	iio_channel_attr_write_longlong(
		iio_device_find_channel(phy, "voltage0", true),
		"hardwaregain",
		gain); /* RX LO frequency 2.4GHz */

    /* Create context */
    if ((radio = luaradio_new()) == NULL) {
        perror("Allocating memory");
        return -1;
    }

    /* Load flow graph */
    if (luaradio_load(radio, script) < 0) {
        perror("Error loading flow graph.\n");
	iio_context_destroy(ctx);
        return -1;
    }

    /* Start flow graph */
    if (luaradio_start(radio) < 0) {
        perror("Error starting flow graph. \n");
	iio_context_destroy(ctx);
        return -1;
    }

    /* Wait until completion */
    if (luaradio_wait(radio) < 0) {
        perror("Error running for flow graph. \n");
        return -1;
    }

    /* Free context */
    luaradio_free(radio);
    iio_context_destroy(ctx);
    return 0;
}


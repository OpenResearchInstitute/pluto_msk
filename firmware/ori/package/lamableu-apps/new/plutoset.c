#include <iio.h>
 
int main (int argc, char **argv)
{
	struct iio_context *ctx;
	struct iio_device *phy;
 
	ctx = iio_create_context_from_uri("local:");
 
	phy = iio_context_find_device(ctx, "ad9361-phy");
 
	iio_channel_attr_write_longlong(
		iio_device_find_channel(phy, "altvoltage0", true),
		"frequency",
		434000000); /* RX LO frequency 2.4GHz */
 
	iio_channel_attr_write_longlong(
		iio_device_find_channel(phy, "voltage0", false),
		"sampling_frequency",
		2000000); /* RX baseband rate 5 MSPS */
 
/*	receive(ctx);  */
 
	iio_context_destroy(ctx); 
 
	return 0;
} 

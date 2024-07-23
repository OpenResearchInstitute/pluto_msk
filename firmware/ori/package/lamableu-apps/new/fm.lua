local radio = require('radio')
local frequency = tonumber(arg[1])
local top = radio.CompositeBlock():connect(
    radio.SoapySDRSource('driver=plutosdr',frequency - 250e3, 1102500, {gain=68}),
    radio.TunerBlock(-250e3, 200e3, 5),
    radio.WBFMMonoDemodulator(),
    radio.DownsamplerBlock(5),
    radio.WAVFileSink('/tmp/record.wav',1,8)
)
top:run()



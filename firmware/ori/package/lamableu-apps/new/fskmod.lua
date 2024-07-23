-- Input : random bits (1200bit/s, output IQ stream)
-- Based on : http://luaradio.io/docs/creating-blocks.html#blocks
-- Transmit: use "./luaradio ./fskmod.lua  | pv | iio_writedev -n 192.168.2.1 -b 1000000 cf-ad9361-dds-core-lpc" 


local radio = require('radio')
local ffi = require('ffi')

local BFSKModulator = radio.block.factory('BFSKModulator')

function BFSKModulator:instantiate(deviation, sample_rate)
    self.deviation = deviation
    self.sample_rate = sample_rate

    self:add_type_signature({radio.block.Input("in", radio.types.Bit)},
                            {radio.block.Output("out", radio.types.ComplexFloat32)})
end

ffi.cdef[[
typedef struct fskmod_s * fskmod;
fskmod fskmod_create(unsigned int _m, unsigned int _k, float _bandwidth);
void fskmod_destroy(fskmod _q);
void fskmod_modulate(fskmod _q, unsigned int _s, complex_float32_t *_y);
]]
local libliquid = radio.platform.libs.liquid

function BFSKModulator:initialize()
    self.samples_per_bit = math.floor(self.sample_rate / radio.block.Block.get_rate(self))

    self.modulator = ffi.gc(
        libliquid.fskmod_create(1, self.samples_per_bit, (self.deviation / self.sample_rate)/2),
        libliquid.fskmod_destroy
    )
    if self.modulator == nil then
        error("Creating liquid fskmod object.")
    end

    self.out = radio.types.ComplexFloat32.vector()
end

function BFSKModulator:get_rate()
    return self.sample_rate
end

function BFSKModulator:process(x)
    local out = self.out:resize(x.length * self.samples_per_bit)

    for i = 0, x.length-1 do
--        libliquid.fskmod_modulate(self.modulator, x.data[i].value-48, out.data[i*self.samples_per_bit])
        libliquid.fskmod_modulate(self.modulator, x.data[i].value, out.data[i*self.samples_per_bit])
    end

    return out
end

-- local source = radio.RawFileSource('/root/luaradio/bits.txt', radio.types.Bit,300, true)
local source = radio.UniformRandomSource(radio.types.Bit, 1200)
local bfsk = BFSKModulator(10e3 , 576e3)
local interpolator = radio.InterpolatorBlock(2)
local sink = radio.IQFileSink('/root/luaradio/toto.txt', 'f32le')
-- local sinkiio = radio.IQFileSink('/tmp/iq.test', 's16le')
local sinkiio = radio.IQFileSink(1, 's16le')

-- Connections


local plutoiq = radio.CompositeBlock()
      plutoiq:connect(source,radio.ThrottleBlock(),bfsk,sinkiio)
if os.getenv('DISPLAY') then
      plutoiq:connect(bfsk,radio.ThrottleBlock(), radio.GnuplotSpectrumSink())
end

plutoiq:run()

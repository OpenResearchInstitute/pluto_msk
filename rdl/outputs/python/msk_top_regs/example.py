
from .lib import AsyncCallbackSet

from .reg_model.msk_top_regs import msk_top_regs_cls
from .sim.msk_top_regs import msk_top_regs_simulator_cls

if __name__ == '__main__':

    sim = msk_top_regs_simulator_cls(address=0)

    # create an instance of the class
    reg_model = msk_top_regs_cls(callbacks=AsyncCallbackSet(read_callback=sim.read,
                                                                       write_callback=sim.write))
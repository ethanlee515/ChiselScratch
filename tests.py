import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.types import LogicArray
from cocotb.runner import get_runner

def nextval(v):
    return v + 1

@cocotb.test()
async def echo_test(dut):
    clock = Clock(dut.clock, 10, units="us")
    cocotb.start_soon(clock.start(start_high=False))
    for i in range(10):
        v = dut.io_fake_dac.value
        print(v)
        v = nextval(v)
        dut.io_fake_adc = v
        await RisingEdge(dut.clock)

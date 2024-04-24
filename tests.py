import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge
from cocotb.types import LogicArray
from cocotb.runner import get_runner
import functools
import random
import os

def split(n, m):
    locs = random.sample(range(n + m - 1), m - 1)
    locs.sort()
    res = [locs[0]]
    for i in range(m - 2):
        res.append(locs[i + 1] - locs[i] - 1)
    res.append(n + m - 2 - locs[-1])
    return res

def nextvals(vs):
    s = sum(vs)
    return split(s + 1, len(vs))

def printvals(vals):
    intvals = list(v.integer for v in vals)
    adds = " + ".join(str(v) for v in intvals)
    print(f"{adds} = {sum(intvals)}")


@cocotb.test()
async def echo_test(dut):
    nregs = int(os.environ["NUMREG"])
    clock = Clock(dut.clock, 10, units="us")
    cocotb.start_soon(clock.start(start_high=False))
    for i in range(15):
        vals = list(getattr(dut, f"io_fake_dac_{j}").value for j in range(nregs))
        printvals(vals)
        vals = nextvals(vals)
        for j in range(nregs):
            getattr(dut, f"io_fake_adc_{j}").value = vals[j]
        await FallingEdge(dut.clock)


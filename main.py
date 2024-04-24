#!/usr/bin/env python3

import sys
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.types import LogicArray
from cocotb.runner import get_runner

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: ./main.py n")
        exit(1)
    runner = get_runner("verilator")
    runner.build(verilog_sources=["./echo.sv"], hdl_toplevel="Echo")
    # Why is `hdl_toplevel` repeated here?
    runner.test(hdl_toplevel="Echo",
            test_module="tests",
            extra_env={"NUMREG": sys.argv[1]})


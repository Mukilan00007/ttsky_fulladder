import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # --- 1. SET INITIAL VALUES ---
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    
    # --- 2. THE RESET SEQUENCE (Fixes the 'XXXXXXXX' error) ---
    dut._log.info("Resetting the DUT...")
    dut.rst_n.value = 0          # Pull reset low
    await Timer(100, units="ns") # Wait for the reset to propagate
    dut.rst_n.value = 1          # Pull reset high
    await Timer(100, units="ns") # Wait for the circuit to settle
    dut._log.info("Reset complete.")

    # --- 3. RUN YOUR ADDER TESTS ---
    
    # Test Case 1: 1 + 1 + 0 = 2 (Binary 10)
    # ui_in[0]=1, ui_in[1]=1, ui_in[2]=0 -> ui_in = 3
    dut.ui_in.value = 3
    await Timer(10, units="ns")
    dut._log.info(f"Input: 3, Output: {int(dut.uo_out.value)}")
    assert dut.uo_out.value == 2

    # Test Case 2: 1 + 1 + 1 = 3 (Binary 11)
    # ui_in[0]=1, ui_in[1]=1, ui_in[2]=1 -> ui_in = 7
    dut.ui_in.value = 7
    await Timer(10, units="ns")
    dut._log.info(f"Input: 7, Output: {int(dut.uo_out.value)}")
    assert dut.uo_out.value == 3

    dut._log.info("All tests passed!")

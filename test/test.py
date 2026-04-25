import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # --- 1. SET INITIAL VALUES ---
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # --- 2. RESET SEQUENCE ---
    dut._log.info("Resetting the DUT...")
    dut.rst_n.value = 0          # Active low reset
    await Timer(100, units="ns")
    dut.rst_n.value = 1
    await Timer(100, units="ns")
    dut._log.info("Reset complete.")

    # --- 3. TEST COUNT UP ---
    # ui_in[0] = reset
    # ui_in[1] = up_down
    # reset=0, up_down=1  => 00000010 = 2
    dut.ui_in.value = 2

    for i in range(5):
        await Timer(10, units="ns")
        dut._log.info(f"Count Up Step {i+1}: Output = {int(dut.uo_out.value)}")

    # --- 4. TEST COUNT DOWN ---
    # reset=0, up_down=0 => 00000000 = 0
    dut.ui_in.value = 0

    for i in range(5):
        await Timer(10, units="ns")
        dut._log.info(f"Count Down Step {i+1}: Output = {int(dut.uo_out.value)}")

    # --- 5. TEST RESET AGAIN ---
    # reset=1 => 00000001 = 1
    dut.ui_in.value = 1
    await Timer(10, units="ns")
    dut._log.info(f"After Reset: Output = {int(dut.uo_out.value)}")

    assert dut.uo_out.value == 0

    dut._log.info("All tests passed!")

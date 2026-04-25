import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_adder(dut):
    dut._log.info("Start")
    
    # Set input to 3 (binary 011 -> a=1, b=1, cin=0)
    dut.ui_in.value = 3
    await Timer(10, units="ns")
    
    # 1 + 1 + 0 = 2. So uo_out should be 2.
    assert dut.uo_out.value == 2
    
    # Set input to 7 (binary 111 -> a=1, b=1, cin=1)
    dut.ui_in.value = 7
    await Timer(10, units="ns")
    
    # 1 + 1 + 1 = 3. So uo_out should be 3.
    assert dut.uo_out.value == 3

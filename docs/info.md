## How it works
This project implements a combinatorial 3-input Full Adder. It uses the first three bits of the input bus (`ui_in[0]`, `ui_in[1]`, and `ui_in[2]`) as the three binary inputs (A, B, and Carry-in). 

The internal logic calculates the sum using the expression `{carry, sum} = a + b + c`. 
- **uo_out[0]**: Represents the **Sum** (LSB).
- **uo_out[1]**: Represents the **Carry-out** (MSB).

## How to test
After power-on and releasing reset (`rst_n` high), you can test the logic by applying signals to the input pins:
1. Set `ui_in` to `1` (`001` binary): `uo_out` should be `1` (Sum=1, Carry=0).
2. Set `ui_in` to `3` (`011` binary): `uo_out` should be `2` (Sum=0, Carry=1).
3. Set `ui_in` to `7` (`111` binary): `uo_out` should be `3` (Sum=1, Carry=1).

The automated tests are handled by cocotb in `test/test.py`.

## External hardware
None. This project uses internal logic only.

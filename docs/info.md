## How it works
This project implements an **8-bit synchronous Up/Down Counter**. It uses the input pins to control counting operation.

The inputs are:

- `ui_in[0]` → **Reset**
- `ui_in[1]` → **Up/Down control**
  - `1` = Count Up
  - `0` = Count Down
- `clk` → Clock signal

The internal logic updates the counter value on every **positive edge** of the clock:

```verilog
if (reset)
    count <= 8'b00000000;
else if (up_down)
    count <= count + 1;
else
    count <= count - 1;


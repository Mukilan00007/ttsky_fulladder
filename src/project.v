`default_nettype none

module tt_um_example (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

    // Internal wires for clarity
    wire a = ui_in[0];
    wire b = ui_in[1];
    wire cin = ui_in[2];
    wire sum;
    wire cout;

    // Full Adder Logic
    // {cout, sum} results in:
    // 0+0+0 = 00 (0)
    // 1+0+0 = 01 (1)
    // 1+1+0 = 10 (2)
    // 1+1+1 = 11 (3)
    assign {cout, sum} = a + b + cin;

    // Assigning to the output bus
    assign uo_out[0] = sum;   // LSB
    assign uo_out[1] = cout;  // MSB
    assign uo_out[7:2] = 6'b000000;

    // All uio_ pins must be assigned to 0 if unused
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // Tie off unused inputs to avoid compiler warnings
    wire _unused = &{ena, clk, rst_n, ui_in[7:3], uio_in, 1'b0};

endmodule

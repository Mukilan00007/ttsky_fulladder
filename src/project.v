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

    // Internal wires for the full adder logic
    wire a = ui_in[0];
    wire b = ui_in[1];
    wire c = ui_in[2];
    wire sum;
    wire carry;

    // Concatenation: {MSB, LSB} 
    // If a=1, b=1, c=0, then {carry, sum} = 2'b10 (decimal 2)
    assign {carry, sum} = a + b + c;

    // Assign results to the output bus
    assign uo_out[0] = sum;   // Bit 0: Sum
    assign uo_out[1] = carry; // Bit 1: Carry
    assign uo_out[7:2] = 6'b000000; // Drive unused output bits to 0

    // Set unused outputs to 0
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // List all unused inputs to prevent warnings
    // We use a dummy wire to "touch" unused inputs
    wire _unused = &{ena, clk, rst_n, ui_in[7:3], uio_in, 1'b0};

endmodule

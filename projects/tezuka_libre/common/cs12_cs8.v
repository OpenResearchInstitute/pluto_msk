module cs12_cs8 (
    input  signed [11:0] sample_in1,  // 12-bit signed input sample 1
    input  signed [11:0] sample_in2,  // 12-bit signed input sample 2
    output reg  [15:0] combined_out // 16-bit combined output
);

    reg signed [7:0] reduced_sample1;
    reg signed [7:0] reduced_sample2;

    always @(*) begin
       if (sample_in1[3]) begin
        // Si le bit de poids faible est 1, ajouter 1 pour arrondir
            reduced_sample1 = sample_in1[11:4] + 1;
        end else begin
    // Sinon, ne pas arrondir
        reduced_sample1 = sample_in1[11:4];
    end    

     if (sample_in2[3]) begin
        // Si le bit de poids faible est 1, ajouter 1 pour arrondir
            reduced_sample2 = sample_in2[11:4] + 1;
        end else begin
    // Sinon, ne pas arrondir
        reduced_sample2 = sample_in2[11:4];
       end

        // Combine the two reduced 8-bit samples into a 16-bit output
        combined_out = {reduced_sample2, reduced_sample1};
    end

endmodule

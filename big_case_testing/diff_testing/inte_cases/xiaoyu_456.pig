D bv32 v956
D bv8 v585
D bv32 v198
D bv32 v828
D bv8 v347
O v828
O v347
A v198 ( 01000101 )
A v585 ( 01000100011001010001001111010000 )
A v198 ( v585 )
A v828 ( 11000111 )
O v828
O v347
A v585 ( 0010010011111101 )
A v956 ( ( 01000010110000000111110101000100 ) + ( v347 ) )
O v198
D bv64 v126
A v126 ( 10100010 )
B 442 ( v126 )
D bv64 v804
D bv8 v398
D bv32 v262
D bv32 v993
D bv16 v226
D bv32 v907
A v907 ( 00000000000000000000000000000001 )
D bv16 v968
D bv16 v848
D bv64 v465
A v993 ( ( v398 ) & ( ( 1000100001101011 ) - ( v198 ) ) )
A v126 ( v993 )
A v848 ( ( ! ( ! ( ! ( v347 ) ) ) ) | ( 01010010 ) )
A v226 ( ! ( v804 ) )
A v262 ( 10001100 )
A v956 ( v398 )
A v398 ( v347 )
O v804
O v465
O v968
O v198
O v907
O v956
O v126
R v968
R v848
R v465
A v907 ( ( v907 ) - ( ! ( ( v585 ) & ( ( ( 0000000000000000 ) + ( ( 00000000000000000000000000000010 ) | ( 0000000000000000000000000000000000000000000000000000000000000001 ) ) ) & ( ! ( 0000000000000001 ) ) ) ) ) )
B 026 ( v907 )
R v907
D bv64 v768
D bv64 v250
D bv32 v578
D bv16 v030
D bv32 v165
A v250 ( ( ! ( ! ( 00011000100010110000111001101101 ) ) ) - ( ! ( v165 ) ) )
A v226 ( 00011111 )
A v768 ( ( ! ( ( ( 00110101 ) & ( ! ( 0100111001101000000001111110001111000111100000000110101111111011 ) ) ) - ( 11001010111100001101101110110001 ) ) ) + ( v828 ) )
A v578 ( 00110010111001010101100100101110 )
A v347 ( v993 )
A v262 ( 0101011100101111010010111010100110110101110110101110010100100111 )
A v956 ( v578 )
A v165 ( ( ! ( ! ( 1100001000010000110111011000010100010111111110110011110011100111 ) ) ) + ( ( 10000100010001000101111000110011 ) + ( ! ( v828 ) ) ) )
A v578 ( ( 0110011111000010 ) | ( ( 11101110100011111101000011111110 ) - ( 00110101 ) ) )
A v226 ( 0010011001011000 )
A v347 ( ! ( v768 ) )
D bv16 v422
A v422 ( 0000000000000000000000000000000000000000000000000000000000000010 )
A v422 ( ( v422 ) - ( ( 00000000000000000000000000000001 ) & ( ( ! ( ! ( ( 0000000000000011 ) & ( 0000000000000000000000000000000000000000000000000000000000000001 ) ) ) ) + ( ( ! ( 00000011 ) ) + ( ( 00000010 ) - ( ! ( 0000000000000000000000000000000000000000000000000000000000000010 ) ) ) ) ) ) )
B 067 ( v422 )
R v422
D bv64 v862
A v862 ( 0000000000000010 )
A v862 ( ( v862 ) - ( 00000001 ) )
B 072 ( v862 )
R v862
A v262 ( ! ( v804 ) )
A v250 ( 0010100101010010 )
A v126 ( ( ! ( 00010111 ) ) + ( v993 ) )
A v030 ( ( v578 ) + ( 10001111011101001100011001110001 ) )
A v585 ( 0010111111111011100110101000000111101110010001000111100001010100 )
A v347 ( v262 )
A v804 ( v398 )
A v993 ( v956 )
O v804
O v126
O v030
O v578
O v262
D bv32 v009
D bv8 v500
D bv16 v569
D bv16 v961
D bv32 v317
D bv32 v667
A v956 ( ! ( ( ( ! ( ! ( 00010001110110100110110000001101 ) ) ) + ( ! ( v667 ) ) ) | ( ! ( ( ( 0010101100000001 ) + ( 1001010000110110101001101010001110111110100110000011110110001111 ) ) + ( ( 1010000111111010 ) - ( 0000011111110000 ) ) ) ) ) )
A v198 ( ( ! ( ! ( ( v250 ) | ( v250 ) ) ) ) & ( ( 1110001001000000000111100000100000011010010000011110000001011010 ) + ( ( ( ( 0101010011011110010110100111100111001010101001100110110000111001 ) & ( 10011101 ) ) - ( v226 ) ) - ( 1111101010111110011010000001100010110000011000011101011010011011 ) ) ) )
A v317 ( ! ( ! ( ( v165 ) + ( v768 ) ) ) )
A v961 ( v030 )
A v398 ( ! ( ( ( 11100100111111010011110011010100 ) & ( 11011100 ) ) | ( ( 1010000011000010 ) + ( v828 ) ) ) )
A v126 ( v226 )
A v956 ( v667 )
A v569 ( ! ( ! ( 01101000010111111000000101100100 ) ) )
A v667 ( ( 11011011 ) & ( v126 ) )
A v030 ( ( 1111110101100011 ) + ( ( v198 ) | ( ! ( ( ( 1110011101100110011001011110110011100110110010000101001110111100 ) + ( 1011001010111000 ) ) - ( v993 ) ) ) ) )
A v198 ( ! ( v250 ) )
A v347 ( ! ( ( 1111000000111100 ) & ( ! ( 11001011 ) ) ) )
A v226 ( ( 11011001 ) & ( ( ! ( v250 ) ) | ( v578 ) ) )
O v347
O v165
O v667
O v226
O v578
R v009
R v500
R v569
R v961
R v317
R v667
D bv32 v684
A v684 ( v956 )
B 121 ( v684 )
R v684
D bv8 v633
A v633 ( 1011000101010100 )
B 125 ( v633 )
R v633
R v768
R v250
R v578
R v030
R v165
D bv64 v260
D bv8 v432
D bv32 v665
D bv8 v117
D bv32 v982
D bv64 v358
D bv64 v110
D bv64 v408
O v260
O v804
O v408
O v956
O v398
O v358
O v982
D bv64 v483
A v483 ( 00000000000000000000000000000000 )
B 149 ( 00000000000000000000000000000000 )
R v483
A v982 ( v110 )
A v260 ( ! ( ( ! ( 00011001100100000100001011110101 ) ) - ( ( v398 ) - ( v347 ) ) ) )
A v665 ( ( v956 ) - ( v226 ) )
D bv16 v856
A v856 ( v260 )
B 156 ( v260 )
R v856
O v408
O v358
O v110
O v993
O v665
O v347
D bv16 v203
A v804 ( ( ! ( ! ( v804 ) ) ) | ( 0110010010001101 ) )
A v993 ( 1100001010001010 )
A v126 ( 00000010111000010100001110011100 )
O v358
O v347
O v956
O v203
O v993
O v665
O v198
O v585
O v126
A v347 ( v198 )
O v665
R v203
D bv16 v540
A v540 ( 00000000 )
B 182 ( v540 )
R v540
D bv32 v366
A v366 ( 00000000000000000000000000000011 )
A v366 ( ( v366 ) - ( 00000001 ) )
B 185 ( v366 )
R v366
D bv32 v404
A v404 ( v585 )
B 191 ( v585 )
R v404
D bv32 v005
D bv16 v071
A v110 ( ! ( v260 ) )
A v585 ( 00110110 )
A v982 ( v804 )
A v993 ( ( 0001011111101001011000000000001110100110101010100110011010111001 ) + ( v110 ) )
A v260 ( 0111011111111000 )
A v665 ( ( ( ( v071 ) + ( ! ( v585 ) ) ) | ( ! ( ! ( ( 1010010011001001 ) - ( 0101111011000001111000100111010100001010110101100001001010011001 ) ) ) ) ) | ( ! ( 0110000101101100 ) ) )
A v828 ( ( ( v358 ) - ( ! ( v117 ) ) ) + ( ! ( v585 ) ) )
A v358 ( v260 )
A v126 ( ( v993 ) + ( 0100011010110011110110111001111000111110000000100101011111001000 ) )
O v005
O v804
O v126
R v005
R v071
R v260
R v432
R v665
R v117
R v982
R v358
R v110
R v408
D bv32 v409
A v409 ( 00000001 )
D bv32 v722
D bv16 v207
D bv16 v768
D bv64 v173
D bv32 v509
D bv64 v000
D bv64 v732
D bv32 v656
D bv32 v805
A v585 ( 11110001110110111011101011010010 )
A v207 ( v347 )
O v000
O v226
O v509
O v956
O v722
O v828
A v509 ( ! ( 1100010010100110 ) )
R v722
R v207
R v768
R v173
R v509
R v000
R v732
R v656
R v805
A v409 ( ( v409 ) - ( 00000001 ) )
B 218 ( v409 )
R v409
D bv64 v024
A v024 ( 00000001 )
B 272 ( 00000001 )
D bv64 v699
A v828 ( ( 00101010 ) + ( 1100011111011111 ) )
A v956 ( v198 )
A v585 ( ! ( v226 ) )
A v262 ( v226 )
A v347 ( ( v699 ) - ( 01100101 ) )
A v226 ( ( ( ! ( v828 ) ) + ( ( 10100001 ) + ( ! ( 00111001 ) ) ) ) & ( 01100000 ) )
A v828 ( v993 )
A v699 ( ( ! ( ( ! ( 0100001110101001101001000010110011011110011001100110011111010101 ) ) & ( ( ( 10111010000010111010000111011011 ) | ( 0111101100000000010100011001000101100101111111000100111101110011 ) ) | ( v993 ) ) ) ) & ( ! ( v226 ) ) )
A v804 ( ! ( 0100101010111011110100011001000100101101010101110111100110001101 ) )
A v804 ( 1101000001011100 )
A v262 ( 01001111 )
A v993 ( 1101111000111100 )
A v347 ( ! ( ( v398 ) + ( v226 ) ) )
A v398 ( ( v024 ) & ( ( ! ( v347 ) ) | ( ! ( 01100001111001100110010001010111 ) ) ) )
A v585 ( ( v226 ) - ( v024 ) )
A v828 ( ( ! ( 1111011010111001 ) ) | ( ( ! ( ( ! ( 01100111101001110010001011011000 ) ) & ( ! ( 10000010111110111110001110011011 ) ) ) ) & ( ( v262 ) & ( 0100001000000111 ) ) ) )
A v126 ( 0111110100110000010001010110001010010100101101111000001111111111 )
A v198 ( ( ! ( v347 ) ) - ( 10011100 ) )
A v956 ( 00101100 )
R v699
R v024
D bv16 v169
A v169 ( 00000001 )
B 302 ( v169 )
D bv16 v085
D bv16 v650
D bv16 v036
D bv8 v849
D bv64 v562
D bv64 v682
D bv16 v922
D bv64 v290
D bv64 v205
A v262 ( ( 0010011000011110100000110111100111010100011000000010001010000100 ) & ( v585 ) )
A v226 ( ( ( 01011111 ) + ( ( v347 ) & ( 10100011 ) ) ) & ( ( 00101001000101111111010000111110 ) - ( ! ( ! ( ! ( 1000111011011111111100001110100000110101111001001010001100110010 ) ) ) ) ) )
A v682 ( v226 )
A v585 ( 11100000 )
A v922 ( ! ( v562 ) )
A v585 ( v956 )
A v849 ( ! ( ( ! ( v650 ) ) + ( ! ( ! ( ! ( 10001100 ) ) ) ) ) )
O v226
R v085
R v650
R v036
R v849
R v562
R v682
R v922
R v290
R v205
R v169
D bv32 v948
A v948 ( 00000001 )
D bv8 v578
D bv64 v552
A v828 ( 01000101111000000111101100011110 )
A v226 ( 1111100000100000 )
A v585 ( ! ( v198 ) )
A v578 ( ( ( ! ( ( v262 ) - ( ( 11101000111000001111110101001001 ) | ( 0101110001110011011110010011001101101100101010111000011100000000 ) ) ) ) - ( ( v585 ) & ( ! ( ( 01111110 ) & ( 01110110 ) ) ) ) ) - ( v956 ) )
A v398 ( ! ( ( v198 ) & ( ! ( 0101100011111010 ) ) ) )
A v993 ( v804 )
A v347 ( ( ! ( v956 ) ) | ( ( 0101010001010111101100010010110110100010010100011101110000111001 ) + ( ( 0101011101010011 ) - ( ! ( 11010000100111001101111011110010 ) ) ) ) )
A v956 ( v198 )
A v552 ( 10011011001110001101101110101011 )
A v126 ( ( 1101111001111010 ) - ( v578 ) )
A v262 ( ( 01111011101101010001000110110111 ) | ( 1001000111111100111110001011001010110100111100010110010111111010 ) )
A v804 ( ( ( ! ( 0110101001101100 ) ) | ( ( 11000100100110101000001010001001 ) | ( ( ( 10010001 ) + ( 00110101 ) ) - ( v993 ) ) ) ) + ( 00010000 ) )
O v578
O v804
O v828
O v552
O v226
O v198
O v552
O v347
O v578
O v948
O v585
O v804
O v262
R v578
R v552
A v948 ( ( v948 ) - ( 00000001 ) )
B 305 ( v948 )
R v948
A v398 ( v226 )
A v126 ( 10101000 )
A v804 ( ( 1100110001001110 ) + ( 0011101001110111 ) )
A v226 ( 01000110 )
A v347 ( 0000110001000010 )
A v262 ( ( ! ( ! ( 00101110011100010101100101000101 ) ) ) | ( v993 ) )
A v828 ( ( v398 ) | ( v198 ) )
A v956 ( v828 )
D bv8 v072
D bv32 v637
A v637 ( 00000000000000000000000000000010 )
A v637 ( ( v637 ) - ( 00000001 ) )
B 348 ( v637 )
R v637
O v226
O v072
O v198
D bv32 v042
A v042 ( 0000000000000000 )
B 357 ( v042 )
R v042
O v828
O v585
O v804
O v072
O v198
O v585
O v956
O v993
D bv32 v331
A v331 ( 0000000000000000000000000000000000000000000000000000000000000001 )
A v331 ( ( v331 ) - ( 00000001 ) )
B 368 ( v331 )
R v331
O v828
O v956
O v072
O v993
O v585
O v347
O v262
O v226
O v126
O v398
D bv16 v650
D bv8 v362
D bv8 v997
D bv8 v234
D bv64 v392
D bv16 v665
D bv16 v826
D bv64 v978
A v398 ( ( ! ( ( ! ( ! ( 1011100011110111010110101000111111001101000011110111001011000001 ) ) ) & ( v392 ) ) ) + ( ! ( ( ( v392 ) & ( ( 01110110 ) & ( 0000001111111011100001100111001111010110010100000011000001101011 ) ) ) - ( 00000010111110010111110001110001 ) ) ) )
A v198 ( v956 )
A v665 ( v665 )
A v585 ( v956 )
A v993 ( 01010101111111000110011110011100 )
A v804 ( ! ( ! ( 0011000010110001101101001110010111100011100101010100110111010010 ) ) )
A v997 ( 00010011 )
A v347 ( v234 )
A v126 ( v234 )
A v650 ( v234 )
A v997 ( 0110000010101111 )
A v978 ( ( 1010011100110110 ) - ( 01100101 ) )
A v804 ( 11101011100111101101010011101100 )
A v392 ( ( ! ( 0000001000100100 ) ) - ( ! ( ! ( ( ! ( 1011011000101011 ) ) - ( ( 00011000 ) - ( 0011010000101100011100111111101010001010100111011001101100101001 ) ) ) ) ) )
A v826 ( ! ( ! ( 01101111 ) ) )
A v362 ( 11000100 )
A v398 ( v997 )
A v665 ( ( 01001100100110001101010101000111 ) & ( ! ( ! ( v392 ) ) ) )
A v956 ( v234 )
A v650 ( 0110001100001101 )
A v126 ( ! ( ( v804 ) + ( v585 ) ) )
O v978
O v993
O v392
O v226
O v828
O v362
O v398
O v126
R v650
R v362
R v997
R v234
R v392
R v665
R v826
R v978
O v956
D bv8 v862
A v862 ( 00000001 )
B 430 ( 00000001 )
R v862
R v072
A v347 ( v347 )
A v993 ( 1111011110010010101111111010001010011110110101111001011101100111 )
A v828 ( ! ( 10100110 ) )
A v226 ( v828 )
A v585 ( ! ( ( ! ( ( 0111011101100011101100000001010010000010001010100010110000110110 ) | ( v347 ) ) ) | ( 00111111 ) ) )
R v804
R v398
R v262
R v993
R v226
R v126
A v347 ( ( 1111001000110101010110101010110010100101001010001100111100101000 ) - ( ( ! ( 11101101101110011001010000000111 ) ) - ( ! ( v585 ) ) ) )
A v585 ( ! ( ! ( ! ( 0001001110001010 ) ) ) )
A v828 ( ! ( v585 ) )
A v198 ( v347 )
A v956 ( 10100110 )
D bv16 v454
A v454 ( ! ( v585 ) )
B 693 ( v454 )
D bv8 v913
D bv8 v321
D bv16 v420
D bv32 v013
D bv32 v548
D bv64 v907
D bv8 v906
D bv32 v429
D bv8 v017
D bv8 v380
D bv64 v042
D bv8 v352
D bv16 v214
D bv32 v148
D bv8 v329
D bv16 v442
D bv64 v311
D bv16 v805
D bv8 v407
A v407 ( 00000001 )
A v407 ( ( v407 ) - ( v585 ) )
B 471 ( v407 )
R v407
D bv8 v929
D bv8 v304
D bv8 v231
D bv8 v634
D bv32 v825
A v148 ( ! ( 01111001100101010111010010100111 ) )
A v017 ( ( v042 ) - ( ( v013 ) | ( ( ( 0101100010001100 ) + ( 10100001 ) ) - ( v198 ) ) ) )
A v042 ( ( ! ( ( v454 ) | ( v321 ) ) ) | ( v906 ) )
A v347 ( ( v321 ) | ( ( 1001010011001010 ) - ( 01100111 ) ) )
A v906 ( 01010100 )
A v420 ( v380 )
A v231 ( 1011010101001101100100100100111100110111011010010010111110110111 )
A v634 ( 0001001010110110 )
A v828 ( ( v304 ) + ( 00001000110011001110000001101101 ) )
A v907 ( ( ( ( 1110001111110101 ) & ( ( v828 ) & ( ( 0100111101101110 ) | ( 0110100111010000 ) ) ) ) & ( 11000000000011000010100001001111 ) ) - ( ! ( v304 ) ) )
O v380
O v585
O v198
O v956
O v214
O v805
A v198 ( 11011100 )
A v548 ( 00111100 )
A v311 ( ( 1100010011000111 ) - ( v805 ) )
A v442 ( ( 0101101011011010100011001101000011010001010011010110101000011010 ) - ( 11010011 ) )
A v907 ( v825 )
A v017 ( ( ( 10000100 ) - ( 0011110000110110 ) ) - ( v198 ) )
A v805 ( ( v352 ) - ( 01101110 ) )
A v913 ( ( v442 ) | ( 0100111001011100 ) )
A v906 ( v017 )
A v454 ( v429 )
A v929 ( 0001100001000110110011001111010110101101100001011010001101110011 )
A v013 ( ( ! ( ! ( 1010000101000101100010010011111000011110010100100100100111000010 ) ) ) & ( ! ( ! ( ( v956 ) | ( ( 0110100010110001 ) + ( 1011111011111111 ) ) ) ) ) )
A v148 ( ! ( v454 ) )
A v442 ( ! ( ( 01001100 ) + ( ( v906 ) + ( 00111110110011001110011000001110 ) ) ) )
A v352 ( v454 )
A v634 ( ! ( ( 0101111000100100101000100000010101010110000101001111011100001010 ) + ( ( ( v429 ) + ( 01110011 ) ) - ( ( v042 ) - ( 11010100100111000011011010011100 ) ) ) ) )
A v347 ( 0001110001101110000001111000111111000000011101011011010011010110 )
A v585 ( ! ( ( v329 ) - ( ! ( v906 ) ) ) )
R v929
R v304
R v231
R v634
R v825
D bv64 v672
A v672 ( ( 01010111101000000011000001011100 ) - ( ( v352 ) - ( ( 01000011 ) + ( 1101110111000000000110000110110100101111111110101001111010001000 ) ) ) )
B 521 ( ( 01010111101000000011000001011100 ) - ( ( v352 ) - ( ( 01000011 ) + ( 1101110111000000000110000110110100101111111110101001111010001000 ) ) ) )
R v672
D bv64 v531
A v531 ( 10111000 )
B 525 ( v531 )
R v531
A v906 ( ( 01000001 ) | ( 10100101 ) )
A v352 ( 1011111101010100 )
A v013 ( 01100001000000110010110110000001 )
A v311 ( 0100010110110100101000101100100000000111010101010010000001110000 )
A v805 ( ! ( ! ( v956 ) ) )
A v329 ( 11110100010011010010110100101101 )
A v013 ( ( 0011110101010011100101001100100010101101000100011000011000110110 ) + ( 1110010010110111 ) )
A v148 ( v442 )
A v420 ( v347 )
A v907 ( 0100111000000100 )
A v017 ( ! ( v148 ) )
A v913 ( 0111000101111001110110011010011111100100011100110101000101000111 )
A v013 ( ! ( v148 ) )
A v042 ( ! ( ( ! ( v805 ) ) + ( ! ( 1110000101010100 ) ) ) )
A v906 ( ! ( ( 0010010010111100 ) - ( v311 ) ) )
A v956 ( ( ! ( ( ( v420 ) + ( ! ( 11100100 ) ) ) | ( ! ( 0111101000001101000000001101111111000000110000001100011111010001 ) ) ) ) | ( ( 0010110101010101011011101010100100011000101101111110101001111011 ) & ( v420 ) ) )
A v420 ( ( 0000101000001101011001000111001101001011111010100011110011101011 ) & ( 1100011111001001 ) )
A v311 ( ( ! ( ( v013 ) + ( ! ( 1001010011111111 ) ) ) ) & ( 0011101010101110 ) )
D bv64 v780
A v780 ( v329 )
B 547 ( v780 )
R v780
O v585
A v013 ( ( v380 ) | ( ! ( v454 ) ) )
R v017
R v380
R v042
R v352
R v214
R v148
R v329
R v442
R v311
R v805
D bv16 v844
A v844 ( 0010000110001110101000100010101101011101001011111010010001110011 )
B 596 ( 0010000110001110101000100010101101011101001011111010010001110011 )
D bv8 v897
D bv16 v867
D bv32 v679
D bv8 v300
D bv8 v215
D bv8 v687
D bv64 v294
D bv8 v678
D bv64 v136
D bv64 v711
A v420 ( ! ( ( 0101001110000011000000000000000010011110001111000011110101001100 ) - ( 00110001001000100101111101010001 ) ) )
A v867 ( v711 )
A v429 ( v321 )
A v347 ( v321 )
A v548 ( ! ( v347 ) )
A v906 ( 00110101 )
O v454
O v136
O v906
O v678
O v907
O v867
O v844
R v897
R v867
R v679
R v300
R v215
R v687
R v294
R v678
R v136
R v711
R v844
O v906
O v585
O v013
O v913
O v420
O v454
O v321
O v548
D bv8 v261
A v261 ( ( ( v906 ) & ( v956 ) ) & ( ! ( 01101011101111111111000011010010 ) ) )
B 635 ( v261 )
D bv16 v590
A v261 ( 1001011100111011110100100010111110001000100100110011010001000001 )
A v906 ( ( ! ( ! ( ! ( 11100111 ) ) ) ) & ( ( 01011010 ) - ( 10010100111101110111110010101100 ) ) )
A v321 ( ( v454 ) - ( ! ( 10111010 ) ) )
A v454 ( 10010111001100100010010000011011 )
A v347 ( v420 )
A v956 ( ! ( v198 ) )
A v907 ( 0111110000011110 )
A v198 ( ( v828 ) & ( ! ( 1010001001100100000101011000010010111011110111000010100100111110 ) ) )
O v013
O v956
O v454
O v585
O v321
O v548
O v347
O v548
O v590
O v013
O v347
O v429
O v454
O v828
O v198
O v907
O v261
R v590
R v261
D bv32 v287
D bv64 v847
D bv32 v859
D bv8 v030
D bv32 v335
D bv8 v712
D bv8 v492
A v492 ( 0000000000000001 )
A v492 ( ( v492 ) - ( 00000001 ) )
B 644 ( v492 )
R v492
O v548
O v321
O v013
O v429
O v030
O v198
O v712
O v906
O v859
O v847
D bv16 v676
D bv16 v575
D bv16 v315
D bv64 v487
D bv64 v665
D bv16 v086
D bv16 v136
D bv16 v337
D bv64 v415
D bv64 v331
O v335
O v665
R v676
R v575
R v315
R v487
R v665
R v086
R v136
R v337
R v415
R v331
R v287
R v847
R v859
R v030
R v335
R v712
R v913
R v321
R v420
R v013
R v548
R v907
R v906
R v429
R v454
R v956
R v585
R v198
R v828
R v347

# CSC4001 Project Draft

## PIG Language

### Tokens

| token    | expression          | statement    | example               |
| -------- | ------------------- | ------------ | --------------------- |
| D        | D                   | `D TYPE VAR` | `D bv8 v001`          |
| A        | A                   | `A VAR Exp`  | `A v001 ( 00000101 )` |
| B        | B                   | `B LINE Exp` | `B 001 ( v000 )`      |
| O        | O                   | `O VAR`      | `O v001`              |
| R        | R                   | `R VAR`      | `R v001`              |
| ADD      | +                   |              |                       |
| SUB      | -                   |              |                       |
| AND      | &                   |              |                       |
| OR       | \|                  |              |                       |
| NOT      | !                   |              |                       |
| LINE     | $[0-9]^3$           |              |                       |
| CONSTANT | $[01]^{8|16|32|64}$ |              |                       |
| LP       | (                   |              |                       |
| RP       | )                   |              |                       |
| TYPE     | bv(8\|16\|32\|64)   |              |                       |
| VAR      | v$[0-9]^3$          |              |                       |


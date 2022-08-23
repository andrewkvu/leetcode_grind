class Solution {
    public int getSum(int a, int b) {
        // a ^ b = 0010 XOR
        // a & b << 1001 shift left --> 10010
        // add the a ^ b and a & b
        // by ^ the a^b and a & b
        // then & them
        // keep doing that until the output is 0, since there is no carry
        
        while (b != 0) {
            int temp = (a & b) << 1; // uses original value of a before computed with the ^=
            a ^= b;
            b = temp;
        }
        return a;
    }
}
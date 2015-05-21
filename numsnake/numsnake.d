//*****************************************************************************
//*****************************************************************************
//
// Solve "number snake":
//
//    http://www.theguardian.com/science/alexs-adventures-in-numberland/2015/may/20/can-you-do-the-maths-puzzle-for-vietnamese-eight-year-olds-that-has-stumped-parents-and-teachers
//
//*****************************************************************************
//*****************************************************************************

/*
a + 13*b:c + d + 12*e - f + g*h:i = 66 + 21

a + d - f + 13*b/c + 12*e + g*h/i = 87

Primes...: 1, 2, 3,    5,    7,    
Rest.....:          4,    6,    8, 9

b/c = 4/2, 6/2, 8/2, 6/3, 9/3

...Better use computer to solve...

*/

import std.stdio;
import std.algorithm;

void recurse(float[] nums = [])
{
    static int solutions = 0;
    
    //writeln(nums);
    if(nums.length == 9)
    {
        float d1 = 13*nums[4]/nums[5];
        float d2 = nums[6]*nums[7]/nums[8];
        /*
        if(d1 != cast(int)d1) return;
        if(d2 != cast(int)d2) return;
        */
        float result =
            nums[0]
            + nums[1]
            - nums[2]
            + 12*nums[3]
            + 13*nums[4]/nums[5]
            + nums[6]*nums[7]/nums[8]
            - 11
            - 10; 

        if(result == 66) {
            writef("%3d. ", ++solutions); writeln(nums);
        }
    }
    else foreach(num; 1 .. 10)
    {
        if(find(nums, num).length != 0) continue;
        recurse(nums ~ num);
    }
}

void main()
{
    recurse();
}

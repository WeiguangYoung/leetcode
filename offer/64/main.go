package main

func sumNums(n int) int {
    ans, A, B := 0, n, n + 1
    addGreatZero := func() bool {
        ans += A
        return ans > 0
    }

    _ = ((B & 1) > 0) && addGreatZero()
    A <<= 1
    B >>= 1

    _ = ((B & 1) > 0) && addGreatZero()
    A <<= 1
    B >>= 1

    _ = ((B & 1) > 0) && addGreatZero()
    A <<= 1
    B >>= 1

    _ = ((B & 1) > 0) && addGreatZero()
    A <<= 1
    B >>= 1

    _ = ((B & 1) > 0) && addGreatZero()
    A <<= 1
    B >>= 1

    _ = ((B & 1) > 0) && addGreatZero()
    A <<= 1
    B >>= 1

    _ = ((B & 1) > 0) && addGreatZero()
    A <<= 1
    B >>= 1

    _ = ((B & 1) > 0) && addGreatZero()
    A <<= 1
    B >>= 1

    _ = ((B & 1) > 0) && addGreatZero()
    A <<= 1
    B >>= 1

    _ = ((B & 1) > 0) && addGreatZero()
    A <<= 1
    B >>= 1

    _ = ((B & 1) > 0) && addGreatZero()
    A <<= 1
    B >>= 1

    _ = ((B & 1) > 0) && addGreatZero()
    A <<= 1
    B >>= 1

    _ = ((B & 1) > 0) && addGreatZero()
    A <<= 1
    B >>= 1

    _ = ((B & 1) > 0) && addGreatZero()
    A <<= 1
    B >>= 1
    return ans >> 1
}

func main(){
	sumNums(3)
}
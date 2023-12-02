package main

import (
    "fmt"
    "os"
	s "strings"
	"unicode"
	"strconv"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func main() {

    dat, err := os.ReadFile("input.txt")
    check(err)
    arr := s.Split(string(dat), "\n")

	res := 0
	for i, line := range arr {
		f, l := "n", "n"
		for pos, char := range line {
			if unicode.IsDigit(char) && f == "n" {
				f = string(char)
				l = string(char)
			} else if unicode.IsDigit(char) {
				l = string(char)
			}
			_ = pos
		}
		_ = i
		num, err := strconv.Atoi(string(f + l))
		check(err)
		res += num
	}
	fmt.Println(res)
}
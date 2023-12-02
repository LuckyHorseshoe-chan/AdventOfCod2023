package main

import (
    "fmt"
    "os"
	s "strings"
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
	nums_map := make(map[string]string)
	nums_map["1"] = "1"
	nums_map["2"] = "2"
	nums_map["3"] = "3"
	nums_map["4"] = "4"
	nums_map["5"] = "5"
	nums_map["6"] = "6"
	nums_map["7"] = "7"
	nums_map["8"] = "8"
	nums_map["9"] = "9"
	nums_map["one"] = "1"
	nums_map["two"] = "2"
	nums_map["three"] = "3"
	nums_map["four"] = "4"
	nums_map["five"] = "5"
	nums_map["six"] = "6"
	nums_map["seven"] = "7"
	nums_map["eight"] = "8"
	nums_map["nine"] = "9"
	ind := -1
	for i, line := range arr {
		f, l := "n", "n"
		f_i, l_i := 10000, -1 
		for str, num := range nums_map {
			ind = s.Index(line, str)
			if ind < f_i && ind != -1{
				f_i = ind
				f = string(num)
			}
			ind = s.LastIndex(line, str)
			if ind > l_i{
				l_i = ind
				l = string(num)
			}
		}
		_ = i
		sum, err := strconv.Atoi(string(f + l))
		check(err)
		res += sum
	}
	fmt.Println(res)
}
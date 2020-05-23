package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	stdin := bufio.NewReader(os.Stdin)
	stdout := bufio.NewWriter(os.Stdout)

	temp, _, _ := stdin.ReadLine()
	num, _ := strconv.Atoi(string(temp))

	
	for i:= num; i >= 1; i-- {
		stdout.WriteString(strconv.Itoa(i) + "\n")
	}
	
	stdout.Flush()
}
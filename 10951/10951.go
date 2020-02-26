package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	stdin := bufio.NewScanner(os.Stdin)
	stdout := bufio.NewWriter(os.Stdout)
	defer stdout.Flush()

	for stdin.Scan() {
		input := stdin.Bytes()
		sum := int(input[0]-'0') + int(input[2]-'0')
		stdout.WriteString(strconv.Itoa(sum) + "\n")
	}
}

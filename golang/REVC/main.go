package main

import (
	"fmt"
	"os"
	"strings"
)

// reverse the string, then turn nucleotides into their complements

func main() {
	filepath := "rosalind_revc.txt"
	content, err := os.ReadFile(filepath)
	if err != nil {
		// log.Fatal(err)
		panic(err)
	}

	dnaString := string(content)
	dnaStringRev := Reverse(dnaString)
	dnaStringRevC := Complement(dnaStringRev)
	fmt.Println(dnaStringRevC)
}

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func Complement(s string) string {
	runes := []rune(s)
	var comp strings.Builder
	for i := range runes {
		current := string(runes[i])
		switch current {
		case "A":
			comp.WriteString("T")
		case "C":
			comp.WriteString("G")
		case "G":
			comp.WriteString("C")
		case "T":
			comp.WriteString("A")
		}
	}
	return comp.String()
}

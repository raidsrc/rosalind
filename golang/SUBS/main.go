package subs

import (
	"fmt"
	"os"
	"strings"
)

// scan through long string, search for occurrences of substring

func main() {
	filepath := "rosalind_subs.txt"
	content, err := os.ReadFile(filepath)
	if err != nil {
		// log.Fatal(err)
		panic(err)
	}

	contentString := string(content)
	lines := strings.Split(contentString, "\n")
	sequenceString := strings.TrimSpace(lines[0])
	motifString := strings.TrimSpace(lines[1])
	// search for motifString in sequenceString using .index
	// output that number
	// trim the string from beginning all the way to that number + 1, store number of chars trimmed
	// repeat the search, output number + previous number
	// repeat as long as length of long string is > 1

	// alt implementation
	// iterate through runes looking at windows of size len(motifString)
	// if window matches motifString exactly, note down the index

	indices := []int{}
	for i, j := 0, len(motifString); j < len(sequenceString); i, j = i+1, j+1 {
		windowText := sequenceString[i:j]
		if windowText == motifString {
			indices = append(indices, i+1)
		}
	}
	fmt.Println(indices)

	// indices := []int{}

	// i := 0
	// for i != -1 && i < len(sequenceString) {
	// 	totalDistanceCovered := 0
	// 	for k := 0; k < len(indices); k++ {
	// 		totalDistanceCovered += indices[k]
	// 	}
	// 	i = strings.Index(sequenceString, motifString)
	// 	j := i + totalDistanceCovered
	// 	indices = append(indices, j)
	// 	sequenceString = sequenceString[i+1:]
	// }
	// fmt.Println(indices)

}

package rna

import (
	"fmt"
	"os"
	"strings"
	// "log"
)

// convert T's into U's

func main() {
	filepath := "rosalind_rna.txt"
	content, err := os.ReadFile(filepath)
	if err != nil {
		// log.Fatal(err)
		panic(err)
	}

	dnaString := string(content)
	rnaString := strings.ReplaceAll(dnaString, "T", "U")
	fmt.Println(rnaString)

}

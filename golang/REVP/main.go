package revp

import (
	"fmt"
	"os"
	"path/whatever/golang/revc"
	"strings"
)

func main() {
	filepath := "rosalind_revp.txt"
	content, err := os.ReadFile(filepath)
	if err != nil {
		// log.Fatal(err)
		panic(err)
	}

	contentString := string(content)
	lines := strings.Split(contentString, "\n")
	s := ""
	for i := 1; i < len(lines); i++ {
		s += strings.TrimSpace(lines[i])
	}
	fmt.Println(s)
	// srevc := revc.Reverse(revc.Complement(s))
	// now scan a window through the two strings char by char, if window of 1st string == window of 2nd string we got a reverse palindrome, save the index and length.

	indices := [][]int{}
	for windowSize := 4; windowSize <= 12; windowSize++ { // increase the window size and go through the string again
		i, j := 0, 0
		for i, j = 0, windowSize; j <= len(s); i, j = i+1, j+1 {
			sWindowText := s[i:j]
			sWindowTextRevC := revc.Reverse(revc.Complement(sWindowText))
			if sWindowText == sWindowTextRevC {
				data := []int{i + 1, windowSize}
				indices = append(indices, data)
			}
		}
	}

	for i := 0; i < len(indices); i++ {
		fmt.Print(indices[i][0], indices[i][1], "\n")
	}
}

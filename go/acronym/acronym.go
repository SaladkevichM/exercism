// This is a "stub" file.  It's a little start on your solution.
// It's not a complete solution though; you have to write some code.

// Package acronym should have a package comment that summarizes what it's about.
// https://golang.org/doc/effective_go.html#commentary
package acronym

import (
	"fmt"
	"strings"
)

// Abbreviate should have a comment documenting it.
func Abbreviate(s string) string {
	// Write some code here to pass the test suite.
	// Then remove all the stock comments.
	// They're here to help you get started but they only clutter a finished solution.
	// If you leave them in, reviewers may protest!

	tokens := strings.Split(s, " ")

	if len(tokens) == 1 {
		return strings.ToUpper(s[:1])
	}

	res := ""

	for _, word := range tokens {
		if len(word) == 1 {
			runes := []rune(word)
			if runes[0] > 26 && runes[0] < 33 {
				continue
			}
			if runes[0] > 58 {
				continue
			}
		}
		if strings.Contains(word, "-") {
			word = strings.TrimSpace(word)
			tmp := strings.Split(word, "-")
			if len(tmp) == 2 {
				fmt.Println("&&&&&&&&&")
				fmt.Println(tmp)
				part1 := tmp[0]
				part2 := tmp[1]
				res = res + part1[:1] + part2[:1]
			}
		} else {
			res = res + word[:1]
		}
	}

	return strings.ToUpper(res)
}

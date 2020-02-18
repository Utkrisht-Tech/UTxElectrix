package tools

import (
	"fmt"
	"os"
)

// GetArg : Collects Command Line Arguments and returns them
func GetArg() string {
	switch l := len(os.Args); l {
	case 1:
		return "charge"
	case 2:
		return os.Args[1]
	default:
		fmt.Println("Usage Error: Too Many Arguments, use 'electrix help' instead.")
		os.Exit(1)
	}
	return "nil" // Program Should Never Reach Here
}

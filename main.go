package main

import "log"

func main() {
	log.Printf("Pingmesh get started")
	GetConfig().Load()
	GetConfig().Print()
}

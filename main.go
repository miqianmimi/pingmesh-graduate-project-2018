package main

func main() {
	Info.Println("Pingmesh get started")
	GetConfig().Load()
	GetConfig().Print()
}

package main

import (
	"encoding/json"
	"log"
	"os"
	"sync"
)

type Config struct {
	ListenPort         uint16 `json:"listenPort"`
	PinglistPrefix     string `json:"pinglistPrefix"`
	CollectPeriodInSec int    `json:"collectPeriodInSec"`
	PinglogFile        string `json:"pinglogFile"`
}

var instance *Config
var once sync.Once

func GetConfig() *Config {
	once.Do(func() {
		instance = &Config{}
	})
	return instance
}

func (c *Config) Load() {
	file, err := os.Open("./conf/agent.conf")
	defer file.Close()
	if err != nil {
		log.Fatal("open configuration file failed")
	}
	decoder := json.NewDecoder(file)
	err = decoder.Decode(c)
	if err != nil {
		log.Fatal("parse configuration failed")
	}
}

func (c *Config) Print() {
	log.Printf("%#v\n", *c)
}

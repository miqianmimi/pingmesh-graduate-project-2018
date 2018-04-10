package main

import (
	"io"
	"log"
	"os"
)

var (
	Info    *log.Logger
	Warning *log.Logger
	Error   *log.Logger
)

func init() {
	errFile, err := os.OpenFile("/tmp/errors.log", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0644)
	if err != nil {
		log.Fatal("open errors.log failed", err)
	}
	Info = log.New(os.Stdout, "Info:", log.LstdFlags|log.Lmicroseconds|log.Lshortfile|log.LUTC)
	Warning = log.New(os.Stdout, "Warning:", log.LstdFlags|log.Lmicroseconds|log.Lshortfile|log.LUTC)
	Error = log.New(io.MultiWriter(os.Stderr, errFile), "Warning:", log.LstdFlags|log.Lmicroseconds|log.Lshortfile|log.LUTC)
}

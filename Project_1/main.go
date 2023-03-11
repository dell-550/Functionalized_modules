package main

import (
	"fmt"
	"github.com/gohouse/converter"
)

func main() {
	err := converter.NewTable2Struct().
		SavePath("F:/go/Project_1/model/model.go").
		Dsn("root:luo12138@tcp(localhost:3306)/myfriends?charset=utf8").
		Run()
	fmt.Println(err)
}

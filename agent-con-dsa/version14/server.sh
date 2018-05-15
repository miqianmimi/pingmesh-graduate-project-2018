#server
echo " "
#echo $1,$2;
#echo " "

mv s.cpp $1/;
cd $1 ;
g++ s.cpp -o s -std=c++11;
./s;
echo " "
echo "server $2 启动完成"
echo " "
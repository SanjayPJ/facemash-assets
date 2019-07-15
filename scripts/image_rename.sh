count=0
for entry in "./girls"/*
do
  echo "$entry"
  mv "$entry" "./girls/$count.jpeg"
  count=$(($count + 1))
done

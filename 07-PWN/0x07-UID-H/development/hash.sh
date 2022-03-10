flag=nonsaltyhashlist
for (( i=0; i<${#flag}; i++ )); do
  echo -n "${flag:$i:1}" | md5sum >> hashes.txt
done

# cut -d' ' -f1 hashes.txt > hashes.txt

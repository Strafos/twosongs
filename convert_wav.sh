SUFF=mp3
suff=wav
for f in ./songs/*.mp3
do
	mpg123 -w ${f%.$SUFF}.$suff $f
done
rm *.mp3

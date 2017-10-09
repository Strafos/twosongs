# rm BPM.txt
for f in ./cls_met/*.wav
do
    python2 bpm_detection.py --filename "$f"
done

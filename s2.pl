$MODEL = 'gpt-4';
system("python eli/center_embed.py --file_list data/lists/ce-q0-l1-4 --model $MODEL --sample_n 200 --tuning_n 0 --seed 42");


$OUTPUTERR = "dec15errout";
$OUTPUT = "dec15out";
$SAMPLESIZE = 200;

#@MODEL = ("gpt-3.5-turbo", "llama3-70b", "llama3-8b");
@MODEL = ("llama3-70b", "llama3-8b");
@TUNE = (0,5);
$F = "ce-q0-l1-4";

for my $M (@MODEL) {
    for my $T (@TUNE) {
	print "Executing: python eli/center_embed.py --file_list data/lists/$F  --model $M  --sample_n $SAMPLESIZE --tuning_n $T  --seed 42  \n";
	system("python eli/center_embed.py --file_list data/lists/$F  --model $M  --sample_n $SAMPLESIZE --tuning_n $T  --seed 42 >> $OUTPUT 2>>$OUTPUTERR ");
    }
}













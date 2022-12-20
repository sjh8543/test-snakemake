with open(snakemake.input[0],"r") as f:
    with open( snakemake.output[0],"w") as f2:
        f2.write( f.read() )

from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='4eam', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='4eamA', atom_files='4eam.pdb')
aln.append(file='/content/ANCESTRAL/target.fasta', align_codes='target', alignment_format='FASTA')
aln.align2d()
aln.write(file='aligned.fasta', alignment_format='FASTA')
aln.write(file='aligned.ali', alignment_format='PIR')
aln.write(file='aligned.pap', alignment_format='PAP')